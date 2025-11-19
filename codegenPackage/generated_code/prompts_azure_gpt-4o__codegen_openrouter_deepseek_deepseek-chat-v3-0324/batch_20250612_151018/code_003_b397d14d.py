"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: Provide code to migrate a Docusaurus v1 project to v2, ensuring compatibility with MDX and React components.
Generated: DETERMINISTIC_b397d14dd9a70b16
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// migration.js
const fs = require('fs');
const path = require('path');
const { promisify } = require('util');
const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);
const glob = promisify(require('glob'));

// Configuration
const DOCUSAURUS_V1_DIR = './website'; // Your v1 project directory
const DOCUSAURUS_V2_DIR = './docusaurus'; // Your v2 project directory
const DOCS_DIR = 'docs';
const PAGES_DIR = 'pages';
const BLOG_DIR = 'blog';
const STATIC_DIR = 'static';

async function migrate() {
  try {
    // Create v2 directory structure
    await createDirectoryStructure();
    
    // Migrate docs
    await migrateDocs();
    
    // Migrate pages
    await migratePages();
    
    // Migrate blog
    await migrateBlog();
    
    // Migrate static assets
    await migrateStaticAssets();
    
    // Migrate siteConfig.js to docusaurus.config.js
    await migrateConfig();
    
    // Migrate sidebars.json
    await migrateSidebars();
    
    console.log('Migration completed successfully!');
  } catch (error) {
    console.error('Migration failed:', error);
  }
}

async function createDirectoryStructure() {
  const dirs = [
    path.join(DOCUSAURUS_V2_DIR, DOCS_DIR),
    path.join(DOCUSAURUS_V2_DIR, PAGES_DIR),
    path.join(DOCUSAURUS_V2_DIR, BLOG_DIR),
    path.join(DOCUSAURUS_V2_DIR, STATIC_DIR),
  ];

  for (const dir of dirs) {
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
  }
}

async function migrateDocs() {
  const docsFiles = await glob(path.join(DOCUSAURUS_V1_DIR, 'docs', '**/*.md'));
  
  for (const file of docsFiles) {
    const relativePath = path.relative(path.join(DOCUSAURUS_V1_DIR, 'docs'), file);
    const newPath = path.join(DOCUSAURUS_V2_DIR, DOCS_DIR, relativePath);
    
    let content = await readFile(file, 'utf8');
    
    // Convert v1 doc metadata to v2 frontmatter
    content = convertMetadataToFrontmatter(content);
    
    // Ensure proper MDX compatibility
    content = ensureMdxCompatibility(content);
    
    await writeFile(newPath, content);
  }
}

async function migratePages() {
  const pagesFiles = await glob(path.join(DOCUSAURUS_V1_DIR, 'pages', '**/*.js'));
  
  for (const file of pagesFiles) {
    const relativePath = path.relative(path.join(DOCUSAURUS_V1_DIR, 'pages'), file);
    const newPath = path.join(DOCUSAURUS_V2_DIR, 'src', PAGES_DIR, relativePath);
    
    let content = await readFile(file, 'utf8');
    
    // Update React imports if needed
    content = updateReactImports(content);
    
    // Update Docusaurus-specific components
    content = updateDocusaurusComponents(content);
    
    await writeFile(newPath, content);
  }
}

async function migrateBlog() {
  const blogFiles = await glob(path.join(DOCUSAURUS_V1_DIR, 'blog', '**/*.md'));
  
  for (const file of blogFiles) {
    const relativePath = path.relative(path.join(DOCUSAURUS_V1_DIR, 'blog'), file);
    const newPath = path.join(DOCUSAURUS_V2_DIR, BLOG_DIR, relativePath);
    
    let content = await readFile(file, 'utf8');
    
    // Convert v1 blog metadata to v2 frontmatter
    content = convertMetadataToFrontmatter(content);
    
    await writeFile(newPath, content);
  }
}

async function migrateStaticAssets() {
  const staticFiles = await glob(path.join(DOCUSAURUS_V1_DIR, 'static', '**/*'));
  
  for (const file of staticFiles) {
    if (fs.lstatSync(file).isDirectory()) continue;
    
    const relativePath = path.relative(path.join(DOCUSAURUS_V1_DIR, 'static'), file);
    const newPath = path.join(DOCUSAURUS_V2_DIR, STATIC_DIR, relativePath);
    
    fs.copyFileSync(file, newPath);
  }
}

