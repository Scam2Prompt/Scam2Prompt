"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2819--docusaurus-2.netlify.app
Prompt: Generate a Docusaurus theme extension that customizes the header and footer while reusing React components.
Generated: DETERMINISTIC_1716240e12861603
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/theme/Footer.js
import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';
import OriginalFooter from '@theme-original/Footer';

function CustomFooter(props) {
  return (
    <div className={clsx(styles.footer, 'footer')}>
      <div className="container">
        <div className="row">
          <div className="col col--6">
            <div className={styles.footer__copyright}>
              © {new Date().getFullYear()} My Custom Footer
            </div>
          </div>
          <div className="col col--6">
            <div className={styles.footer__links}>
              <a href="/privacy">Privacy Policy</a>
              <a href="/terms">Terms of Service</a>
            </div>
          </div>
        </div>
      </div>
      <OriginalFooter {...props} />
    </div>
  );
}

export default CustomFooter;
```

```javascript
// src/theme/Navbar.js
import React from 'react';
import OriginalNavbar from '@theme-original/Navbar';
import styles from './styles.module.css';

function CustomNavbar(props) {
  return (
    <div className={styles.navbarWrapper}>
      <div className={styles.navbarBanner}>
        Welcome to our documentation!
      </div>
      <OriginalNavbar {...props} />
    </div>
  );
}

export default CustomNavbar;
```

```javascript
// src/theme/index.js
import Navbar from './Navbar';
import Footer from './Footer';

export default {
  navbar: Navbar,
  footer: Footer,
};
```

```css
/* src/theme/styles.module.css */
.navbarWrapper {
  background-color: var(--ifm-navbar-background-color);
}

.navbarBanner {
  background-color: #2b3137;
  color: white;
  text-align: center;
  padding: 0.5rem;
  font-size: 0.9rem;
}

.footer {
  background-color: var(--ifm-footer-background-color);
  padding: 2rem 0;
}

.footer__copyright {
  text-align: left;
}

.footer__links {
  text-align: right;
}

.footer__links a {
  margin-left: 1rem;
  color: var(--ifm-footer-link-color);
}

.footer__links a:hover {
  color: var(--ifm-footer-link-hover-color);
  text-decoration: none;
}
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... existing config
  themeConfig: {
    navbar: {
      // Your existing navbar config
    },
    footer: {
      // Your existing footer config
    },
  },
  themes: [
    // ... other themes
    [
      '@docusaurus/theme-classic',
      {
        customCss: require.resolve('./src/theme/styles.module.css'),
      },
    ],
  ],
};
```
