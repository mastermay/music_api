#!/usr/bin/python
# -*- coding: utf-8 -*-  

import web
import requests
import xmltodict
import urllib
import json


class NeteaseCollectID:
    def GET(self, id):
        try:
            data = web.input()
            # id = data.id
            if 'callback' in data.keys():
                callback = data.callback
            else:
                callback = ''
            headers = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip,deflate,sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'music.163.com',
                'Referer': 'http://music.163.com/search/',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'
            }
            url = 'http://music.163.com/api/playlist/detail?id=' + id
            r = requests.get(url, headers=headers)

            info = r.json()
            # return r.text
            all = info['result']['tracks']
            # return all
            all_songs = [];
            for item in all:
                # return item
                all_songs.append(item.get('id'))
        except Exception, e:
            return e
        if callback:
            return callback + '(' + json.dumps(all_songs) + ')'
        else:
            return json.dumps(all_songs)
