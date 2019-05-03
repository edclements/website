#!/usr/bin/env python

import yaml
import spotipy

sp = spotipy.Spotify()

releases = yaml.load(open('_data/music-picks/2019.yml', 'r'))
for release in releases:
    if 'spotify' in release:
        print(release['artist'])
        print(release['title'])
        print('\n')
        results = sp.search(q=release['title'], limit=20)
        print(results)
        print('\n')
        time.sleep(0.5)
