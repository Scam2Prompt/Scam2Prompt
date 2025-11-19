"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: Can you provide a code example of embedding JSX components into Markdown using Docusaurus?
Generated: DETERMINISTIC_c5f8914a9275b1c4
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready code example of embedding JSX components in Markdown using Docusaurus:

```mdx
---
title: JSX in Markdown Example
description: Demonstrating JSX components in Docusaurus Markdown
---

import TabItem from '@theme/TabItem';
import Tabs from '@theme/Tabs';
import MyComponent from '@site/src/components/MyComponent';

# JSX in Markdown

Docusaurus allows you to embed JSX components directly in your Markdown files.

## Basic Usage

Here's an inline JSX component: <button onClick={() => alert('Clicked!')}>Click Me</button>

## Using Theme Components

<Tabs>
  <TabItem value="apple" label="Apple">
    This is an apple 🍎
  </TabItem>
  <TabItem value="orange" label="Orange">
    This is an orange 🍊
  </TabItem>
</Tabs>

## Custom Components

Here's our custom component:

<MyComponent 
  title="Sample Title" 
  description="This description comes from the Markdown"
/>

## Mixing Markdown with JSX

Regular Markdown content works alongside JSX:

1. First item
2. Second item

<div style={{padding: '16px', backgroundColor: '#f5f5f5'}}>
  ### This header is inside a div
  - With markdown content
  - That gets processed normally
</div>

## Dynamic Content

You can use expressions:

Current date: {new Date().toLocaleDateString()}

Math expression: {5 * 5}
```

Note: For this to work properly, you need:
1. A `.mdx` file extension
2. Proper Docusaurus configuration with MDX support
3. Any custom components imported and available in the project
