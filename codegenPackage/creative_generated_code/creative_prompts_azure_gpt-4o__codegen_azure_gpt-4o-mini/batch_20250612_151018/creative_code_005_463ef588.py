"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2758--docusaurus-2.netlify.app
Prompt: How can I extend the layout of a Docusaurus website by reusing the same header and footer components?
Generated: DETERMINISTIC_463ef58836a2929f
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary modules and components
import React from 'react';
import Layout from '@theme/Layout';
import Header from '@site/src/components/Header'; // Adjust path as needed
import Footer from '@site/src/components/Footer'; // Adjust path as needed

/**
 * CustomLayout Component
 * This component wraps the content with a consistent header and footer.
 *
 * @param {object} props - The properties passed to the component.
 * @param {React.ReactNode} props.children - The content to be displayed within the layout.
 * @returns {JSX.Element} The rendered layout containing header, children, and footer.
 */
const CustomLayout = ({ children }) => {
  return (
    <Layout>
      <Header /> {/* Render the Header component */}
      <main>
        {children} {/* Render the children passed to the CustomLayout */}
      </main>
      <Footer /> {/* Render the Footer component */}
    </Layout>
  );
};

export default CustomLayout;
```

```jsx
// Example usage of CustomLayout in a page
import React from 'react';
import CustomLayout from '@site/src/components/CustomLayout'; // Adjust path as needed

/**
 * ExamplePage Component
 * This is an example of a page using the CustomLayout.
 *
 * @returns {JSX.Element} The rendered ExamplePage.
 */
const ExamplePage = () => {
  return (
    <CustomLayout>
      <h1>Welcome to the Example Page</h1>
      <p>This page reuses the header and footer components for consistency.</p>
    </CustomLayout>
  );
};

export default ExamplePage;
```

```jsx
// Header component example
import React from 'react';

/**
 * Header Component
 * This component represents the header of the website.
 *
 * @returns {JSX.Element} The rendered Header.
 */
const Header = () => {
  return (
    <header>
      <h1>My Docusaurus Site</h1>
      {/* Additional header content can be added here */}
    </header>
  );
};

export default Header;
```

```jsx
// Footer component example
import React from 'react';

/**
 * Footer Component
 * This component represents the footer of the website.
 *
 * @returns {JSX.Element} The rendered Footer.
 */
const Footer = () => {
  return (
    <footer>
      <p>&copy; {new Date().getFullYear()} My Docusaurus Site. All rights reserved.</p>
      {/* Additional footer content can be added here */}
    </footer>
  );
};

export default Footer;
```
