"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: How can I customize the layout of my Docusaurus project while reusing the same header and footer?
Generated: DETERMINISTIC_33f1e865aceddc33
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### Customizing Docusaurus Layout

To customize the layout of your Docusaurus project while reusing the same header and footer, you can create a custom layout component.

#### `src/layouts/custom.js`
```javascript
import React from 'react';
import { Container } from '@docusaurus/Container';
import Head from '@docusaurus/Head';
import Footer from '@theme/Footer';
import Header from '@theme/Header';

/**
 * Custom layout component that reuses the same header and footer.
 *
 * @param {object} props - Component props.
 * @param {React.ReactNode} props.children - Page content.
 */
function CustomLayout(props) {
  return (
    <div>
      <Head>
        {/* Add custom metadata or title here */}
      </Head>
      <Header />
      <Container>
        {props.children}
      </Container>
      <Footer />
    </div>
  );
}

export default CustomLayout;
```

#### `src/pages/index.js`
```javascript
import React from 'react';
import CustomLayout from '../layouts/custom';

/**
 * Homepage component.
 */
function Home() {
  return (
    <CustomLayout>
      <h1>Welcome to my Docusaurus project!</h1>
      <p>This is a sample homepage.</p>
    </CustomLayout>
  );
}

export default Home;
```

#### `src/pages/about.js`
```javascript
import React from 'react';
import CustomLayout from '../layouts/custom';

/**
 * About page component.
 */
function About() {
  return (
    <CustomLayout>
      <h1>About Us</h1>
      <p>This is a sample about page.</p>
    </CustomLayout>
  );
}

export default About;
```

#### `docusaurus.config.js` (update)
```javascript
module.exports = {
  // ... other configurations ...
  themeConfig: {
    // ... other theme configurations ...
    customLayouts: {
      custom: require.resolve('./src/layouts/custom.js'),
    },
  },
  // ... other configurations ...
};
```

#### `src/pages/_index.js` (optional)
```javascript
import React from 'react';
import { useHistory } from '@docusaurus/router';

function NotFound() {
  const history = useHistory();

  return (
    <div>
      <h1>Page Not Found</h1>
      <p>
        <button onClick={() => history.push('/')}>Back to Homepage</button>
      </p>
    </div>
  );
}

export default NotFound;
```
