1. Load `SAFI_God.csv` and `SAFI_Ruaca.csv` into Dataframes and explore their contents to determine how they should be joined.
2. Using the `SAFI_God` and `SAFI_Ruaca` csv files, create a Dataframe which is the result of an outer join using the `key_ID` column to join on.
3. What do you notice about the column names in the new Dataframe?
4. Using `shift`+`tab` in Jupyter examine the possible parameters for the `merge()` function.
5. Re-write the code so that the columns names which are common to both files have suffixes indicating the filename from which they come.
6. If you add the parameter `indicator=True`, what additional information is provided in the resulting Dataframe?