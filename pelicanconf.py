#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'jaycode'
SITENAME = 'TeguhWijaya.com'
SITEURL = 'http://teguhwijaya.com'

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Home', 'http://teguhwijaya.com'),
         ('Technical', 'http://teguhwijaya.com/category/technical'),
         ('Value Analysis', 'http://teguhwijaya.com/category/value-analysis'))

# Social widget
SOCIAL = ()
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins', './themes/voce/plugins']
PLUGINS = ['pelican-ipynb.markup', 'pelican-assets', 'assets']
THEME = "./themes/voce"

GOOGLE_ANALYTICS_ID = 'UA-55135714-1'
GOOGLE_ANALYTICS_PROP = 'teguhwijaya.com'
MANGLE_EMAILS = True
GLOBAL_KEYWORDS = 'Artificial Intelligence, Finance, Algo Trading'
FUZZY_DATES = True
USER_LOGO_URL = 'images/1.png'