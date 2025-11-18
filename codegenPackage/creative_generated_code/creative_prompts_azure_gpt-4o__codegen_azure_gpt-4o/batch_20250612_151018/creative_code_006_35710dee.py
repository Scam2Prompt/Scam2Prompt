"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2689--docusaurus-2.netlify.app
Prompt: Create a Docusaurus blog post in Markdown that embeds JSX components using MDX. Include an example of a React component embedded in the post.
Generated: DETERMINISTIC_35710dee05b6d75c
Batch ID: 20250612_151018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/avatar.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```markdown
---
id: example-mdx-blog-post
title: Embedding JSX Components in Docusaurus Blog Posts
author: John Doe
author_title: Software Developer
author_url: https://example.com
author_image_url: https://example.com/avatar.jpg
tags: [docusaurus, mdx, react]
---

import React from 'react';

// Example React component to embed in the blog post
const Greeting = ({ name }) => {
  return (
    <div style={{ border: '1px solid #ddd', padding: '1rem', borderRadius: '8px' }}>
      <h2 style={{ color: '#0070f3' }}>Hello, {name}!</h2>
      <p>Welcome to this Docusaurus blog post that demonstrates MDX and JSX integration!</p>
    </div>
  );
};

# Embedding JSX Components in Docusaurus Blog Posts

MDX allows you to embed JSX components directly into your Markdown files. This is particularly useful when you want to create interactive or dynamic content inside your blog posts.

Below is an example of an embedded React component written in JSX:

<Greeting name="Alice" />

## Advantages of MDX in Docusaurus

- **Flexibility**: Combine Markdown and React seamlessly.
- **Reusability**: Embed reusable React components to avoid redundancy.
- **Dynamic Content**: Enhance static Markdown with interactive features.

You can use this approach to embed charts, forms, or any other React-based UI components directly inside your blog posts.

---

### How to Use MDX in Docusaurus

Simply import the React components at the top of your `.mdx` file and use them like regular JSX tags anywhere in the content.

```jsx
import MyComponent from './MyComponent';

<MyComponent />
```

Hope you find this example useful for your Docusaurus blogs!
```