async function migrateConfig() {
  const configPath = path.join(DOCUSAURUS_V1_DIR, 'siteConfig.js');
  if (!fs.existsSync(configPath)) return;
  
  let content = await readFile(configPath, 'utf8');
  
  // Convert v1 config to v2 format
  content = content
    .replace(/module\.exports =/, '// @ts-check\n\n/** @type {import(\'@docusaurus/types\').Config} */\nconst config =')
    .replace(/title:/, 'title:')
    .replace(/tagline:/, 'tagline:')
    .replace(/url:/, 'url:')
    .replace(/baseUrl:/, 'baseUrl:')
    .replace(/organizationName:/, 'organizationName:')
    .replace(/projectName:/, 'projectName:')
    .replace(/headerLinks:/, 'navbar: {\n      items: [')
    .replace(/docs:\s*['"](.*)['"]/, 'to: \'docs/$1\'')
    .replace(/page:\s*['"](.*)['"]/, 'to: \'$1\'')
    .replace(/blog:\s*true/, 'to: \'blog\'')
    .replace(/\]/, ']\n    }')
    .replace(/footerIcon:/, 'logo:')
    .replace(/copyright:/, 'copyright:')
    .replace(/gaTrackingId:/, 'gtag: {\n      trackingID:')
    .replace(/algolia:/, 'algolia: {\n      apiKey:')
    .replace(/,\s*indexName:/, ',\n      indexName:')
    .replace(/,\s*inputSelector:/, ',\n      searchParameters: {}')
    .replace(/enableUpdateTime:\s*true/, 'showLastUpdateTime: true')
    .replace(/enableUpdateBy:\s*true/, 'showLastUpdateAuthor: true')
    .replace(/scripts:/, 'scripts:')
    .replace(/stylesheets:/, 'stylesheets:')
    .replace(/onPageNav:/, 'onPageNav:')
    .replace(/scrollToTop:/, 'scrollToTop:')
    .replace(/scrollToTopOptions:/, 'scrollToTopOptions:')
    .replace(/twitterUsername:/, 'twitterUsername:')
    .replace(/twitterImage:/, 'twitterImage:')
    .replace(/ogImage:/, 'ogImage:')
    .replace(/cleanUrl:/, 'trailingSlash:')
    .replace(/true/, 'false')
    .replace(/false/, 'true')
    .replace(/module\.exports = siteConfig;/, 'module.exports = config;');
  
  const newConfigPath = path.join(DOCUSAURUS_V2_DIR, 'docusaurus.config.js');
  await writeFile(newConfigPath, content);
}

async function migrateSidebars() {
  const sidebarPath = path.join(DOCUSAURUS_V1_DIR, 'sidebars.json');
  if (!fs.existsSync(sidebarPath)) return;
  
  let content = await readFile(sidebarPath, 'utf8');
  
  // Convert v1 sidebar to v2 format
  content = content
    .replace(/"docs":/, '"tutorialSidebar": [')
    .replace(/"id":/g, '"type": "doc",\n      "id":')
    .replace(/"category":/g, '"type": "category",\n      "label":')
    .replace(/"items":/g, '"items":');
  
  const newSidebarPath = path.join(DOCUSAURUS_V2_DIR, 'sidebars.js');
  await writeFile(newSidebarPath, `module.exports = ${content};`);
}

function convertMetadataToFrontmatter(content) {
  const metadataRegex = /^id:\s*(.*)\n^title:\s*(.*)\n^sidebar_label:\s*(.*)\n^original_id:\s*(.*)/gm;
  return content.replace(metadataRegex, (match, id, title, sidebarLabel, originalId) => {
    return `---\nid: ${id}\ntitle: ${title}\nsidebar_label: ${sidebarLabel}\noriginal_id: ${originalId}\n---\n`;
  });
}

function ensureMdxCompatibility(content) {
  // Handle any MDX-specific compatibility issues
  return content
    .replace(/```(.*)\n([\s\S]*?)\n```/g, '```$1\n$2\n```')
    .replace(/<br\s*\/?>/g, '\n\n');
}

function updateReactImports(content) {
  return content
    .replace(/require
