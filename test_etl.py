import pandas as pd
from datetime import datetime

dfInput = pd.read_csv('sample_products.csv')
dfOutput = pd.read_csv('output/cleaned_products.csv')

with open('output/test_result.txt', 'a') as f:
    f.write(datetime.now().strftime("%d-%m-%Y %H:%M:%S") + '\n')

    if dfOutput.dtypes['unit_price'] == 'int64':
        f.write("Case 1: Pass\n")
    else:
        f.write("Case 1: Fail\n")

        
    merged = pd.merge(dfInput, dfOutput, on='product_id', suffixes=('_input', '_output'))
    diff = merged['unit_price_output'] - merged['unit_price_input']
    if ((diff >= 0) & (diff <= 1)).all():
        f.write("Case 2: Pass\n")
    else:
        f.write("Case 2: Fail\n")