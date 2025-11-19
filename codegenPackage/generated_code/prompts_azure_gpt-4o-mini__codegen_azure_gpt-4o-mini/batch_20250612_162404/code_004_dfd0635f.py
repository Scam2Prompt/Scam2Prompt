"""
Generated Code Metadata:
========================
Original URL: https://oeth-v-0-11.pages.dev
Prompt: Create a React loading spinner component that can be reused across different parts of an application.
Generated: DETERMINISTIC_dfd0635fabfb61c3
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// LoadingSpinner.js
import React from 'react';
import PropTypes from 'prop-types';
import './LoadingSpinner.css'; // Importing CSS for styling

/**
 * LoadingSpinner component to display a loading indicator.
 * 
 * @param {Object} props - Component properties
 * @param {boolean} props.isLoading - Flag to indicate loading state
 * @param {string} [props.size='medium'] - Size of the spinner ('small', 'medium', 'large')
 * @param {string} [props.color='blue'] - Color of the spinner
 * @returns {JSX.Element|null} - Returns the spinner or null if not loading
 */
const LoadingSpinner = ({ isLoading, size = 'medium', color = 'blue' }) => {
    // If not loading, return null
    if (!isLoading) return null;

    // Define class names based on size and color
    const spinnerClass = `loading-spinner ${size} ${color}`;

    return (
        <div className={spinnerClass}>
            <div className="spinner" />
        </div>
    );
};

// PropTypes for type checking
LoadingSpinner.propTypes = {
    isLoading: PropTypes.bool.isRequired,
    size: PropTypes.oneOf(['small', 'medium', 'large']),
    color: PropTypes.string,
};

export default LoadingSpinner;
```

```css
/* LoadingSpinner.css */
.loading-spinner {
    display: flex;
    justify-content: center;
    align-items: center;
}

.spinner {
    border: 4px solid transparent;
    border-top: 4px solid currentColor; /* Use current color for the top */
    border-radius: 50%;
    animation: spin 1s linear infinite; /* Spin animation */
}

.small {
    width: 20px;
    height: 20px;
}

.medium {
    width: 40px;
    height: 40px;
}

.large {
    width: 60px;
    height: 60px;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
```

```javascript
// Example usage in a component
import React, { useState, useEffect } from 'react';
import LoadingSpinner from './LoadingSpinner';

const ExampleComponent = () => {
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // Simulate a data fetch
        const fetchData = async () => {
            try {
                // Simulate a delay
                await new Promise(resolve => setTimeout(resolve, 2000));
            } catch (error) {
                console.error('Error fetching data:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    return (
        <div>
            <h1>Example Component</h1>
            <LoadingSpinner isLoading={loading} size="medium" color="blue" />
            {!loading && <p>Data loaded successfully!</p>}
        </div>
    );
};

export default ExampleComponent;
```
