"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: Explain how to extend a Docusaurus project layout using React components and provide an example.
Generated: DETERMINISTIC_d05e8b406a15ad6c
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary React and Docusaurus components
import React from 'react';
import Layout from '@theme/Layout';
import { useHistory } from 'react-router-dom';

// Custom Header Component
const CustomHeader = () => {
    return (
        <header style={{ backgroundColor: '#4a90e2', padding: '20px', color: '#fff' }}>
            <h1>My Custom Header</h1>
        </header>
    );
};

// Custom Footer Component
const CustomFooter = () => {
    return (
        <footer style={{ backgroundColor: '#333', padding: '10px', color: '#fff', textAlign: 'center' }}>
            <p>© 2023 My Docusaurus Project</p>
        </footer>
    );
};

// Main Page Component
const CustomPage = () => {
    const history = useHistory();

    // Function to handle button click
    const handleNavigation = () => {
        try {
            history.push('/another-page'); // Navigation to another page
        } catch (error) {
            console.error("Navigation error:", error); // Error handling
        }
    };

    return (
        <Layout>
            <CustomHeader />
            <main style={{ padding: '20px' }}>
                <h2>Welcome to My Custom Docusaurus Page</h2>
                <p>This is a simple demonstration of extending the Docusaurus layout with additional components.</p>
                <button onClick={handleNavigation} style={{ padding: '10px 15px', cursor: 'pointer' }}>
                    Go to Another Page
                </button>
            </main>
            <CustomFooter />
        </Layout>
    );
};

// Export the CustomPage component as the default export
export default CustomPage;
```
