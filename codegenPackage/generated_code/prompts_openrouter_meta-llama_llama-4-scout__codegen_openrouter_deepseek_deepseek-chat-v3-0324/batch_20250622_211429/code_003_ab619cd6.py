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

```mdx
---
title: Embedding React Components in MDX
slug: embedding-react-in-mdx
---

import MyComponent from './MyComponent';

# Embedding React Components in MDX

MDX allows you to seamlessly integrate React components into your Markdown content. Here's an example:

## Basic Usage

Simply import and use your component:

```jsx
<MyComponent title="Hello from React!" />
```

## With Props

You can pass props just like in regular JSX:

```jsx
<MyComponent 
  title="Customizable Component"
  color="blue"
  size={20}
/>
```

## Interactive Example

Here's an interactive counter component:

```jsx
<Counter initialCount={5} />
```

## Styled Components

Works with styled components too:

```jsx
<StyledButton 
  primary 
  onClick={() => alert('Clicked!')}
>
  Click Me
</StyledButton>
```

Remember to import all components at the top of your MDX file.
```

```jsx
// MyComponent.js
import React from 'react';

/**
 * A simple demo component for MDX embedding
 * @param {string} title - The title to display
 * @param {string} [color='black'] - Text color
 * @param {number} [size=16] - Font size
 */
const MyComponent = ({ title, color = 'black', size = 16 }) => {
  return (
    <div style={{ color, fontSize: `${size}px`, padding: '1rem' }}>
      <h3>{title}</h3>
      <p>This component was embedded in MDX!</p>
    </div>
  );
};

export default MyComponent;
```

```jsx
// Counter.js
import React, { useState } from 'react';

/**
 * Interactive counter component
 * @param {number} initialCount - Starting count value
 */
const Counter = ({ initialCount = 0 }) => {
  const [count, setCount] = useState(initialCount);

  return (
    <div style={{ padding: '1rem', border: '1px solid #ddd' }}>
      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
      <button onClick={() => setCount(c => c - 1)}>Decrement</button>
    </div>
  );
};

export default Counter;
```

```jsx
// StyledButton.js
import styled from 'styled-components';

/**
 * A styled button component
 */
const StyledButton = styled.button`
  background: ${props => props.primary ? 'blue' : 'white'};
  color: ${props => props.primary ? 'white' : 'black'};
  font-size: 1em;
  margin: 1em;
  padding: 0.5em 1em;
  border: 2px solid blue;
  border-radius: 3px;
  cursor: pointer;

  &:hover {
    opacity: 0.8;
  }
`;

export default StyledButton;
```
