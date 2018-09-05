## all of the __ are blanks fo you to fill in

# load in the SAFI_clean dataset
df_clean = pd.__('data/SAFI_clean.csv')

# make a new df with the dummy varialbes
# check the help on get_dummies to see how it can work for our dataset
__ = df_clean['items_owned'].str.get_dummies(__)

# look at the first few rows, make a new cell here


print('total per item',__)
# total sum can be thought of as a sum of the sums
print('total items:', __)


# extra challenge: concatenate the new df to the old one
df_clean = pd.__([df_clean,__]) # read help to see what
df_clean.head()

# extra extra challenge
# use groupby to get item counts per respondent_wall_type
# hint you can get the list of items via items_df.columns
