"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: Create a React-based custom layout for a Docusaurus website, reusing the default header and footer components.
Generated: DETERMINISTIC_c9abf12e5d077349
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// src/layouts/CustomLayout.js

import React from 'react';
import PropTypes from 'prop-types';
import { Header, Footer } from '@docusaurus/theme-classic';
import './CustomLayout.css'; // Importing custom styles for the layout

/**
 * CustomLayout component to create a reusable layout for Docusaurus pages.
 *
 * @param {object} props - React props containing children and other optional parameters.
 * @param {React.ReactNode} props.children - The child components to be rendered within the layout.
 * @param {string} [props.className] - Optional additional class names for styling.
 * @returns {JSX.Element} The rendered CustomLayout component.
 */
const CustomLayout = ({ children, className }) => {
  return (
    <div className={`custom-layout ${className}`}>
      <Header />
      <main className="custom-layout__main">{children}</main>
      <Footer />
    </div>
  );
};

// Prop validation to ensure correct data types for props
CustomLayout.propTypes = {
  children: PropTypes.node.isRequired,
  className: PropTypes.string,
};

// Default props for the component
CustomLayout.defaultProps = {
  className: '',
};

export default CustomLayout;
```

```javascript
// src/pages/index.js

import React from 'react';
import CustomLayout from '../layouts/CustomLayout';

const HomePage = () => {
  return (
    <CustomLayout>
      <h1>Welcome to My Docusaurus Site</h1>
      <p>This is the homepage of my custom layout example.</p>
    </CustomLayout>
  );
};

export default HomePage;
```

```css
/* src/layouts/CustomLayout.css */

.custom-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* Ensures the layout covers the full height of the viewport */
}

.custom-layout__main {
  flex: 1; /* Allows the main section to grow and occupy remaining space */
  padding: 20px; /* Adds padding around the main content */
  background-color: #f9f9f9; /* Light background for contrast */
}
```

```javascript
// docusaurus.config.js

module.exports = {
  // Other Docusaurus configuration settings...
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // Configuration for docs
        },
        blog: {
          // Configuration for blog
        },
        theme: {
          customCss: require.resolve('./src/layouts/CustomLayout.css'),
        },
      },
    ],
  ],
};
```
