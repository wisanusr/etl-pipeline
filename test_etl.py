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