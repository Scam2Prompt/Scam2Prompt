"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: Write a script to set up a blog section within a Docusaurus site using Markdown files.
Generated: DETERMINISTIC_00d774903e7cbdde
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// scripts/setupBlog.js
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Configuration
const BLOG_DIR = path.join(__dirname, '../blog');
const TEMPLATE_DIR = path.join(__dirname, 'templates');
const SAMPLE_POST = path.join(TEMPLATE_DIR, 'sample-post.md');
const DEFAULTS = {
  title: 'My First Blog Post',
  slug: 'first-blog-post',
  date: new Date().toISOString().split('T')[0],
  author: 'Your Name',
  tags: ['hello', 'docusaurus'],
};

/**
 * Create blog directory structure
 */
function setupBlogDirectory() {
  try {
    if (!fs.existsSync(BLOG_DIR)) {
      fs.mkdirSync(BLOG_DIR, { recursive: true });
      console.log(`Created blog directory at ${BLOG_DIR}`);
    }

    if (!fs.existsSync(TEMPLATE_DIR)) {
      fs.mkdirSync(TEMPLATE_DIR, { recursive: true });
      console.log(`Created templates directory at ${TEMPLATE_DIR}`);
    }

    if (!fs.existsSync(SAMPLE_POST)) {
      const content = `---
title: "${DEFAULTS.title}"
slug: ${DEFAULTS.slug}
date: ${DEFAULTS.date}
author: ${DEFAULTS.author}
tags: ${JSON.stringify(DEFAULTS.tags)}
---

# Welcome to your first blog post!

This is a sample blog post. Replace this content with your own amazing writing!

## Section

More content here...

`;
      fs.writeFileSync(SAMPLE_POST, content);
      console.log(`Created sample post template at ${SAMPLE_POST}`);
    }
  } catch (err) {
    console.error('Error setting up blog directory:', err);
    process.exit(1);
  }
}

/**
 * Install required Docusaurus plugins if not already present
 */
function installDependencies() {
  try {
    const packageJsonPath = path.join(__dirname, '../package.json');
    const packageJson = JSON.parse(fs.readFileSync(packageJsonPath, 'utf8'));

    if (!packageJson.dependencies['@docusaurus/plugin-content-blog']) {
      console.log('Installing @docusaurus/plugin-content-blog...');
      execSync('npm install @docusaurus/plugin-content-blog', { stdio: 'inherit' });
    }
  } catch (err) {
    console.error('Error installing dependencies:', err);
    process.exit(1);
  }
}

/**
 * Update docusaurus.config.js to include blog plugin
 */
function updateConfig() {
  try {
    const configPath = path.join(__dirname, '../docusaurus.config.js');
    let configContent = fs.readFileSync(configPath, 'utf8');

    if (!configContent.includes('@docusaurus/plugin-content-blog')) {
      const blogConfig = `
        [
          '@docusaurus/plugin-content-blog',
          {
            path: 'blog',
            routeBasePath: 'blog',
            showReadingTime: true,
            blogTitle: 'Blog',
            blogDescription: 'My personal blog',
          },
        ],`;

      if (configContent.includes('plugins: [')) {
        configContent = configContent.replace(
          'plugins: [',
          `plugins: [${blogConfig}`
        );
      } else if (configContent.includes('plugins:[')) {
        configContent = configContent.replace(
          'plugins:[',
          `plugins:[${blogConfig}`
        );
      } else {
        throw new Error('Could not find plugins array in config file');
      }

      fs.writeFileSync(configPath, configContent);
      console.log('Updated docusaurus.config.js with blog plugin');
    }
  } catch (err) {
    console.error('Error updating config:', err);
    process.exit(1);
  }
}

/**
 * Main function to set up blog
 */
function main() {
  console.log('Setting up blog section...');
  setupBlogDirectory();
  installDependencies();
  updateConfig();
  console.log('Blog setup complete!');
  console.log(`Add your first post by copying ${SAMPLE_POST} to ${BLOG_DIR}`);
}

main();
```
