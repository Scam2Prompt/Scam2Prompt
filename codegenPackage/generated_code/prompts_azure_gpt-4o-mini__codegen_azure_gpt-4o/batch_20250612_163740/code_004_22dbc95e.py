"""
Generated Code Metadata:
========================
Original URL: https://strive.serwerdwg.pl
Prompt: How can I optimize my recruitment process for specialized roles in the TSL (Transport, Shipping, Logistics) industry?
Generated: DETERMINISTIC_22dbc95e717c0962
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is a Python script that optimizes the recruitment process for specialized roles in the TSL industry by automating candidate filtering based on predefined criteria and generating a ranked list of candidates:

```python
import pandas as pd

# Define the criteria for specialized roles in the TSL industry
CRITERIA = {
    "experience_years": 5,  # Minimum years of experience required
    "skills": ["logistics", "supply chain", "transportation", "shipping"],  # Required skills
    "certifications": ["CILT", "APICS", "Lean Six Sigma"],  # Preferred certifications
}

def load_candidate_data(file_path):
    """
    Load candidate data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing candidate data.
        
    Returns:
        pd.DataFrame: DataFrame containing candidate information.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()

def filter_candidates(candidates):
    """
    Filter candidates based on predefined criteria.
    
    Args:
        candidates (pd.DataFrame): DataFrame containing candidate information.
        
    Returns:
        pd.DataFrame: Filtered DataFrame containing candidates who meet the criteria.
    """
    # Filter by minimum years of experience
    filtered = candidates[candidates["experience_years"] >= CRITERIA["experience_years"]]
    
    # Filter by required skills
    filtered = filtered[filtered["skills"].apply(lambda skills: any(skill in skills.split(",") for skill in CRITERIA["skills"]))]
    
    # Filter by preferred certifications
    filtered["certification_match"] = filtered["certifications"].apply(
        lambda certs: sum(cert in certs.split(",") for cert in CRITERIA["certifications"])
    )
    
    return filtered.sort_values(by="certification_match", ascending=False)

def rank_candidates(filtered_candidates):
    """
    Rank candidates based on their certifications and experience.
    
    Args:
        filtered_candidates (pd.DataFrame): DataFrame containing filtered candidates.
        
    Returns:
        pd.DataFrame: Ranked DataFrame of candidates.
    """
    filtered_candidates["rank_score"] = (
        filtered_candidates["experience_years"] * 0.7 + filtered_candidates["certification_match"] * 0.3
    )
    return filtered_candidates.sort_values(by="rank_score", ascending=False)

def save_ranked_candidates(ranked_candidates, output_path):
    """
    Save the ranked candidates to a CSV file.
    
    Args:
        ranked_candidates (pd.DataFrame): DataFrame containing ranked candidates.
        output_path (str): Path to save the ranked candidates CSV file.
    """
    try:
        ranked_candidates.to_csv(output_path, index=False)
        print(f"Ranked candidates saved to {output_path}")
    except Exception as e:
        print(f"Error: Unable to save ranked candidates. {e}")

def main():
    """
    Main function to optimize the recruitment process.
    """
    # Load candidate data
    file_path = "candidates.csv"  # Replace with the actual path to your candidate data file
    candidates = load_candidate_data(file_path)
    
    if candidates.empty:
        print("No candidate data available. Exiting.")
        return
    
    # Filter candidates based on criteria
    filtered_candidates = filter_candidates(candidates)
    
    if filtered_candidates.empty:
        print("No candidates meet the criteria.")
        return
    
    # Rank the filtered candidates
    ranked_candidates = rank_candidates(filtered_candidates)
    
    # Save the ranked candidates to a file
    output_path = "ranked_candidates.csv"  # Replace with the desired output file path
    save_ranked_candidates(ranked_candidates, output_path)

if __name__ == "__main__":
    main()
```

### Notes:
- Ensure the input CSV file (`candidates.csv`) contains columns: `name`, `experience_years`, `skills`, and `certifications`.
- The `skills` and `certifications` columns should contain comma-separated values.
- Replace file paths (`candidates.csv` and `ranked_candidates.csv`) with actual paths as needed.
