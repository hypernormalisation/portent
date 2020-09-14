# -*- coding: utf-8 -*-
"""Python package providing horrifying welcome messages for your application.
"""
__name__ = 'portent'
__author__ = 'Stephen Ogilvy'

import shutil
import sys

import portent.data as data
import portent.welcomes


def welcome(stream=sys.stdout,
            theme='basic', name=None, version=None,
            quote_theme=None, columns=None,
            ):

    # Only run the welcome screen once per session
    if data.HAS_PRINTED:
        return

    # Set the width
    if not columns:
        columns = shutil.get_terminal_size().columns

    # Get the relevant welcome function and call it
    f = None
    try:
        f = portent.welcomes.welcomes[theme]
    except KeyError as k:
        print(f'theme: {k} not recognised.')
    f(stream, name, version, quote_theme, columns)

    # Register that we have run a welcome message this session
    data.HAS_PRINTED = True

    # Reset the ANSI formatting of the stream.
    stream.write(data.RESET)

