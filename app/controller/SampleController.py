#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, jinja2_template as template
from app.service.SampleService import *

class SampleController(object):
    @route('/all')
    def all():
        list = SampleService.get_list()
        print(list)

        return template('index', list=list)
