import numpy as np
import pandas as pd

class DF_Util():

    def __init__(self, df):
        self.df = df

    def train_val_test_split(self):
        mask = np.random.rand(len(df)) < 0.75
        self.train = self.df[mask]
        self.test = self.df[~mask]
        self.val = self.train[mask]
        
    def split_date(self, column):
        self.df[column] = pd.to_datetime(self.df[column])
        self.df["Date_Month"] = self.df[column].dt.month
        self.df["Date_Day"] = self.df[column].dt.day
        self.df["Date_Year"] = self.df[column].dt.year
        self.df.drop(column, axis=1)
        