# $Id: install.py 1373 2015-10-14 13:50:32Z mwall $
# installer for WindFinder
# Copyright 2014 Matthew Wall

from setup import ExtensionInstaller

def loader():
    return WindFinderInstaller()

class WindFinderInstaller(ExtensionInstaller):
    def __init__(self):
        super(WindFinderInstaller, self).__init__(
            version="0.10",
            name='windfinder',
            description='Upload weather data to WindFinder.',
            author="Matthew Wall",
            author_email="mwall@users.sourceforge.net",
            restful_services='user.windfinder.WindFinder',
            config={
                'StdRESTful': {
                    'WindFinder': {
                        'station_id': 'INSERT_WINDFINDER_STATION_ID',
                        'password': 'INSERT_WINDFINDER_PASSWORD'}}},
            files=[('bin/user', ['bin/user/windfinder.py'])]
            )
