import os
import glob
import requests

import pandas as pd

from utils import parse_gpx, get_output_path

def get_nearest(coords):
  lat, lon = coords
  response = requests.get(f"http://127.0.0.1:5000/nearest/v1/foot/{lon},{lat}")
  response.raise_for_status()

  df = pd.DataFrame(columns=['latitude', 'longitude', 'node_id'])
  
  data = response.json()
  if 'waypoints' in data:
      waypoints = data['waypoints']
      info = [(
        lat,
        lon,
        wp['nodes'],
        wp['location'][1], 
        wp['location'][0], 
        wp['distance'],
      ) for wp in waypoints]
      df = pd.DataFrame(info, columns=[
        'lat',
        'lon',
        'nodes',
        'node_lat', 
        'node_lon', 
        'distance',
      ])
  
  return df

def query_osrm(df):
  results = []
  
  for _, row in df.iterrows():
    nearest_df = get_nearest((row['latitude'], row['longitude']))
    results.append(nearest_df)

  return pd.concat(results).reset_index(drop=True)   

gpx_files = glob.glob(
  os.path.join('../gpx/raw/', '*.gpx')
)
for gpx_file in gpx_files:
  output_path = get_output_path('../gpx/nodes/', gpx_file, 'csv')
  
  if os.path.exists(output_path):
    continue
  
  df = parse_gpx(gpx_file)
  
  osrm_df = query_osrm(df)
  
  osrm_df.to_csv(output_path, index=False)