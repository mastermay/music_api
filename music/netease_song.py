#!/usr/bin/python
# -*- coding: utf-8 -*-  

import web
import requests
import xmltodict
import urllib
import json

class NeteaseSong:
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
                'Accept': '*/*',
                'Accept-Encoding': 'gzip,deflate,sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'music.163.com',
                'Referer': 'http://music.163.com/search/',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'
                }
            url = 'http://music.163.com/api/song/detail?ids=[' + id + ']'
            r = requests.get(url,headers=headers)

            info = r.json()
            location=info['songs'][0].get('mp3Url')
            album_name=info['songs'][0]['album'].get('name')
            songpic = info['songs'][0]['album'].get('picUrl')
            songpic_m = info['songs'][0]['album'].get('picUrl')
            songpic_l = info['songs'][0]['album'].get('picUrl')
            title = info['songs'][0].get('name')
            singer = info['songs'][0]['artists'][0].get('name')
            lyric_url = 'http://music.163.com/api/song/media?id=' + id
            
            if lyric_url and is_lyric:
                r = requests.get(lyric_url,headers=headers)
                info = r.json()
                if 'lyric' in info.keys():
                    lyric = info['lyric']
                else:
                    lyric = ''
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
                "location": location
            }
        except Exception, e:
            return e
        if callback :
            return callback + '(' + json.dumps(info) + ')'
        else :
            return json.dumps(info)