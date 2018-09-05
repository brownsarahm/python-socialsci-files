# Try to answer the following questionns, by modifying the following code
# in which months do the most farmers lack food?
# what is the average number of months farmers lack food?
# how many farmers never lack food? - how does this impact our average?
# does village relate to food shortage? housing type?

# recall the counting items exercise
# create dummy variales for each of the values in
lack_food_df = df_clean['months_lack_food'].str.__

# this format will add a column
#  -- hint for summing: is axis 1
lack_food_df['count_lack_food'] = ___

# sum down columns, to get total per month
print('count per month',__)


# concatenate this back to the whole data for further analyses

# use groupby to analyze the relationship between food shortage and other varialbes
# recal
