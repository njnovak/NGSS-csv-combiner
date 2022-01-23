"""
Author: Nicholas Novak
File Version: 0.5
Summary: Take a series of formatted csv files and combine them into one based upon recurring variables.
Contact: nnovak@umd.edu  |  Note: Contact for any support questions or bugs, send email with subject
"NGSS csv combiner report".

Written with all permissions for use by Michael Novak and any affiliated NGSS assiciates.


"""
import os

def grab_all_csv_files():
    ''' A function to locate all legal csv files to combine

    Parameters: None

    Returns: A list of all local csv files to combine

    TODO: Find local files
    '''
    ret_list = []
    local_files = os.listdir(os.getcwd())
    for filename in local_files:
        if "Elements of NGSS Dimensions.csv" in filename:
            ret_list.append(filename)


    return([ret_list])
