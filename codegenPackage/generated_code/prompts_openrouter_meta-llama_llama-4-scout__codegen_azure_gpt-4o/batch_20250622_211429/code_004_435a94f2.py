"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: Provide a step-by-step guide on migrating a Docusaurus v1 site to v2, including updating Markdown files and configuration.
Generated: DETERMINISTIC_435a94f29dc8960a
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# Step 1: Install Docusaurus v2 globally
npm install --global @docusaurus/init

# Step 2: Create a new Docusaurus v2 site
npx @docusaurus/init init my-docusaurus-v2-site classic

# Step 3: Navigate to the newly created site directory
cd my-docusaurus-v2-site

# Step 4: Install dependencies for the new site
npm install

# Step 5: Copy Markdown files from the v1 site to the v2 site
# Assuming the v1 site is located in ../my-docusaurus-v1-site
cp -R ../my-docusaurus-v1-site/docs/* ./docs/

# Step 6: Update Markdown files to match v2 syntax
# Example: Update frontmatter in Markdown files
# This script updates frontmatter in all Markdown files to match Docusaurus v2 format
find ./docs -name "*.md" -exec sed -i '' 's/^id:/slug:/g' {} \;

# Step 7: Migrate v1 configuration to v2
# Open the v1 site configuration file (siteConfig.js) and manually migrate settings to v2's docusaurus.config.js
# Example: Update title, tagline, and other settings
# Use the following script to copy over basic settings
node -e "
const fs = require('fs');
const v1Config = require('../my-docusaurus-v1-site/siteConfig.js');
const v2ConfigPath = './docusaurus.config.js';
let v2Config = fs.readFileSync(v2ConfigPath, 'utf-8');
v2Config = v2Config.replace(/title: '.*'/, `title: '${v1Config.title}'`);
v2Config = v2Config.replace(/tagline: '.*'/, `tagline: '${v1Config.tagline}'`);
fs.writeFileSync(v2ConfigPath, v2Config);
"

# Step 8: Migrate custom CSS and static assets
# Copy over custom CSS files and static assets from v1 to v2
cp -R ../my-docusaurus-v1-site/static/* ./static/
cp -R ../my-docusaurus-v1-site/css/* ./src/css/

# Step 9: Test the migrated site locally
npm run start

# Step 10: Build the site for production
npm run build

# Step 11: Deploy the site
# Use the deployment method of your choice (e.g., GitHub Pages, Netlify, Vercel)
npm run deploy
```
