"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://askcardiologist.in
Prompt: Develop a Python program to analyze and categorize Dr. S. Nagendra Boopathy's research publications based on topics like interventional cardiology, structural heart disease, and intracoronary imaging.
Generated: DETERMINISTIC_c0bb522601281819
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from collections import defaultdict

def load_publications(file_path):
    """
    Load research publications from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing publications.
        
    Returns:
        list[dict]: List of publications as dictionaries.
    """
    publications = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                publications.append(row)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please check the file path.")
    except Exception as e:
        print(f"Error: An unexpected error occurred while loading publications: {e}")
    return publications


def categorize_publications(publications):
    """
    Categorize publications based on predefined topics.
    
    Args:
        publications (list[dict]): List of publications.
        
    Returns:
        dict[str, list[dict]]: Categorized publications.
    """
    categories = {
        "Interventional Cardiology": ["stent", "angioplasty", "interventional cardiology"],
        "Structural Heart Disease": ["mitral valve", "structural heart disease", "transcatheter"],
        "Intracoronary Imaging": ["intracoronary imaging", "OCT", "IVUS"],
    }
    
    categorized = defaultdict(list)
    
    for publication in publications:
        title = publication.get("title", "").lower()
        abstract = publication.get("abstract", "").lower()
        
        for category, keywords in categories.items():
            if any(keyword in title or keyword in abstract for keyword in keywords):
                categorized[category].append(publication)
                break  # Assign publication to the first matching category
                
    return categorized


def save_categorized_publications(categorized, output_dir):
    """
    Save categorized publications to separate CSV files.
    
    Args:
        categorized (dict[str, list[dict]]): Categorized publications.
        output_dir (str): Directory to save categorized files.
    """
    try:
        for category, publications in categorized.items():
            file_name = f"{output_dir}/{category.replace(' ', '_')}_publications.csv"
            with open(file_name, mode='w', encoding='utf-8', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=publications[0].keys())
                writer.writeheader()
                writer.writerows(publications)
            print(f"Publications categorized under '{category}' saved to {file_name}.")
    except Exception as e:
        print(f"Error: An unexpected error occurred while saving categorized publications: {e}")


def main():
    """
    Main function to execute the program logic.
    """
    # Input file containing research publications (CSV format)
    input_csv = "publications.csv"
    # Output directory to save categorized publications
    output_directory = "output"
    
    # Step 1: Load publications
    print("Loading publications...")
    publications = load_publications(input_csv)
    
    if not publications:
        print("No publications found or failed to load. Exiting.")
        return
    
    # Step 2: Categorize publications
    print("Categorizing publications...")
    categorized_publications = categorize_publications(publications)
    
    # Step 3: Save categorized publications
    print("Saving categorized publications...")
    save_categorized_publications(categorized_publications, output_directory)
    
    print("Program completed successfully.")


if __name__ == "__main__":
    main()
```
