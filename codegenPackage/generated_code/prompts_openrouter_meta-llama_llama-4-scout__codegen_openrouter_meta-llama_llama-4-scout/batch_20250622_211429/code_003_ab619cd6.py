"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2783--docusaurus-2.netlify.app
Prompt: Create a code example for a Docusaurus blog post that uses MDX to embed a React component.
Generated: DETERMINISTIC_ab619cd6cca6b9cc
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// MyComponent.js
import React from 'react';

/**
 * A simple React component to demonstrate MDX usage in Docusaurus.
 * @returns {JSX.Element} The component's JSX element.
 */
function MyComponent() {
  return (
    <div>
      <h2>Hello from MyComponent!</h2>
      <p>This is a paragraph from MyComponent.</p>
    </div>
  );
}

export default MyComponent;
```

```mdx
// blog-post.mdx
import MyComponent from '@site/src/components/MyComponent';

## Using MDX with React Components

MDX allows you to use React components directly in your Markdown files.

## Example Usage

<MyComponent />

## More Markdown Content

You can write more Markdown content alongside your React components.

## Another Component Example

<MyComponent />
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... other configurations ...
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        // ... other preset configurations ...
        mdx: {
          // Enable MDX support
          extension: ['.md', '.mdx'],
        },
      },
    ],
  ],
};
```

```bash
# Installation command (if not already installed)
npm install @docusaurus/preset-classic @mdx-js/react
```
