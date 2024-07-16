# Scripts

Scripts to process raw GPX files.

### Setup 

```
python3 -m venv ~/.venv/better-osrm-routes
source ~/.venv/better-osrm-routes/bin/activate
pip install -r requirements.txt
```

### Scripts

Make maps of all GPX routes:

```
python make-maps.py
```

Run `docker compose up` to launch OSRM and get nodes:

```
python get-nodes.py
```