1. Load `SN7577i_aa.csv` and `SN7577i_bb.csv` into dataframes and explore their contents to determine how they should be joined.
2. Using the `SN7577i_aa` and `SN7577i_bb` csv files, create a dataframe which is the result of an outer join using the 'Id' column to join on.
3. What do you notice about the column names in the new dataframe?
4. Using shift+ tab in Jupyter examine the possible parameters for the `merge` method.
5. re-write the code so that the columns names which are common to both files have suffixes indicating the filename from which they come
6. If you add the parameter 'indicator=True', what additional information is provided in the resulting dataframe?