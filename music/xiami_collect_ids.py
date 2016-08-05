#!/usr/bin/python
# -*- coding: utf-8 -*-  

import web
import requests
import xmltodict
import urllib
import json


class XiamiCollectID:
    def GET(self, id):
        try:
            data = web.input()
            # id = data.id
            if 'callback' in data.keys():
                callback = data.callback
            else:
                callback = ''
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X; en-us)    AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53',
                'Referer': 'http://www.xiami.com/song/playlist/id/' + id + '/type/3'
            }
            url = 'http://www.xiami.com/song/playlist/id/' + id + '/type/3'
            r = requests.get(url, headers=headers)
            info = xmltodict.parse(r.text)
            all = info['playlist']['trackList']['track']

            all_songs = [];
            for item in all:
                # return item
                all_songs.append(item['song_id'])
        except Exception, e:
            return 0
        if callback:
            return callback + '(' + json.dumps(all_songs) + ')'
        else:
            return json.dumps(all_songs)
