# load in the data file SAFI_crops
SAFI_crops = pd.___

# look at the first few rows of  that data
SAFI_crops.__

# filter the data to look at only the plots with maize

maize_farms = SAFI_crops

# save that to a separate.csv
maize_farms.to_csv('data/maize_farms.csv')

# sum to total area of crops per farm
crops_per_farm = SAFI_crops.__(__)
crops_per_farm.[__]__

# sum the total area of land per crop, across all farmers
land_per_crop = SAFI_crops.__(__)
land_per_crop.__
