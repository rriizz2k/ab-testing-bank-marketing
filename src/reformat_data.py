import pandas as pd

def load_data():
    df = pd.read_csv('data/bank-additional-full.csv', sep=';')
    df.to_csv('data/bank.csv', index=False)

load_data()