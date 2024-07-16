import os
import glob

import matplotlib.pyplot as plt
import contextily as ctx

from utils import parse_gpx, get_output_path

def get_map_path(output_dir, filename):
  map_filename = os.path.splitext(os.path.basename(filename))[0] + '.png'
  return output_dir + '/' + map_filename

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
  os.path.join('../gpx/', '*.gpx')
)
for gpx_file in gpx_files:
  df = parse_gpx(gpx_file)
  
  map_path = get_output_path('../gpx/maps/', gpx_file, 'png')
  
  make_map(df, map_path)
