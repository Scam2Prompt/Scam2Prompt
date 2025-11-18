"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2614--docusaurus-2.netlify.app
Prompt: Generate a React-based layout customization for a Docusaurus website, reusing the same header and footer across pages.
Generated: DETERMINISTIC_839ec798828c6b4b
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// src/layouts/Layout.js

import React from 'react';
import PropTypes from 'prop-types';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/layout.css';

/**
 * Layout component that wraps around the main content of the Docusaurus pages.
 * It includes a consistent header and footer across all pages.
 * 
 * @param {Object} props - React props
 * @param {React.Node} props.children - Child components to render within the layout
 */
const Layout = ({ children }) => {
  return (
    <div className="layout">
      {/* Render the Header component */}
      <Header />
      
      <main className="main-content">
        {/* Main content passed as children */}
        {children}
      </main>
      
      {/* Render the Footer component */}
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

```jsx
// src/components/Header.js

import React from 'react';
import { Link } from '@docusaurus/router';
import '../styles/header.css';

/**
 * Header component that renders the navigation and branding for the website.
 */
const Header = () => {
  return (
    <header className="header">
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/about">About</Link></li>
          <li><Link to="/contact">Contact</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
```

```jsx
// src/components/Footer.js

import React from 'react';
import '../styles/footer.css';

/**
 * Footer component that displays information across all pages.
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

```jsx
// src/pages/index.js

import React from 'react';
import Layout from '../layouts/Layout';

/**
 * Home page component that serves as the landing page.
 */
const HomePage = () => {
  return (
    <Layout>
      <h1>Welcome to My Docusaurus Site</h1>
      <p>This is the home page. Explore our content!</p>
    </Layout>
  );
};

export default HomePage;
```

```jsx
// src/pages/about.js

import React from 'react';
import Layout from '../layouts/Layout';

/**
 * About page component that provides information about the site.
 */
const AboutPage = () => {
  return (
    <Layout>
      <h1>About Us</h1>
      <p>This page provides information about our team and mission.</p>
    </Layout>
  );
};

export default AboutPage;
```

```css
/* styles/layout.css */

.layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* styles/header.css */

.header {
  background-color: #333;
  color: white;
  padding: 1rem;
}

.header nav ul {
  list-style: none;
  padding: 0;
}

.header nav ul li {
  display: inline;
  margin-right: 15px;
}

.header nav a {
  color: white;
  text-decoration: none;
}

/* styles/footer.css */

.footer {
  background-color: #333;
  color: white;
  text-align: center;
  padding: 1rem;
  margin-top: auto;
}
```

This code provides a complete layout with reusable Header and Footer components in a Docusaurus website. It includes CSS styles for basic layout and formatting, and uses PropTypes for type checking.
