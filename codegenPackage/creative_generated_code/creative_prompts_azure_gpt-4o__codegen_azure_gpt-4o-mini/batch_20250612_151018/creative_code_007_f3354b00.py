"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-44--gracious-swanson-bcc8c1.netlify.app
Prompt: Write a React component that fetches data from an API and displays it, following Tim Mansell's coding style.
Generated: DETERMINISTIC_f3354b0033f69c84
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';

/**
 * FetchDataComponent fetches data from a provided API endpoint
 * and displays the results in a simple list format.
 * 
 * @param {string} apiUrl - The URL of the API to fetch data from.
 */
const FetchDataComponent = ({ apiUrl }) => {
    // State to hold fetched data and loading state
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Fetch data from the API when the component mounts
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(apiUrl);
                
                // Check if the response is OK
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const result = await response.json();
                setData(result);
            } catch (err) {
                // Catch and set any errors that occur during fetch
                setError(err.message);
            } finally {
                // Set loading to false after fetching data
                setLoading(false);
            }
        };

        fetchData();
    }, [apiUrl]);

    // Render loading state, error state, or the fetched data
    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    return (
        <div>
            <h2>Fetched Data</h2>
            <ul>
                {data.map((item, index) => (
                    <li key={index}>{JSON.stringify(item)}</li>
                ))}
            </ul>
        </div>
    );
};

FetchDataComponent.propTypes = {
    apiUrl: PropTypes.string.isRequired,
};

export default FetchDataComponent;
```
