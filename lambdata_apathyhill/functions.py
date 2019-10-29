import numpy as np
import pandas as pd

def train_val_test_split(df):
    mask = np.random.rand(len(df)) < 0.75
    train = df[mask]
    test = df[~mask]
    val = train[mask]
    return (train, val, test)

def split_date(df, column):
    df[column] = pd.to_datetime(df[column])
    df["Date_Month"] = df[column].dt.month
    df["Date_Day"] = df[column].dt.day
    df["Date_Year"] = df[column].dt.year
    df.drop(column, axis=1)
    return df