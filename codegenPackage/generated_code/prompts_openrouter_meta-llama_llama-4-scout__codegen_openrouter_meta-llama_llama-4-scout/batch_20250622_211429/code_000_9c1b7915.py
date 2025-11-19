"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Write a Markdown/MDX code snippet for a Docusaurus documentation page that includes a JSX component.
Generated: DETERMINISTIC_9c1b79157942e380
Batch ID: 20250622_211429
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:3000/docs/example`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```markdown
# Using a Custom JSX Component in Docusaurus

## Overview

This example demonstrates how to use a custom JSX component in a Docusaurus documentation page.

## Usage

### CustomComponent.jsx
```jsx
// src/components/CustomComponent.jsx
import React from 'react';

/**
 * A custom JSX component for demonstration purposes.
 * @param {object} props - The component props.
 * @param {string} props.message - The message to display.
 * @returns {JSX.Element} The custom component.
 */
function CustomComponent({ message }) {
  return (
    <div>
      <h2>Custom Component</h2>
      <p>{message}</p>
    </div>
  );
}

export default CustomComponent;
```

### Markdown/MDX Page
```markdown
// docs/example.mdx
import React from 'react';
import CustomComponent from '@site/src/components/CustomComponent';

## Example Usage

<CustomComponent message="Hello, World!" />

## Code

```jsx
// You can also use the component in code blocks
<CustomComponent message="Code block example" />
```

## Notes

* Make sure to update the `docusaurus.config.js` file to include the custom component directory.
* You can use the component in any MDX file by importing it and using the JSX syntax.
```

## docusaurus.config.js Configuration
```javascript
// docusaurus.config.js
module.exports = {
  // ...
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        // ...
        customFields: {
          // Add the custom component directory
          customComponents: ['src/components'],
        },
      },
    ],
  ],
  // ...
};
```

## Installation and Usage

To use this code, create a new file in the `docs` directory (e.g., `example.mdx`) and copy the Markdown/MDX content into it. Create a new file in the `src/components` directory (e.g., `CustomComponent.jsx`) and copy the JSX component code into it.

Run `npm run build` or `yarn build` to build the Docusaurus site, then `npm run serve` or `yarn serve` to start the development server. Open your browser and navigate to `http://localhost:3000/docs/example` to see the custom component in action.
```
