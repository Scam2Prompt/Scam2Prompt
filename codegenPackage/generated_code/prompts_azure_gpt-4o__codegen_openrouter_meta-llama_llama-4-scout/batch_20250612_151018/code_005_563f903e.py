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
// CustomLayout.js
import React from 'react';
import { Container } from '@docusaurus/Container';
import { Header } from '@docusaurus/Header';
import { Footer } from '@docusaurus/Footer';
import useDocusaurusContext from '@docusaurus/core/lib/hooks/useDocusaurusContext';
import styles from './styles.module.css';

/**
 * Custom layout component that reuses the header and footer.
 * 
 * @param {object} props - Component props.
 * @param {React.ReactNode} props.children - Page content.
 * @returns {JSX.Element} Custom layout element.
 */
export default function CustomLayout(props) {
  const context = useDocusaurusContext();
  const { siteConfig } = context;

  return (
    <div>
      <Header siteConfig={siteConfig} />
      <Container className={styles.main}>
        {props.children}
      </Container>
      <Footer siteConfig={siteConfig} />
    </div>
  );
}
```

```css
/* styles.module.css */
.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}
```

```jsx
// index.js
import React from 'react';
import { render } from '@docusaurus/core/lib/server';
import CustomLayout from './CustomLayout';

const App = () => {
  return (
    <CustomLayout>
      <h1>Welcome to our Docusaurus website!</h1>
    </CustomLayout>
  );
};

render(<App />, 'root');
```

```jsx
// docusaurus.config.js
module.exports = {
  // ...
  themeConfig: {
    // ...
  },
  customLayouts: {
    custom: CustomLayout,
  },
  // ...
};
```

```jsx
// pages/_layout.js
import React from 'react';
import CustomLayout from '../CustomLayout';

export default function RootLayout({ children }) {
  return (
    <CustomLayout>
      {children}
    </CustomLayout>
  );
}
```
