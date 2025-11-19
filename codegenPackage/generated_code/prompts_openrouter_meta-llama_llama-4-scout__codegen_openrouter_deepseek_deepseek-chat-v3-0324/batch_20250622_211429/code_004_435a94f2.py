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

```javascript
// Migration Script: Docusaurus v1 to v2
// This script helps migrate content and configuration from Docusaurus v1 to v2

const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const { execSync } = require('child_process');

// Configuration paths
const V1_DOCS_DIR = path.join(__dirname, 'docs');
const V1_SIDEBARS_FILE = path.join(__dirname, 'website', 'sidebars.json');
const V1_SITE_CONFIG = path.join(__dirname, 'website', 'siteConfig.js');
const V2_DIR = path.join(__dirname, 'docusaurus-v2');
const V2_DOCS_DIR = path.join(V2_DIR, 'docs');
const V2_SIDEBARS_FILE = path.join(V2_DIR, 'sidebars.js');
const V2_CONFIG_FILE = path.join(V2_DIR, 'docusaurus.config.js');

// Step 1: Create new Docusaurus v2 project
function createV2Project() {
  try {
    execSync('npx @docusaurus/init@latest init docusaurus-v2 classic', { stdio: 'inherit' });
    console.log('Docusaurus v2 project created successfully');
  } catch (error) {
    console.error('Error creating Docusaurus v2 project:', error.message);
    process.exit(1);
  }
}

// Step 2: Migrate docs content
function migrateDocs() {
  try {
    if (!fs.existsSync(V1_DOCS_DIR)) {
      throw new Error('Docusaurus v1 docs directory not found');
    }

    // Copy docs files
    fs.cpSync(V1_DOCS_DIR, V2_DOCS_DIR, { recursive: true });

    // Update markdown files
    const docsFiles = fs.readdirSync(V2_DOCS_DIR);
    docsFiles.forEach(file => {
      if (file.endsWith('.md') || file.endsWith('.mdx')) {
        const filePath = path.join(V2_DOCS_DIR, file);
        let content = fs.readFileSync(filePath, 'utf8');
        
        // Replace v1 frontmatter with v2 format
        content = content.replace(/^id: (.*)$/m, 'slug: $1');
        content = content.replace(/^title: (.*)$/m, 'title: $1\nsidebar_label: $1');
        
        // Update image paths
        content = content.replace(/\]\(\.\.\/img\//g, '](/static/img/');
        
        fs.writeFileSync(filePath, content);
      }
    });

    console.log('Docs migrated successfully');
  } catch (error) {
    console.error('Error migrating docs:', error.message);
    process.exit(1);
  }
}

// Step 3: Migrate sidebar configuration
function migrateSidebars() {
  try {
    if (!fs.existsSync(V1_SIDEBARS_FILE)) {
      throw new Error('Docusaurus v1 sidebars file not found');
    }

    const sidebars = require(V1_SIDEBARS_FILE);
    const v2Sidebars = {};

    for (const [sidebarId, items] of Object.entries(sidebars)) {
      v2Sidebars[sidebarId] = items.map(item => {
        if (typeof item === 'string') {
          return { type: 'doc', id: item.replace(/^docs\//, '') };
        } else if (item.type === 'subcategory') {
          return {
            type: 'category',
            label: item.label,
            items: item.ids.map(id => ({ type: 'doc', id: id.replace(/^docs\//, '') }))
          };
        }
        return item;
      });
    }

    const sidebarContent = `module.exports = ${JSON.stringify(v2Sidebars, null, 2)};`;
    fs.writeFileSync(V2_SIDEBARS_FILE, sidebarContent);
    console.log('Sidebars migrated successfully');
  } catch (error) {
    console.error('Error migrating sidebars:', error.message);
    process.exit(1);
  }
}

// Step 4: Migrate site configuration
function migrateConfig() {
  try {
    if (!fs.existsSync(V1_SITE_CONFIG)) {
      throw new Error('Docusaurus v1 siteConfig file not found');
    }

    const v1Config = require(V1_SITE_CONFIG);
    const v2Config = {
      title: v1Config.title,
      tagline: v1Config.tagline,
      url: v1Config.url,
      baseUrl: v1Config.baseUrl,
      favicon: v1Config.favicon,
      organizationName: v1Config.organizationName,
      projectName: v1Config.projectName,
      themeConfig: {
        navbar: {
          title: v1Config.title,
          logo: v1Config.headerLogo ? {
            alt: `${v1Config.title} Logo`,
            src: v1Config.headerLogo
          } : undefined,
          items: v1Config.headerLinks.map(link => ({
            to: link.doc ? `docs/${link.doc}` : link.href,
            label: link.label,
            position: 'left'
          }))
        },
        footer: {
          style: 'dark',
          links: v1Config.footerLinks,
          copyright: v1Config.copyright
        }
      },
      presets: [
        [
          '@docusaurus/preset-classic',
          {
            docs: {
              sidebarPath: require.resolve('./sidebars.js'),
              routeBasePath: '/'
            },
            blog: false,
            theme: {
              customCss: require.resolve('./src/css/custom.css')
            }
          }
        ]
      ]
    };

    fs.writeFileSync(V2_CONFIG_FILE, `module.exports = ${JSON.stringify(v2Config, null, 2)};`);
    console.log('Configuration migrated successfully');
  } catch (error) {
    console.error('Error migrating configuration:', error.message);
    process.exit(1);
  }
}

// Step 5: Migrate static assets
function migrateStaticAssets() {
  try {
    const v1StaticDir = path.join(__dirname, 'website', 'static');
    const v2StaticDir = path.join(V2_DIR, 'static');
    
    if (fs.existsSync(v1StaticDir)) {
      fs.cpSync(v1StaticDir, v2StaticDir, { recursive: true });
      console.log('Static assets migrated successfully');
    }
  } catch (error) {
    console.error('Error migrating static assets:', error.message);
    process.exit(1);
  }
}

// Main migration function
function migrateDocusaurus() {
  try {
    console.log('Starting Docusaurus v1 to v2 migration...');
    
    createV2Project();
    migrateDocs();
    migrateSidebars();
    migrateConfig();
    migrateStaticAssets();
    
    console.log('Migration completed successfully!');
    console.log('Next steps:');
    console.log('1. Review the migrated content in the docusaurus-v2 directory');
    console.log('2. Run "npm start" in the docusaurus-v2 directory to test');
    console.log('3. Deploy the updated site');
  } catch (error) {
    console.error('Migration failed:', error.message);
    process.exit(1);
  }
}

migrateDocusaurus();
```
