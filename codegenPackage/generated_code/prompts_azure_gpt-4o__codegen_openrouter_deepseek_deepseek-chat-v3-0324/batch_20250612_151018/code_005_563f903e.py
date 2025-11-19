"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: How can I extend the layout of a Docusaurus website using React components while reusing the header and footer? Write the code for a custom layout.
Generated: DETERMINISTIC_563f903e72069cbf
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React from 'react';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

/**
 * CustomLayout component that extends the default Docusaurus layout
 * while reusing the header and footer.
 * 
 * @param {Object} props - Component props
 * @param {string} props.title - Page title
 * @param {string} props.description - Page description
 * @param {React.ReactNode} props.children - Child components
 * @returns {JSX.Element} Custom layout component
 */
function CustomLayout({ title, description, children }) {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout
      title={title}
      description={description || siteConfig.tagline}
    >
      <Head>
        <meta property="og:title" content={title} />
        <meta property="og:description" content={description || siteConfig.tagline} />
      </Head>

      <main className="custom-layout">
        <div className="container">
          {children}
        </div>
      </main>
    </Layout>
  );
}

export default CustomLayout;
```

```jsx
// Example usage of CustomLayout in a page component
import React from 'react';
import CustomLayout from '../components/CustomLayout';

function ExamplePage() {
  return (
    <CustomLayout
      title="Example Page"
      description="This is an example page using the custom layout"
    >
      <div className="custom-content">
        <h1>Welcome to the Example Page</h1>
        <p>This content is wrapped in the custom layout.</p>
      </div>
    </CustomLayout>
  );
}

export default ExamplePage;
```

```css
/* Optional: Add custom styling for the layout */
.custom-layout {
  padding: 2rem 0;
}

.custom-layout .container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.custom-content {
  background: #fff;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```
