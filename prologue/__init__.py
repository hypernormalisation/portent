# -*- coding: utf-8 -*-
"""Python package providing horrifying welcome messages for your application.
"""
__name__ = 'prologue'
__author__ = 'Stephen Ogilvy'

import random
import sys
import textwrap
from datetime import datetime

#
# def return_random_quote():
#     """Return a random quote from the welcome_quote_list."""
#     random.seed(hash(str(datetime.utcnow())) * random.gauss(0, 1))
#     return random.choice(welcome_quote_list)
#
#
# def return_random_attribution():
#     """Return a random quote from the attribution list."""
#     random.seed(hash(str(datetime.utcnow())) * random.gauss(0, 1))
#     return random.choice(attribution_list)
#
#
# ##########################################################################
# # Welcome message colours.
# ##########################################################################
# def welcome_message(on=True):
#     if not cfg.has_displayed_welcome:
#         if not on:
#             return
#         sys.stdout.write(data.GREEN)
#         sys.stdout.write('$' * total_columns + '\n')
#         sys.stdout.write('$' * total_columns + '\n')
#         sys.stdout.write(data.BOLD + data.GREEN)
#         str1 = 'Welcome to tradingsolutions v{}'.format(tradingsolutions.__version__)
#         str2 = 'Are you ready to make big money?'
#         str5 = datetime.utcnow().strftime('%D %T')
#         str3_base = '"' + return_random_quote() + '"'
#         str3_list = textwrap.wrap(str3_base, total_columns - 10, break_long_words=False)
#         str4 = '- ' + return_random_attribution()
#         sys.stdout.write('$$$' + ''.center(total_columns - 6, ' ') + '$$$\n')
#         sys.stdout.write('$$$' + data.RED + str1.center(total_columns - 6, ' ')
#                          + data.GREEN + '$$$\n')
#         sys.stdout.write('$$$' + data.RED + str5.center(total_columns - 6, ' ')
#                          + data.GREEN + '$$$\n')
#         sys.stdout.write('$$$' + data.RED + str2.center(total_columns - 6, ' ')
#                          + data.GREEN + '$$$\n')
#         sys.stdout.write('$$$' + ''.center(total_columns - 6, ' ') + '$$$\n')
#         for str3 in str3_list:
#             sys.stdout.write('$$$' + data.RED + str3.center(total_columns - 6, ' ')
#                              + data.GREEN + '$$$\n')
#         sys.stdout.write('$$$ ' + data.RED + str4.rjust(total_columns - 10, ' ')
#                          + data.GREEN + '   $$$\n')
#         sys.stdout.write('$$$' + ''.center(total_columns - 6, ' ') + '$$$\n')
#         sys.stdout.write(data.GREEN)
#         sys.stdout.write('$' * total_columns + '\n')
#         sys.stdout.write('$' * total_columns + '\n')
#         sys.stdout.write(data.RESET)
#         cfg.has_displayed_welcome = True
#         return
