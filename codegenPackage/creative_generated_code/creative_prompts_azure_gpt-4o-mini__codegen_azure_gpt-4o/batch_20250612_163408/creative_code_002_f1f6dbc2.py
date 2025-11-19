"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Explain how to extend a Docusaurus layout using React components while maintaining a consistent header and footer.
Generated: DETERMINISTIC_f1f6dbc21a660e62
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and components from Docusaurus
import React from 'react';
import Layout from '@theme/Layout'; // Base layout provided by Docusaurus
import useDocusaurusContext from '@docusaurus/useDocusaurusContext'; // Access site context

// Example of extending the Docusaurus layout
const CustomPage = () => {
  // Get site metadata from Docusaurus context
  const { siteConfig } = useDocusaurusContext();

  return (
    // Use the Layout component to maintain consistent header and footer
    <Layout
      title="Custom Page Title" // Title for the page
      description="This is a custom page built using Docusaurus Layout!" // Meta description
    >
      {/* Main content of the custom page */}
      <main
        style={{
          padding: '2rem',
          textAlign: 'center',
        }}
      >
        {/* Display site title dynamically */}
        <h1>Welcome to {siteConfig.title}</h1>

        {/* Add custom content below */}
        <p>This is an example of extending the Docusaurus layout.</p>
        <button
          onClick={() => alert('Hello, Docusaurus!')}
          style={{
            padding: '1rem 2rem',
            backgroundColor: '#3578E5',
            color: '#fff',
            border: 'none',
            borderRadius: '5px',
            cursor: 'pointer',
          }}
        >
          Click Me
        </button>
      </main>
    </Layout>
  );
};

export default CustomPage; // Export the component for use
```
