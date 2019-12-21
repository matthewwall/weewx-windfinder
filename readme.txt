windfinder - weewx extension that sends data to WindFinder
Copyright 2014 Matthew Wall

Installation instructions:

1) run the extension installer:

wee_extension --install weewx-windfinder.tgz

2) modify weewx.conf:

[StdRESTful]
    [[WindFinder]]
        station_id = WINDFINDER_STATION_ID
        password = WINDFINDER_PASSWORD

3) restart weewx

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start

For configuration options and details, see the comments in windfinder.py
