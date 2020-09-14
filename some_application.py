__name__ = 'tradingsolutions'
__version__ = '1.2.2'

import portent

portent.welcome(name=__name__, version=__version__, theme='basic')

# Test it only runs once per session.
portent.welcome()