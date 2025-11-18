"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thephantomnetwork.net
Prompt: Generate a script to analyze and categorize creative projects, such as those described on "The Phantom Network," including video edits, logos, and gaming-related posts.
Generated: DETERMINISTIC_1f105bd575aaf892
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from typing import List, Dict, Union

# Define categories for creative projects
CATEGORIES = {
    "video_edit": ["edit", "video", "transition", "clip"],
    "logo_design": ["logo", "design", "branding", "identity"],
    "gaming_post": ["gaming", "game", "play", "stream", "esports"],
    "other": []
}

def load_project_data(file_path: str) -> List[Dict[str, Union[str, List[str]]]]:
    """
    Load project data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing project data.
    
    Returns:
        List[Dict[str, Union[str, List[str]]]]: List of project entries.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON structure in file {file_path}")
        return []

def categorize_projects(projects: List[Dict[str, Union[str, List[str]]]]) -> Dict[str, List[Dict]]:
    """
    Categorize projects based on predefined categories.
    
    Args:
        projects (List[Dict[str, Union[str, List[str]]]]): List of project entries.
        
    Returns:
        Dict[str, List[Dict]]: Categorized projects grouped by category.
    """
    categorized_projects = {category: [] for category in CATEGORIES.keys()}
    
    for project in projects:
        category_found = False
        keywords = project.get('keywords', [])
        
        # Match project with category
        for category, category_keywords in CATEGORIES.items():
            if any(keyword in keywords for keyword in category_keywords):
                categorized_projects[category].append(project)
                category_found = True
                break
        
        # If no category matches, assign to 'other'
        if not category_found:
            categorized_projects["other"].append(project)
    
    return categorized_projects

def save_categorized_projects(categorized_projects: Dict[str, List[Dict]], output_dir: str):
    """
    Save categorized projects to JSON files in the specified output directory.
    
    Args:
        categorized_projects (Dict[str, List[Dict]]): Categorized projects grouped by category.
        output_dir (str): Directory to save the categorized JSON files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for category, projects in categorized_projects.items():
        output_path = os.path.join(output_dir, f"{category}_projects.json")
        try:
            with open(output_path, 'w') as file:
                json.dump(projects, file, indent=4)
            print(f"Saved {len(projects)} projects to {output_path}")
        except IOError as e:
            print(f"Error: Unable to save projects to {output_path} ({e})")

def main():
    """
    Main function to load, analyze, and categorize creative projects.
    """
    # Path to input file containing project data
    input_file = "projects_data.json"
    
    # Directory to save categorized project data
    output_directory = "categorized_projects"
    
    # Load project data
    print("Loading project data...")
    projects = load_project_data(input_file)
    
    if not projects:
        print("No projects to process. Exiting.")
        return
    
    # Categorize projects
    print("Categorizing projects...")
    categorized_projects = categorize_projects(projects)
    
    # Save categorized projects to output files
    print("Saving categorized projects...")
    save_categorized_projects(categorized_projects, output_directory)
    
    print("Done.")

if __name__ == "__main__":
    main()
```
