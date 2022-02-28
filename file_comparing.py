import pandas as pd
import collections
df_c = pd.read_csv("Desktop/MAPS_BHARUN_b491bbf9-36be-4827-aa08-2fddbe10452d.csv")
#print(df_c)
df_e = pd.read_csv("Desktop/part-00000-ed26d85e-23d3-4b06-b3a7-110f96447143-c000.csv")
#print(df_e)

columnnames1 = list(df_c)
columnnames2 = list(df_e)

if collections.Counter(columnnames1) == collections.Counter(columnnames2):
    print ("Number of columns and Names match, Comparison possible...\n\n")
else:
    print ("Number of columns and Names are not matching!!! Please check the input!")

if df_c.equals(df_e):
    print("same data")
else:
    print("not matching with data")
