"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2794--docusaurus-2.netlify.app
Prompt: How can I extend the layout of a Docusaurus website by reusing React components for a custom header and footer? Provide example code.
Generated: DETERMINISTIC_9eacb5887d6af886
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Docusaurus Custom Header and Footer Example**
====================================================

### `src/components/CustomHeader.js`
```jsx
// CustomHeader.js
import React from 'react';

/**
 * Custom header component.
 * @returns {JSX.Element} Custom header element.
 */
function CustomHeader() {
  return (
    <header style={{ backgroundColor: '#f0f0f0', padding: '1rem' }}>
      <div className="container">
        <h1>Custom Header</h1>
      </div>
    </header>
  );
}

export default CustomHeader;
```

### `src/components/CustomFooter.js`
```jsx
// CustomFooter.js
import React from 'react';

/**
 * Custom footer component.
 * @returns {JSX.Element} Custom footer element.
 */
function CustomFooter() {
  return (
    <footer style={{ backgroundColor: '#f0f0f0', padding: '1rem' }}>
      <div className="container">
        <p>&copy; {new Date().getFullYear()} Custom Footer</p>
      </div>
    </footer>
  );
}

export default CustomFooter;
```

### `src/pages/index.js`
```jsx
// index.js (optional, for testing)
import React from 'react';
import CustomHeader from '../components/CustomHeader';
import CustomFooter from '../components/CustomFooter';

function Home() {
  return (
    <div>
      <CustomHeader />
      <main style={{ padding: '2rem' }}>
        <h1>Welcome to my Docusaurus site!</h1>
      </main>
      <CustomFooter />
    </div>
  );
}

export default Home;
```

### `docusaurus.config.js`
```javascript
// docusaurus.config.js
module.exports = {
  // ... other configurations ...
  themeConfig: {
    // ... other theme configurations ...
    customCss: [require.resolve('./src/css/custom.css')],
  },
  // ... other configurations ...
  customFields: {
    // ... other custom fields ...
  },
  // Add custom header and footer to layout
  layout: {
    template: 'custom',
  },
};
```

### `src/theme/Layout.js`
```jsx
// src/theme/Layout.js (override default layout)
import React from 'react';
import CustomHeader from '../components/CustomHeader';
import CustomFooter from '../components/CustomFooter';
import { useLocation } from '@docusaurus/router';

export default function Layout({ children }) {
  const location = useLocation();

  return (
    <div>
      <CustomHeader />
      {children}
      <CustomFooter />
    </div>
  );
}
```

### `src/theme/custom.css`
```css
/* custom.css (optional, for styling) */
body {
  font-family: Arial, sans-serif;
}

.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 1rem;
}
```
