
import pandas as pd

def eda_summary(df):
    """
    Perform a summary of exploratory data analysis.
    
    Parameters:
    df (pd.DataFrame): The dataset to analyze.
    
    Returns:
    dict: A dictionary with key EDA insights.
    """
    summary = {
        "columns": df.columns.tolist(),
        "shape": df.shape,
        "missing_values": df.isnull().sum().to_dict(),
        "summary_statistics": df.describe().to_dict()
    }
    
    print("EDA Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")
    return summary

def calculate_correlations(df):
    """
    Calculate the correlation matrix for the dataset.
    
    Parameters:
    df (pd.DataFrame): The dataset to analyze.
    
    Returns:
    pd.DataFrame: Correlation matrix.
    """
    numeric_df = df.select_dtypes(include='number')  # Only use numeric columns for correlation
    corr_matrix = numeric_df.corr()
    print("Correlation Matrix:\n", corr_matrix)
    return corr_matrix
