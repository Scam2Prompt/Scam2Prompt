"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: Write code to customize the layout of a Docusaurus site by reusing React components for the header and footer.
Generated: DETERMINISTIC_8658984340fd75c6
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// src/components/CustomHeader.js
import React from 'react';
import { Link } from '@docusaurus/router';

/**
 * Custom header component for Docusaurus site.
 * Reuses existing Docusaurus header components.
 */
function CustomHeader() {
  return (
    <header>
      <nav>
        <ul>
          <li>
            <Link to="/docs">Docs</Link>
          </li>
          <li>
            <Link to="/blog">Blog</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default CustomHeader;
```

```jsx
// src/components/CustomFooter.js
import React from 'react';

/**
 * Custom footer component for Docusaurus site.
 * Reuses existing Docusaurus footer components.
 */
function CustomFooter() {
  return (
    <footer>
      <div>
        &copy; {new Date().getFullYear()} My Docusaurus Site
      </div>
    </footer>
  );
}

export default CustomFooter;
```

```jsx
// src/theme.js
import React from 'react';
import CustomHeader from './components/CustomHeader';
import CustomFooter from './components/CustomFooter';

/**
 * Custom theme for Docusaurus site.
 * Reuses existing Docusaurus theme components.
 */
export default function Theme({ children }) {
  return (
    <div>
      <CustomHeader />
      {children}
      <CustomFooter />
    </div>
  );
}
```

```jsx
// docusaurus.config.js
module.exports = {
  // ...
  themeConfig: {
    // ...
  },
  customFields: {
    // ...
  },
  themes: ['./src/theme'],
};
```

```jsx
// src/pages/index.js
import React from 'react';
import Layout from '@theme/Layout';
import useDocusaurusContext from '@docusaurus/core/lib/modules/useDocusaurusContext';

/**
 * Homepage component for Docusaurus site.
 */
export default function Home() {
  const context = useDocusaurusContext();
  const { siteConfig } = context;

  return (
    <Layout title={siteConfig.title} description={siteConfig.tagline}>
      <h1>Welcome to {siteConfig.title}</h1>
      <p>{siteConfig.tagline}</p>
    </Layout>
  );
}
```

```bash
# yarn add @docusaurus/core @docusaurus/router
```
