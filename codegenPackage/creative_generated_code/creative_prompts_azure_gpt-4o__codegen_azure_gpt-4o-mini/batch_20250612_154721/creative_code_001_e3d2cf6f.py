"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-dapps.com
Prompt: Generate a script to parse and analyze `.sql` files from a web server directory, like the one found at connect-dapps.com.
Generated: DETERMINISTIC_e3d2cf6f0f517701
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_sql_file(file_path):
    """
    Parses a SQL file and extracts queries.

    Args:
        file_path (str): The path to the SQL file.

    Returns:
        list: A list of SQL queries extracted from the file.
    """
    queries = []
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Split the content by semicolons to separate queries
            queries = [query.strip() for query in content.split(';') if query.strip()]
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except IOError as e:
        logging.error(f"Error reading file {file_path}: {e}")
    return queries

def analyze_query(query):
    """
    Analyzes a SQL query for basic metrics.

    Args:
        query (str): The SQL query to analyze.

    Returns:
        dict: Dictionary containing analysis results.
    """
    analysis = {
        'length': len(query),
        'select_count': len(re.findall(r'\bSELECT\b', query, re.IGNORECASE)),
        'insert_count': len(re.findall(r'\bINSERT\b', query, re.IGNORECASE)),
        'update_count': len(re.findall(r'\bUPDATE\b', query, re.IGNORECASE)),
        'delete_count': len(re.findall(r'\bDELETE\b', query, re.IGNORECASE)),
    }
    return analysis

def parse_and_analyze_sql_files(directory):
    """
    Parses and analyzes all SQL files in the specified directory.

    Args:
        directory (str): The directory containing SQL files.

    Returns:
        dict: A dictionary with file names as keys and their analysis as values.
    """
    results = {}
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.sql'):
                file_path = os.path.join(directory, filename)
                logging.info(f"Parsing file: {filename}")
                queries = parse_sql_file(file_path)

                # Analyze each query and store results
                analysis_results = []
                for query in queries:
                    analysis_results.append(analyze_query(query))

                results[filename] = analysis_results
    except FileNotFoundError:
        logging.error(f"Directory not found: {directory}")
    except IOError as e:
        logging.error(f"Error accessing directory {directory}: {e}")
    return results

def main():
    """
    Main function to execute the script.
    """
    directory = '/path/to/sql/files'  # Change this to your SQL files directory
    analysis_results = parse_and_analyze_sql_files(directory)
    
    # Print the analysis results
    for file, analysis in analysis_results.items():
        print(f"Analysis for {file}:")
        for query_analysis in analysis:
            print(query_analysis)

if __name__ == "__main__":
    main()
```
