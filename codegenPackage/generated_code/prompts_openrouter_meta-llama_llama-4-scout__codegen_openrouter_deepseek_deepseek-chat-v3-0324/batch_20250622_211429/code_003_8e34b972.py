"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: Create a code example for a custom Docusaurus theme that reuses the default header and footer.
Generated: DETERMINISTIC_8e34b972dff86075
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/theme/Layout.js
import React from 'react';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

// Custom layout component that reuses the default header and footer
function CustomLayout({children, title, description}) {
  const {siteConfig} = useDocusaurusContext();

  return (
    <Layout
      title={title}
      description={description || siteConfig.tagline}
    >
      <Head>
        {/* Add any custom meta tags here */}
        <meta property="og:type" content="website" />
      </Head>

      {/* Reuse default header via Layout component */}
      
      {/* Main content */}
      <main className="custom-main">
        {children}
      </main>

      {/* Footer is automatically included via Layout component */}
    </Layout>
  );
}

export default CustomLayout;
```

```javascript
// src/theme/custom.css
/* Custom styles for the theme */
.custom-main {
  padding: 2rem 0;
  flex: 1;
  width: 100%;
}

/* Override default styles if needed */
:root {
  --ifm-color-primary: #25c2a0;
  --ifm-color-primary-dark: #20a78d;
  --ifm-color-primary-darker: #1e9c84;
  --ifm-color-primary-darkest: #18806c;
  --ifm-color-primary-light: #2ad1ae;
  --ifm-color-primary-lighter: #32d6b2;
  --ifm-color-primary-lightest: #4fddbf;
}
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... existing config ...

  themes: [
    // Keep default theme
    '@docusaurus/theme-classic',
  ],

  plugins: [
    // Your plugins here
  ],

  themeConfig: {
    // Your theme config here
    navbar: {
      // Your navbar config (will be reused by CustomLayout)
      title: 'My Site',
      items: [
        {
          to: 'docs/',
          activeBasePath: 'docs',
          label: 'Docs',
          position: 'left',
        },
        // ... other navbar items
      ],
    },
    footer: {
      // Your footer config (will be reused by CustomLayout)
      style: 'dark',
      links: [
        // ... footer links
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc.`,
    },
  },
};
```

```javascript
// src/pages/index.js
import React from 'react';
import CustomLayout from '../theme/Layout';

function Home() {
  return (
    <CustomLayout title="Home" description="Welcome to my website">
      <div className="container">
        <h1>Welcome to My Custom Docusaurus Site</h1>
        <p>This page uses a custom layout while reusing the default header and footer.</p>
      </div>
    </CustomLayout>
  );
}

export default Home;
```
