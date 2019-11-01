"""Various functions to use with the Pandas Libraries"""

import numpy as np
import pandas as pd

class DF_Util():

    def __init__(self):
        """This function currently has no functionality"""
        return

    def train_val_test_split(self, df, test_percent=0.75, val_percent=0.75):
        """Split a DataFrame into training, validation, and test sets"""
        mask_test = np.random.rand(len(df)) > test_percent
        train = df[~mask_test]
        test = df[mask_test]

        mask_val = np.random.rand(len(train)) > val_percent
        val = train[mask_val]
        train = train[~mask_val]

        return (train, val, test)
        
    def split_date(self, df, column):
        """Splits the date of a DataFrame column into its days, months, and years."""
        df[column] = pd.to_datetime(df[column])
        df["Date_Month"] = df[column].dt.month
        df["Date_Day"] = df[column].dt.day
        df["Date_Year"] = df[column].dt.year
        df.drop(column, axis=1)

        return df