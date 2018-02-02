Clone this repo:
https://github.com/mariiagracheva/volta

Create virtual environment inside a directory:
$ virtualenv env
$ source env/bin/activate

Install the requirements:
$ pip install -r requirements.txt

Start running server from command line:
$ python server.py

Open up your browser and navigate to 'localhost:5000/'


Blue clusters of working Volta stations are displayed on the map. For that I used GoogleMaps MarkerClusterer.
Stations that have a different from "active" status are displayed with single pins: "needs service" - red pins,  "under construction" - yellow pins.
This data presentation gives an understanding whethier a person can find a working station close to a non-active one or not.
