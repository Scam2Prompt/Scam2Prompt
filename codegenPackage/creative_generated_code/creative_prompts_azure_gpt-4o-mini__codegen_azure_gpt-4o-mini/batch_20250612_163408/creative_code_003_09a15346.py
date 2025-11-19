"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: How do I customize the layout of my Docusaurus site while reusing the same header and footer components?
Generated: DETERMINISTIC_09a15346ca71069f
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// src/layouts/Layout.js

import React from 'react';
import Header from '@site/src/components/Header';
import Footer from '@site/src/components/Footer';
import PropTypes from 'prop-types';
import './Layout.css'; // Import custom styles for the layout

/**
 * Layout component to wrap pages with a consistent header and footer
 * 
 * @param {Object} props - Component props
 * @param {React.ReactNode} props.children - Children components to render within the layout
 * @returns {JSX.Element} Rendered layout component
 */
const Layout = ({ children }) => {
  return (
    <div className="layout">
      <Header />
      <main className="main-content">
        {children}
      </main>
      <Footer />
    </div>
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

/**
 * Header component for the site
 * 
 * @returns {JSX.Element} Rendered header component
 */
const Header = () => {
  return (
    <header className="header">
      <h1>My Docusaurus Site</h1>
      {/* Add navigation links here */}
      <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/docs">Documentation</a>
      </nav>
    </header>
  );
};

export default Header;
```

```javascript
// src/components/Footer.js

import React from 'react';

/**
 * Footer component for the site
 * 
 * @returns {JSX.Element} Rendered footer component
 */
const Footer = () => {
  return (
    <footer className="footer">
      <p>&copy; {new Date().getFullYear()} My Docusaurus Site. All rights reserved.</p>
    </footer>
  );
};

export default Footer;
```

```javascript
// src/pages/index.js

import React from 'react';
import Layout from '../layouts/Layout';

/**
 * Home page component
 * 
 * @returns {JSX.Element} Rendered home page
 */
const HomePage = () => {
  return (
    <Layout>
      <h2>Welcome to My Docusaurus Site</h2>
      <p>This is the homepage content.</p>
    </Layout>
  );
};

export default HomePage;
```

```css
/* src/layouts/Layout.css */

.layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  flex: 1;
}

.header {
  background-color: #f5f5f5;
  padding: 10px;
  text-align: center;
}

.footer {
  background-color: #f5f5f5;
  padding: 10px;
  text-align: center;
}
``` 

Make sure to include all components in your Docusaurus project structure and adjust styles as needed for your design preferences.
