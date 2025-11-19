"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2728--docusaurus-2.netlify.app
Prompt: Write a tutorial on migrating a Docusaurus project from version 1 to version 2.
Generated: DETERMINISTIC_a33e1da142b83b44
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// migration-guide.js
/**
 * Docusaurus v1 to v2 Migration Script
 * 
 * This script helps migrate a Docusaurus v1 project to v2.
 * It performs the following steps:
 * 1. Updates package.json dependencies
 * 2. Migrates configuration files
 * 3. Updates directory structure
 * 4. Handles customizations
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Configuration paths
const PATHS = {
  v1Config: path.join(process.cwd(), 'siteConfig.js'),
  v2Config: path.join(process.cwd(), 'docusaurus.config.js'),
  v1Sidebars: path.join(process.cwd(), 'sidebars.json'),
  v2Sidebars: path.join(process.cwd(), 'sidebars.js'),
  packageJson: path.join(process.cwd(), 'package.json')
};

// Migration steps
function migrateDocusaurus() {
  try {
    console.log('Starting Docusaurus v1 to v2 migration...');
    
    // Step 1: Update package.json
    updatePackageJson();
    
    // Step 2: Migrate configuration
    migrateConfig();
    
    // Step 3: Migrate sidebars
    migrateSidebars();
    
    // Step 4: Install new dependencies
    installDependencies();
    
    console.log('Migration completed successfully!');
    console.log('Next steps:');
    console.log('1. Review the new configuration files');
    console.log('2. Test your site locally with `npm run start`');
    console.log('3. Check for any customizations that need updating');
  } catch (error) {
    console.error('Migration failed:', error.message);
    process.exit(1);
  }
}

function updatePackageJson() {
  console.log('Updating package.json...');
  
  if (!fs.existsSync(PATHS.packageJson)) {
    throw new Error('package.json not found');
  }
  
  const packageJson = require(PATHS.packageJson);
  
  // Remove old dependencies
  delete packageJson.dependencies['docusaurus'];
  
  // Add new dependencies
  packageJson.dependencies['@docusaurus/core'] = '^2.0.0';
  packageJson.dependencies['@docusaurus/preset-classic'] = '^2.0.0';
  
  // Update scripts
  packageJson.scripts = {
    ...packageJson.scripts,
    'start': 'docusaurus start',
    'build': 'docusaurus build',
    'swizzle': 'docusaurus swizzle',
    'deploy': 'docusaurus deploy',
    'serve': 'docusaurus serve'
  };
  
  fs.writeFileSync(PATHS.packageJson, JSON.stringify(packageJson, null, 2));
}

function migrateConfig() {
  console.log('Migrating configuration...');
  
  if (!fs.existsSync(PATHS.v1Config)) {
    throw new Error('siteConfig.js not found');
  }
  
  // Load v1 config
  const v1Config = require(PATHS.v1Config);
  
  // Create v2 config
  const v2Config = `// docusaurus.config.js
module.exports = {
  title: '${v1Config.title}',
  tagline: '${v1Config.tagline || ''}',
  url: '${v1Config.url}',
  baseUrl: '${v1Config.baseUrl}',
  favicon: '${v1Config.favicon || 'img/favicon.ico'}',
  organizationName: '${v1Config.organizationName || ''}',
  projectName: '${v1Config.projectName || ''}',
  themeConfig: {
    navbar: {
      title: '${v1Config.headerTitle || v1Config.title}',
      logo: {
        alt: '${v1Config.title} Logo',
        src: '${v1Config.headerLogo || ''}',
      },
      items: ${JSON.stringify(v1Config.headerLinks || [], null, 2)},
    },
    footer: {
      style: '${v1Config.footerIcon ? 'dark' : 'light'}',
      logo: ${v1Config.footerIcon ? `{
        alt: '${v1Config.title} Logo',
        src: '${v1Config.footerIcon}',
        href: '${v1Config.url}',
      }` : 'undefined'},
      copyright: \`Copyright © \${new Date().getFullYear()} ${v1Config.copyright || v1Config.title}\`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          routeBasePath: '/',
        },
        blog: ${v1Config.blog ? JSON.stringify({
          path: 'blog',
          routeBasePath: '/blog',
        }) : 'false'},
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};`;
  
  fs.writeFileSync(PATHS.v2Config, v2Config);
}

function migrateSidebars() {
  console.log('Migrating sidebars...');
  
  if (!fs.existsSync(PATHS.v1Sidebars)) {
    console.log('No sidebars.json found, skipping...');
    return;
  }
  
  const sidebars = require(PATHS.v1Sidebars);
  const sidebarContent = `// sidebars.js
module.exports = ${JSON.stringify(sidebars, null, 2)};`;
  
  fs.writeFileSync(PATHS.v2Sidebars, sidebarContent);
}

function installDependencies() {
  console.log('Installing dependencies...');
  try {
    execSync('npm install', { stdio: 'inherit' });
  } catch (error) {
    throw new Error('Failed to install dependencies');
  }
}

// Run migration
migrateDocusaurus();
```
