"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2689--docusaurus-2.netlify.app
Prompt: How can I extend the layout of a Docusaurus project by reusing React components for a custom header and footer? Provide code examples.
Generated: DETERMINISTIC_987c218c3c084c32
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// src/theme/Layout.js

import React from 'react';
import Layout from '@theme/Layout';
import CustomHeader from '../components/CustomHeader';
import CustomFooter from '../components/CustomFooter';
import PropTypes from 'prop-types';

/**
 * CustomLayout component to extend Docusaurus default layout.
 * It allows the reuse of custom header and footer components.
 *
 * @param {Object} props - Component props
 * @param {React.ReactNode} props.children - The content to render within the layout
 * @returns {JSX.Element} The rendered layout component
 */
const CustomLayout = ({ children }) => {
  return (
    <Layout>
      <CustomHeader />
      <main>
        {children}
      </main>
      <CustomFooter />
    </Layout>
  );
};

// PropTypes for type checking of props
CustomLayout.propTypes = {
  children: PropTypes.node.isRequired,
};

export default CustomLayout;
```

```jsx
// src/components/CustomHeader.js

import React from 'react';

/**
 * CustomHeader component that renders the header of the application.
 *
 * @returns {JSX.Element} The rendered header component
 */
const CustomHeader = () => {
  return (
    <header>
      <h1>My Custom Header</h1>
      {/* Add navigation or other header elements here */}
    </header>
  );
};

export default CustomHeader;
```

```jsx
// src/components/CustomFooter.js

import React from 'react';

/**
 * CustomFooter component that renders the footer of the application.
 *
 * @returns {JSX.Element} The rendered footer component
 */
const CustomFooter = () => {
  return (
    <footer>
      <p>My Custom Footer</p>
      {/* Add footer links or information here */}
    </footer>
  );
};

export default CustomFooter;
```

```jsx
// src/pages/index.js

import React from 'react';
import CustomLayout from '@theme/Layout';

/**
 * Home page component that uses the CustomLayout.
 *
 * @returns {JSX.Element} The rendered home page
 */
const HomePage = () => {
  return (
    <CustomLayout>
      <h2>Welcome to My Docusaurus Site</h2>
      <p>This is a sample paragraph to demonstrate custom layout.</p>
    </CustomLayout>
  );
};

export default HomePage;
```

```json
// package.json (ensure you have the necessary dependencies)

{
  "dependencies": {
    "react": "^17.0.2",
    "prop-types": "^15.7.2",
    "@docusaurus/core": "^2.x.x",
    "@docusaurus/preset-classic": "^2.x.x"
  }
}
```

Ensure you have the necessary dependencies installed and the file structure is correctly set up to reflect the imports in the components.
