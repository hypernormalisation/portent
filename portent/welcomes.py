"""Welcome message functions for portent.
"""
import textwrap
from datetime import datetime

import portent.data as data
import portent.quotes as quotes


def welcome_message_basic(stream, name, version, quote_theme, columns):
    """Basic welcome screen."""
    if not quote_theme:
        quote_theme = 'satire'

    nc = int(columns / 2)

    q, a = quotes.get_quote_and_attribution_tuple(quote_theme)
    q = '"' + q + '"'
    a = f'- {a}'
    q_list = textwrap.wrap(q, nc - 5, break_long_words=False)

    stream.write(data.BOLD + '-'*nc+'\n')
    if name:
        stream.write(f': Welcome to {data.BLUE}{name}!\n')
    else:
        stream.write(': Welcome!\n')
    if version:
        stream.write(f'{data.WHITE}: Version: {data.CYAN}{version}\n')

    stream.write(f'{data.WHITE}: Inspirational quote of the day:\n')
    for l in q_list:
        stream.write(':   ' + data.MAGENTA + l + data.WHITE + '\n')

    attribution_length = nc
    if len(q) < nc:
        attribution_length = len(q) + 5

    stream.write(':' + data.PURPLE + a.rjust(attribution_length - 6) +
                 data.WHITE + '\n')
    stream.write('-'*nc+'\n')


def welcome_message_finance(stream, name, version, quote_theme, columns):
    """Finance themed welcome screen"""
    if not quote_theme:
        quote_theme = 'satire'

    stream.write(data.GREEN + data.BOLD)
    stream.write('$' * columns + '\n')
    stream.write(data.BOLD + data.GREEN)

    str1 = 'Welcome!'
    if name and version:
        str1 = f'Welcome to {name} v{version}'
    elif name:
        str1 = f'Welcome to {name}!'
    str2 = 'The great bulls of finance advise you:'
    str5 = datetime.utcnow().strftime('%D %T')
    q, a = quotes.get_quote_and_attribution_tuple(quote_theme)
    str3_base = '"' + q + '"'
    str3_list = textwrap.wrap(str3_base, columns - 10, break_long_words=False)
    str4 = f'- {a}'

    stream.write('$$$' + ''.center(columns - 6, ' ') + '$$$\n')
    stream.write('$$$' + data.RED + str1.center(columns - 6, ' ')
                 + data.GREEN + '$$$\n')
    stream.write('$$$' + data.RED + str5.center(columns - 6, ' ')
                 + data.GREEN + '$$$\n')
    stream.write('$$$' + data.RED + str2.center(columns - 6, ' ')
                 + data.GREEN + '$$$\n')
    stream.write('$$$' + ''.center(columns - 6, ' ') + '$$$\n')
    for str3 in str3_list:
        stream.write('$$$' + data.WHITE + str3.center(columns - 6, ' ')
                     + data.GREEN + '$$$\n')
    stream.write('$$$ ' + data.WHITE + str4.rjust(columns - 15, ' ')
                 + data.GREEN + '        $$$\n')
    stream.write('$$$' + ''.center(columns - 6, ' ') + '$$$\n')
    stream.write(data.GREEN)
    stream.write('$' * columns + '\n')
    stream.write(data.RESET)


welcomes = {
    'basic': welcome_message_basic,
    'finance': welcome_message_finance,
}
