![N|Solid](http://is2.mzstatic.com/image/thumb/Purple111/v4/a0/3d/98/a03d98cb-34ad-06f6-cc1f-225f7e3a97a2/source/175x175bb.jpg)

# Nextdoor iOS Free Item Check


This script uses the unofficial private phone API to pull free items from the classifieds section for your Nextdoor neighborhood.

### Dependencies

 - You'll need to retrieve your API credentials via a proxy though this site - https://stevesie.com/apps/nextdoor-api
 - Link your phone via their app and make a note of the `trace_uuid`, `authorization`, `cookie`, `nd_id_token` and `nd_signature` params
 - This script will run locally, but it is build to run as a background process on a server. I recommend https://pythonanywhere.com

### How to launch it

1. Clone the Repository
```sh
$ git clone https://github.com/ramsaymax/NextdoorCheck.git
```
2. run with
```sh
$ python nextdoorCheck.py
```
