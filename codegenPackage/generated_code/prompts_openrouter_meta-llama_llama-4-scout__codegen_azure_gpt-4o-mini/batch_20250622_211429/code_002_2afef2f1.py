"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2619--docusaurus-2.netlify.app
Prompt: Generate a code example for extending the layout of a Docusaurus project using React, while reusing the same header and footer.
Generated: DETERMINISTIC_2afef2f1a41b109e
Batch ID: 20250622_211429
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
import Header from '../components/Header'; // Importing the Header component
import Footer from '../components/Footer'; // Importing the Footer component

/**
 * CustomLayout component that wraps around the main content of the page.
 * It includes a reusable Header and Footer.
 *
 * @param {Object} props - The props for the component.
 * @param {React.ReactNode} props.children - The content to be displayed within the layout.
 * @returns {JSX.Element} The rendered layout component.
 */
const CustomLayout = ({ children }) => {
  return (
    <div className="custom-layout">
      <Header /> {/* Render the Header component */}
      <main>{children}</main> {/* Render the main content */}
      <Footer /> {/* Render the Footer component */}
    </div>
  );
};

// PropTypes for type checking
CustomLayout.propTypes = {
  children: PropTypes.node.isRequired, // children must be a valid React node
};

export default CustomLayout;
```

```javascript
// src/pages/ExamplePage.js

import React from 'react';
import CustomLayout from '../layouts/CustomLayout';

/**
 * ExamplePage component that demonstrates the use of CustomLayout.
 *
 * @returns {JSX.Element} The rendered ExamplePage component.
 */
const ExamplePage = () => {
  return (
    <CustomLayout>
      <h1>Welcome to the Example Page</h1>
      <p>This page uses a custom layout with a shared header and footer.</p>
    </CustomLayout>
  );
};

export default ExamplePage;
```

```javascript
// src/components/Header.js

import React from 'react';

/**
 * Header component that displays the site header.
 *
 * @returns {JSX.Element} The rendered Header component.
 */
const Header = () => {
  return (
    <header>
      <h1>My Docusaurus Site</h1>
      {/* Add navigation links here */}
    </header>
  );
};

export default Header;
```

```javascript
// src/components/Footer.js

import React from 'react';

/**
 * Footer component that displays the site footer.
 *
 * @returns {JSX.Element} The rendered Footer component.
 */
const Footer = () => {
  return (
    <footer>
      <p>&copy; {new Date().getFullYear()} My Docusaurus Site. All rights reserved.</p>
    </footer>
  );
};

export default Footer;
```

```javascript
// src/pages/index.js

import React from 'react';
import CustomLayout from '../layouts/CustomLayout';

/**
 * HomePage component that serves as the landing page of the site.
 *
 * @returns {JSX.Element} The rendered HomePage component.
 */
const HomePage = () => {
  return (
    <CustomLayout>
      <h1>Welcome to My Docusaurus Site</h1>
      <p>This is the home page.</p>
    </CustomLayout>
  );
};

export default HomePage;
```

```javascript
// src/styles/custom.css

.custom-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* Ensures the layout takes full height */
}

header, footer {
  background-color: #f8f9fa; /* Light background for header and footer */
  padding: 1rem;
  text-align: center;
}
```
