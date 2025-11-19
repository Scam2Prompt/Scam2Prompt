"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2614--docusaurus-2.netlify.app
Prompt: Generate a React-based layout customization for a Docusaurus website, reusing the same header and footer across pages.
Generated: DETERMINISTIC_839ec798828c6b4b
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/layouts/Layout.js

import React from 'react';
import PropTypes from 'prop-types';
import Header from '../components/Header';
import Footer from '../components/Footer';
import './Layout.css'; // Import custom styles for the layout

/**
 * Layout component that wraps around the main content of the page.
 * It includes a header and footer that are reused across different pages.
 *
 * @param {Object} props - The props for the Layout component.
 * @param {React.ReactNode} props.children - The content to be displayed within the layout.
 * @returns {JSX.Element} The rendered layout component.
 */
const Layout = ({ children }) => {
    return (
        <div className="layout">
            <Header />
            <main className="layout-content">
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
import { Link } from 'react-router-dom';
import './Header.css'; // Import custom styles for the header

/**
 * Header component that contains navigation links.
 *
 * @returns {JSX.Element} The rendered header component.
 */
const Header = () => {
    return (
        <header className="header">
            <nav>
                <ul className="nav-list">
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

```javascript
// src/components/Footer.js

import React from 'react';
import './Footer.css'; // Import custom styles for the footer

/**
 * Footer component that displays copyright information.
 *
 * @returns {JSX.Element} The rendered footer component.
 */
const Footer = () => {
    return (
        <footer className="footer">
            <p>&copy; {new Date().getFullYear()} Your Company. All rights reserved.</p>
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
 * Home page component.
 *
 * @returns {JSX.Element} The rendered home page.
 */
const HomePage = () => {
    return (
        <Layout>
            <h1>Welcome to Our Docusaurus Site</h1>
            <p>This is the home page content.</p>
        </Layout>
    );
};

export default HomePage;
```

```javascript
// src/pages/about.js

import React from 'react';
import Layout from '../layouts/Layout';

/**
 * About page component.
 *
 * @returns {JSX.Element} The rendered about page.
 */
const AboutPage = () => {
    return (
        <Layout>
            <h1>About Us</h1>
            <p>This is the about page content.</p>
        </Layout>
    );
};

export default AboutPage;
```

```javascript
// src/pages/contact.js

import React from 'react';
import Layout from '../layouts/Layout';

/**
 * Contact page component.
 *
 * @returns {JSX.Element} The rendered contact page.
 */
const ContactPage = () => {
    return (
        <Layout>
            <h1>Contact Us</h1>
            <p>This is the contact page content.</p>
        </Layout>
    );
};

export default ContactPage;
```

```css
/* src/layouts/Layout.css */

.layout {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.layout-content {
    flex: 1;
}
```

```css
/* src/components/Header.css */

.header {
    background-color: #282c34;
    padding: 1rem;
}

.nav-list {
    list-style: none;
    display: flex;
    gap: 1rem;
}

.nav-list a {
    color: white;
    text-decoration: none;
}
```

```css
/* src/components/Footer.css */

.footer {
    background-color: #282c34;
    color: white;
    text-align: center;
    padding: 1rem;
}
```

This code provides a clean, reusable layout for a Docusaurus website, including a header and footer that are consistent across different pages. Each component is well-documented, and styles are separated for maintainability.
