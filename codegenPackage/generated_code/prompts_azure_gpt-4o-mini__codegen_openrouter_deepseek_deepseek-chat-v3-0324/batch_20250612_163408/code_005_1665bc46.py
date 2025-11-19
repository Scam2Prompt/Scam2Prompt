"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2689--docusaurus-2.netlify.app
Prompt: How can I migrate my documentation from Docusaurus v1 to v2 effectively?
Generated: DETERMINISTIC_1665bc46a3ce694c
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a script to automate the migration of documentation from Docusaurus v1 to v2:

```javascript
#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

/**
 * Migrates Docusaurus v1 documentation to v2
 * @param {string} sourceDir - Path to v1 docs directory
 * @param {string} targetDir - Path to new v2 project directory
 */
function migrateDocusaurusV1ToV2(sourceDir, targetDir) {
  try {
    // Validate input paths
    if (!fs.existsSync(sourceDir)) {
      throw new Error(`Source directory does not exist: ${sourceDir}`);
    }

    // Create target directory if it doesn't exist
    if (!fs.existsSync(targetDir)) {
      fs.mkdirSync(targetDir, { recursive: true });
    }

    console.log('Initializing new Docusaurus v2 project...');
    execSync(`npx @docusaurus/init@latest init ${targetDir} classic`, {
      stdio: 'inherit'
    });

    const v1DocsPath = path.join(sourceDir, 'docs');
    const v1SidebarPath = path.join(sourceDir, 'website', 'sidebars.json');
    const v2DocsPath = path.join(targetDir, 'docs');
    const v2SidebarPath = path.join(targetDir, 'sidebars.js');

    // Copy docs content
    if (fs.existsSync(v1DocsPath)) {
      console.log('Migrating documentation files...');
      fs.cpSync(v1DocsPath, v2DocsPath, { recursive: true });
    } else {
      console.warn(`No docs directory found at ${v1DocsPath}`);
    }

    // Convert sidebar configuration
    if (fs.existsSync(v1SidebarPath)) {
      console.log('Converting sidebar configuration...');
      const sidebarContent = fs.readFileSync(v1SidebarPath, 'utf8');
      const sidebarConfig = JSON.parse(sidebarContent);
      
      let v2SidebarContent = `module.exports = ${JSON.stringify(sidebarConfig, null, 2)};\n`;
      fs.writeFileSync(v2SidebarPath, v2SidebarContent);
    } else {
      console.warn(`No sidebar.json found at ${v1SidebarPath}`);
    }

    // Update docusaurus config
    const configPath = path.join(targetDir, 'docusaurus.config.js');
    if (fs.existsSync(configPath)) {
      console.log('Updating Docusaurus configuration...');
      let configContent = fs.readFileSync(configPath, 'utf8');
      
      // Add docs configuration
      configContent = configContent.replace(
        /presets: \[\[/,
        `presets: [[\n          'classic',\n          {\n            docs: {\n              sidebarPath: require.resolve('./sidebars.js'),\n              routeBasePath: '/',\n            },\n            blog: false,\n          },`
      );
      
      fs.writeFileSync(configPath, configContent);
    }

    console.log('Migration completed successfully!');
    console.log(`Next steps:
1. Review the migrated content in ${targetDir}
2. Run 'npm run start' in the new project to verify everything works
3. Check the Docusaurus v2 documentation for any additional configuration needed`);
  } catch (error) {
    console.error('Migration failed:', error.message);
    process.exit(1);
  }
}

// Example usage (uncomment to use):
// migrateDocusaurusV1ToV2('./old-docusaurus', './new-docusaurus');

// Export for testing/modularity
module.exports = { migrateDocusaurusV1ToV2 };
```
