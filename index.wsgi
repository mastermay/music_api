#!/usr/bin/python
# -*- coding: utf-8 -*-  

import web

from music import *

urls = (
    '/', 'Index',

    '/music/(\d+)', 'XiamiSong',
    '/music/lyrics/(\d+)', 'XiamiLyric',
    '/music/songs/(\d+)', 'XiamiSong',
    '/music/albums/(\d+)', 'XiamiAlbum',
    '/music/artists/(\d+)', 'XiamiArtist',
    '/music/collections/(\d+)', 'XiamiCollect',

    '/music/albums/ids/(\d+)', 'XiamiAlbumID',
    '/music/artists/ids/(\d+)', 'XiamiArtistID',
    '/music/collections/ids/(\d+)', 'XiamiCollectID',

    '/music/xiami/(\d+)', 'XiamiSong',
    '/music/xiami/lyrics/(\d+)', 'XiamiLyric',
    '/music/xiami/songs/(\d+)', 'XiamiSong',
    '/music/xiami/albums/(\d+)', 'XiamiAlbum',
    '/music/xiami/artists/(\d+)', 'XiamiArtist',
    '/music/xiami/collections/(\d+)', 'XiamiCollect',

    '/music/xiami/albums/ids/(\d+)', 'XiamiAlbumID',
    '/music/xiami/artists/ids/(\d+)', 'XiamiArtistID',
    '/music/xiami/collections/ids/(\d+)', 'XiamiCollectID',

    '/music/163/(\d+)', 'NeteaseSong',
    '/music/163/lyrics/(\d+)', 'NeteaseLyric',
    '/music/163/songs/(\d+)', 'NeteaseSong',
    '/music/163/albums/(\d+)', 'NeteaseAlbum',
    '/music/163/artists/(\d+)', 'NeteaseArtist',
    '/music/163/collections/(\d+)', 'NeteaseCollect',

    '/music/163/albums/ids/(\d+)', 'NeteaseAlbumID',
    '/music/163/artists/ids/(\d+)', 'NeteaseArtistID',
    '/music/163/collections/ids/(\d+)', 'NeteaseCollectID'

)

app = web.application(urls, globals())
application = app.wsgifunc()

if __name__ == "__main__":
    app.run()
