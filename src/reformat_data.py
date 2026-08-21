import pandas as pd

def reformat_data():
    df = pd.read_csv('data/bank-additional-full.csv', sep=';')
    df.to_csv('data/bank.csv', index=False)

reformat_data()