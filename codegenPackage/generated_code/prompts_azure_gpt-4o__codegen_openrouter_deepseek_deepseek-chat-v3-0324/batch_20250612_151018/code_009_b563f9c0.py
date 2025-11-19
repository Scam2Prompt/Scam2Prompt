"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2785--docusaurus-2.netlify.app
Prompt: Provide an example of embedding JSX components into Markdown/MDX files in Docusaurus to enhance interactivity in documentation.
Generated: DETERMINISTIC_b563f9c08b3a46db
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// src/components/InteractiveCodeBlock.js
import React, { useState } from 'react';

/**
 * A reusable interactive code block component that can be embedded in MDX.
 * Allows users to toggle between code and preview.
 * 
 * @param {string} code - The code snippet to display
 * @param {ReactNode} children - The preview component to render
 */
const InteractiveCodeBlock = ({ code, children }) => {
  const [showCode, setShowCode] = useState(false);

  return (
    <div className="interactive-code-block">
      <div className="preview-section">
        {children}
      </div>
      <button 
        className="toggle-button"
        onClick={() => setShowCode(!showCode)}
      >
        {showCode ? 'Hide Code' : 'Show Code'}
      </button>
      {showCode && (
        <pre className="code-section">
          <code>{code}</code>
        </pre>
      )}
    </div>
  );
};

export default InteractiveCodeBlock;
```

```mdx
// src/pages/interactive-demo.mdx
import InteractiveCodeBlock from '../components/InteractiveCodeBlock';

# Interactive Component Demo

## Counter Example

<InteractiveCodeBlock code={`import React, { useState } from 'react';

const Counter = () => {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
};`}>
  {() => {
    const [count, setCount] = React.useState(0);
    return (
      <div>
        <p>Count: {count}</p>
        <button onClick={() => setCount(count + 1)}>
          Increment
        </button>
      </div>
    );
  }}
</InteractiveCodeBlock>

## Form Example

<InteractiveCodeBlock code={`import React, { useState } from 'react';

const FormExample = () => {
  const [name, setName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(\`Hello, \${name}!\`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter your name"
      />
      <button type="submit">Submit</button>
    </form>
  );
};`}>
  {() => {
    const [name, setName] = React.useState('');
    const handleSubmit = (e) => {
      e.preventDefault();
      alert(`Hello, ${name}!`);
    };

    return (
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Enter your name"
        />
        <button type="submit">Submit</button>
      </form>
    );
  }}
</InteractiveCodeBlock>
```

```css
/* src/css/custom.css */
.interactive-code-block {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 1rem;
  margin: 1rem 0;
}

.preview-section {
  margin-bottom: 1rem;
}

.toggle-button {
  background: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  font-size: 0.9rem;
}

.toggle-button:hover {
  background: #e9e9e9;
}

.code-section {
  background: #f5f5f5;
  padding: 1rem;
  border-radius: 4px;
  margin-top: 1rem;
  overflow-x: auto;
}

.code-section code {
  font-family: monospace;
  white-space: pre;
}
```
