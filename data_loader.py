
import pandas as pd

def load_data(filepath):
    """
    Load dataset from an Excel file.
    
    Parameters:
    filepath (str): Path to the Excel file.

    Returns:
    pd.DataFrame: Loaded data as a DataFrame.
    """
    try:
        data = pd.read_excel(filepath)
        print(f"Data loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return None

def clean_data(df):
    """
    Clean the dataset by handling missing values and duplicates.

    Parameters:
    df (pd.DataFrame): Data to be cleaned.

    Returns:
    pd.DataFrame: Cleaned data.
    """
    # Drop duplicate rows
    df = df.drop_duplicates()
    
    # Fill or drop missing values
    if df.isnull().sum().any():
        df = df.fillna(df.median(numeric_only=True))  # Fill missing numeric values with the median
        print("Missing values handled by filling with median values.")
    
    print(f"Data cleaned. Current shape: {df.shape[0]} rows, {df.shape[1]} columns.")
    return df
