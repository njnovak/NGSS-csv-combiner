"""
Author: Nicholas Novak
File Version: 0.5
Summary: Take a series of formatted csv files and combine them into one based upon recurring variables.
Contact: nnovak@umd.edu  |  Note: Contact for any support questions or bugs, send email with subject
"NGSS csv combiner report".

Written with all permissions for use by Michael Novak and any affiliated NGSS assiciates.


"""

def open_ref_file(filename):
    """ Open the reference file and create a dictionary with all of the phrases and questions to be used.
    
    Parameters:
    filename (string): A string containing the name of the reference file.
    
    Returns:
    A dictionary with all phrases and questions included.
    
    TODO:
    Check out dict size
    """
    
    ref_dict = []
    with open(filename,'r') as file:
        file_lines = file.readlines()
        for i in range(len(file_lines)):
            try:
                fi = float(file_lines[i])
                ref_dict.append(file_lines[i+1].strip())
            except:
                pass
#     print(ref_dict)
    return(ref_dict)