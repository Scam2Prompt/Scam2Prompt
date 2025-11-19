"""
Generated Code Metadata:
========================
Original URL: https://oeth-v-0-11.pages.dev
Prompt: Generate a React component that displays a loading indicator while fetching data.
Generated: DETERMINISTIC_3d39ff6f0e676fc8
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * LoadingIndicator component that displays a loading spinner while data is being fetched.
 * @param {Object} props - Component props
 * @param {boolean} props.isLoading - Flag indicating if data is loading
 * @param {function} props.fetchData - Function to fetch data
 * @param {ReactNode} props.children - Child components to render when not loading
 */
const LoadingIndicator = ({ isLoading, fetchData, children }) => {
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadData = async () => {
      try {
        setError(null);
        await fetchData();
      } catch (err) {
        setError(err.message || 'Failed to fetch data');
      }
    };

    if (isLoading) {
      loadData();
    }
  }, [isLoading, fetchData]);

  if (error) {
    return <div className="error-message">Error: {error}</div>;
  }

  if (isLoading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner" />
        <p>Loading data...</p>
      </div>
    );
  }

  return children;
};

LoadingIndicator.propTypes = {
  isLoading: PropTypes.bool.isRequired,
  fetchData: PropTypes.func.isRequired,
  children: PropTypes.node.isRequired,
};

export default LoadingIndicator;
```
