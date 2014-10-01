#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tarek Ziadé'
SITENAME = 'Les Foulé.es'
SITEURL = ''    #http://foule.es'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MENUITEMS = [('Accueil', '/')]
STATIC_PAGES = {}
THEME = "themes/tarek"

DATE_FORMATS = {'fr': ('fr_FR','%a %d %b %Y'),
                }
DISQUS_SITENAME = "foulees"

ARTICLE_SAVE_AS = ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}.html'
PAGE_SAVE_AS = PAGE_URL = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'

PDF_GENERATOR = False
FEED_RSS = 'feed'
TAG_FEED_RSS  = 'tag/%s/feed'

