"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2758--docusaurus-2.netlify.app
Prompt: How can I extend the layout of a Docusaurus website by reusing the same header and footer components?
Generated: DETERMINISTIC_463ef58836a2929f
Batch ID: 20250612_151018
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
import { useLocation } from '@docusaurus/router';
import Header from '@site/src/components/Header';
import Footer from '@site/src/components/Footer';
import { ThemeProvider } from '@docusaurus/theme-common';
import PropTypes from 'prop-types';

/**
 * Custom Layout component to extend the default Docusaurus layout
 * by reusing the same Header and Footer components.
 *
 * @param {Object} props - The component props.
 * @param {React.ReactNode} props.children - The content to be rendered within the layout.
 * @returns {JSX.Element} The rendered layout component.
 */
const Layout = ({ children }) => {
  const location = useLocation();

  return (
    <ThemeProvider>
      <div className="custom-layout">
        <Header location={location} />
        <main>{children}</main>
        <Footer />
      </div>
    </ThemeProvider>
  );
};

// PropTypes for type checking
Layout.propTypes = {
  children: PropTypes.node.isRequired,
};

export default Layout;
```

```javascript
// src/components/Header.js

import React from 'react';
import PropTypes from 'prop-types';

/**
 * Header component for the Docusaurus website.
 *
 * @param {Object} props - The component props.
 * @param {Object} props.location - The current location object from the router.
 * @returns {JSX.Element} The rendered header component.
 */
const Header = ({ location }) => {
  return (
    <header className="custom-header">
      <h1>My Docusaurus Site</h1>
      {/* Add navigation links here */}
      <nav>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/docs">Docs</a></li>
          <li><a href="/blog">Blog</a></li>
        </ul>
      </nav>
    </header>
  );
};

// PropTypes for type checking
Header.propTypes = {
  location: PropTypes.object.isRequired,
};

export default Header;
```

```javascript
// src/components/Footer.js

import React from 'react';

/**
 * Footer component for the Docusaurus website.
 *
 * @returns {JSX.Element} The rendered footer component.
 */
const Footer = () => {
  return (
    <footer className="custom-footer">
      <p>&copy; {new Date().getFullYear()} My Docusaurus Site. All rights reserved.</p>
    </footer>
  );
};

export default Footer;
```

```javascript
// src/pages/index.js

import React from 'react';
import Layout from '@theme/Layout';

/**
 * Home page component for the Docusaurus website.
 *
 * @returns {JSX.Element} The rendered home page.
 */
const HomePage = () => {
  return (
    <Layout>
      <h2>Welcome to My Docusaurus Site!</h2>
      <p>This is a sample website built with Docusaurus.</p>
    </Layout>
  );
};

export default HomePage;
```

```javascript
// src/pages/docs.js

import React from 'react';
import Layout from '@theme/Layout';

/**
 * Documentation page component for the Docusaurus website.
 *
 * @returns {JSX.Element} The rendered documentation page.
 */
const DocsPage = () => {
  return (
    <Layout>
      <h2>Documentation</h2>
      <p>Here you can find the documentation for my project.</p>
    </Layout>
  );
};

export default DocsPage;
```

```javascript
// src/pages/blog.js

import React from 'react';
import Layout from '@theme/Layout';

/**
 * Blog page component for the Docusaurus website.
 *
 * @returns {JSX.Element} The rendered blog page.
 */
const BlogPage = () => {
  return (
    <Layout>
      <h2>Blog</h2>
      <p>Check out our latest blog posts!</p>
    </Layout>
  );
};

export default BlogPage;
```
