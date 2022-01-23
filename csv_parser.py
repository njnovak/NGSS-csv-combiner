"""
Author: Nicholas Novak
File Version: 0.5
Summary: Take a series of formatted csv files and combine them into one based upon recurring variables.
Contact: nnovak@umd.edu  |  Note: Contact for any support questions or bugs, send email with subject
"NGSS csv combiner report".

Written with all permissions for use by Michael Novak and any affiliated NGSS assiciates.


"""
import csv
from pair import Pair
from make_final_list import make_final_list
from open_ref_file import open_ref_file
from grab_all_csv_files import grab_all_csv_files


def open_csv(csv_name):
    ref = open_ref_file("MS Reference for elements of practices and CCCs.txt")

    
    with open(csv_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_list = []
        # Create a list of all phrases in a given file
        for row in csv_reader:
            if row[1] in ref:
                csv_list.append(row[1])
    out_list = []
    ref_list = open_ref_file("MS Reference for elements of practices and CCCs.txt")
    temp_list = [Pair(phrs,0) for phrs in ref_list]

    indices = [l for l in csv_list if l in ref_list]

    
    c = 0
    for j in csv_list:

        for k in range(len(temp_list)):

            if j in temp_list[k].phrase:
                temp_list[k].count+=1
    return temp_list


