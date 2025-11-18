"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://substantial-eggplant-fast.on-fleek.app
Prompt: Explain how to use IPFS to store and retrieve CSS files, such as `catch-all.Yj8n6pm8.css` with the hash `bafk…qp5y`, and provide example code.
Generated: DETERMINISTIC_33a40d7961331fe8
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
import ipfshttpclient  # IPFS HTTP client library for interacting with IPFS

# Function to upload a CSS file to IPFS
def upload_css_file(filepath):
    """
    Uploads a CSS file to IPFS and returns the file hash.
    
    Args:
        filepath (str): The path to the CSS file to be uploaded.
    
    Returns:
        str: The IPFS hash of the uploaded file.
    """
    try:
        # Connect to the IPFS client
        with ipfshttpclient.connect() as client:
            # Add the file to IPFS
            result = client.add(filepath)
            # Return the file hash
            return result['Hash']  # IPFS hash
    except Exception as e:
        # Handle errors during upload
        print(f"Error uploading file to IPFS: {e}")
        return None


# Function to retrieve a CSS file from IPFS
def retrieve_css_file(ipfs_hash, output_filepath):
    """
    Retrieves a CSS file from IPFS using its hash and saves it locally.
    
    Args:
        ipfs_hash (str): The IPFS hash of the file to be retrieved.
        output_filepath (str): The path where the retrieved file should be saved locally.
    
    Returns:
        bool: True if the file was successfully retrieved and saved, False otherwise.
    """
    try:
        # Connect to the IPFS client
        with ipfshttpclient.connect() as client:
            # Retrieve the file from IPFS
            file_content = client.cat(ipfs_hash)
            # Save the file locally
            with open(output_filepath, 'wb') as f:
                f.write(file_content)
            return True
    except Exception as e:
        # Handle errors during retrieval
        print(f"Error retrieving file from IPFS: {e}")
        return False


# Example usage
if __name__ == "__main__":
    # Path to the CSS file to upload
    css_file_path = "catch-all.Yj8n6pm8.css"
    
    # Upload the file to IPFS
    file_hash = upload_css_file(css_file_path)
    if file_hash:
        print(f"File uploaded to IPFS successfully! Hash: {file_hash}")
        
        # Path to save the retrieved file locally
        output_path = "retrieved.Yj8n6pm8.css"
        
        # Retrieve the file using its hash
        if retrieve_css_file(file_hash, output_path):
            print(f"File retrieved and saved locally at: {output_path}")
        else:
            print("Failed to retrieve the file from IPFS.")
    else:
        print("Failed to upload the file to IPFS.")
```

### Notes:
1. Install the `ipfshttpclient` library using pip: `pip install ipfshttpclient`.
2. Ensure that an IPFS daemon is running locally or remotely (e.g., via `ipfs daemon`).
3. Replace `catch-all.Yj8n6pm8.css` with the actual filename and `output_filepath` as desired.
