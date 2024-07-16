import os
import glob

import matplotlib.pyplot as plt
import contextily as ctx

from utils import parse_gpx, get_output_path

def make_map(df, filename):
  plt.figure(figsize=(15, 8))
  
  plt.plot(df['longitude'], df['latitude'], color='red', label='Route')
  ctx.add_basemap(plt.gca(), crs='EPSG:4326', source=ctx.providers.OpenStreetMap.Mapnik)
  
  plt.legend()
  plt.xticks([], [])
  plt.yticks([], [])
  plt.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False)
  
  plt.savefig(filename, bbox_inches='tight', pad_inches=0)

gpx_files = glob.glob(
  os.path.join('../gpx/raw/', '*.gpx')
)
for gpx_file in gpx_files:  
  output_path = get_output_path('../gpx/maps/', gpx_file, 'png')
  
  if os.path.exists(output_path):
    continue
  
  df = parse_gpx(gpx_file)
  make_map(df, output_path)
