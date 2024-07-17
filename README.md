# better-osrm-routes

Improve OSRM routes with GPX files.

## How to use

- add GPX files to `gpx/raw`
- create maps of GPX files with `python scripts/make-maps.py`
- get OSM nodes inside GPX files `python scripts/get-nodes.py`
- create OSM file based on OSM nodes `python scripts/create-osm.py`

## Merge GPX OSM with public OSM

Use:

```
osmium merge \
--overwrite \
osm/hanoi.osm.pbf \
gpx/osm/custom.osm \
-o custom_osm/hanoi_with_gpx.osm.pbf
```

Check the merged OSM is as expected:

```
osmium cat \
--overwrite \
custom_osm/hanoi_with_gpx.osm.pbf \
-o custom_osm/hanoi_with_gpx.osm
```

## Where to find GPX files?

You can get your own GPX files from [Garmin Connect](https://connect.garmin.com/modern/courses) or running events. You can also create your own GPX based on heatmap on Strava.

