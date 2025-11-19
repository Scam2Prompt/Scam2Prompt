"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2689--docusaurus-2.netlify.app
Prompt: Create a Docusaurus blog post in Markdown that embeds JSX components using MDX. Include an example of a React component embedded in the post.
Generated: DETERMINISTIC_35710dee05b6d75c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**My MDX Blog Post**
========================

import React from 'react';
import MyComponent from '../components/MyComponent';

## Introduction

This is an example of a Docusaurus blog post that uses MDX to embed JSX components.

## Embedded React Component

<MyComponent />

## More Markdown Content

You can write regular Markdown content here.

### Code Block

```jsx
// Example code block
function HelloWorld() {
  return <h1>Hello, World!</h1>;
}
```

## Another Embedded React Component

<MyComponent name="John Doe" />

### MyComponent.js

```jsx
// components/MyComponent.js
import React from 'react';

const MyComponent = ({ name }) => {
  return (
    <div>
      <h2>Hello, {name}!</h2>
      <p>This is a reusable React component.</p>
    </div>
  );
};

export default MyComponent;
```

## Conclusion

This demonstrates how to embed React components in a Docusaurus blog post using MDX.
