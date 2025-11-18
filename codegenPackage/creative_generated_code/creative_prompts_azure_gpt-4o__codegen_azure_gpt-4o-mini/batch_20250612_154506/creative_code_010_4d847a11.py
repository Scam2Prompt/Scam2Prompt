"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Create a React component for displaying live-streamed lottery results, as described in VZ99's lottery hall feature.
Generated: DETERMINISTIC_4d847a1113299745
Batch ID: 20250612_154506
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
import './LotteryResults.css'; // Importing CSS for styling

/**
 * LotteryResults Component
 * This component fetches and displays live-streamed lottery results.
 * 
 * Props:
 * - apiEndpoint: The endpoint from which to fetch lottery results.
 * 
 * State:
 * - results: Holds the current lottery results fetched from the API.
 * - error: Holds any error messages during data fetching.
 * - loading: Indicates if the data is currently being loaded.
 */
const LotteryResults = ({ apiEndpoint }) => {
  const [results, setResults] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchLotteryResults = async () => {
      try {
        setLoading(true);
        const response = await fetch(apiEndpoint);

        // Check if the response is ok (status within the range 200-299)
        if (!response.ok) {
          throw new Error(`Error fetching data: ${response.statusText}`);
        }

        const data = await response.json();
        setResults(data.results); // Assuming the data has a `results` field
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    // Fetch results every 10 seconds
    const intervalId = setInterval(fetchLotteryResults, 10000);
    
    // Initial fetch
    fetchLotteryResults();

    // Cleanup interval on component unmount
    return () => clearInterval(intervalId);
  }, [apiEndpoint]);

  // Render loading state
  if (loading) {
    return <div className="loading">Loading lottery results...</div>;
  }

  // Render error state
  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  // Render results
  return (
    <div className="lottery-results">
      <h2>Live Lottery Results</h2>
      <ul>
        {results.map((result, index) => (
          <li key={index}>
            <span className="result-number">{result.number}</span>
            <span className="result-time">{result.time}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

// Prop validation
LotteryResults.propTypes = {
  apiEndpoint: PropTypes.string.isRequired,
};

// Export the component
export default LotteryResults;
```

**CSS (LotteryResults.css)**:
```css
.lottery-results {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.loading {
  font-size: 1.2em;
  color: #007bff;
}

.error {
  color: red;
  font-weight: bold;
}

.result-number {
  font-size: 1.5em;
  font-weight: bold;
}

.result-time {
  font-size: 1em;
  color: #666;
}
```
