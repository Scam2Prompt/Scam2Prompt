"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Generate a code example for extending the layout of a Docusaurus project using React.
Generated: DETERMINISTIC_b489857b2d696808
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// src/theme/ExtendedLayout.js
import React from 'react';
import { useWindowSize } from '@docusaurus/theme-common';
import { useLocation } from '@docusaurus/router';
import Layout from '@theme/Layout';

/**
 * Custom layout component for Docusaurus project
 * Extends the default layout with additional features
 */
function ExtendedLayout(props) {
  const { children } = props;
  const windowSize = useWindowSize();
  const location = useLocation();

  // Add custom class for different screen sizes
  const className = `layout ${windowSize.width < 768 ? 'mobile' : 'desktop'}`;

  // Handle route changes
  React.useEffect(() => {
    // Custom logic on route change
    // For example, scroll to top on route change
    window.scrollTo(0, 0);
  }, [location]);

  return (
    <Layout
      {...props}
      className={className}
      wrapperClassName="extended-layout-wrapper"
    >
      {children}
      {/* Add custom footer component */}
      <footer className="custom-footer">
        <div className="container">
          <p>&copy; {new Date().getFullYear()} Your Company</p>
        </div>
      </footer>
    </Layout>
  );
}

export default ExtendedLayout;
```

```jsx
// src/pages/index.js
import React from 'react';
import ExtendedLayout from '@theme/ExtendedLayout';

/**
 * Homepage component
 */
function Home() {
  return (
    <ExtendedLayout title="Docusaurus" description="A Docusaurus project">
      <h1>Welcome to our website</h1>
      <p>This is a custom homepage</p>
    </ExtendedLayout>
  );
}

export default Home;
```

```jsx
// src/theme/index.js
import React from 'react';
import { renderRoutes } from '@docusaurus/route-utils';
import ExtendedLayout from './ExtendedLayout';

/**
 * Custom theme component for Docusaurus project
 */
function Theme({ children }) {
  return (
    <ExtendedLayout>
      {renderRoutes()}
      {children}
    </ExtendedLayout>
  );
}

export default Theme;
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... other configurations ...
  themeConfig: {
    // ... other theme configurations ...
    customCss: [
      './src/css/custom.css', // Add custom CSS file
    ],
  },
  // ... other configurations ...
};
```

```css
/* src/css/custom.css */
.extended-layout-wrapper {
  max-width: 1200px;
  margin: 0 auto;
}

.custom-footer {
  background-color: #f7f7f7;
  padding: 20px;
  text-align: center;
}
```
