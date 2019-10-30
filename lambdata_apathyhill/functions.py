import numpy as np
import pandas as pd

class DF_Util():

    def __init__(self):

    def train_val_test_split(self, df, test_percent, val_percent):
        mask_test = np.random.rand(len(df)) > test_percent
        train = df[~mask_test]
        test = df[mask_test]

        mask_test = np.random.rand(len(df)) > val_percent
        val = train[mask]
        train = train[~mask]

        return (train, val, vest)
        
    def split_date(self, df, column):
        df[column] = pd.to_datetime(df[column])
        df["Date_Month"] = df[column].dt.month
        df["Date_Day"] = df[column].dt.day
        df["Date_Year"] = df[column].dt.year
        df.drop(column, axis=1)
        