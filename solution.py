import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from pandas.api.types import is_object_dtype
import etl.data_loader as dl
import eda.eda_engine as eda


data_loader = dl.DataLoader("data/dataset.csv")
data_df = data_loader.load_data()

pass

eda_engine = eda.EDA_Engine(data_df)
eda_engine.overview()
eda_engine.granular_unique_categorical_values()

pass