"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2735--docusaurus-2.netlify.app
Prompt: Generate a code example for customizing the layout of a Docusaurus project using React.
Generated: DETERMINISTIC_f6b768d1cbb510c8
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// src/theme/Layout.js
import React from 'react';
import { useLocation } from '@docusaurus/router';
import { Navbar, Footer } from '@docusaurus/preset-classic';
import styles from './styles.module.css';

/**
 * Custom layout component for Docusaurus project
 * @param {object} props - Component props
 * @param {React.ReactNode} props.children - Page content
 */
function Layout(props) {
  const location = useLocation();

  // Check if the current page is the homepage
  const isHomePage = location.pathname === '/';

  return (
    <div className={styles.container}>
      <Navbar />
      <main className={styles.main}>{props.children}</main>
      {!isHomePage && <Footer />}
    </div>
  );
}

export default Layout;
```

```css
/* src/theme/styles.module.css */
.container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.main {
  flex-grow: 1;
  padding: 20px;
}
```

```jsx
// src/pages/index.js
import React from 'react';
import Layout from '@theme/Layout';
import useDocusaurusContext from '@docusaurus/core/lib/hooks/useDocusaurusContext';

function Home() {
  const context = useDocusaurusContext();
  const { siteConfig } = context;

  return (
    <Layout title={siteConfig.title} description={siteConfig.tagline}>
      <h1>Welcome to {siteConfig.title}</h1>
      <p>{siteConfig.tagline}</p>
    </Layout>
  );
}

export default Home;
```

```jsx
// src/pages/custom-page.js
import React from 'react';
import Layout from '@theme/Layout';

function CustomPage() {
  return (
    <Layout title="Custom Page" description="This is a custom page">
      <h1>Custom Page Content</h1>
    </Layout>
  );
}

export default CustomPage;
```

```javascript
// docusaurus.config.js
module.exports = {
  // ...
  themeConfig: {
    // ...
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        // ...
      },
    ],
  ],
};
```

```javascript
// docusaurus.config.js (updated)
/* eslint-disable @typescript-eslint/no-var-requires */
const config = {
  // ...
  themeConfig: {
    customCss: require.resolve('./src/theme/styles.module.css'),
  },
  // ...
};

module.exports = config;
```
