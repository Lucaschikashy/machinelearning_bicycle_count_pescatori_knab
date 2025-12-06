def _encode_dates(X):
    """
    Encode date features from a datetime column.
    
    Parameters:
    -----------
    X : pd.DataFrame
        DataFrame containing a 'date' column with datetime values
        
    Returns:
    --------
    pd.DataFrame
        DataFrame with encoded date features (year, month, day, weekday, hour)
    """
    X = X.copy()  # Ensure we're working on a copy
    # Encode the date information
    X["year"] = X["date"].dt.year
    X["month"] = X["date"].dt.month
    X["day"] = X["date"].dt.day
    X["weekday"] = X["date"].dt.weekday  # 0=Monday, 6=Sunday
    X["hour"] = X["date"].dt.hour
    # Keep the rest of the columns as they are
    return X
