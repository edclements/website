#!/usr/bin/env python

import sys
import yaml
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import time

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

releases = yaml.load(open('_data/music-picks/2018.yml', 'r'))
for release in releases:
    if 'spotify' not in release:
        print(release['artist'])
        print(release['title'])
        try:
            results = sp.search(q=release['title'],type='album', limit=20)
            url = results['albums']['items'][0]['external_urls']['spotify']
            print(url)
            release['spotify'] = url
        except:
            print('not found')
        finally:
            print('\n')
            time.sleep(0.5)

with open('_data/music-picks/2018.yml', 'w') as outfile:
    yaml.dump(releases, outfile, default_flow_style=False)
