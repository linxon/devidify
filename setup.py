#!/usr/bin/env python

from distutils.core import setup

setup(name = 'Devidify',
      version = '1.14',
      description = 'A humble little hack for extracting audio tracks from DVDs.',
      author = 'Matthew Newton',
      author_email = 'devidify@mahnamahna.net',
      license = 'GPL version 2',
      url = 'http://www.mahnamahna.net/devidify',
      scripts = ['devidify'],
      data_files = [('devidify', ['devidify.glade', 'README', 'TODO', 'COPYING', 'NEWS']),
                    ('applications', ['devidify.desktop'])],
      long_description = '''
Devidify is a humble little hack for extracting audio tracks
from DVDs. It runs on Linux systems where the following tools
are available: mplayer, lsdvd, lame (for mp3 encoding), oggenc
(for ogg encoding). PyGTK is also required.'''
      )
