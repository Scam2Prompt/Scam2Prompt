"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-v-0-11.pages.dev
Prompt: Write a code snippet for a React app that shows a "Loading..." message during data retrieval.
Generated: DETERMINISTIC_620850942630d842
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState, useEffect } from 'react';

const DataFetchingComponent = () => {
  // State to manage loading and fetched data
  const [isLoading, setIsLoading] = useState(true);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Simulate data fetching with a delay
    const fetchData = async () => {
      try {
        setIsLoading(true); // Start loading
        setError(null); // Reset error state
        
        // Replace this with actual API call, e.g., fetch('/api/data')
        const simulatedFetch = new Promise((resolve) => {
          setTimeout(() => resolve({ message: 'Data successfully retrieved!' }), 2000);
        });
        const result = await simulatedFetch;
        
        setData(result); // Set the fetched data
      } catch (err) {
        // Handle any potential errors
        setError('Failed to fetch data');
      } finally {
        setIsLoading(false); // End loading
      }
    };

    fetchData();
  }, []); // Empty dependency array ensures this runs only once on component mount

  // Render logic
  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h1>Fetched Data:</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

export default DataFetchingComponent;
```
