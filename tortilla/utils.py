# -*- coding: utf-8 -*-

from formats import FormatBank, discover_json, discover_yaml
from munch import Munch as Bunch, munchify as bunchify

formats = FormatBank()

discover_json(formats, content_type='application/json')
discover_yaml(formats, content_type='application/x-yaml')


def run_from_ipython():
    return getattr(__builtins__, "__IPYTHON__", False)
