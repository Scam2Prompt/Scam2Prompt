"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: Provide a code example for embedding JSX components into Markdown files in a Docusaurus project using MDX.
Generated: DETERMINISTIC_121e25ece9fbf096
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Importing necessary React and Docusaurus modules
import React from 'react';
import { MDXProvider } from '@mdx-js/react';

// Importing custom components to use in Markdown
import MyComponent from './MyComponent';
import AnotherComponent from './AnotherComponent';

// Creating a custom components mapping for MDX
const components = {
  MyComponent,
  AnotherComponent,
};

// Main MDXWrapper component
const MDXWrapper = ({ children }) => {
  return (
    // Providing custom components to MDX
    <MDXProvider components={components}>
      <div className="mdx-wrapper">
        {children}
      </div>
    </MDXProvider>
  );
};

// Exporting the MDXWrapper component for use in the Docusaurus project
export default MDXWrapper;
```

```markdown
<!-- Example of an MDX file using the MDXWrapper -->
import MDXWrapper from './MDXWrapper.mdx';

// Using the MDXWrapper to enable JSX components
<MDXWrapper>
  # Welcome to My Docusaurus Site

  Here is a regular Markdown paragraph.

  <MyComponent someProp="value" />

  Another paragraph follows.

  <AnotherComponent />
</MDXWrapper>
```
