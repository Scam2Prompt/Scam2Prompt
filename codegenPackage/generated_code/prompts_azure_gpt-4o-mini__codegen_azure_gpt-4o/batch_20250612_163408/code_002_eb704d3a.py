"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2783--docusaurus-2.netlify.app
Prompt: Can you provide an example of embedding JSX components into Markdown using Docusaurus and MDX?
Generated: DETERMINISTIC_eb704d3ab828b0f8
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// File: docs/example.md

import React from 'react';

// Import custom JSX components
import Alert from '@site/src/components/Alert';
import Button from '@site/src/components/Button';

/**
 * This is an example of embedding JSX components into Markdown using MDX in Docusaurus.
 * MDX allows you to mix Markdown and React components seamlessly.
 */

# Embedding JSX Components in Markdown

This is a regular Markdown paragraph. Below, we will embed some custom React components.

## Example: Alert Component

<Alert type="info">
  This is an informational alert embedded directly into Markdown using MDX.
</Alert>

## Example: Button Component

<Button onClick={() => alert('Button clicked!')}>
  Click Me
</Button>

## Regular Markdown Content

You can continue writing regular Markdown content after embedding JSX components.

- This is a list item.
- Another list item.

> This is a blockquote.

---

### Conclusion

MDX makes it easy to combine Markdown and React components, enabling dynamic and interactive documentation.
```

```jsx
// File: src/components/Alert.jsx

import React from 'react';
import PropTypes from 'prop-types';
import './Alert.css'; // Optional: Add custom styles for the Alert component

/**
 * Alert Component
 * Displays an alert box with a specified type and content.
 * 
 * Props:
 * - type: The type of alert (e.g., 'info', 'warning', 'error').
 * - children: The content to display inside the alert.
 */
const Alert = ({ type, children }) => {
  const alertClass = `alert alert-${type}`; // Dynamically set the class based on the type
  return <div className={alertClass}>{children}</div>;
};

// Prop type validation
Alert.propTypes = {
  type: PropTypes.oneOf(['info', 'warning', 'error']).isRequired,
  children: PropTypes.node.isRequired,
};

export default Alert;
```

```jsx
// File: src/components/Button.jsx

import React from 'react';
import PropTypes from 'prop-types';
import './Button.css'; // Optional: Add custom styles for the Button component

/**
 * Button Component
 * Renders a clickable button with an onClick handler.
 * 
 * Props:
 * - onClick: Function to execute when the button is clicked.
 * - children: The content to display inside the button.
 */
const Button = ({ onClick, children }) => {
  return (
    <button className="custom-button" onClick={onClick}>
      {children}
    </button>
  );
};

// Prop type validation
Button.propTypes = {
  onClick: PropTypes.func.isRequired,
  children: PropTypes.node.isRequired,
};

export default Button;
```

```css
/* File: src/components/Alert.css */

/* Basic styles for the Alert component */
.alert {
  padding: 1rem;
  border-radius: 4px;
  margin: 1rem 0;
  font-size: 1rem;
}

.alert-info {
  background-color: #e7f3fe;
  color: #3178c6;
}

.alert-warning {
  background-color: #fff4e5;
  color: #d97706;
}

.alert-error {
  background-color: #fdecea;
  color: #d32f2f;
}
```

```css
/* File: src/components/Button.css */

/* Basic styles for the Button component */
.custom-button {
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}

.custom-button:hover {
  background-color: #0056b3;
}
```

This code demonstrates how to embed JSX components into Markdown using MDX in Docusaurus. It includes reusable components (`Alert` and `Button`) with proper styling and error handling.
