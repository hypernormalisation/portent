__name__ = 'some_application'
__version__ = '1.2.2'

import sys
import prologue
import prologue.welcomes

# m = prologue.return_module_reference()
# print(m)
# print(m.keys())
# print(m['__name__'])

m = sys.modules[__name__]

prologue.welcomes.welcome_message(module=m)