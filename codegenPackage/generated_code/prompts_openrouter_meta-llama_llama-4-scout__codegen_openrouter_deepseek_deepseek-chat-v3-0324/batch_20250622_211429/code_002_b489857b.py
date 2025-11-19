"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Generate a code example for extending the layout of a Docusaurus project using React.
Generated: DETERMINISTIC_b489857b2d696808
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
 * CustomLayout extends the default Docusaurus Layout component
 * to add custom elements while maintaining all existing functionality.
 * 
 * @param {Object} props - Component props
 * @param {ReactNode} props.children - Child components to render
 * @param {string} [props.title] - Page title
 * @param {string} [props.description] - Page description
 * @returns {JSX.Element} Custom layout component
 */
function CustomLayout({ children, title, description }) {
  return (
    <Layout title={title} description={description}>
      {/* Custom header section */}
      <header className="custom-header">
        <div className="container">
          <h1 className="header-title">{title}</h1>
          <p className="header-description">{description}</p>
        </div>
      </header>

      {/* Main content area */}
      <main className="custom-main">
        {children}
      </main>

      {/* Custom footer section */}
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

```css
/* src/css/custom.css */

.custom-header {
  background-color: var(--ifm-color-primary);
  color: white;
  padding: 2rem 0;
  margin-bottom: 2rem;
}

.header-title {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.header-description {
  font-size: 1.2rem;
  opacity: 0.9;
}

.custom-main {
  min-height: calc(100vh - 300px);
  padding: 2rem 0;
}

.custom-footer {
  background-color: var(--ifm-footer-background-color);
  padding: 2rem 0;
  text-align: center;
}
```

```jsx
// src/pages/index.js

import React from 'react';
import CustomLayout from '../components/CustomLayout';

function Home() {
  return (
    <CustomLayout 
      title="Welcome to My Docs" 
      description="A custom Docusaurus implementation"
    >
      <div className="container">
        <h2>Home Page Content</h2>
        <p>This page uses our custom layout component.</p>
      </div>
    </CustomLayout>
  );
}

export default Home;
```

```js
// docusaurus.config.js

module.exports = {
  // ... existing config ...
  plugins: [
    // ... other plugins ...
    [
      '@docusaurus/plugin-content-docs',
      {
        // ... doc plugin config ...
      },
    ],
  ],
  themes: [
    // ... other themes ...
    [
      '@docusaurus/theme-classic',
      {
        customCss: require.resolve('./src/css/custom.css'),
      },
    ],
  ],
};
```
  navbar: {
      title: 'My Site',
      items: [
        // ... existing navbar items ...
      ],
    },
  },
};
```
