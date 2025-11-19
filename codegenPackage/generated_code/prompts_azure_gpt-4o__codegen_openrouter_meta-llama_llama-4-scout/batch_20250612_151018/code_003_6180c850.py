"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2785--docusaurus-2.netlify.app
Prompt: Create a Docusaurus plugin to customize the layout of a documentation site using React components while reusing the same header and footer.
Generated: DETERMINISTIC_6180c850f5fce454
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CustomLayoutPlugin.js
import React from 'react';
import { useThemeConfig } from '@docusaurus/theme-common';
import { useLocation } from '@docusaurus/route';
import Layout from '@theme/Layout';
import Header from '@theme/Header';
import Footer from '@theme/Footer';

/**
 * Custom layout plugin for Docusaurus.
 * 
 * This plugin allows for customization of the layout of a documentation site
 * using React components while reusing the same header and footer.
 */
function CustomLayoutPlugin() {
  const themeConfig = useThemeConfig();
  const location = useLocation();

  // Check if the current route requires a custom layout
  const isCustomLayout = location.pathname.startsWith('/custom');

  return (
    <Layout>
      <Header />
      {isCustomLayout ? (
        // Custom layout content
        <div className="custom-layout-content">
          {/* Custom content here */}
          <h1>Custom Layout Page</h1>
        </div>
      ) : (
        // Default layout content
        <div className="default-layout-content">
          {/* Default content here */}
          <h1>Default Layout Page</h1>
        </div>
      )}
      <Footer />
    </Layout>
  );
}

export default CustomLayoutPlugin;
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... other configurations ...
  plugins: [
    [
      '@docusaurus/plugin-content-pages',
      {
        id: 'custom-pages',
        path: 'src/pages/custom',
        routeBasePath: '/custom',
        include: ['**/*.md'],
        exclude: ['**/_*.md'],
        createBottomBar: true,
      },
    ],
    './CustomLayoutPlugin', // Add the custom layout plugin
  ],
};
```

```javascript
// src/pages/custom/index.js
import React from 'react';
import { Link } from '@docusaurus/router';

function CustomPage() {
  return (
    <div>
      <h1>Custom Page</h1>
      <p>
        <Link to="/docs">Back to docs</Link>
      </p>
    </div>
  );
}

export default CustomPage;
```

```css
/* src/css/custom.css */
.custom-layout-content {
  background-color: #f0f0f0;
  padding: 20px;
}

.default-layout-content {
  background-color: #ffffff;
  padding: 20px;
}
```

```javascript
// src/theme/Layout.js
import React from 'react';
import Head from '@docusaurus/Head';
import { useLocation } from '@docusaurus/route';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import { useThemeConfig } from '@docusaurus/theme-common';
import Footer from '@theme/Footer';
import Header from '@theme/Header';

function Layout(props) {
  const { children } = props;
  const themeConfig = useThemeConfig();
  const { siteConfig } = useDocusaurusContext();
  const location = useLocation();

  return (
    <div>
      <Head>
        <title>{siteConfig.title}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>
      <Header />
      <main>{children}</main>
      <Footer />
    </div>
  );
}

export default Layout;
```
