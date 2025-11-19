"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2803--docusaurus-2.netlify.app
Prompt: Can you provide a code example of how to extend a Docusaurus project layout using React components?
Generated: DETERMINISTIC_1a974c51277b9b4d
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// File: src/components/CustomFooter.js

import React from 'react';
import Link from '@docusaurus/Link';
import styles from './CustomFooter.module.css'; // Custom CSS for styling

/**
 * CustomFooter Component
 * Extends the default Docusaurus layout by adding a custom footer.
 */
const CustomFooter = () => {
  return (
    <footer className={styles.footer}>
      <div className={styles.container}>
        <p>&copy; {new Date().getFullYear()} My Docusaurus Project. All rights reserved.</p>
        <nav>
          <Link to="/privacy-policy" className={styles.link}>
            Privacy Policy
          </Link>
          <Link to="/terms-of-service" className={styles.link}>
            Terms of Service
          </Link>
        </nav>
      </div>
    </footer>
  );
};

export default CustomFooter;
```

```jsx
// File: src/theme/Layout.js

import React from 'react';
import DefaultLayout from '@theme-original/Layout';
import CustomFooter from '../components/CustomFooter';

/**
 * Layout Component
 * Overrides the default Docusaurus layout to include a custom footer.
 */
export default function Layout(props) {
  return (
    <>
      {/* Render the default layout */}
      <DefaultLayout {...props} />
      
      {/* Add the custom footer */}
      <CustomFooter />
    </>
  );
}
```

```css
/* File: src/components/CustomFooter.module.css */

/* Styling for the custom footer */
.footer {
  background-color: #282c34;
  color: #ffffff;
  padding: 20px;
  text-align: center;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.link {
  color: #61dafb;
  margin: 0 10px;
  text-decoration: none;
}

.link:hover {
  text-decoration: underline;
}
```

```json
// File: docusaurus.config.js

// Ensure the custom layout is used by Docusaurus
module.exports = {
  // Other configurations...
  themes: [
    // Add the custom layout theme
    '@docusaurus/theme-classic',
  ],
};
```
