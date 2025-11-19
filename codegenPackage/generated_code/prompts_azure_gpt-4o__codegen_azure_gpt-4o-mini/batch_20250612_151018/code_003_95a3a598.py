"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Provide a code example for customizing the layout of a Docusaurus site by reusing React components for the header and footer.
Generated: DETERMINISTIC_95a3a598d925c5c5
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/components/Header.js

import React from 'react';
import { Link } from 'react-router-dom';
import PropTypes from 'prop-types';
import './Header.css'; // Import custom styles for the header

/**
 * Header component for the Docusaurus site.
 * @param {Object} props - Component properties.
 * @param {string} props.siteTitle - The title of the site.
 */
const Header = ({ siteTitle }) => {
    return (
        <header className="custom-header">
            <h1>{siteTitle}</h1>
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

Header.propTypes = {
    siteTitle: PropTypes.string.isRequired,
};

export default Header;
```

```javascript
// src/components/Footer.js

import React from 'react';
import './Footer.css'; // Import custom styles for the footer

/**
 * Footer component for the Docusaurus site.
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
// src/theme/Layout.js

import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import PropTypes from 'prop-types';
import './Layout.css'; // Import custom styles for the layout

/**
 * Custom layout component that wraps the main content with a header and footer.
 * @param {Object} props - Component properties.
 * @param {React.ReactNode} props.children - The main content to be displayed.
 * @param {string} props.siteTitle - The title of the site.
 */
const Layout = ({ children, siteTitle }) => {
    return (
        <div className="custom-layout">
            <Header siteTitle={siteTitle} />
            <main>{children}</main>
            <Footer />
        </div>
    );
};

Layout.propTypes = {
    children: PropTypes.node.isRequired,
    siteTitle: PropTypes.string.isRequired,
};

export default Layout;
```

```javascript
// src/pages/index.js

import React from 'react';
import Layout from '../theme/Layout';

/**
 * Home page component for the Docusaurus site.
 */
const HomePage = () => {
    return (
        <Layout siteTitle="My Docusaurus Site">
            <h2>Welcome to My Docusaurus Site</h2>
            <p>This is a sample site using Docusaurus with a custom layout.</p>
        </Layout>
    );
};

export default HomePage;
```

```javascript
// src/pages/about.js

import React from 'react';
import Layout from '../theme/Layout';

/**
 * About page component for the Docusaurus site.
 */
const AboutPage = () => {
    return (
        <Layout siteTitle="About Us">
            <h2>About Us</h2>
            <p>This page provides information about our site.</p>
        </Layout>
    );
};

export default AboutPage;
```

```javascript
// src/pages/contact.js

import React from 'react';
import Layout from '../theme/Layout';

/**
 * Contact page component for the Docusaurus site.
 */
const ContactPage = () => {
    return (
        <Layout siteTitle="Contact Us">
            <h2>Contact Us</h2>
            <p>Feel free to reach out via email or social media.</p>
        </Layout>
    );
};

export default ContactPage;
```

```css
/* src/components/Header.css */

.custom-header {
    background-color: #f8f9fa;
    padding: 20px;
    text-align: center;
}

.custom-header nav ul {
    list-style-type: none;
    padding: 0;
}

.custom-header nav ul li {
    display: inline;
    margin: 0 15px;
}
```

```css
/* src/components/Footer.css */

.custom-footer {
    background-color: #343a40;
    color: white;
    text-align: center;
    padding: 10px 0;
}
```

```css
/* src/theme/Layout.css */

.custom-layout {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

main {
    flex: 1;
    padding: 20px;
}
```
