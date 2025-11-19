"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: Provide a step-by-step guide on migrating a Docusaurus project from version 1 to version 2, including any necessary changes to Markdown files.
Generated: DETERMINISTIC_460fb5806ff883ec
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# Step 1: Install Docusaurus CLI globally (if not already installed)
npm install -g @docusaurus/cli

# Step 2: Create a new Docusaurus v2 project
# Replace "my-docusaurus-project" with your desired project name
npx @docusaurus/init@latest init my-docusaurus-project classic

# Step 3: Navigate to the newly created project directory
cd my-docusaurus-project

# Step 4: Install dependencies for the new Docusaurus v2 project
npm install

# Step 5: Copy Markdown files from the old Docusaurus v1 project to the new v2 project
# Assuming your old Markdown files are located in "old-project/docs"
cp -r ../old-project/docs ./docs

# Step 6: Update Markdown files to match Docusaurus v2 format
# Example: Update frontmatter in Markdown files
# Use a script to automate this if you have many files
# Below is a Node.js script to update frontmatter in Markdown files

# Create a file named "updateMarkdown.js" in the root of your new project
cat <<EOF > updateMarkdown.js
const fs = require('fs');
const path = require('path');

// Directory containing Markdown files
const docsDir = path.join(__dirname, 'docs');

// Function to update frontmatter in Markdown files
function updateFrontmatter(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  let updatedContent = content;

  // Example: Replace "id" with "slug" in frontmatter
  updatedContent = updatedContent.replace(/^id:\s*(.+)$/gm, 'slug: $1');

  // Example: Add "title" field if missing
  if (!/^title:\s*/gm.test(updatedContent)) {
    const titleMatch = updatedContent.match(/^#\s*(.+)$/m);
    if (titleMatch) {
      const title = titleMatch[1];
      updatedContent = `title: ${title}\n` + updatedContent;
    }
  }

  fs.writeFileSync(filePath, updatedContent, 'utf-8');
}

// Process all Markdown files in the docs directory
fs.readdirSync(docsDir).forEach((file) => {
  const filePath = path.join(docsDir, file);
  if (path.extname(filePath) === '.md') {
    console.log(`Updating frontmatter for: ${file}`);
    updateFrontmatter(filePath);
  }
});

console.log('Markdown files updated successfully.');
EOF

# Step 7: Run the script to update Markdown files
node updateMarkdown.js

# Step 8: Update Docusaurus configuration
# Open "docusaurus.config.js" and configure the site settings
# Example: Update the "navbar" and "sidebar" settings to match your old project

# Step 9: Start the development server to verify the migration
npm run start

# Step 10: Build the project for production
npm run build

# Step 11: Deploy the project (optional)
# Example: Deploy to GitHub Pages
GIT_USER=<YourGitHubUsername> npm run deploy
```
