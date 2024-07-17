import os
import glob
import ast

import pandas as pd

import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom 

def get_filename(filename):
 return os.path.splitext(os.path.basename(filename))[0]

def create_osm(df, osm_file):
    osm = ET.Element("osm")
    osm.set("version", "0.6")
    osm.set("generator", "CGImap 0.9.2 (596732 spike-08.openstreetmap.org)")
    osm.set("copyright", "OpenStreetMap and contributors")
    osm.set("attribution", "http://www.openstreetmap.org/copyright")
    osm.set("license", "http://opendatacommons.org/licenses/odbl/1-0/")

    tags = [
        {"k": "highway", "v": "footway"},
        {"k": "foot", "v": "designated"},
    ]

    ways_df = df.groupby('filename')['node_id'].agg(lambda x: list(x.unique())).reset_index()
    
    for idx, row in ways_df.iterrows():
        way_id = idx + 1

        way = ET.SubElement(
            osm,
            "way",
            id=str(way_id),
            visible="true",
            version="1",
        )

        ET.SubElement(
            way, 
            "tag", 
            k="name", 
            v="Custom GPX Route",
        )

        for node_id in row["node_id"]:
            nd = ET.SubElement(way, "nd")
            nd.set("ref", str(node_id))

        for tag_data in tags:
            tag = ET.SubElement(way, "tag")
            tag.set("k", tag_data["k"])
            tag.set("v", tag_data["v"]) 

        xml_str = minidom.parseString(ET.tostring(osm)).toprettyxml(indent="  ")

    dir = os.path.dirname(osm_file)
    if not os.path.exists(dir):
        os.makedirs(dir)

    with open(osm_file, "w") as f:
        f.write(xml_str)

node_dfs = []

csv_files = glob.glob(
  os.path.join('gpx/nodes/', '*.csv')
)
for csv_file in csv_files:
  filename = get_filename(csv_file)
  
  df = pd.read_csv(csv_file)
  df['filename'] = filename
  
  # Remove matched nodes that are too far
  df = df[df['distance'] <= 10]
  
  df['nodes'] = df['nodes'].apply(ast.literal_eval)
  
  # Split nodes into separate rows
  df = df.explode('nodes').reset_index(drop=True)
  df = df.rename(columns={'nodes': 'node_id'})
  
  node_dfs.append(df[['node_id', 'filename']])

all_node_dfs = pd.concat(node_dfs).reset_index(drop=True)

create_osm(
  all_node_dfs,
  'gpx/osm/custom.osm',
)