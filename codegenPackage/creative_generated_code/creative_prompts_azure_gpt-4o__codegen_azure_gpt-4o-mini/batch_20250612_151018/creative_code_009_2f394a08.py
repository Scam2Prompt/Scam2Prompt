"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: Generate a code snippet to integrate ReasonReact components into a Docusaurus-powered documentation site.
Generated: DETERMINISTIC_2f394a089782a16f
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React from 'react';
import { useEffect } from 'react';
import { createRoot } from 'react-dom/client';
import { HelloWorld } from './HelloWorld.bs'; // Import the ReasonReact component

// Define a function to mount the ReasonReact component
function mountReasonReactComponent() {
  // Select the DOM element where the ReasonReact component will be mounted
  const container = document.getElementById('reason-react-root');
  
  if (!container) {
    console.error("Container for ReasonReact component not found.");
    return;
  }

  // Create a root for the React component
  const root = createRoot(container);

  // Render the ReasonReact component
  root.render(
    <React.StrictMode>
      <HelloWorld />
    </React.StrictMode>
  );
}

// Use useEffect to mount the component when the document is ready
useEffect(() => {
  mountReasonReactComponent();
}, []);

// Export a Docusaurus-compatible React component
export default function ReasonReactIntegration() {
  return (
    <div>
      <h2>ReasonReact Component Integration</h2>
      {/* Container for the ReasonReact component */}
      <div id="reason-react-root"></div>
    </div>
  );
}
```

```reason
// HelloWorld.re - A simple ReasonReact component

[@react.component]
let make = () => {
  <div>
    <h1>Hello, ReasonReact!</h1>
    <p>This is a component integrated into Docusaurus.</p>
  </div>;
};
``` 

### Usage
1. Ensure you have ReasonReact and Docusaurus set up in your project.
2. Place the `HelloWorld.re` file in your source directory.
3. Import `ReasonReactIntegration` in your Docusaurus documentation page where you want the component to appear.
