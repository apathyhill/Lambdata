"""Unit testing for the Data Functions of Lambdata"""

import unittest
import numpy as np
import pandas as pd
import data_functions as dfn

util = dfn.DF_Util()

class LambdataTests(unittest.TestCase):
    def test_trainvaltestsplit(self):
        df_test = pd.DataFrame(data={"column": [0]*1000})
        tr, v, te = util.train_val_test_split(df_test)
        self.assertAlmostEqual(len(tr)/1000, 0.75*0.75, places=1)
        self.assertAlmostEqual(len(te)/1000, 0.25, places=1)
        self.assertAlmostEqual(len(v)/1000, 0.75*0.25, places=1)
            
    def test_datetime(self):
        df_test = pd.DataFrame(data={"date": ["2019-06-30"]})
        df_test = util.split_date(df_test, "date")
        assert(df_test["Date_Month"][0], 6)
        assert(df_test["Date_Day"][0], 30)
        assert(df_test["Date_Year"][0], 2019)

if __name__ == "__main__":
    unittest.main()
