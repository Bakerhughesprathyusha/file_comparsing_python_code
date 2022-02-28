import pandas as pd
import glob
import os
import collections

folder = './Desktop/extracted'
# Here we are storing folder_names in list_of_folder_names
list_of_folder_names = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder,name))]
print(list_of_folder_names)

not_matched_folder_column_names =[]
not_matched_folder_csvfile_data_value = []

for each_folder in list_of_folder_names:
    print(each_folder)
    file_name_in_category = glob.glob('Desktop/category/'+ each_folder + '/*.csv')
    file_name_in_extracted = glob.glob('Desktop/extracted/'+ each_folder + '/*.csv')

    # loading category data in df_c variable using pandas
    df_c = pd.read_csv(file_name_in_category[0])
    # loading extracted data in df_e variable using pandas
    df_e = pd.read_csv(file_name_in_extracted[0])

    # storing the column names of category in columnnames1
    columnnames1 = list(df_c)
    # storing the column names of category in columnnames2
    columnnames2 = list(df_e)

    if collections.Counter(columnnames1) == collections.Counter(columnnames2):
        # if column names are matched the will compare data else will skip the folder
        print (f"Number of columns and Names match for {each_folder} Comparison possible for category and extraction")
    else:
        not_matched_folder_column_names.append(each_folder)
        print ("Number of columns and Names are not matching!!! Please check the input!")
        continue

    if df_c.equals(df_e):
        print(f"same data in {each_folder}")
    else:
        not_matched_folder_csvfile_data_value.append(each_folder)
        print("not matching with data")
    
    print("\n\n")

print("Column names not matched so we are not comparing the values for this folders:- ", not_matched_folder_column_names)
print("column names matched but values in it are not matched:- ", not_matched_folder_csvfile_data_value)