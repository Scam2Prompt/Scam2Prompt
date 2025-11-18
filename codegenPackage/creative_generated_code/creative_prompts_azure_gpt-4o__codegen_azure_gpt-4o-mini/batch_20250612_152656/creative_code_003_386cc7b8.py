"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokoswap-admin-build.pages.dev
Prompt: Provide an example of JavaScript code to dynamically load and initialize components from a minimal UI kit in a React project.
Generated: DETERMINISTIC_386cc7b82cdcc200
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';

// Component to dynamically load and initialize UI components
const DynamicComponentLoader = ({ componentName }) => {
  const [Component, setComponent] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Function to dynamically import the component
    const loadComponent = async () => {
      try {
        const module = await import(`./components/${componentName}`);
        setComponent(() => module.default); // Assuming the default export is the component
      } catch (err) {
        // Handle errors during component loading
        console.error(`Error loading component ${componentName}:`, err);
        setError(`Failed to load component: ${componentName}`);
      }
    };

    if (componentName) {
      loadComponent();
    }
  }, [componentName]);

  // Render loading state, error message, or the loaded component
  if (error) {
    return <div className="error">{error}</div>;
  }

  if (!Component) {
    return <div className="loading">Loading component...</div>;
  }

  return <Component />;
};

// Example usage of DynamicComponentLoader
const App = () => {
  const [currentComponent, setCurrentComponent] = useState('Button'); // Default component

  return (
    <div>
      <h1>Dynamic UI Component Loader</h1>
      <button onClick={() => setCurrentComponent('Button')}>Load Button</button>
      <button onClick={() => setCurrentComponent('Card')}>Load Card</button>
      <DynamicComponentLoader componentName={currentComponent} />
    </div>
  );
};

// Export the App component
export default App;
```

### Note:
- Ensure that your components are stored in the `./components/` directory and are exported as default exports for this code to work correctly.
- Styles and CSS classes (e.g., `.loading`, `.error`) should be defined in your CSS files for proper styling.
