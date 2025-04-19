import pandas as pd
import numpy as np
from pandas.api.types import is_object_dtype
import matplotlib.pyplot as plt

# from pandas.api.types import is_numeric_dtype
# from pandas.api.types import is_object_dtype
# from pandas.api.types import is_string_dtype
# from pandas.api.types import is_datetime64_any_dtype as is_datetime
# from pandas.api.types import is_timedelta64_dtype
# from pandas.api.types import is_bool_dtype
# from pandas.api.types import is_categorical_dtype
# from pandas.api.types import is_integer_dtype
# from pandas.api.types import is_float_dtype
# from pandas.api.types import is_unsigned_integer_dtype
# from pandas.api.types import is_signed_integer_dtype
# from pandas.api.types import is_floating_dtype
# from pandas.api.types import is_complex_dtype
# from pandas.api.types import is_datetime64tz_dtype
# from pandas.api.types import is_period_dtype
# from pandas.api.types import is_sparse
# from pandas.api.types import is_interval_dtype
# from pandas.api.types import is_object_dtype
# from pandas.api.types import is_string_dtype


# Set the default figure size for matplotlib
#plt.rcParams['figure.figsize'] = [10, 5]

class EDA_Engine():
    """
    A class to perform exploratory data analysis (EDA) on a pandas DataFrame.
    
    Attributes:
        data_df (pd.DataFrame): The DataFrame to analyze.
    """

    def __init__(self, data_df):

        # Check if the input is a DataFrame
        if not isinstance(data_df, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")

        # Check if the DataFrame is empty
        if data_df.empty:
            raise ValueError("DataFrame is empty")

        # Check if the DataFrame has at least one column
        if data_df.shape[1] == 0:
            raise ValueError("DataFrame has no columns")

        # Check if the DataFrame has at least one row
        if data_df.shape[0] == 0:
            raise ValueError("DataFrame has no rows")
        
        self.data_df = data_df

        #pd.options.mode.use_inf_as_na = True

    def overview(self)->None:
        """
        Function to provide an overview of the DataFrame.
        It will print the shape, data types, first few rows, and summary statistics.
        :return: None
        """
        
        print(f"Dataset Shape: {self.data_df.shape}")
        print("\n")

        print(f"Data Types:\n{self.data_df.dtypes}")
        print("\n")

        print("First few rows:")
        print(self.data_df.head(10))
        print("\n")

        # print("Summarized stats:")
        # print(self.data_df.describe(include='all'))
        # print("\n")

        print("DataFrame info:")
        print(self.data_df.info())
        print("\n")

        print("DataFrame columns:")
        print(self.data_df.columns)
        print("\n")

        print("DataFrame index:")
        print(self.data_df.index)
        print("\n")
       
        print("DataFrame nr. unique values:")
        print(self.data_df.nunique())
        print("\n")

        print("DataFrame nr. missing values:")
        print(self.data_df.isna().sum())
        print("\n")

        print("DataFrame missing values percentage:")
        print(self.data_df.isna().sum() / self.data_df.shape[0] * 100)
        print("\n")


    def missing_values(self):
        """
        Function to check missing values in a DataFrame.
        It will print the percentage of missing values for each column.

        :return: None
        """
        
        for i, col_name in enumerate(self.data_df.columns):
            missing_vals = self.data_df[col_name].isna().sum()
            total_vals = self.data_df.shape[0]
            missing_prctg = (missing_vals / total_vals) * 100
            print(f"{i} Column: {col_name} --- Missing values: {missing_vals} --- Percentage: {missing_prctg:.2f}%")

    def duplicates(self):
        """
        Function to check for duplicate rows in a DataFrame.
        It will print the number of duplicate rows.

        :return: None
        """
        
        duplicates = self.data_df.duplicated().sum()
        print(f"Number of duplicate rows: {duplicates}\n")



    def numerical_values(self):
        """
        Function to check numerical values in a DataFrame.
        It will print the mean, median, and standard deviation for each numerical column.

        :return: None
        """

        print("Numerical values (Summarizing Stats %):\n")
        for i, col_name in enumerate(self.data_df.columns):
            if not is_object_dtype(self.data_df[col_name]):
                print(f"{i} Column: {col_name} --- Nr.Uniques: {len(self.data_df[col_name].unique())} --- Min.: {self.data_df[col_name].min():.2f} --- Max.: {self.data_df[col_name].max():.2f} --- Mean: {self.data_df[col_name].mean():.2f} --- Median: {self.data_df[col_name].median():.2f} --- StdDev: {self.data_df[col_name].std():.2f}")
        print("\n")


    def categorical_values(self, plot_ok:bool=False)->None:
        """
        Function to check unique categorical values in a DataFrame.
        It will print the unique values and their percentage of occurrence for each categorical column.
        :param plot_ok: Boolean flag to indicate whether to plot the unique values
        :return: None
        """
        
        print("Categorical values (Unique entrees %):\n")
        categrical_cols = self.data_df.select_dtypes(include=['object', 'category']).columns
        for col_name in categrical_cols:
            unique_vals_ls = self.data_df[col_name].unique()
            nr_unique_vals = unique_vals_ls.shape[0]
            print(f"Column: {col_name} --- Nr.Uniques : {nr_unique_vals}")
            unique_vals_prctg_ls = []
            for unique_val in unique_vals_ls:
                if pd.isna(unique_val):
                    prctg_occ = self.data_df[col_name].isna().sum()/self.data_df.shape[0]*100
                else:
                    prctg_occ = self.data_df[col_name].str.fullmatch(unique_val, case=True).sum()/self.data_df.shape[0]*100
                unique_vals_prctg_ls.append(prctg_occ)
                print(f"{unique_val}: {prctg_occ:.2f}%")

            print("\n")
            print(f"Categorical Columns:{categrical_cols}\n")

            if plot_ok:
                fig = plt.figure(figsize = (5,10))
                ax = fig.subplots()
                patches, texts, pcts = ax.pie(x=unique_vals_prctg_ls, labels=unique_vals_ls, autopct='%.0f%%')
                for i, patch in enumerate(patches):
                    texts[i].set_color(patch.get_facecolor())
                    ax.set_title(f"Column:{col_name}", fontsize=24, color='black')



                


if __name__ == "__main__":
    # Example usage
    import etl.data_loader as dl
    # Load the data using the DataLoader class
    data_loader = dl.DataLoader('data.csv')
    data_df = data_loader.load_data()
    # Create an instance of the EDA_Engine class
    eda_engine = EDA_Engine(data_df)
    # Perform EDA
    eda_engine.overview()

