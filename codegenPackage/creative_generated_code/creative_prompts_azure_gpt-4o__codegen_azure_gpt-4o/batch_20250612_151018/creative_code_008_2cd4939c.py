"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2820--docusaurus-2.netlify.app
Prompt: Write code to embed interactive JSX components into Markdown files in a Docusaurus project.
Generated: DETERMINISTIC_2cd4939cebe39ada
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary modules and components
import React from 'react';

// Docusaurus provides a way to extend Markdown functionality using MDX
// MDX allows embedding JSX components directly within Markdown files.

// Example interactive JSX component
const Counter = () => {
  // State to keep track of the counter value
  const [count, setCount] = React.useState(0);

  // Function to increment the counter
  const increment = () => setCount(count + 1);

  // Function to decrement the counter
  const decrement = () => {
    if (count > 0) {
      setCount(count - 1);
    }
  };

  return (
    <div style={{ textAlign: 'center', margin: '20px 0' }}>
      <h3>Interactive Counter</h3>
      <p style={{ fontSize: '20px' }}>Count: {count}</p>
      <button onClick={decrement} disabled={count === 0}>
        -
      </button>
      <button onClick={increment}>+</button>
    </div>
  );
};

export default Counter;

// Usage Instructions:
// 1. Save this component in your Docusaurus project's `src/components` folder (e.g., `src/components/Counter.jsx`).
// 2. In your Markdown file (e.g., `docs/my-markdown-page.md`), use the following MDX syntax to embed the Counter component:
//
// ```mdx
// import Counter from '@site/src/components/Counter';
//
// # Interactive Counter Example
//
// Below is an interactive JSX component embedded in a Markdown file:
//
// <Counter />
// ```
//
// 3. Run your Docusaurus project (`npm start` or `yarn start`) and navigate to the Markdown page.
// 4. The Counter component should appear with interactive functionality.
```
