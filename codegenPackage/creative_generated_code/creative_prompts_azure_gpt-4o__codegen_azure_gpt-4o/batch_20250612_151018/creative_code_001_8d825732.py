"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: How can I use Docusaurus to implement document versioning for a project with multiple release versions? Provide an example.
Generated: DETERMINISTIC_8d825732c0c0ea67
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Install Docusaurus CLI globally, if not already installed
npm install -g @docusaurus/init

# Create a new Docusaurus project
npx create-docusaurus@latest my-project classic

# Change directory to the newly created project
cd my-project

# Install the required packages for versioning
# Docusaurus has built-in support for versioning
npm install

# Initialize versioning by creating the initial version
npm run docusaurus docs:version 1.0.0

# Above command will create a version folder at `versioned_docs/version-1.0.0` and update `versions.json`
```

### Folder Structure After Versioning
``bash..
