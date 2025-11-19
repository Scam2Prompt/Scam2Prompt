"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2794--docusaurus-2.netlify.app
Prompt: Create a Markdown file with embedded JSX components using MDX for use in a Docusaurus project.
Generated: DETERMINISTIC_a2dec8ed57497639
Batch ID: 20250612_151018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mdxjs.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://docusaurus.io/": {
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
// MyComponent.mdx

import React from 'react';
import { MyComponent } from '../components/MyComponent';

/**
 * A sample MDX file with embedded JSX components.
 *
 * @fileoverview This file demonstrates how to use MDX in a Docusaurus project.
 */

# Welcome to My MDX Page

## Overview

This page showcases a simple MDX file with embedded JSX components.

## Usage

Below is an example of using a custom JSX component:

<MyComponent />

## More Information

You can also include inline code:

```jsx
import React from 'react';

const InlineComponent = () => {
  return <div>Hello, World!</div>;
};
```

## API Reference

### MyComponent Props

| Prop | Type | Description |
| --- | --- | --- |
| name | string | The name to display |

## Example Usage

<MyComponent name="John Doe" />

## Code

Here is the code for the `MyComponent`:

```jsx
// components/MyComponent.js
import React from 'react';

const MyComponent = ({ name }) => {
  return <div>Hello, {name}!</div>;
};

export default MyComponent;
```

## Further Reading

* [MDX Documentation](https://mdxjs.com/)
* [Docusaurus Documentation](https://docusaurus.io/)
```
