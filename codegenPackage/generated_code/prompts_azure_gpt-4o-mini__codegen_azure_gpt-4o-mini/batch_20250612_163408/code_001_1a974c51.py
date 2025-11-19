"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2803--docusaurus-2.netlify.app
Prompt: Can you provide a code example of how to extend a Docusaurus project layout using React components?
Generated: DETERMINISTIC_1a974c51277b9b4d
Batch ID: 20250612_163408
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
import { Layout as DocusaurusLayout } from '@docusaurus/theme-classic';
import { useLocation } from '@docusaurus/router';
import PropTypes from 'prop-types';

// Custom Layout component to extend Docusaurus layout
const CustomLayout = ({ children }) => {
  const location = useLocation();

  // Error handling for invalid children
  if (!children) {
    console.error('CustomLayout: No children provided');
    return null;
  }

  return (
    <DocusaurusLayout>
      <header>
        <h1>My Custom Header</h1>
        <nav>
          {/* Example navigation links */}
          <a href="/">Home</a>
          <a href="/docs">Documentation</a>
          <a href="/blog">Blog</a>
        </nav>
      </header>
      <main>
        {/* Render the current location for debugging */}
        <p>Current location: {location.pathname}</p>
        {children}
      </main>
      <footer>
        <p>© {new Date().getFullYear()} My Company</p>
      </footer>
    </DocusaurusLayout>
  );
};

// PropTypes for type checking
CustomLayout.propTypes = {
  children: PropTypes.node.isRequired,
};

export default CustomLayout;
```

```javascript
// src/pages/index.js

import React from 'react';
import CustomLayout from '../theme/Layout';

// Main page component
const HomePage = () => {
  return (
    <CustomLayout>
      <h2>Welcome to My Docusaurus Site</h2>
      <p>This is a custom layout example using React components.</p>
    </CustomLayout>
  );
};

export default HomePage;
```

```javascript
// src/pages/docs.js

import React from 'react';
import CustomLayout from '../theme/Layout';

// Documentation page component
const DocsPage = () => {
  return (
    <CustomLayout>
      <h2>Documentation</h2>
      <p>Here you can find all the documentation for our project.</p>
    </CustomLayout>
  );
};

export default DocsPage;
```

```javascript
// src/pages/blog.js

import React from 'react';
import CustomLayout from '../theme/Layout';

// Blog page component
const BlogPage = () => {
  return (
    <CustomLayout>
      <h2>Blog</h2>
      <p>Read our latest blog posts here.</p>
    </CustomLayout>
  );
};

export default BlogPage;
```

```javascript
// src/theme/CustomHead.js

import React from 'react';
import { Helmet } from 'react-helmet';

// Custom head component for additional meta tags
const CustomHead = () => {
  return (
    <Helmet>
      <title>My Docusaurus Site</title>
      <meta name="description" content="A custom Docusaurus site" />
    </Helmet>
  );
};

export default CustomHead;
```

```javascript
// src/theme/Layout.js (updated to include CustomHead)

import React from 'react';
import { Layout as DocusaurusLayout } from '@docusaurus/theme-classic';
import { useLocation } from '@docusaurus/router';
import PropTypes from 'prop-types';
import CustomHead from './CustomHead';

// Custom Layout component to extend Docusaurus layout
const CustomLayout = ({ children }) => {
  const location = useLocation();

  if (!children) {
    console.error('CustomLayout: No children provided');
    return null;
  }

  return (
    <DocusaurusLayout>
      <CustomHead />
      <header>
        <h1>My Custom Header</h1>
        <nav>
          <a href="/">Home</a>
          <a href="/docs">Documentation</a>
          <a href="/blog">Blog</a>
        </nav>
      </header>
      <main>
        <p>Current location: {location.pathname}</p>
        {children}
      </main>
      <footer>
        <p>© {new Date().getFullYear()} My Company</p>
      </footer>
    </DocusaurusLayout>
  );
};

CustomLayout.propTypes = {
  children: PropTypes.node.isRequired,
};

export default CustomLayout;
```
