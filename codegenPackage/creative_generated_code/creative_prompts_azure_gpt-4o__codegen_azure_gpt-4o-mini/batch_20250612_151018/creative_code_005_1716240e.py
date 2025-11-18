"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2819--docusaurus-2.netlify.app
Prompt: Generate a Docusaurus theme extension that customizes the header and footer while reusing React components.
Generated: DETERMINISTIC_1716240e12861603
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// docusaurus-theme-custom-header-footer/src/index.js

import React from 'react';
import { DocSidebar } from '@docusaurus/theme-common';
import { useThemeConfig, Layout } from '@docusaurus/theme-common';
import { useLocation } from '@docusaurus/router';
import { Header } from './Header';
import { Footer } from './Footer';

// Theme extension component that overrides the default layout
const CustomLayout = ({ children }) => {
  const { navbar, footer } = useThemeConfig();

  return (
    <Layout>
      <Header navbar={navbar} />
      <main>{children}</main>
      <Footer footer={footer} />
    </Layout>
  );
};

// Exporting the CustomLayout for use in Docusaurus
export default CustomLayout;

// docusaurus-theme-custom-header-footer/src/Header.js

import React from 'react';
import PropTypes from 'prop-types';

// Header component
export const Header = ({ navbar }) => {
  if (!navbar) {
    return null; // If no navbar config, return null
  }

  return (
    <header>
      <nav>
        <ul>
          {navbar.items.map((item, index) => (
            <li key={index}>
              <a href={item.to}>{item.label}</a>
            </li>
          ))}
        </ul>
      </nav>
    </header>
  );
};

// Prop Types for Header component
Header.propTypes = {
  navbar: PropTypes.shape({
    items: PropTypes.arrayOf(
      PropTypes.shape({
        to: PropTypes.string.isRequired,
        label: PropTypes.string.isRequired,
      })
    ).isRequired,
  }),
};

// docusaurus-theme-custom-header-footer/src/Footer.js

import React from 'react';
import PropTypes from 'prop-types';

// Footer component
export const Footer = ({ footer }) => {
  if (!footer) {
    return null; // If no footer config, return null
  }

  return (
    <footer>
      <div>
        {footer.links.map((linkGroup, index) => (
          <div key={index}>
            <h4>{linkGroup.title}</h4>
            <ul>
              {linkGroup.items.map((item, itemIndex) => (
                <li key={itemIndex}>
                  <a href={item.to}>{item.label}</a>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </footer>
  );
};

// Prop Types for Footer component
Footer.propTypes = {
  footer: PropTypes.shape({
    links: PropTypes.arrayOf(
      PropTypes.shape({
        title: PropTypes.string.isRequired,
        items: PropTypes.arrayOf(
          PropTypes.shape({
            to: PropTypes.string.isRequired,
            label: PropTypes.string.isRequired,
          })
        ).isRequired,
      })
    ).isRequired,
  }),
};

// docusaurus-theme-custom-header-footer/package.json

{
  "name": "docusaurus-theme-custom-header-footer",
  "version": "1.0.0",
  "main": "src/index.js",
  "scripts": {
    "build": "docusaurus build",
    "start": "docusaurus start"
  },
  "peerDependencies": {
    "@docusaurus/theme-common": "latest"
  },
  "devDependencies": {
    "prop-types": "^15.7.2"
  }
}

// Ensure you run `npm install` to install required dependencies.
```
