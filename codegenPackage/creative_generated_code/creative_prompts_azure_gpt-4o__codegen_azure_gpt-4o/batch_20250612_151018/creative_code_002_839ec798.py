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
// Header.js
import React from 'react';
import { Link } from '@docusaurus/router';
import styles from './Header.module.css';

/**
 * The Header component used across all pages.
 */
const Header = () => {
  return (
    <header className={styles.header}>
      <nav className={styles.nav}>
        <Link to="/" className={styles.navLink}>Home</Link>
        <Link to="/docs" className={styles.navLink}>Docs</Link>
        <Link to="/blog" className={styles.navLink}>Blog</Link>
      </nav>
    </header>
  );
};

export default Header;
```

```jsx
// Footer.js
import React from 'react';
import styles from './Footer.module.css';

/**
 * The Footer component used across all pages.
 */
const Footer = () => {
  return (
    <footer className={styles.footer}>
      <p>&copy; {new Date().getFullYear()} My Docusaurus Site. All Rights Reserved.</p>
    </footer>
  );
};

export default Footer;
```

```jsx
// Layout.js
import React from 'react';
import Header from './Header';
import Footer from './Footer';
import styles from './Layout.module.css';

/**
 * A reusable layout component to wrap content with a common header and footer.
 * @param {Object} props - Props passed to the layout.
 * @param {React.ReactNode} props.children - Content to render inside the layout.
 */
const Layout = ({ children }) => {
  return (
    <div className={styles.layout}>
      <Header />
      <main className={styles.main}>{children}</main>
      <Footer />
    </div>
  );
};

export default Layout;
```

```jsx
// styles/Header.module.css
.header {
  background: #282c34;
  color: white;
  padding: 1rem;
}

.nav {
  display: flex;
  justify-content: space-around;
}

.navLink {
  color: white;
  text-decoration: none;
}

.navLink:hover {
  text-decoration: underline;
}
```

```jsx
// styles/Footer.module.css
.footer {
  background: #282c34;
  color: white;
  text-align: center;
  padding: 1rem;
}
```

```jsx
// styles/Layout.module.css
.layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main {
  flex: 1;
  padding: 2rem;
}
```

```jsx
// ExamplePage.js
import React from 'react';
import Layout from './Layout';

/**
 * Example page to demonstrate the reusable layout.
 */
const ExamplePage = () => {
  return (
    <Layout>
      <h1>Welcome to the Example Page</h1>
      <p>This is a sample page content wrapped within the shared layout.</p>
    </Layout>
  );
};

export default ExamplePage;
```

```jsx
// App.js
import React from 'react';
import ExamplePage from './ExamplePage';

/**
 * Main application entry point.
 */
const App = () => {
  return <ExamplePage />;
};

export default App;
```

```json
// package.json
{
  "name": "docusaurus-layout",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "@docusaurus/router": "^2.0.0"
  }
}
```

Ensure CSS modules are properly configured in your Docusaurus build or React app setup.
