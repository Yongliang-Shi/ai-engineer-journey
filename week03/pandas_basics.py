# Lab reagent inventory

import pandas as pd

reagent = ['Hydrochloric Acid', 'Sodium Hydroxide', 'Sodium Chloride', 'Ethanol', 'Isopropanol']
formula = ['HCl', 'NaOH', 'NaCl', 'C2H5OH', 'C3H8OH']
concentration_molar = [12.1, 2.0, 5.0, 8.8, 13.0]
stock_ml = [500, 400, 250, 300, 100]
hazard_class = ['corrosive', 'corrosive', 'none', 'flammable', 'flammable']

# Dict to DataFrame
reagent_dict = {'reagent': reagent, 'formula': formula, 'concentration_molar': concentration_molar, 'stock_ml': stock_ml, 'hazard_class': hazard_class}
df = pd.DataFrame(reagent_dict)

# Custom row index
row_labels = ['A', 'B', 'C', 'D', 'E']
df.index = row_labels

# Column selection: both forms
# As a series
print(df['formula'])

# As a single-column DataFrame
print(df[['formula']])

# .loc row/column selections
# Select the full row of reagent NaCl
print(df.loc[['C'], :])

# Select the formula and stock of reagent HCl, NaOH
print(df.loc[['A', 'B'], ['formula', 'stock_ml']])

# .iloc positional selection
print(df.iloc[[2], :])

# Select the formula and stock of reagent HCl, NaOH
print(df.iloc[[0, 1], [1, 3]])

# Boolean filtering
low_stock = df[df['stock_ml'] < 200]
print(low_stock)