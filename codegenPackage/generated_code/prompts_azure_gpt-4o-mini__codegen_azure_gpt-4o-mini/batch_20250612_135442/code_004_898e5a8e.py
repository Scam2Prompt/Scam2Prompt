"""
Generated Code Metadata:
========================
Original URL: https://ashkar2023.github.io
Prompt: Suggest best practices for building interactive web experiences using React, referencing the skills of Muhammed Ashkar as a MERN stack developer.
Generated: DETERMINISTIC_898e5a8ed53f6b85
Batch ID: 20250612_135442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

// A functional component for an interactive web experience
const InteractiveComponent = ({ initialCount }) => {
    // State to manage the count
    const [count, setCount] = useState(initialCount);

    // Effect to log the count whenever it changes
    useEffect(() => {
        console.log(`Count has changed to: ${count}`);
    }, [count]); // Dependency array to run effect only when count changes

    // Function to handle incrementing the count
    const handleIncrement = () => {
        setCount(prevCount => prevCount + 1);
    };

    // Function to handle decrementing the count
    const handleDecrement = () => {
        setCount(prevCount => (prevCount > 0 ? prevCount - 1 : 0)); // Prevent negative count
    };

    // Render the component
    return (
        <div style={styles.container}>
            <h1 style={styles.header}>Interactive Counter</h1>
            <p style={styles.count}>Current Count: {count}</p>
            <button style={styles.button} onClick={handleIncrement}>
                Increment
            </button>
            <button style={styles.button} onClick={handleDecrement}>
                Decrement
            </button>
        </div>
    );
};

// PropTypes for type checking
InteractiveComponent.propTypes = {
    initialCount: PropTypes.number.isRequired,
};

// Default props
InteractiveComponent.defaultProps = {
    initialCount: 0,
};

// Styles for the component
const styles = {
    container: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '20px',
        border: '1px solid #ccc',
        borderRadius: '8px',
        width: '300px',
        margin: 'auto',
    },
    header: {
        fontSize: '24px',
        marginBottom: '10px',
    },
    count: {
        fontSize: '20px',
        margin: '10px 0',
    },
    button: {
        padding: '10px 15px',
        margin: '5px',
        fontSize: '16px',
        cursor: 'pointer',
        border: 'none',
        borderRadius: '5px',
        backgroundColor: '#007bff',
        color: '#fff',
        transition: 'background-color 0.3s',
    },
};

// Export the component for use in other parts of the application
export default InteractiveComponent;
```
