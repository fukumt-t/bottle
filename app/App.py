#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
sys.path.append('../libs')

import bottle
from bottle import default_app, TEMPLATE_PATH
TEMPLATE_PATH.append('../views/')

from app.controller import *

class App(object):
    app = bottle.default_app()

    from bottle import run
    app.run(host='localhost', port=8080)
