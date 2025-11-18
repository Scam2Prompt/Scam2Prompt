"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Provide a code example for customizing the layout of a Docusaurus site by reusing React components for the header and footer.
Generated: DETERMINISTIC_95a3a598d925c5c5
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// src/components/Header.js
import React from 'react';
import { Link } from 'react-router-dom';
import PropTypes from 'prop-types';
import './Header.css'; // Import your header styles

/**
 * Header component for the Docusaurus site.
 * 
 * @param {Object} props - Props for the Header component.
 * @param {string} props.siteTitle - Title of the site.
 */
const Header = ({ siteTitle }) => {
    return (
        <header className="custom-header">
            <h1>{siteTitle}</h1>
            <nav>
                <ul>
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/docs">Documentation</Link></li>
                    <li><Link to="/blog">Blog</Link></li>
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
import './Footer.css'; // Import your footer styles

/**
 * Footer component for the Docusaurus site.
 */
const Footer = () => {
    return (
        <footer className="custom-footer">
            <p>&copy; {new Date().getFullYear()} Your Site Name. All rights reserved.</p>
            <nav>
                <ul>
                    <li><a href="/terms">Terms of Service</a></li>
                    <li><a href="/privacy">Privacy Policy</a></li>
                </ul>
            </nav>
        </footer>
    );
};

export default Footer;
```

```javascript
// src/layouts/Layout.js
import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import './Layout.css'; // Import layout styles

/**
 * Layout component that wraps the main content with a header and footer.
 * 
 * @param {Object} props - Props for the Layout component.
 * @param {React.ReactNode} props.children - The main content to display.
 */
const Layout = ({ children }) => {
    return (
        <div className="custom-layout">
            <Header siteTitle="Your Site Title" />
            <main>{children}</main>
            <Footer />
        </div>
    );
};

export default Layout;
```

```javascript
// src/pages/index.js
import React from 'react';
import Layout from '../layouts/Layout';

/**
 * Home page of the Docusaurus site.
 */
const Home = () => {
    return (
        <Layout>
            <h2>Welcome to Your Site!</h2>
            <p>This is the home page content.</p>
        </Layout>
    );
};

export default Home;
```

```javascript
// src/css/Header.css
.custom-header {
    background-color: #f8f9fa;
    padding: 10px;
    text-align: center;
}

.custom-header nav ul {
    list-style: none;
    padding: 0;
}

.custom-header nav ul li {
    display: inline;
    margin: 0 15px;
}
```

```javascript
// src/css/Footer.css
.custom-footer {
    background-color: #343a40;
    color: white;
    text-align: center;
    padding: 10px;
}
```

```javascript
// src/css/Layout.css
.custom-layout {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.custom-layout main {
    flex: 1;
    padding: 20px;
}
``` 

Make sure to include proper error handling in production-ready code, especially when dealing with network requests or user input, but this example primarily focuses on layout customization, which generally has fewer error-prone areas.
