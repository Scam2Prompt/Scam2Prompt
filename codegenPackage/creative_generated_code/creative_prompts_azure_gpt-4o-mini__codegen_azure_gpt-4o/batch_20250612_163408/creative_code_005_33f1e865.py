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
// Docusaurus allows customization of the layout by overriding the default `Layout` component.
// Below is an example of how you can create a custom layout while reusing the default header and footer.

// Import necessary components and hooks
import React from 'react';
import Layout from '@theme/Layout'; // Default layout provided by Docusaurus
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

// CustomLayout Component
const CustomLayout = ({ children }) => {
  // Fetch site configuration (e.g., title, metadata) using Docusaurus context
  const { siteConfig } = useDocusaurusContext();

  return (
    // Reuse the default Layout component
    <Layout
      title={siteConfig.title} // Set title dynamically from site config
      description={siteConfig.tagline} // Set description dynamically from site config
    >
      {/* Custom content can be added below */}
      <div style={{ padding: '20px', backgroundColor: '#f3f4f6' }}>
        {/* Header is part of the Layout, so it automatically gets reused */}
        <main>{children}</main> {/* Dynamically render page content */}
        {/* Footer is part of the Layout, so it automatically gets reused */}
      </div>
    </Layout>
  );
};

export default CustomLayout;

// Usage:
// In the `src/pages` or a specific route, you can use `CustomLayout` to wrap your content.
// Example:
// import CustomLayout from '../path/to/CustomLayout';
//
// const MyPage = () => {
//   return (
//     <CustomLayout>
//       <h1>Welcome to My Custom Page</h1>
//       <p>This is a custom layout with the default header and footer.</p>
//     </CustomLayout>
//   );
// };
//
// export default MyPage;

// This component can now be reused across your Docusaurus project to create pages with custom layouts
// while preserving the default header and footer functionality.
```
