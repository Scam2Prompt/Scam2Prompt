"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Explain how to extend a Docusaurus layout using React components while maintaining a consistent header and footer.
Generated: DETERMINISTIC_f1f6dbc21a660e62
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready React component that extends a Docusaurus layout while maintaining consistent header and footer:

```jsx
import React from 'react';
import Layout from '@theme/Layout';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

/**
 * ExtendedLayout component that wraps custom content with Docusaurus layout
 * while maintaining consistent header and footer.
 * 
 * @param {Object} props - Component props
 * @param {React.ReactNode} props.children - The content to be rendered within the layout
 * @param {string} [props.title] - Page title (optional)
 * @param {string} [props.description] - Page description (optional)
 * @returns {JSX.Element} The extended layout component
 */
const ExtendedLayout = ({ children, title, description }) => {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout
      title={title || siteConfig.title}
      description={description || siteConfig.tagline}
    >
      <main className="container margin-vert--lg">
        {/* Custom content area that maintains header/footer */}
        <div className="extended-content">
          {children}
        </div>
      </main>
    </Layout>
  );
};

export default ExtendedLayout;
```

Example usage in a page component:

```jsx
import React from 'react';
import ExtendedLayout from '../components/ExtendedLayout';

/**
 * CustomPage component demonstrating ExtendedLayout usage
 */
const CustomPage = () => {
  return (
    <ExtendedLayout
      title="Custom Page"
      description="This is a custom page with extended layout"
    >
      <div className="custom-content">
        <h1>Welcome to My Custom Page</h1>
        <p>This content is wrapped with Docusaurus header and footer.</p>
      </div>
    </ExtendedLayout>
  );
};

export default CustomPage;
```
