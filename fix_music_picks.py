#!/usr/bin/env python

import sys
import yaml
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import time

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

releases = yaml.load(open('_data/music-picks/2019.yml', 'r'))
for release in releases:
    if 'spotify' in release:
        print(release['artist'])
        print(release['title'])
        results = sp.search(q=release['title'],type='album', limit=20)
        print(results['albums']['items'][0]['external_urls']['spotify'])
        print('\n')
        time.sleep(0.5)
