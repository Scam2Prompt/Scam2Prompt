"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-v-0-10.pages.dev
Prompt: What libraries can I use to manage loading states in React applications effectively?
Generated: DETERMINISTIC_b40759b29f7b79a6
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';

// Custom Hook for managing loading state
const useLoading = (asyncFunction) => {
    // State to track loading status
    const [loading, setLoading] = useState(false);
    // State to track error
    const [error, setError] = useState(null);
    // State to hold the result
    const [data, setData] = useState(null);

    // Function to execute the async task
    const execute = async () => {
        setLoading(true);
        setError(null);
        try {
            const result = await asyncFunction();
            setData(result);
        } catch (err) {
            setError(err.message || 'An error occurred');
        } finally {
            setLoading(false);
        }
    };

    return { loading, error, data, execute };
};

// Example component using the useLoading hook
const DataFetcher = () => {
    // Simulated async function to fetch data
    const fetchData = async () => {
        // Simulating network delay
        return new Promise((resolve) => {
            setTimeout(() => {
                resolve("Fetched Data");
            }, 2000);
        });
    };

    // Using the custom loading hook
    const { loading, error, data, execute } = useLoading(fetchData);

    // Handle component render based on loading state
    return (
        <div>
            <button onClick={execute}>Fetch Data</button>
            {loading && <p>Loading...</p>}
            {error && <p>Error: {error}</p>}
            {data && <p>Data: {data}</p>}
        </div>
    );
};

// Main App component
const App = () => {
    return (
        <div>
            <h1>React Loading State Example</h1>
            <DataFetcher />
        </div>
    );
};

// Export the App component
export default App;
```
