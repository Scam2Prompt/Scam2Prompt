"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: Write a React-based customization for a Docusaurus website layout, reusing the header and footer components.
Generated: DETERMINISTIC_70fb132abd627ae6
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/layouts/CustomLayout.js

import React from 'react';
import PropTypes from 'prop-types';
import Header from '../components/Header';
import Footer from '../components/Footer';
import { useLocation } from '@docusaurus/router';
import styles from './CustomLayout.module.css';

/**
 * CustomLayout component that wraps the main content of the Docusaurus site.
 * It includes a reusable header and footer.
 *
 * @param {Object} props - The component props.
 * @param {React.ReactNode} props.children - The content to be displayed within the layout.
 * @returns {JSX.Element} The rendered layout component.
 */
const CustomLayout = ({ children }) => {
  const location = useLocation();

  // Error handling for invalid routes
  if (!children) {
    console.error('No children provided to CustomLayout.');
    return <div>Error: No content available.</div>;
  }

  return (
    <div className={styles.customLayout}>
      <Header location={location} />
      <main className={styles.mainContent}>
        {children}
      </main>
      <Footer />
    </div>
  );
};

// PropTypes for type checking
CustomLayout.propTypes = {
  children: PropTypes.node.isRequired,
};

export default CustomLayout;
```

```javascript
// src/components/Header.js

import React from 'react';
import PropTypes from 'prop-types';
import { Link } from '@docusaurus/router';
import styles from './Header.module.css';

/**
 * Header component for the Docusaurus site.
 *
 * @param {Object} props - The component props.
 * @param {Object} props.location - The current location object from the router.
 * @returns {JSX.Element} The rendered header component.
 */
const Header = ({ location }) => {
  return (
    <header className={styles.header}>
      <nav>
        <Link to="/" className={location.pathname === '/' ? styles.active : ''}>
          Home
        </Link>
        <Link to="/about" className={location.pathname === '/about' ? styles.active : ''}>
          About
        </Link>
        <Link to="/contact" className={location.pathname === '/contact' ? styles.active : ''}>
          Contact
        </Link>
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
import styles from './Footer.module.css';

/**
 * Footer component for the Docusaurus site.
 *
 * @returns {JSX.Element} The rendered footer component.
 */
const Footer = () => {
  return (
    <footer className={styles.footer}>
      <p>&copy; {new Date().getFullYear()} My Docusaurus Site. All rights reserved.</p>
    </footer>
  );
};

export default Footer;
```

```css
/* src/layouts/CustomLayout.module.css */

.customLayout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.mainContent {
  flex: 1;
}
```

```css
/* src/components/Header.module.css */

.header {
  background-color: #f8f9fa;
  padding: 1rem;
}

nav {
  display: flex;
  gap: 1rem;
}

.active {
  font-weight: bold;
  text-decoration: underline;
}
```

```css
/* src/components/Footer.module.css */

.footer {
  background-color: #343a40;
  color: white;
  text-align: center;
  padding: 1rem;
}
```
