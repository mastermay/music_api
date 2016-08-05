#!/usr/bin/python
# -*- coding: utf-8 -*-

import web
import requests
import xmltodict
import urllib
import json


class Index:
    def GET(self):
        # return 'api'
        music = {
            'xiami_song': 'https://api.lostg.com/music/xiami/songs/{id}',
            'xiami_artist': 'https://api.lostg.com/music/xiami/artists/{id}',
            'xiami_lyric': 'https://api.lostg.com/music/xiami/lyrics/{id}',
            'xiami_collection': 'https://api.lostg.com/music/xiami/collections/{id}',
            'xiami_album': 'https://api.lostg.com/music/xiami/albums/{id}',

            'xiami_artist_ids': 'https://api.lostg.com/music/xiami/artists/ids/{id}',
            'xiami_collection_ids': 'https://api.lostg.com/music/xiami/collections/ids/{id}',
            'xiami_album_ids': 'https://api.lostg.com/music/xiami/albums/ids/{id}',

            'netease_song': 'https://api.lostg.com/music/163/songs/{id}',
            'netease_artist': 'https://api.lostg.com/music/163/artists/{id}',
            'netease_lyric': 'https://api.lostg.com/music/163/lyrics/{id}',
            'netease_collection': 'https://api.lostg.com/music/163/collections/{id}',
            'netease_album': 'https://api.lostg.com/music/163/albums/{id}',

            'netease_artist_ids': 'https://api.lostg.com/music/163/artists/ids{id}',
            'netease_collection_ids': 'https://api.lostg.com/music/163/collections/ids/{id}',
            'netease_album_ids': 'https://api.lostg.com/music/163/albums/ids/{id}'
        }
        api = {
            'music': music,
            'latex': 'to be continued'
        }
        return json.dumps(api, indent=1)
