"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellybabiesnft.web.app
Prompt: Write a React component that displays the total claimed $Jelly tokens and percentage of claimed tokens, based on the "Total Claimed" and "% of Claimed" stats shown on the Jelly Babies NFT webpage.
Generated: DETERMINISTIC_8c2c68d7b6872660
Batch ID: 20250612_142645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

// A component to display $Jelly token statistics: total claimed and percentage claimed
const JellyTokenStats = ({ fetchStats }) => {
  // State variables for storing stats
  const [totalClaimed, setTotalClaimed] = useState(0);
  const [percentageClaimed, setPercentageClaimed] = useState(0);
  const [error, setError] = useState(null);

  // Fetch stats when the component mounts
  useEffect(() => {
    const fetchData = async () => {
      try {
        setError(null); // Reset error before fetching data
        const stats = await fetchStats(); // Fetch stats from provided function
        if (stats && stats.totalClaimed !== undefined && stats.percentageClaimed !== undefined) {
          setTotalClaimed(stats.totalClaimed); // Update total claimed state
          setPercentageClaimed(stats.percentageClaimed); // Update percentage claimed state
        } else {
          throw new Error('Invalid stats data'); // Throw error if data is invalid
        }
      } catch (err) {
        setError(err.message); // Handle errors by setting error state
      }
    };

    fetchData(); // Execute data fetch
  }, [fetchStats]);

  return (
    <div className="jelly-token-stats">
      {/* Display error message if there's an error */}
      {error ? (
        <div className="error">
          <p>Error: {error}</p>
        </div>
      ) : (
        <div className="stats">
          <h2>$Jelly Token Stats</h2>
          <p>Total Claimed: {totalClaimed}</p>
          <p>Percentage Claimed: {percentageClaimed}%</p>
        </div>
      )}
    </div>
  );
};

// PropTypes for ensuring proper props are passed
JellyTokenStats.propTypes = {
  fetchStats: PropTypes.func.isRequired, // Function to fetch stats, required prop
};

export default JellyTokenStats;

/**
 * Example usage:
 * 
 * import React from 'react';
 * import JellyTokenStats from './JellyTokenStats';
 * 
 * const fetchStats = async () => {
 *   // Mock fetching data from the Jelly Babies NFT webpage API
 *   return {
 *     totalClaimed: 100000,
 *     percentageClaimed: 75,
 *   };
 * };
 * 
 * const App = () => (
 *   <div>
 *     <JellyTokenStats fetchStats={fetchStats} />
 *   </div>
 * );
 * 
 * export default App;
 */
```
