import pandas as pd

class DataLoader():
    """
    A utility class for loading and handling data from various file formats.

    This class supports loading data from the following file formats:
    - CSV (.csv)
    - Parquet (.parquet)
    - JSON (.json)
    - Excel (.xlsx)

    Attributes:
        file_path (str): The path to the data file to be loaded.
        data_reader (callable): The Pandas function used to read the data, determined by the file extension.
        data (DataFrame): The loaded data as a Pandas DataFrame.

    Methods:
        load_data():
            Loads the data from the specified file using the appropriate Pandas reader function.
        
        get_data_types():
            Returns the data types of the columns in the loaded DataFrame.

    Raises:
        ValueError: If the file format is unsupported or if there is an error during data loading.
    """
    def __init__(self, file_path:str=None):
        self.file_path = file_path
        self.data_reader = None

        if file_path.endswith('.csv'):
            self.data_reader = pd.read_csv
        elif file_path.endswith('.parquet'):
            self.data_reader = pd.read_parquet
        elif file_path.endswith('.json'):
            self.data_reader = pd.read_json
        elif file_path.endswith('.xlsx'):
            self.data_reader = pd.read_excel
        else:
            raise ValueError("Unsupported file format. Supported formats are: .csv, .json, .xlsx")

        self.data = self.load_data()

    def load_data(self):
        if self.data_reader is None:
            raise ValueError("No data reader defined. Please check the file format.")
        try:
            data = self.data_reader(self.file_path)
            return data
        except Exception as e:
            raise ValueError(f"Error loading data: {e}")
    
    def get_data_types(self):
        if self.data is None:
            raise ValueError("Data not loaded. Please load the data first.")
        

        return self.data.dtypes
        

if __name__ == "__main__":
    data_loader = DataLoader('data.csv')
    print(data_loader.data.head())