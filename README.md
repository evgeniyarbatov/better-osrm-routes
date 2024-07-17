# better-osrm-routes

Improve OSRM routes with GPX files.

## Get GPX Files

You can get your own GPX files from [Garmin Connect](https://connect.garmin.com/modern/courses) or running events. You can also create your own GPX based on heatmap on Strava.

## Convert GPX to OSM Ways

Follow `scripts` to convert GPX to OSM ways.

## Merge OSM Maps

Merge OSM based on GPX files and public OSM:

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
custom_osm/hanoi_with_gpx.osm.pbf \
-o custom_osm/hanoi_with_gpx.osm
```