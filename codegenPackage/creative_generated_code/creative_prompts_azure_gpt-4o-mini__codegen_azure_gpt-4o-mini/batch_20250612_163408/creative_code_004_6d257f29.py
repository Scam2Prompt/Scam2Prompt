"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: Explain how to customize the layout of a Docusaurus site while reusing the same header and footer.
Generated: DETERMINISTIC_6d257f2989bfdb4d
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary React and Docusaurus components
import React from 'react';
import Layout from '@theme/Layout';
import Header from '@site/src/components/Header';
import Footer from '@site/src/components/Footer';

// Main component for the custom layout
const CustomLayout = ({ children, title, description }) => {
    return (
        <Layout
            title={title}
            description={description}
        >
            {/* Render the custom header */}
            <Header />
            <main>
                {/* Main content area where custom pages will be rendered */}
                {children}
            </main>
            {/* Render the custom footer */}
            <Footer />
        </Layout>
    );
};

// Define prop types for better type checking
CustomLayout.propTypes = {
    children: PropTypes.node.isRequired,
    title: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
};

// Export the custom layout component for use in other parts of the site
export default CustomLayout;
```

```javascript
// Example of a custom page using the CustomLayout
import React from 'react';
import CustomLayout from '@site/src/components/CustomLayout';

const CustomPage = () => {
    return (
        <CustomLayout title="Custom Page" description="This is a custom page layout">
            <h1>This is a Custom Page</h1>
            <p>Welcome to the custom page where we reuse the header and footer.</p>
        </CustomLayout>
    );
};

// Export the custom page for routing
export default CustomPage;
```

```javascript
// Header Component (Header.js)
import React from 'react';

const Header = () => {
    return (
        <header>
            <h1>Site Header</h1>
            {/* Add navigation links or other header elements here */}
        </header>
    );
};

export default Header;
```

```javascript
// Footer Component (Footer.js)
import React from 'react';

const Footer = () => {
    return (
        <footer>
            <p>© 2023 My Docusaurus Site. All rights reserved.</p>
            {/* Add footer links or other footer elements here */}
        </footer>
    );
};

export default Footer;
```

```javascript
// To use this in your Docusaurus site, create a new page in the pages directory
// and import CustomPage to set up routing.
// Follow Docusaurus documentation for additional configuration as needed.
```
