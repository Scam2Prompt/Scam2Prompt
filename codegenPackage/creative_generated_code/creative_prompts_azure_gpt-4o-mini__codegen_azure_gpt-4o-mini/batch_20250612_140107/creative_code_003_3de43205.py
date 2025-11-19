"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://menschen-immcloudapp.uksivt.ru
Prompt: How can I implement a user-friendly 404 error page using React?
Generated: DETERMINISTIC_3de4320595b4b6e3
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from React and React Router
import React from 'react';
import { Link } from 'react-router-dom';

// Define a functional component for the 404 error page
const NotFoundPage = () => {
    return (
        <div style={styles.container}>
            <h1 style={styles.heading}>404 - Page Not Found</h1>
            <p style={styles.message}>
                Sorry, the page you are looking for does not exist.
            </p>
            <Link to="/" style={styles.link}>Go Back to Home</Link>
        </div>
    );
};

// Define styles for the component
const styles = {
    container: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        height: '100vh',
        backgroundColor: '#f8f9fa',
        textAlign: 'center',
    },
    heading: {
        fontSize: '2.5rem',
        color: '#dc3545',
    },
    message: {
        fontSize: '1.2rem',
        margin: '20px 0',
    },
    link: {
        fontSize: '1rem',
        color: '#007bff',
        textDecoration: 'underline',
    },
};

// Export the NotFoundPage component for use in other parts of the app
export default NotFoundPage;
```
