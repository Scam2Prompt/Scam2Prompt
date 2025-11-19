"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2809--docusaurus-2.netlify.app
Prompt: Create a Docusaurus plugin to customize the layout while reusing the default header and footer components.
Generated: DETERMINISTIC_a4065d9022817ea3
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/plugins/custom-layout/index.js
const path = require('path');

module.exports = function (context, options) {
  return {
    name: 'custom-layout-plugin',
    getThemePath() {
      return path.resolve(__dirname, './theme');
    },
  };
};

// src/plugins/custom-layout/theme/index.js
const React = require('react');
const Layout = require('@theme/Layout').default;
const Navbar = require('@theme/Navbar').default;
const Footer = require('@theme/Footer').default;

function CustomLayout(props) {
  const { children, noFooter, wrapperClassName } = props;

  return (
    <Layout>
      <Navbar />
      <main className={wrapperClassName}>
        {children}
      </main>
      {!noFooter && <Footer />}
    </Layout>
  );
}

module.exports = CustomLayout;

// docusaurus.config.js (partial)
module.exports = {
  // ... other config
  plugins: [
    [
      require.resolve('./src/plugins/custom-layout'),
      {
        // Plugin options if needed
      },
    ],
  ],
  themeConfig: {
    // ... other theme config
  },
};
```
