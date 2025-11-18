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

```jsx
// Tim Mansell's coding style emphasizes clean, modular, and readable code.
// This React component fetches data from an API and displays it in a production-ready manner.

import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types'; // For type checking

// Functional Component to fetch and display data
const DataFetcher = ({ apiUrl }) => {
  // State to manage fetched data, loading status, and errors
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  // Effect Hook to fetch data when the component mounts or apiUrl changes
  useEffect(() => {
    const fetchData = async () => {
      try {
        setIsLoading(true); // Set loading state
        setError(null); // Reset error state

        const response = await fetch(apiUrl);

        // Handle HTTP errors
        if (!response.ok) {
          throw new Error(`HTTP Error: ${response.status} ${response.statusText}`);
        }

        const result = await response.json(); // Parse JSON response
        setData(result); // Update data state
      } catch (err) {
        setError(err.message); // Update error state
      } finally {
        setIsLoading(false); // Reset loading state
      }
    };

    fetchData();
  }, [apiUrl]); // Dependency array ensures re-fetching on apiUrl changes

  // Render loading, error, or data states
  return (
    <div>
      {isLoading && <p>Loading...</p>}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      {!isLoading && !error && (
        <ul>
          {/* Render data items if available */}
          {data.map((item, index) => (
            <li key={index}>{JSON.stringify(item)}</li>
          ))}
        </ul>
      )}
    </div>
  );
};

// Prop type validation for the component
DataFetcher.propTypes = {
  apiUrl: PropTypes.string.isRequired, // apiUrl must be a string and is required
};

export default DataFetcher;
```
