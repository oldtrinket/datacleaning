# make a script that cleans the xlsx file and saves it as a csv file

import pandas as pd
import numpy

# read the xlsx file

df = pd.read_excel('HG Gadget Retails.xlsx')

# drop the rows with missing values

df = df.dropna()

# save the cleaned data as a csv file

df.to_csv('data_cleaned.csv', index=False)

print('Data cleaned and saved as data_cleaned.csv')

# end of script

