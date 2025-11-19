"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2758--docusaurus-2.netlify.app
Prompt: Generate a sample Docusaurus layout that reuses React components for a consistent header and footer across pages.
Generated: DETERMINISTIC_88314bc388485f6d
Batch ID: 20250612_163408
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/mywebsite": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://twitter.com/mywebsite": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Docusaurus project sample layout with reusable React components for consistent header and footer across pages
// File: src/components/Header.js
import React from 'react';
import Link from '@docusaurus/Link';
import styles from './Header.module.css'; // CSS Module for styling

const Header = () => {
  return (
    <header className={styles.header}>
      <div className={styles.logo}>
        <Link to="/">MyWebsite</Link>
      </div>
      <nav className={styles.nav}>
        <Link to="/about" className={styles.navLink}>About</Link>
        <Link to="/docs" className={styles.navLink}>Docs</Link>
        <Link to="/contact" className={styles.navLink}>Contact</Link>
      </nav>
    </header>
  );
};

export default Header;

// File: src/components/Footer.js
import React from 'react';
import styles from './Footer.module.css'; // CSS Module for styling

const Footer = () => {
  return (
    <footer className={styles.footer}>
      <p>© {new Date().getFullYear()} MyWebsite. All rights reserved.</p>
      <div className={styles.links}>
        <a href="https://twitter.com/mywebsite" target="_blank" rel="noopener noreferrer">Twitter</a>
        <a href="https://github.com/mywebsite" target="_blank" rel="noopener noreferrer">GitHub</a>
      </div>
    </footer>
  );
};

export default Footer;

// File: src/pages/Layout.js
import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import styles from './Layout.module.css'; // CSS Module for styling

// Layout component ensures consistent header and footer across all pages
const Layout = ({ children }) => {
  return (
    <div className={styles.layout}>
      <Header />
      <main className={styles.main}>
        {children}
      </main>
      <Footer />
    </div>
  );
};

export default Layout;

// File: src/pages/index.js
import React from 'react';
import Layout from './Layout';
import styles from './Home.module.css'; // CSS Module for styling

// Home page content
const Home = () => {
  return (
    <Layout>
      <div className={styles.home}>
        <h1>Welcome to MyWebsite</h1>
        <p>Your one-stop solution for amazing documentation.</p>
      </div>
    </Layout>
  );
};

export default Home;

// File: src/pages/about.js
import React from 'react';
import Layout from './Layout';
import styles from './About.module.css'; // CSS Module for styling

// About page content
const About = () => {
  return (
    <Layout>
      <div className={styles.about}>
        <h1>About Us</h1>
        <p>We are passionate about great documentation and exceptional user experiences.</p>
      </div>
    </Layout>
  );
};

export default About;

// File: src/pages/contact.js
import React from 'react';
import Layout from './Layout';
import styles from './Contact.module.css'; // CSS Module for styling

// Contact page content
const Contact = () => {
  return (
    <Layout>
      <div className={styles.contact}>
        <h1>Contact Us</h1>
        <p>Feel free to reach out via email or our social channels.</p>
      </div>
    </Layout>
  );
};

export default Contact;

// Sample CSS Module: src/components/Header.module.css
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #282c34;
  color: white;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav {
  display: flex;
  gap: 1rem;
}

.navLink {
  color: white;
  text-decoration: none;
}

// Sample CSS Module: src/components/Footer.module.css
.footer {
  text-align: center;
  padding: 1rem;
  background-color: #f1f1f1;
  color: #333;
}

.links a {
  margin: 0 0.5rem;
  color: #0078d4;
  text-decoration: none;
}

// Sample CSS Module: src/pages/Layout.module.css
.layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main {
  flex: 1;
  padding: 2rem;
}

// Sample CSS Module: src/pages/Home.module.css
.home {
  text-align: center;
}

.home h1 {
  font-size: 2.5rem;
}

.home p {
  font-size: 1.25rem;
}

// Sample CSS Module: src/pages/About.module.css
.about {
  padding: 2rem;
}

.about h1 {
  font-size: 2rem;
  color: #444;
}

// Sample CSS Module: src/pages/Contact.module.css
.contact {
  padding: 2rem;
}

.contact h1 {
  font-size: 2rem;
  color: #444;
}
```
