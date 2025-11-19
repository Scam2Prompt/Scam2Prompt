"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://team-2.netlify.app
Prompt: Can you provide code examples for enabling JavaScript features in a React app?
Generated: DETERMINISTIC_687c7cee2d300f63
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from React
import React, { useState, useEffect } from 'react';

// Create a functional component
const FeatureToggleComponent = () => {
    // State to manage the feature toggle
    const [isFeatureEnabled, setIsFeatureEnabled] = useState(false);

    // Function to toggle the feature
    const toggleFeature = () => {
        setIsFeatureEnabled(prevState => !prevState);
    };

    // Side effect to log the feature status whenever it changes
    useEffect(() => {
        console.log(`Feature is now ${isFeatureEnabled ? 'enabled' : 'disabled'}`);
    }, [isFeatureEnabled]);

    return (
        <div>
            <h1>Feature Toggle Example</h1>
            <button onClick={toggleFeature}>
                {isFeatureEnabled ? 'Disable Feature' : 'Enable Feature'}
            </button>
            {isFeatureEnabled && <p>The feature is currently enabled!</p>}
        </div>
    );
};

// Main application component
const App = () => {
    return (
        <div>
            <FeatureToggleComponent />
        </div>
    );
};

// Error boundary component to handle potential errors in the child component tree
class ErrorBoundary extends React.Component {
    constructor(props) {
        super(props);
        this.state = { hasError: false };
    }

    static getDerivedStateFromError(error) {
        // Update state so the next render shows the fallback UI
        return { hasError: true };
    }

    componentDidCatch(error, info) {
        // You can also log the error to an error reporting service
        console.error("Error caught by Error Boundary:", error, info);
    }

    render() {
        if (this.state.hasError) {
            return <h1>Something went wrong.</h1>;
        }

        return this.props.children;
    }
}

// Render the application with error handling
const rootElement = document.getElementById('root');

// Check if the root element exists and render the App wrapped in ErrorBoundary
if (rootElement) {
    ReactDOM.render(
        <ErrorBoundary>
            <App />
        </ErrorBoundary>,
        rootElement
    );
} else {
    console.error("Root element not found. Please ensure the HTML has an element with id 'root'.");
}
```
