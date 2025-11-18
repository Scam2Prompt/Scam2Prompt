"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igeog.uerj.br
Prompt: Write Python code to process and extract information from the list of candidates and results provided in the IGEOG selection process documents, such as "Listagem de inscrições deferidas e indeferidas" and "Resultado Final."
Generated: DETERMINISTIC_b7d5c8d52802e2b6
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import os

def process_selection_documents(file_paths):
    """
    Processes selection documents to extract information about candidates and their results.
    
    Args:
    file_paths (list of str): List of file paths to the documents.

    Returns:
    dict: Dictionary containing processed data with 'deferidos', 'indeferidos', and 'final_results' as keys.
    """
    if not file_paths:
        raise ValueError("file_paths cannot be empty")

    # Initialize data structures to store processed information
    processed_data = {
        "deferidos": [],  # List of candidates with accepted applications
        "indeferidos": [],  # List of candidates with rejected applications
        "final_results": []  # List of candidates' final results
    }

    # Regular expressions for matching patterns in the documents
    deferido_pattern = re.compile(r"\bDEFERIDO\b", re.IGNORECASE)
    indeferido_pattern = re.compile(r"\bINDEFERIDO\b", re.IGNORECASE)
    candidate_name_pattern = re.compile(r"^[A-Za-z\s]+")  # Matches candidate names
    final_result_pattern = re.compile(r"(APROVADO|REPROVADO)", re.IGNORECASE)

    # Process each file
    for file_path in file_paths:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    
                    # Extract candidate names
                    candidate_name_match = candidate_name_pattern.match(line)
                    candidate_name = candidate_name_match.group() if candidate_name_match else None
                    
                    if not candidate_name:
                        continue  # Skip lines without candidate names
                    
                    # Check deferido or indeferido status
                    if deferido_pattern.search(line):
                        processed_data["deferidos"].append(candidate_name)
                    elif indeferido_pattern.search(line):
                        processed_data["indeferidos"].append(candidate_name)

                    # Check final results status
                    final_result_match = final_result_pattern.search(line)
                    if final_result_match:
                        final_status = final_result_match.group().upper()
                        processed_data["final_results"].append({
                            "name": candidate_name,
                            "status": final_status
                        })

        except Exception as e:
            print(f"Error processing file {file_path}: {e}")
            continue

    return processed_data


def main():
    """
    Main function to demonstrate processing selection documents.
    Modify the file_paths list with actual file paths to test the function.
    """
    # Example file paths (replace with actual paths)
    file_paths = [
        "Listagem_de_inscricoes.txt",
        "Resultado_Final.txt"
    ]

    try:
        results = process_selection_documents(file_paths)
        print("Processed Data:")
        print("Deferidos:", results["deferidos"])
        print("Indeferidos:", results["indeferidos"])
        print("Final Results:", results["final_results"])
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
