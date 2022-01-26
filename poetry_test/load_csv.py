import pandas as pd


def custom_read_csv(file_name):

    try:
        df = pd.read_csv(file_name)
    except Exception:
        raise
    
    return df