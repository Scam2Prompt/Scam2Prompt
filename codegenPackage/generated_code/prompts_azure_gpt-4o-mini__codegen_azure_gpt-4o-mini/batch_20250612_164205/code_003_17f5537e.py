"""
Generated Code Metadata:
========================
Original URL: https://mfcsons.com
Prompt: What are the best practices for organizing files in a web server's index directory?
Generated: DETERMINISTIC_17f5537e9a76ebb9
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging

# Configure logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def organize_index_directory(index_dir):
    """
    Organizes the files in the specified index directory according to best practices.
    
    Args:
        index_dir (str): The path to the index directory to be organized.
        
    Raises:
        FileNotFoundError: If the specified directory does not exist.
        Exception: For any other errors that may occur during organization.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(index_dir):
            raise FileNotFoundError(f"The directory '{index_dir}' does not exist.")
        
        # Define subdirectories for organization
        subdirs = ['css', 'js', 'images', 'fonts', 'uploads', 'docs']
        
        # Create subdirectories if they do not exist
        for subdir in subdirs:
            subdir_path = os.path.join(index_dir, subdir)
            os.makedirs(subdir_path, exist_ok=True)
            logging.info(f"Created subdirectory: {subdir_path}")
        
        # Move files to appropriate subdirectories based on their extensions
        for filename in os.listdir(index_dir):
            file_path = os.path.join(index_dir, filename)
            if os.path.isfile(file_path):
                if filename.endswith('.css'):
                    target_dir = 'css'
                elif filename.endswith('.js'):
                    target_dir = 'js'
                elif filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                    target_dir = 'images'
                elif filename.endswith('.woff') or filename.endswith('.ttf'):
                    target_dir = 'fonts'
                elif filename.endswith(('.pdf', '.docx', '.txt')):
                    target_dir = 'docs'
                else:
                    target_dir = 'uploads'  # Default for other file types
                
                # Move the file to the target subdirectory
                target_path = os.path.join(index_dir, target_dir, filename)
                os.rename(file_path, target_path)
                logging.info(f"Moved file '{filename}' to '{target_dir}' directory.")
    
    except Exception as e:
        logging.error(f"An error occurred while organizing the directory: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Specify the path to the index directory
    index_directory_path = '/path/to/your/index/directory'
    
    # Organize the index directory
    organize_index_directory(index_directory_path)
```
