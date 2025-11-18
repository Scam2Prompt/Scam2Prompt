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

```javascript
// Import the necessary modules from Docusaurus
import React from 'react';
import Layout from '@theme/Layout';

// Define a custom page layout component that reuses the header and footer provided by Docusaurus
const CustomPage = () => {
  return (
    <Layout>
      {/* Main content of the custom page */}
      <main style={{ padding: '2rem', textAlign: 'center' }}>
        <h1>Welcome to My Custom Page</h1>
        <p>This page reuses the header and footer components from Docusaurus.</p>
      </main>
    </Layout>
  );
};

export default CustomPage;
```

Notes:
- You can save this file as `src/pages/custom-page.js`. The `src/pages` directory in Docusaurus automatically creates routes based on file names.
- This code leverages Docusaurus's `Layout` component, which includes the header and footer by default.
- Ensure that you have Docusaurus set up correctly before using this code.
