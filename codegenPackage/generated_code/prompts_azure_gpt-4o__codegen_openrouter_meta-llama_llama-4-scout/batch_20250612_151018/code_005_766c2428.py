"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2735--docusaurus-2.netlify.app
Prompt: Provide a code example for customizing the layout of a Docusaurus site using React components while reusing the default header and footer.
Generated: DETERMINISTIC_766c2428e20a52d1
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// src/layouts/customLayout.js
import React from 'react';
import { MDXProvider } from '@mdx-js/react';
import { Container } from '@material-ui/core';
import Header from '@theme/Header';
import Footer from '@theme/Footer';
import MDXComponents from '@theme/MDXComponents';

/**
 * Custom layout component that reuses the default header and footer
 * while allowing for customization of the main content area.
 */
export default function CustomLayout(props) {
  return (
    <div>
      <Header />
      <main>
        <Container maxWidth="lg">
          <MDXProvider components={MDXComponents}>
            {props.children}
          </MDXProvider>
        </Container>
      </main>
      <Footer />
    </div>
  );
}
```

```jsx
// src/pages/index.js
import React from 'react';
import CustomLayout from '../layouts/customLayout';
import { Box, Typography } from '@material-ui/core';

/**
 * Homepage component that uses the custom layout.
 */
export default function Home() {
  return (
    <CustomLayout>
      <Box p={4}>
        <Typography variant="h1">Welcome to our Docusaurus site!</Typography>
      </Box>
    </CustomLayout>
  );
}
```

```jsx
// src/theme/MDXComponents.js
import React from 'react';
import { Link } from '@material-ui/core';

/**
 * Custom MDX components that can be used in Markdown files.
 */
export default {
  a: (props) => <Link {...props} />,
  // Add more custom components as needed
};
```

```jsx
// src/theme/Header.js
import React from 'react';
import { Navbar, Container, Nav } from 'react-bootstrap';

/**
 * Default header component.
 */
export default function Header() {
  return (
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand href="#">Docusaurus Site</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="#">Home</Nav.Link>
            <Nav.Link href="#">Docs</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}
```

```jsx
// src/theme/Footer.js
import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';

/**
 * Default footer component.
 */
export default function Footer() {
  return (
    <footer className="footer mt-auto footer-light">
      <Container>
        <Row>
          <Col md={6}>
            <span>Copyright 2023 Docusaurus Site</span>
          </Col>
          <Col md={6} className="text-end">
            <a href="#">Privacy Policy</a>
          </Col>
        </Row>
      </Container>
    </footer>
  );
}
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... other config options ...
  themeConfig: {
    // ... other theme config options ...
    customLayout: 'src/layouts/customLayout',
  },
};
```
