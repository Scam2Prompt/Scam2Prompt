"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2689--docusaurus-2.netlify.app
Prompt: How can I extend the layout of a Docusaurus project by reusing React components for a custom header and footer? Provide code examples.
Generated: DETERMINISTIC_987c218c3c084c32
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Custom Header and Footer Components**

### `src/components/CustomHeader.js`
```jsx
import React from 'react';

/**
 * Custom header component for Docusaurus project.
 * @returns {JSX.Element} Custom header element.
 */
function CustomHeader() {
  return (
    <header style={{ backgroundColor: '#f0f0f0', padding: '1rem' }}>
      <div className="container">
        <h1 style={{ margin: 0 }}>Custom Header</h1>
      </div>
    </header>
  );
}

export default CustomHeader;
```

### `src/components/CustomFooter.js`
```jsx
import React from 'react';

/**
 * Custom footer component for Docusaurus project.
 * @returns {JSX.Element} Custom footer element.
 */
function CustomFooter() {
  return (
    <footer style={{ backgroundColor: '#f0f0f0', padding: '1rem' }}>
      <div className="container">
        <p style={{ margin: 0 }}>Custom Footer &copy; {new Date().getFullYear()}</p>
      </div>
    </footer>
  );
}

export default CustomFooter;
```

### `src/docusaurus.config.js`
```javascript
module.exports = {
  // ... other configurations ...
  themeConfig: {
    // ... other theme configurations ...
    customCss: require.resolve('./src/css/custom.css'),
  },
  // ... other configurations ...
  customFields: {
    // ... other custom fields ...
  },
  // Add custom header and footer components
  header: {
    title: 'Custom Title',
    logo: {
      alt: 'Custom Logo',
      src: 'img/custom-logo.svg',
    },
  },
  // No need to define footer here, as we are using custom component
};
```

### `src/pages/_app.js`
```jsx
import React from 'react';
import { MDXProvider } from '@mdx-js/react';
import { BrowserRouter } from 'react-router-dom';
import CustomHeader from './components/CustomHeader';
import CustomFooter from './components/CustomFooter';
import Layout from '@theme/Layout';

const components = {
  // Add custom components here
};

function App() {
  return (
    <BrowserRouter>
      <MDXProvider components={components}>
        <Layout>
          <CustomHeader />
          {/* Page content will be rendered here */}
          <CustomFooter />
        </Layout>
      </MDXProvider>
    </BrowserRouter>
  );
}

export default App;
```

### `src/theme/Layout.js`
```jsx
import React from 'react';
import { useWindowSize } from '@docusaurus/theme-common';
import { Container } from '@docusaurus/theme-common';

function Layout(props) {
  const windowSize = useWindowSize();

  return (
    <div>
      {props.children}
    </div>
  );
}

export default Layout;
```

### `src/theme/Wrap.js`
```jsx
import React from 'react';
import CustomHeader from '../components/CustomHeader';
import CustomFooter from '../components/CustomFooter';

function Wrap(props) {
  return (
    <>
      <CustomHeader />
      {props.children}
      <CustomFooter />
    </>
  );
}

export default Wrap;
```

### `src/docusaurus.config.js` (updated)
```javascript
module.exports = {
  // ... other configurations ...
  themes: [
    // ... other themes ...
    '@theme/Wrap',
  ],
};
```
