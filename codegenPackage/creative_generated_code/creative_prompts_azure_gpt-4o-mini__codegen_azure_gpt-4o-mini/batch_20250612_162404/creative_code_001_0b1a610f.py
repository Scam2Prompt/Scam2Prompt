"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-v-0-11.pages.dev
Prompt: How can I implement a loading screen in a React application using hooks?
Generated: DETERMINISTIC_0b1a610f5fb2af60
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';

// LoadingScreen component to display a loading spinner or message
const LoadingScreen = () => {
    return (
        <div className="loading-screen">
            <h2>Loading...</h2>
            <div className="spinner"></div>
        </div>
    );
};

// Main component that simulates data fetching with a loading screen
const App = () => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Simulate data fetching with useEffect
    useEffect(() => {
        const fetchData = async () => {
            try {
                setLoading(true); // Set loading to true before fetching
                // Simulating an API call with a timeout
                const response = await new Promise((resolve, reject) => {
                    setTimeout(() => {
                        // Simulate successful data fetch
                        resolve({ message: "Data fetched successfully!" });
                        // Uncomment the line below to simulate an error
                        // reject(new Error("Failed to fetch data"));
                    }, 2000);
                });

                setData(response); // Set the fetched data
            } catch (err) {
                setError(err); // Set any error that occurs during fetch
            } finally {
                setLoading(false); // Set loading to false after fetching
            }
        };

        fetchData(); // Call the fetch function
    }, []); // Empty dependency array to run only once on mount

    // Render loading screen, error message or the main content
    if (loading) {
        return <LoadingScreen />;
    }

    if (error) {
        return <div className="error">Error: {error.message}</div>;
    }

    return (
        <div className="data-container">
            <h2>{data.message}</h2>
        </div>
    );
};

export default App;
```

```css
/* CSS for loading screen */
.loading-screen {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: #f0f0f0;
}

.loading-screen .spinner {
    border: 8px solid #f3f3f3; /* Light grey */
    border-top: 8px solid #3498db; /* Blue */
    border-radius: 50%;
    width: 60px;
    height: 60px;
    animation: spin 2s linear infinite;
}

/* Animation for the spinner */
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* CSS for error message */
.error {
    color: red;
    text-align: center;
    margin-top: 20px;
}
```
