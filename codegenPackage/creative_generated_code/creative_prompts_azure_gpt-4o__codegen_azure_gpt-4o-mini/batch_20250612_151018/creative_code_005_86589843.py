"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: Write code to customize the layout of a Docusaurus site by reusing React components for the header and footer.
Generated: DETERMINISTIC_8658984340fd75c6
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
import { Link } from 'docusaurus-link'; // Adjust the import based on your Docusaurus version
import styles from './Header.module.css'; // Assuming you have a CSS module for styling

/**
 * Header component for the Docusaurus site.
 * @returns {JSX.Element} The header element with navigation links.
 */
const Header = () => {
    return (
        <header className={styles.header}>
            <nav>
                <ul className={styles.navList}>
                    <li>
                        <Link to="/">Home</Link>
                    </li>
                    <li>
                        <Link to="/docs">Documentation</Link>
                    </li>
                    <li>
                        <Link to="/about">About</Link>
                    </li>
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
import styles from './Footer.module.css'; // Assuming you have a CSS module for styling

/**
 * Footer component for the Docusaurus site.
 * @returns {JSX.Element} The footer element with copyright notice and links.
 */
const Footer = () => {
    return (
        <footer className={styles.footer}>
            <div className={styles.footerContent}>
                <p>&copy; {new Date().getFullYear()} Your Company. All rights reserved.</p>
                <nav>
                    <ul className={styles.navList}>
                        <li>
                            <a href="/privacy">Privacy Policy</a>
                        </li>
                        <li>
                            <a href="/terms">Terms of Service</a>
                        </li>
                    </ul>
                </nav>
            </div>
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
import styles from './Layout.module.css'; // Assuming you have a CSS module for styling

/**
 * Main layout component for the Docusaurus site.
 * It includes the header, main content, and footer.
 * @param {Object} props - The props for the component.
 * @param {React.ReactNode} props.children - The content to be rendered.
 * @returns {JSX.Element} The layout with header, content, and footer.
 */
const Layout = ({ children }) => {
    return (
        <div className={styles.layout}>
            <Header />
            <main className={styles.mainContent}>
                {children}
            </main>
            <Footer />
        </div>
    );
};

export default Layout;
```

```javascript
// Example usage in a page or a document
// src/pages/index.js

import React from 'react';
import Layout from '../theme/Layout';

/**
 * Home page component.
 * @returns {JSX.Element} The home page content wrapped in the Layout component.
 */
const HomePage = () => {
    return (
        <Layout>
            <h1>Welcome to Our Docusaurus Site!</h1>
            <p>This is a simple example of customizing the layout.</p>
        </Layout>
    );
};

export default HomePage;
```

```css
/* src/components/Header.module.css */
.header {
    background-color: #f8f9fa;
    padding: 1rem;
}

.navList {
    list-style-type: none;
    display: flex;
    gap: 1rem;
}

/* src/components/Footer.module.css */
.footer {
    background-color: #343a40;
    color: white;
    padding: 1rem;
}

.footerContent {
    display: flex;
    justify-content: space-between;
}

.navList {
    list-style-type: none;
    display: flex;
    gap: 1rem;
}

/* src/theme/Layout.module.css */
.layout {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.mainContent {
    flex: 1;
    padding: 2rem;
}
```
