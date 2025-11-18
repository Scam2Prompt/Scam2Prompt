"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2820--docusaurus-2.netlify.app
Prompt: Write a React component for customizing the layout of a Docusaurus site, reusing the default header and footer.
Generated: DETERMINISTIC_68b8a3538928fa22
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React from 'react';
import { Layout } from '@docusaurus/theme-classic';
import Header from '@theme/Header';
import Footer from '@theme/Footer';

// CustomLayout component for Docusaurus site layout customization
const CustomLayout = ({ children }) => {
  // Check if children are provided
  if (!children) {
    console.error('CustomLayout requires children to render.');
    return null;
  }

  return (
    <Layout>
      {/* Render the default header */}
      <Header />

      <main>
        {/* Render the main content passed as children */}
        {children}
      </main>

      {/* Render the default footer */}
      <Footer />
    </Layout>
  );
};

export default CustomLayout;
```
