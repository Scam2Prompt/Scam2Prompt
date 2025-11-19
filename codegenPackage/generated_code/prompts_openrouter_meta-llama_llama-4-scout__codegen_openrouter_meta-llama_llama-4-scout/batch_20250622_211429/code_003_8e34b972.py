"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: Create a code example for a custom Docusaurus theme that reuses the default header and footer.
Generated: DETERMINISTIC_8e34b972dff86075
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// MyCustomTheme.js
import React from 'react';
import { useThemeConfig, useColorMode } from '@docusaurus/preset-classic';
import Footer from '@theme/Footer';
import Header from '@theme/Header';

/**
 * Custom Docusaurus theme that reuses the default header and footer.
 */
function MyCustomTheme({ children }) {
  const { colorMode } = useColorMode();
  const { customFields } = useThemeConfig();

  return (
    <div>
      <Header />
      <main>{children}</main>
      <Footer />
    </div>
  );
}

export default MyCustomTheme;
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... other configurations ...
  themeConfig: {
    // ... other theme configurations ...
    customFields: {},
  },
  themes: [
    [
      '@docusaurus/preset-classic',
      {
        // ... other preset configurations ...
      },
    ],
  ],
  customThemes: ['my-custom-theme'],
};
```

```javascript
// src/pages/index.js
import React from 'react';
import MyCustomTheme from '../MyCustomTheme';

export default function Home() {
  return (
    <MyCustomTheme>
      <h1>Welcome to my custom theme!</h1>
    </MyCustomTheme>
  );
}
```

```bash
# File structure
my-docusaurus-project/
├── docusaurus.config.js
├── src
│   ├── components
│   │   └── MyCustomTheme.js
│   └── pages
│       └── index.js
└── package.json
```
