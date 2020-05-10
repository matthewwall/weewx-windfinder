windfinder - weewx extension that sends data to WindFinder
Copyright 2014-2020 Matthew Wall
Distributed under the terms of the GNU Public License (GPLv3)

Installation instructions:

1) download

wget -O weewx-windfinder.zip https://github.com/matthewwall/weewx-windfinder/archive/master.zip

2) run the extension installer:

wee_extension --install weewx-windfinder.zip

3) modify weewx.conf:

[StdRESTful]
    [[WindFinder]]
        station_id = WINDFINDER_STATION_ID
        password = WINDFINDER_PASSWORD

4) restart weewx

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start

For configuration options and details, see the comments in windfinder.py
