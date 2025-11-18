"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2735--docusaurus-2.netlify.app
Prompt: Write a guide for migrating a project from Docusaurus v1 to v2, including examples of updating Markdown files and configuration settings.
Generated: DETERMINISTIC_54c65745a7b1756b
Batch ID: 20250612_151018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://my-project.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/my-project": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Guide for migrating a project from Docusaurus v1 to v2

/*
Step 1: Install Docusaurus v2

Run the following command to install Docusaurus v2 in your project folder.
Ensure you have Node.js installed.
*/
const { execSync } = require('child_process');

try {
  console.log('Installing Docusaurus v2...');
  execSync('npx create-docusaurus@latest my-new-docusaurus-project classic', { stdio: 'inherit' });
  console.log('Docusaurus v2 installed successfully.');
} catch (error) {
  console.error('Error installing Docusaurus v2:', error.message);
  process.exit(1);
}

/*
Step 2: Migrate Markdown files

Copy your Markdown files from the old Docusaurus v1 project into the `docs` folder of the new Docusaurus v2 project.
Update the frontmatter headers to match Docusaurus v2 conventions.
*/

const fs = require('fs');
const path = require('path');

// Function to update Markdown frontmatter
function updateMarkdownFrontmatter(filePath) {
  try {
    let content = fs.readFileSync(filePath, 'utf-8');

    // Example: Replace Docusaurus v1 frontmatter with v2 format
    content = content.replace(/---[\s\S]*?---/, (match) => {
      const updated = match
        .replace(/id:/, 'slug:') // Replace `id` with `slug`
        .replace(/title:/, 'title:') // Keep `title` as-is
        .replace(/sidebar_label:/, 'sidebar_position:'); // Replace `sidebar_label` with `sidebar_position`
      return updated;
    });

    fs.writeFileSync(filePath, content, 'utf-8');
    console.log(`Updated ${filePath}`);
  } catch (error) {
    console.error(`Error updating ${filePath}:`, error.message);
  }
}

// Directory containing Markdown files
const markdownDir = path.join(__dirname, 'v1-docs');

fs.readdirSync(markdownDir).forEach((file) => {
  const filePath = path.join(markdownDir, file);
  if (file.endsWith('.md')) {
    updateMarkdownFrontmatter(filePath);
  }
});

/*
Step 3: Migrate Configuration Settings

Docusaurus v2 uses `docusaurus.config.js` instead of `siteConfig.js`.

Example: Update the configuration file below.
*/

const docusaurusConfig = `
module.exports = {
  title: 'My Project',
  tagline: 'Documentation made easy',
  url: 'https://my-project.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',

  // Update navigation bar settings
  themeConfig: {
    navbar: {
      title: 'My Project',
      logo: {
        alt: 'My Project Logo',
        src: 'img/logo.svg',
      },
      items: [
        { to: '/docs/intro', label: 'Docs', position: 'left' },
        { href: 'https://github.com/my-project', label: 'GitHub', position: 'right' },
      ],
    },
  },

  // Add plugins and presets
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
        },
      },
    ],
  ],
};
`;

const configPath = path.join(__dirname, 'my-new-docusaurus-project', 'docusaurus.config.js');

try {
  fs.writeFileSync(configPath, docusaurusConfig, 'utf-8');
  console.log('Configuration file updated successfully.');
} catch (error) {
  console.error('Error updating configuration file:', error.message);
}

/*
Step 4: Run the Development Server

Navigate to the new Docusaurus project directory and start the development server.
*/
try {
  console.log('Starting Docusaurus development server...');
  execSync('cd my-new-docusaurus-project && npm start', { stdio: 'inherit' });
} catch (error) {
  console.error('Error starting the development server:', error.message);
}
```
