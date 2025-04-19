import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import openhouse.etl.data_loader as dl

from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder

class DataEncoder():
    def __init__(self, data_df, dtype:str='ordinal'):
        self.data_df = data_df
        if dtype == 'ordinal':
            self.encoder = OrdinalEncoder
        elif dtype == 'onehot':
            self.encoder = OneHotEncoder
    
    def encode_data(self):
        for col_name in self.data_df.columns:
            ordered_options = np.sort(self.data_df[col_name].unique())
            print(f"{col_name}: {ordered_options}")
            # enc = self.encoder()
            # self.data_df[col_name] = self.encoder().fit_transform(self.data_df[[col_name]])

    

if __name__ == "__main__":
    pass
