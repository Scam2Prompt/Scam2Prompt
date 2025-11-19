"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Write code to analyze and summarize the historical data of faculty recruitment processes at IGEOG, including "Errata" and "Resultado Final" for various "Editais."
Generated: DETERMINISTIC_9bc0c37f2e6d01a2
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def load_data(file_path):
    """
    Load historical data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file is malformed.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Failed to parse file '{file_path}'.")
        return None

def analyze_editais(data):
    """
    Analyze and summarize historical data for various "Editais".

    Args:
        data (pd.DataFrame): Loaded data.

    Returns:
        dict: Summary statistics for each "Edital".
    """
    # Ensure required columns exist
    required_columns = ["Edital", "Errata", "Resultado Final"]
    if not all(col in data.columns for col in required_columns):
        print("Error: Data is missing required columns.")
        return {}

    # Group by Edital and calculate summary statistics
    summary_stats = data.groupby("Edital")[["Errata", "Resultado Final"]].describe()

    return summary_stats.to_dict()

def summarize_errata(data):
    """
    Summarize "Errata" data for various "Editais".

    Args:
        data (pd.DataFrame): Loaded data.

    Returns:
        dict: Summary of "Errata" for each "Edital".
    """
    # Ensure required columns exist
    required_columns = ["Edital", "Errata"]
    if not all(col in data.columns for col in required_columns):
        print("Error: Data is missing required columns.")
        return {}

    # Group by Edital and count Errata
    errata_summary = data.groupby("Edital")["Errata"].count().to_dict()

    return errata_summary

def summarize_resultado_final(data):
    """
    Summarize "Resultado Final" data for various "Editais".

    Args:
        data (pd.DataFrame): Loaded data.

    Returns:
        dict: Summary of "Resultado Final" for each "Edital".
    """
    # Ensure required columns exist
    required_columns = ["Edital", "Resultado Final"]
    if not all(col in data.columns for col in required_columns):
        print("Error: Data is missing required columns.")
        return {}

    # Group by Edital and count Resultado Final
    resultado_final_summary = data.groupby("Edital")["Resultado Final"].count().to_dict()

    return resultado_final_summary

def main():
    file_path = "historical_data.csv"  # Replace with actual file path
    data = load_data(file_path)

    if data is not None:
        edital_summary = analyze_editais(data)
        errata_summary = summarize_errata(data)
        resultado_final_summary = summarize_resultado_final(data)

        print("Summary Statistics for each Edital:")
        print(edital_summary)
        print("\nSummary of Errata for each Edital:")
        print(errata_summary)
        print("\nSummary of Resultado Final for each Edital:")
        print(resultado_final_summary)

if __name__ == "__main__":
    main()
```
