import fuzzywuzzy
from fuzzywuzzy import fuzz
import xlrd
import pandas as pd
from tqdm import tqdm
import argparse

"""
parser = argparse.ArgumentParser()
parser.add_argument("file1", type=str)
parser.add_argument("file2")

args = parser.parse_args()"""

f1p = "/Users/jaspergilley/Documents/INVO/gdr/2019-01-24-InventionReporting_Export_QbTx.xlsx"
f2p = "/Users/jaspergilley/Documents/INVO/gdr/2019-01-24-OSR_GRNTAWRD_table_Export.xlsx"

df1 = pd.read_excel(f1p)
df2 = pd.read_excel(f2p)
df = pd.DataFrame()

try:
    for itc1, row1 in tqdm(df1.iterrows(), total=len(df1.index.values)):
        highestRatio = 0
        for itc2, row2 in df2.iterrows():
            #print(itc1, itc2)
            if type(row1["Grant Number"]) != str or type(row2["Grant Number"]) != str:
                continue
            thisRatio = fuzz.ratio(row1["Grant Number"], row2["Grant Number"])
            if thisRatio > highestRatio:
                highestRatio = thisRatio
                df.at[itc1, "String1"] = row1["Grant Number"]
                df.at[itc1, "String2"] = row2["Grant Number"]
                df.at[itc1, "Similarity Score"] = thisRatio
except KeyboardInterrupt:
    df.to_csv("/Users/jaspergilley/Documents/INVO/gdr/export2.csv")