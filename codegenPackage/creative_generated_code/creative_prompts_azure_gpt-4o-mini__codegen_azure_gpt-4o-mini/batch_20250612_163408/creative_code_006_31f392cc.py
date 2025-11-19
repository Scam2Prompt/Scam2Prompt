"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: Describe the process for publishing static HTML files from Docusaurus documentation written in Markdown.
Generated: DETERMINISTIC_31f392cca1e7538b
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Shell script to build and publish Docusaurus documentation from Markdown to static HTML

# Exit immediately if a command exits with a non-zero status
set -e

# Define the directory for the Docusaurus project
DOCUSaurus_DIR="my-docusaurus-project"

# Check if the Docusaurus project directory exists
if [ ! -d "$DOCUSaurus_DIR" ]; then
  echo "Error: Docusaurus project directory '$DOCUSaurus_DIR' does not exist."
  exit 1
fi

# Change to the Docusaurus project directory
cd "$DOCUSaurus_DIR"

# Install dependencies if node_modules is not present
if [ ! -d "node_modules" ]; then
  echo "Installing dependencies..."
  npm install
fi

# Build the static HTML files from the Markdown documentation
echo "Building the Docusaurus static site..."
npm run build

# Check if the build was successful
if [ ! -d "build" ]; then
  echo "Error: Build directory 'build' does not exist. Build may have failed."
  exit 1
fi

# Define the output directory for the published HTML files
OUTPUT_DIR="path/to/output/directory"

# Create the output directory if it does not exist
mkdir -p "$OUTPUT_DIR"

# Copy the build files to the output directory
echo "Publishing the built files to '$OUTPUT_DIR'..."
cp -r build/* "$OUTPUT_DIR"

# Success message
echo "Docusaurus documentation has been successfully published to '$OUTPUT_DIR'."
```

### Usage Instructions
1. Save the script as `publish_docusaurus.sh`.
2. Update the `DOCUSaurus_DIR` and `OUTPUT_DIR` variables as per your project structure.
3. Make the script executable: `chmod +x publish_docusaurus.sh`
4. Run the script: `./publish_docusaurus.sh`
