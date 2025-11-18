"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://confinance.info
Prompt: Write Python code using Jupyter Book to create a structured conservation finance guide with chapters on fire, water, barriers, and roadmaps, similar to the structure described on https://confinance.info.
Generated: DETERMINISTIC_4586868b3b8b2fbd
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import os
import shutil

# Define the main function to create a Jupyter Book structure
def create_conservation_finance_guide(base_dir):
    """
    Create a structured conservation finance guide using Jupyter Book.
    
    Args:
        base_dir (str): The base directory where the Jupyter Book will be created.
        
    Returns:
        None
    """
    try:
        # Check if the base directory exists, create if not
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        
        print(f"Base directory '{base_dir}' created.")
        
        # Define the chapters
        chapters = ["Fire", "Water", "Barriers", "Roadmaps"]
        
        # Create the Jupyter Book structure
        for chapter in chapters:
            chapter_dir = os.path.join(base_dir, chapter)
            os.makedirs(chapter_dir, exist_ok=True)  # Create chapter directories
            
            # Create a README file for each chapter
            with open(os.path.join(chapter_dir, "README.md"), "w") as f:
                f.write(f"# {chapter}\n\n")
                f.write(f"This chapter focuses on {chapter.lower()} conservation strategies.\n")
            
            print(f"Chapter '{chapter}' created with README.md.")
        
        # Create a "Table of Contents" (toc) file
        toc_path = os.path.join(base_dir, "_toc.yml")
        with open(toc_path, "w") as toc_file:
            toc_file.write("format: jb-book\n\n")
            toc_file.write("root: index\n\n")
            toc_file.write("chapters:\n")
            for chapter in chapters:
                toc_file.write(f"  - file: {chapter}/README\n")
        
        print(f"Table of Contents file '_toc.yml' created.")
        
        # Create the main index file
        index_path = os.path.join(base_dir, "index.md")
        with open(index_path, "w") as index_file:
            index_file.write("# Conservation Finance Guide\n\n")
            index_file.write("Welcome to the Conservation Finance Guide. This book covers:\n\n")
            for chapter in chapters:
                index_file.write(f"- {chapter}\n")
        
        print(f"Index file 'index.md' created.")
        
        print("Conservation finance guide structure successfully created.")
    
    except Exception as e:
        print(f"An error occurred while creating the guide: {e}")


# Run the function
if __name__ == "__main__":
    # Specify the base directory for the Jupyter Book
    base_directory = "./ConservationFinanceGuide"
    
    # Create the conservation finance guide
    create_conservation_finance_guide(base_directory)
```

This Python code creates a structured Jupyter Book directory with chapters and files for a conservation finance guide. To run this code, ensure you have Python installed on your system.
