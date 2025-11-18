"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2728--docusaurus-2.netlify.app
Prompt: Create a React component to customize the layout of a Docusaurus site while reusing the default header and footer.
Generated: DETERMINISTIC_3f1f423747ea398e
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
import Layout from '@theme/Layout'; // Default Docusaurus Layout
import useDocusaurusContext from '@docusaurus/useDocusaurusContext'; // Access Docusaurus site config

// Custom component for the layout
const CustomLayout = ({ children }) => {
  // Use Docusaurus context to fetch site data
  const { siteConfig } = useDocusaurusContext();

  return (
    // Wrapping custom layout around the default Layout
    <Layout
      title={`Custom Layout | ${siteConfig.title}`} // Dynamic title
      description="This is a custom layout for the Docusaurus site." // Meta description for SEO
    >
      {/* Main content of the page */}
      <div style={{ padding: '20px', backgroundColor: '#f5f5f5' }}>
        {/* Custom header section */}
        <div style={{ textAlign: 'center', padding: '10px', backgroundColor: '#0078d4', color: 'white' }}>
          <h1>Welcome to My Custom Layout</h1>
          <p>Enhancing the Docusaurus experience!</p>
        </div>

        {/* Render children components (page content) */}
        <div style={{ marginTop: '20px', padding: '20px', backgroundColor: 'white', borderRadius: '5px' }}>
          {children}
        </div>

        {/* Custom footer section */}
        <footer style={{ marginTop: '50px', textAlign: 'center', padding: '10px', backgroundColor: '#0078d4', color: 'white' }}>
          <p>© {new Date().getFullYear()} {siteConfig.title}. All rights reserved.</p>
        </footer>
      </div>
    </Layout>
  );
};

// Export the component for use in Docusaurus pages
export default CustomLayout;
```
