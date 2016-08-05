#!/usr/bin/python
# -*- coding: utf-8 -*-

import web
import requests
import xmltodict
import urllib
import json


class XiamiLyric:
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
                'Referer': 'http://www.xiami.com/song/playlist/id/' + id
            }
            url = 'http://www.xiami.com/song/playlist/id/' + id
            r = requests.get(url, headers=headers)

            info = xmltodict.parse(r.text)
            lyric_url = info['playlist']['trackList']['track'].get('lyric')

            if lyric_url:
                r = requests.get(lyric_url, headers=headers)
                r.encoding = 'utf-8'
                lyric = r.text
            else:
                lyric = ''

            info = {
                "lyric": lyric
            }
        except Exception, e:
            return 0
        if callback:
            return callback + '(' + json.dumps(info) + ')'
        else:
            return json.dumps(info)
