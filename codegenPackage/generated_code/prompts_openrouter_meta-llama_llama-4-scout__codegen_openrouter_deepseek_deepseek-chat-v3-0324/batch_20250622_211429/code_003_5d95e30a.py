"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2689--docusaurus-2.netlify.app
Prompt: Create a code example that demonstrates how to extend or customize a Docusaurus project's layout using React.
Generated: DETERMINISTIC_5d95e30a5c2b4b70
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// src/components/CustomLayout.js
import React from 'react';
import Layout from '@theme/Layout';

/**
 * CustomLayout component extends the default Docusaurus Layout with additional features
 * @param {Object} props - Component props
 * @param {React.ReactNode} props.children - Child components to render
 * @param {string} [props.title] - Page title
 * @param {string} [props.description] - Page description
 */
function CustomLayout({ children, title, description }) {
  return (
    <Layout title={title} description={description}>
      {/* Custom header section */}
      <header className="custom-header">
        <div className="container">
          <h1 className="hero__title">{title}</h1>
          <p className="hero__subtitle">{description}</p>
        </div>
      </header>

      {/* Main content */}
      <main className="custom-main">
        <div className="container">
          {children}
        </div>
      </main>

      {/* Custom footer */}
      <footer className="custom-footer">
        <div className="container">
          <p>© {new Date().getFullYear()} My Custom Docusaurus Project</p>
        </div>
      </footer>
    </Layout>
  );
}

export default CustomLayout;
```

```jsx
// src/pages/index.js
import React from 'react';
import CustomLayout from '../components/CustomLayout';

/**
 * Home page component using the custom layout
 */
function Home() {
  return (
    <CustomLayout
      title="Welcome to My Docs"
      description="Customized Docusaurus documentation"
    >
      <section className="home-content">
        <h2>Getting Started</h2>
        <p>
          This is a custom home page using our extended layout component.
          Add your content here.
        </p>
      </section>
    </CustomLayout>
  );
}

export default Home;
```

```css
/* src/css/custom.css */
.custom-header {
  background-color: var(--ifm-color-primary);
  color: white;
  padding: 2rem 0;
  text-align: center;
}

.custom-main {
  padding: 2rem 0;
  min-height: calc(100vh - 300px);
}

.custom-footer {
  background-color: var(--ifm-footer-background-color);
  padding: 1rem 0;
  text-align: center;
}

.home-content {
  max-width: 800px;
  margin: 0 auto;
}
```

```js
// docusaurus.config.js
module.exports = {
  // ... existing config ...
  plugins: [
    // ... other plugins ...
    require.resolve('./src/css/custom.css'),
  ],
  // ... rest of config ...
};
```
rem;
  opacity: 0.8;
}

.custom-main {
  min-height: calc(100vh - 300px);
  padding: 2rem 0;
}

.custom-footer {
  background-color: #f5f6f7;
  padding: 2rem 0;
  text-align: center;
}
```
        </div>
      </div>

      <div className={styles.copyright}>
        <p>
          © {new Date().getFullYear()} {siteConfig.title}. All rights reserved.
        </p>
      </div>
    </footer>
  );
}

export default CustomFooter;
```

```css
/* src/components/CustomFooter.module.css */

.footer {
  background-color: var(--ifm-footer-background-color);
  color: var(--ifm-footer-color);
  padding: 2rem 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.logoContainer {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.logoLink {
  display: flex;
}

.logo {
  height: 2.5rem;
}

.tagline {
  margin: 0;
  font-size: 0.9rem;
  opacity: 0.8;
}

.linksContainer {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2rem;
}

.linksColumn {
  min-width: 150px;
}

.columnTitle {
  margin-bottom: 1rem;
  font-size: 1rem;
}

.linkList {
  list-style: none;
  padding: 0;
  margin: 0;
}

.linkList li {
  margin-bottom: 0.5rem;
}

.copyright {
  text-align: center;
  margin-top: 2rem;
  font-size: 0.8rem;
  opacity: 0.7;
}
```

```jsx
// src/theme/Layout.js

import React from 'react';
import Layout from '@theme/Layout';
import CustomFooter from '../../components/CustomFooter';

/**
 * Custom layout component that extends the default Docusaurus layout.
 * 
 * @param {Object} props - Layout props
 * @param {ReactNode} props.children - Child components
 * @param {Object} [props.metadata] - Page metadata
 * @returns {JSX.Element} Custom layout component
 */
export default function CustomLayout({ children, metadata }) {
  return (
    <Layout metadata={metadata}>
      {children}
      <CustomFooter />
    </Layout>
  );
}
```

```jsx
// docusaurus.config.js

module.exports = {
  // ... existing config ...

  themeConfig: {
    // ... existing theme config ...

    footer: {
      // Disable default footer since we're using our custom one
      style: 'dark',
      copyright: false,
    },
  },
};
```
