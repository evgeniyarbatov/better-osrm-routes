# better-osrm-routes

Improve OSRM routes with GPX files.

## Get GPX Files

You can get your own GPX files from [Garmin Connect](https://connect.garmin.com/modern/courses) or running events. You can also create your own GPX based on heatmap on Strava.

## Convert GPX to OSM Ways

Follow `scripts` to convert GPX to OSM ways.

## Merge OSM Maps

Merge OSM based on GPX files and public OSM:

```
osmosis \
--read-pbf file="osm/hanoi.osm.pbf" \
--read-xml file="gpx/osm/custom.osm" \
--merge \
--write-pbf file="custom_osm/hanoi_with_gpx.osm.pbf"
```