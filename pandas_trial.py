import pandas as pd

po = [('Mon', 6421), ('Tue', 6412), ('Wed', 12416), ('Thu', 23483), ('Fri', 8978), ('Sat', 7657), ('Sun', 6555)]

# Generate dataframe from list and write to xlsx.
pd.DataFrame(po).to_excel('output.xlsx', header=False, index=False)