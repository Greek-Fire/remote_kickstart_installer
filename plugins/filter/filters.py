#!/usr/bin/python

class FilterModule(object):
    ''' Nested dict filter '''

    def filters(self):
        return {
            'nesteddict2items': self.recurse
        }

    def recurse(self, nest):
        lis = []


        return lis 
