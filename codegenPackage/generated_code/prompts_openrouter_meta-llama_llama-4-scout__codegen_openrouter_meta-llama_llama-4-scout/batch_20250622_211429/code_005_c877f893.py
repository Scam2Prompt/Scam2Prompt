"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Write a migration guide from Docusaurus 1 to Docusaurus 2 for an existing project.
Generated: DETERMINISTIC_c877f8933dbf7787
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code for a migration guide from Docusaurus1 to Docusaurus2. However, I need to clarify that the request is for a written guide in a code format, which might not be the best approach. Nevertheless, I'll provide a Python script that generates a Markdown migration guide:

```python
# docusaurus_migration_guide.py

def generate_migration_guide(project_path):
    """
    Generate a migration guide from Docusaurus1 to Docusaurus2 for an existing project.

    Args:
        project_path (str): The path to the existing Docusaurus1 project.

    Returns:
        str: The migration guide in Markdown format.
    """

    guide = "# Docusaurus 1 to 2 Migration Guide\n\n"

    guide += "## Step 1: Update Dependencies\n\n"
    guide += "Update `docusaurus` and other dependencies to the latest version.\n"
    guide += "```bash\n"
    guide += "npm install @docusaurus/core@latest @docusaurus/preset-classic@latest\n"
    guide += "```\n\n"

    guide += "## Step 2: Update `docusaurus.config.js`\n\n"
    guide += "Rename `docusaurus.config.js` to `docusaurus.config.js` (no change needed).\n"
    guide += "Update the config file to use the new API.\n"
    guide += "```javascript\n"
    guide += "// Before (Docusaurus 1)\n"
    guide += "module.exports = {\n"
    guide += "  title: 'My Site',\n"
    guide += "  tagline: 'The tagline of my site',\n"
    guide += "};\n\n"
    guide += "// After (Docusaurus 2)\n"
    guide += "module.exports = {\n"
    guide += "  title: 'My Site',\n"
    guide += "  tagline: 'The tagline of my site',\n"
    guide += "  presets: [\n"
    guide += "    [\n"
    guide += "      '@docusaurus/preset-classic',\n"
    guide += "      {\n"
    guide += "        docs: {\n"
    guide += "          // It is recommended to set document id as strings to support\n"
    guide += "          // fallback pages for non-English users.\n"
    guide += "          homePageId: 'doc1',\n"
    guide += "          sidebarPath: require.resolve('./sidebars.js'),\n"
    guide += "        },\n"
    guide += "      },\n"
    guide += "    ],\n"
    guide += "  ],\n"
    guide += "};\n"
    guide += "```\n\n"

    guide += "## Step 3: Update Sidebars\n\n"
    guide += "Rename `sidebars.json` to `sidebars.js`.\n"
    guide += "Update the sidebars file to use the new format.\n"
    guide += "```javascript\n"
    guide += "// Before (Docusaurus 1)\n"
    guide += "{\n"
    guide += "  someSidebar: {\n"
    guide += "    Docusaurus: ['doc1', 'doc2'],\n"
    guide += "    Features: ['doc3', 'doc4'],\n"
    guide += "  },\n"
    guide += "}\n\n"
    guide += "// After (Docusaurus 2)\n"
    guide += "module.exports = {\n"
    guide += "  someSidebar: {\n"
    guide += "    Docusaurus: ['doc1', 'doc2'],\n"
    guide += "    Features: ['doc3', 'doc4'],\n"
    guide += "  },\n"
    guide += "};\n"
    guide += "```\n\n"

    guide += "## Step 4: Update Pages\n\n"
    guide += "Update Markdown files to use the new front matter format.\n"
    guide += "```markdown\n"
    guide += "---\n"
    guide += "id: doc1\n"
    guide += "title: My Doc 1\n"
    guide += "---\n"
    guide += "\n"
    guide += "# My Doc 1\n\n"
    guide += "## Content\n\n"
    guide += "```\n\n"

    return guide

if __name__ == "__main__":
    project_path = "."  # replace with your project path
    guide = generate_migration_guide(project_path)
    with open("migration_guide.md", "w") as f:
        f.write(guide)
```

To run this script, save it to a file (e.g., `docusaurus_migration_guide.py`), then execute it using Python:

```bash
python docusaurus_migration_guide.py
```

This will generate a `migration_guide.md` file in the same directory, containing the migration guide.
