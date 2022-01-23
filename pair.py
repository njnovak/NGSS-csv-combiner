"""
Author: Nicholas Novak
File Version: 0.5
Summary: Take a series of formatted csv files and combine them into one based upon recurring variables.
Contact: nnovak@umd.edu  |  Note: Contact for any support questions or bugs, send email with subject
"NGSS csv combiner report".

Written with all permissions for use by Michael Novak and any affiliated NGSS assiciates.


"""

class Pair(object):
    '''
    This class defines a custom data type. Essentially, a Pair serves as a mutable tuple.
    For this application, phrase will be a string and count an integer.
    '''
    def __init__(self,phrase,count):
        self.phrase = phrase
        self.count = count
