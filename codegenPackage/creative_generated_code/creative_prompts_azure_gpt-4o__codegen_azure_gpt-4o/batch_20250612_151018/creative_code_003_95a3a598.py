"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Provide a code example for customizing the layout of a Docusaurus site by reusing React components for the header and footer.
Generated: DETERMINISTIC_95a3a598d925c5c5
Batch ID: 20250612_151018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your-docusaurus-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-org/your-project/edit/main/website/": {
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
// File: src/components/CustomHeader.js
import React from 'react';
import { useDocusaurusContext } from '@docusaurus/useDocusaurusContext';

// CustomHeader component to replace the default Docusaurus header
const CustomHeader = () => {
  const { siteConfig } = useDocusaurusContext();

  return (
    <header style={{ backgroundColor: '#282c34', color: '#ffffff', padding: '1rem' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1 style={{ margin: 0 }}>{siteConfig.title}</h1>
        <nav>
          <a href="/" style={{ color: '#61dafb', marginRight: '1rem' }}>Home</a>
          <a href="/docs" style={{ color: '#61dafb', marginRight: '1rem' }}>Docs</a>
          <a href="/blog" style={{ color: '#61dafb' }}>Blog</a>
        </nav>
      </div>
    </header>
  );
};

export default CustomHeader;
```

```javascript
// File: src/components/CustomFooter.js
import React from 'react';

// CustomFooter component to replace the default Docusaurus footer
const CustomFooter = () => {
  return (
    <footer style={{ backgroundColor: '#282c34', color: '#ffffff', padding: '1rem', marginTop: '2rem' }}>
      <div style={{ textAlign: 'center' }}>
        <p>&copy; {new Date().getFullYear()} My Docusaurus Site. All rights reserved.</p>
        <p>
          <a href="/privacy" style={{ color: '#61dafb', marginRight: '1rem' }}>Privacy Policy</a>
          <a href="/terms" style={{ color: '#61dafb' }}>Terms of Service</a>
        </p>
      </div>
    </footer>
  );
};

export default CustomFooter;
```

```javascript
// File: src/pages/index.js
import React from 'react';
import Layout from '@theme/Layout';
import CustomHeader from '../components/CustomHeader';
import CustomFooter from '../components/CustomFooter';

// Custom homepage layout using CustomHeader and CustomFooter components
const HomePage = () => {
  return (
    <Layout>
      {/* Replace the default header with CustomHeader */}
      <CustomHeader />
      
      <main style={{ padding: '2rem', textAlign: 'center' }}>
        <h2>Welcome to My Docusaurus Site!</h2>
        <p>Explore the documentation, read the blog, and learn more about our project.</p>
      </main>
      
      {/* Replace the default footer with CustomFooter */}
      <CustomFooter />
    </Layout>
  );
};

export default HomePage;
```

```javascript
// File: docusaurus.config.js
module.exports = {
  title: 'My Docusaurus Site',
  tagline: 'A modern documentation site built with Docusaurus',
  url: 'https://your-docusaurus-site.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'your-org', // Usually your GitHub org/user name.
  projectName: 'your-project', // Usually your repo name.
  themeConfig: {
    navbar: {
      title: 'My Docusaurus Site',
      logo: {
        alt: 'My Docusaurus Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          to: '/docs',
          label: 'Docs',
          position: 'left',
        },
        {
          to: '/blog',
          label: 'Blog',
          position: 'left',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [],
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/your-org/your-project/edit/main/website/',
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/your-org/your-project/edit/main/website/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
```
