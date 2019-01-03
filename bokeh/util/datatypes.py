#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2018, Anaconda, Inc. All rights reserved.
#
# Powered by the Bokeh Development Team.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------
'''

'''

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function, unicode_literals

import logging
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports

# External imports

# Bokeh imports

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

__all__ = (
    'MultiValuedDict',
)

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

class MultiValuedDict(object):
    ''' Store a mapping from keys to multiple values with minimal overhead.

    Avoids storing empty collecctions.

    '''

    def __init__(self):
        '''

        '''
        self._dict = dict()

    def add_value(self, key, value):
        '''

        '''
        if key is None:
            raise ValueError("Key is None")

        if value is None:
            raise ValueError("Can't put None in this dict")

        if isinstance(value, set):
            raise ValueError("Can't put sets in this dict")

        existing = self._dict.get(key)
        if existing is None:
            self._dict[key] = value
        elif isinstance(existing, set):
            existing.add(value)
        else:
            self._dict[key] = set([existing, value])

    def get_all(self, k):
        '''

        '''
        existing = self._dict.get(k)
        if existing is None:
            return []
        elif isinstance(existing, set):
            return list(existing)
        else:
            return [existing]

    def get_one(self, k, duplicate_error):
        '''

        '''
        existing = self._dict.get(k)
        if isinstance(existing, set):
            if len(existing) == 1:
                return next(iter(existing))
            else:
                raise ValueError(duplicate_error + (": %r" % (existing)))
        else:
            return existing

    def remove_value(self, key, value):
        '''

        '''
        if key is None:
            raise ValueError("Key is None")

        existing = self._dict.get(key)
        if isinstance(existing, set):
            existing.discard(value)
            if len(existing) == 0:
                del self._dict[key]
        elif existing == value:
            del self._dict[key]
        else:
            pass

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
