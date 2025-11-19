"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2803--docusaurus-2.netlify.app
Prompt: Can you provide a code example of how to extend a Docusaurus project layout using React components?
Generated: DETERMINISTIC_1a974c51277b9b4d
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/myrepo": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```jsx
// File: src/components/CustomFooter.js
// This file defines a custom footer component to be used in a Docusaurus project layout.

import React from 'react';
import Link from '@docusaurus/Link';
import styles from './CustomFooter.module.css'; // Custom CSS module for styling

// Functional component for the custom footer
const CustomFooter = () => {
  return (
    <footer className={styles.footer}>
      <div className={styles.container}>
        <p className={styles.text}>
          © {new Date().getFullYear()} My Docusaurus Site. All rights reserved.
        </p>
        <nav className={styles.links}>
          <Link to="/privacy-policy" className={styles.link}>
            Privacy Policy
          </Link>
          <Link to="/terms-of-service" className={styles.link}>
            Terms of Service
          </Link>
          <Link to="https://github.com/myrepo" className={styles.link}>
            GitHub
          </Link>
        </nav>
      </div>
    </footer>
  );
};

export default CustomFooter;

// File: src/theme/Layout.js
// This file overrides the default layout in a Docusaurus project to include the custom footer.

import React from 'react';
import DefaultLayout from '@theme-original/Layout';
import CustomFooter from '../components/CustomFooter';

// Higher-order component to extend the default layout
export default function Layout(props) {
  return (
    <>
      <DefaultLayout {...props} />
      {/* Custom footer added below the default layout */}
      <CustomFooter />
    </>
  );
}

// File: src/components/CustomFooter.module.css
// CSS file to style the custom footer.

.footer {
  background-color: #282c34; /* Dark background color */
  color: white; /* White text color */
  padding: 1rem; /* Padding around the footer */
  text-align: center; /* Center align text and links */
}

.container {
  max-width: 1200px; /* Limit the width of the content */
  margin: 0 auto; /* Center the content horizontally */
}

.text {
  margin-bottom: 0.5rem; /* Spacing below the text */
}

.links {
  display: flex; /* Arrange links horizontally */
  justify-content: center; /* Center the links */
  gap: 1rem; /* Space between links */
}

.link {
  color: #61dafb; /* Light blue link color */
  text-decoration: none; /* Remove underline from links */
}

.link:hover {
  text-decoration: underline; /* Add underline on hover */
}
```
