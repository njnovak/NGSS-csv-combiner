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
from csv_parser import open_csv


if __name__ == "__main__":
    input_list = []
    for i in grab_all_csv_files()[0]:
        print(i)
        row_list = open_csv(i)
        input_list.append(row_list)
        
    with open('output.csv','w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        final_list = make_final_list(input_list)
        
        
        for j in range(len(final_list[0])):
            row_list = []
            for k in range(len(final_list)):
                row_list.append(final_list[k][j])
            
            wr.writerow(row_list)