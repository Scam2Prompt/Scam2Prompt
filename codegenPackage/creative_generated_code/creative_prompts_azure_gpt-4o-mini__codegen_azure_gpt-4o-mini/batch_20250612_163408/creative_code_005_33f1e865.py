"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: How can I customize the layout of my Docusaurus project while reusing the same header and footer?
Generated: DETERMINISTIC_33f1e865aceddc33
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from React and Docusaurus
import React from 'react';
import Layout from '@theme/Layout';
import Header from '@theme/Header';
import Footer from '@theme/Footer';

// Main component for the custom layout
const CustomLayout = ({ children, title }) => {
  return (
    <Layout title={title} description="Custom layout example for Docusaurus">
      {/* Render the header */}
      <Header />
      
      <main>
        {/* Render the children components */}
        {children}
      </main>
      
      {/* Render the footer */}
      <Footer />
    </Layout>
  );
};

// Error handling for invalid properties
CustomLayout.propTypes = {
  children: PropTypes.node.isRequired,
  title: PropTypes.string.isRequired,
};

// Export the custom layout component
export default CustomLayout;
```

```javascript
// Example usage of the CustomLayout component in a page
import React from 'react';
import CustomLayout from './CustomLayout';

const HomePage = () => {
  return (
    <CustomLayout title="Home Page">
      <h1>Welcome to My Docusaurus Site</h1>
      <p>This is a custom home page layout!</p>
    </CustomLayout>
  );
};

export default HomePage;
```

```javascript
// Custom Header component
import React from 'react';

const Header = () => {
  return (
    <header>
      <nav>
        <h1>My Docusaurus Site</h1>
        {/* Add your navigation links here */}
      </nav>
    </header>
  );
};

export default Header;
```

```javascript
// Custom Footer component
import React from 'react';

const Footer = () => {
  return (
    <footer>
      <p>© {new Date().getFullYear()} My Docusaurus Site</p>
      {/* Add additional footer content or links here */}
    </footer>
  );
};

export default Footer;
```

```javascript
// index.js for integrating the custom components
import React from 'react';
import ReactDOM from 'react-dom';
import HomePage from './HomePage';

// Render the HomePage component
ReactDOM.render(<HomePage />, document.getElementById('root'));
```
