#!/usr/bin/python
# -*- coding: utf-8 -*-  

import web
import requests
import xmltodict
import urllib
import json


class XiamiSong:
    def GET(self, id):
        try:
            data = web.input()
            # id = data.id
            if 'callback' in data.keys():
                callback = data.callback
            else:
                callback = ''
            if 'lyric' in data.keys():
                is_lyric = 1
            else:
                is_lyric = 0
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X; en-us)    AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53',
                'Referer': 'http://www.xiami.com/song/playlist/id/' + id
            }
            url = 'http://www.xiami.com/song/playlist/id/' + id
            r = requests.get(url, headers=headers)
            info = xmltodict.parse(r.text)
            location = info['playlist']['trackList']['track']['location']
            album_name = info['playlist']['trackList']['track']['album_name']
            songpic = info['playlist']['trackList']['track'].get('album_pic').replace('.jpg', '_2.jpg')
            songpic_m = info['playlist']['trackList']['track'].get('album_pic').replace('.jpg', '_1.jpg')
            songpic_l = info['playlist']['trackList']['track'].get('album_pic')
            title = info['playlist']['trackList']['track'].get('songName')
            singer = info['playlist']['trackList']['track'].get('artist')
            lyric_url = info['playlist']['trackList']['track'].get('lyric')

            num = int(location[0])
            avg_len, remainder = int(len(location[1:]) / num), int(len(location[1:]) % num)
            result = [location[i * (avg_len + 1) + 1: (i + 1) * (avg_len + 1) + 1] for i in range(remainder)]
            result.extend([location[(avg_len + 1) * remainder:][i * avg_len + 1: (i + 1) * avg_len + 1] for i in
                           range(num - remainder)])
            location_url = urllib.unquote(
                ''.join([''.join([result[j][i] for j in range(num)]) for i in range(avg_len)]) + \
                ''.join([result[r][-1] for r in range(remainder)])).replace('^', '0')

            if lyric_url and is_lyric:
                r = requests.get(lyric_url, headers=headers)
                r.encoding = 'utf-8'
                lyric = r.text
            else:
                lyric = ''

            info = {
                "title": title,
                "singer": singer,
                "album": album_name,
                "album_pic": songpic,
                "album_pic_m": songpic_m,
                "album_pic_l": songpic_l,
                "lyric": lyric,
                "location": location_url
            }
        except Exception, e:
            return 0
        if callback:
            return callback + '(' + json.dumps(info) + ')'
        else:
            return json.dumps(info)
