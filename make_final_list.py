"""
Author: Nicholas Novak
File Version: 0.5
Summary: Take a series of formatted csv files and combine them into one based upon recurring variables.
Contact: nnovak@umd.edu  |  Note: Contact for any support questions or bugs, send email with subject
"NGSS csv combiner report".

Written with all permissions for use by Michael Novak and any affiliated NGSS assiciates.


"""

from open_ref_file import open_ref_file

def make_final_list(all_lists):
    ''' A function to create a list of the reference floats, phrases, and counts.
    It will be used to vreate the rows of the final csv file.

    Parameters: 
    all_lists: a list containing lists representing each csv file's phrase counts.

    Returns: A list of lists that contains the reference floats and phrases as well as
    the csv phrase counts.
    '''

    final_csv_list = []
    float_list = []
    with open("MS Reference for elements of practices and CCCs.txt",'r') as file:
        file_lines = file.readlines()
        for i in range(len(file_lines)):
            try:
                fi = float(file_lines[i])
                float_list.append(file_lines[i].strip())
            except:
                pass
    final_csv_list.append(float_list)
    ref = open_ref_file("MS Reference for elements of practices and CCCs.txt")
    final_csv_list.append(ref)
    
    for i in range(len(all_lists)):
        app_list = [j.count for j in all_lists[i]]
        final_csv_list.append(app_list)
    
    return final_csv_list