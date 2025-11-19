"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2785--docusaurus-2.netlify.app
Prompt: Can you provide an example of embedding JSX components in Markdown using Docusaurus?
Generated: DETERMINISTIC_2d4827b9929e32e6
Batch ID: 20250612_163408
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/my-org/my-docusaurus-site/edit/main/website/blog/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://my-docusaurus-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/my-org/my-docusaurus-site/edit/main/website/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```jsx
// MyComponent.jsx
import React from 'react';

/**
 * A simple functional component that displays a greeting message.
 * @param {Object} props - Component props
 * @param {string} props.name - The name to greet
 * @returns {JSX.Element} The rendered greeting message
 */
const MyComponent = ({ name }) => {
  return <h1>Hello, {name}!</h1>;
};

export default MyComponent;
```

```markdown
<!-- Using JSX components in Docusaurus Markdown -->

# Welcome to My Docusaurus Site

Here is an embedded JSX component:

<MyComponent name="Docusaurus User" />
```

```js
// docusaurus.config.js
module.exports = {
  title: 'My Docusaurus Site',
  tagline: 'The best site for documentation',
  url: 'https://my-docusaurus-site.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'my-org', // Usually your GitHub org/user name.
  projectName: 'my-docusaurus-site', // Usually your repo name.
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl: 'https://github.com/my-org/my-docusaurus-site/edit/main/website/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl: 'https://github.com/my-org/my-docusaurus-site/edit/main/website/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
```

```jsx
// src/pages/index.js
import React from 'react';
import MyComponent from '../components/MyComponent';

const HomePage = () => {
  return (
    <div>
      <h1>Welcome to My Docusaurus Site</h1>
      <MyComponent name="Visitor" />
    </div>
  );
};

export default HomePage;
```

```bash
# Install Docusaurus and create a project
npx create-docusaurus@latest my-docusaurus-site classic
cd my-docusaurus-site
npm install
npm start
```

```bash
# To build the site for production
npm run build
```
