"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bda.mcupr.ac.th
Prompt: Recommend a library for creating interactive museum exhibits that could showcase the clay pots and other artifacts from the Buddhist Art Gallery at MCU.
Generated: DETERMINISTIC_12803557f9c59973
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Library Recommendation Code: Interactive Museum Exhibit with Python
# This code uses the Streamlit library to create a simple interactive web application for showcasing museum artifacts.

# Import necessary libraries
import streamlit as st
from PIL import Image
import os

# Define the directory where artifact images are stored
ARTIFACTS_DIR = "artifacts"

# Error handling for missing directory or images
if not os.path.exists(ARTIFACTS_DIR):
    raise FileNotFoundError(f"The directory '{ARTIFACTS_DIR}' does not exist. Please ensure it contains artifact images.")

# Function to load artifact images
def load_artifacts(directory):
    """Loads artifact images from the specified directory."""
    artifacts = []
    for file_name in os.listdir(directory):
        if file_name.lower().endswith(('png', 'jpg', 'jpeg')):
            artifacts.append(os.path.join(directory, file_name))
    return artifacts

# Load all artifacts
artifacts = load_artifacts(ARTIFACTS_DIR)

# Check if there are any artifacts to display
if not artifacts:
    raise ValueError(f"No artifact images found in the directory '{ARTIFACTS_DIR}'. Please add images.")

# Streamlit app starts here
st.title("Interactive Museum Exhibit: Buddhist Art Gallery")

# Introduction section
st.markdown("""
Welcome to the **Buddhist Art Gallery** at MCU!
Explore the collection of clay pots and other artifacts by clicking on the items below.
""")

# Dropdown for selecting an artifact
selected_artifact = st.selectbox(
    "Select an artifact to view:",
    artifacts,
    format_func=lambda x: os.path.basename(x).replace("_", " ").split('.')[0].title()
)

# Display the selected artifact
if selected_artifact:
    st.image(Image.open(selected_artifact), caption=os.path.basename(selected_artifact).replace("_", " ").title())
    st.markdown("""
    **Description:** This artifact is part of the Buddhist Art Gallery collection.
    It showcases the rich cultural heritage preserved at MCU.
    """)

# Footer for additional information
st.markdown("""
---
Interested in learning more? Visit the **Museum of Buddhist Art Gallery** or contact us for personalized tours.
""")

# Note: Ensure that the 'artifacts' directory is populated with images of the artifacts before running the app.
```

### Instructions:
1. Save this code in a Python script file (e.g., `museum_exhibit.py`).
2. Create a folder named `artifacts` in the same directory as the script, and add images of artifacts (e.g., `.png`, `.jpg`, or `.jpeg` files).
3. Install Streamlit and Pillow if not already installed by running:
   ```bash
   pip install streamlit pillow
   ```
4. Run the script using:
   ```bash
   streamlit run museum_exhibit.py
   ```
