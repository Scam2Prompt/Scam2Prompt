"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2794--docusaurus-2.netlify.app
Prompt: How can I extend the layout of a Docusaurus website by reusing React components for a custom header and footer? Provide example code.
Generated: DETERMINISTIC_9eacb5887d6af886
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and components
import React from 'react';
import Layout from '@theme/Layout';
import Header from './Header'; // Custom Header component
import Footer from './Footer'; // Custom Footer component

// Main layout component that extends Docusaurus Layout
const CustomLayout = ({ children, title, description, wrapperClassName }) => {
    return (
        <Layout title={title} description={description}>
            {/* Render custom header */}
            <Header />
            <main className={wrapperClassName}>{children}</main>
            {/* Render custom footer */}
            <Footer />
        </Layout>
    );
};

// Prop types for validation
CustomLayout.propTypes = {
    children: PropTypes.node.isRequired,
    title: PropTypes.string.isRequired,
    description: PropTypes.string,
    wrapperClassName: PropTypes.string,
};

// Default props
CustomLayout.defaultProps = {
    description: 'Default description for the page',
    wrapperClassName: '',
};

export default CustomLayout;
```

```javascript
// Header.js
import React from 'react';

// Custom Header component
const Header = () => {
    return (
        <header>
            <h1>My Custom Header</h1>
            {/* Add navigation links or other elements */}
        </header>
    );
};

export default Header;
```

```javascript
// Footer.js
import React from 'react';

// Custom Footer component
const Footer = () => {
    return (
        <footer>
            <p>© {new Date().getFullYear()} My Website. All rights reserved.</p>
            {/* Add social media links or other elements */}
        </footer>
    );
};

export default Footer;
```

```javascript
// Example usage in a page component
import React from 'react';
import CustomLayout from '../components/CustomLayout';

const MyPage = () => {
    return (
        <CustomLayout title="My Page Title" description="This is my page description">
            <h2>Welcome to My Page</h2>
            <p>This is the content of my page.</p>
        </CustomLayout>
    );
};

export default MyPage;
```
