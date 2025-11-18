"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disneypinnacel.web.app
Prompt: Develop a React component for displaying Disney Pinnacle NFT minting status, including waitlist eligibility and minting progress.
Generated: DETERMINISTIC_946165dfbcfd1459
Batch ID: 20250612_153526
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
import axios from 'axios';

// Define the MintingStatus component
const MintingStatus = ({ userId, apiEndpoint }) => {
  // State variables
  const [isLoading, setIsLoading] = useState(true);
  const [isEligible, setIsEligible] = useState(false);
  const [mintingProgress, setMintingProgress] = useState(0);
  const [error, setError] = useState(null);

  // Fetch minting status data from the server
  useEffect(() => {
    const fetchMintingStatus = async () => {
      setIsLoading(true); // Start loading
      setError(null); // Clear previous errors

      try {
        const response = await axios.get(`${apiEndpoint}/minting-status`, {
          params: { userId },
        });

        // Update state with API response
        setIsEligible(response.data.isEligible || false);
        setMintingProgress(response.data.mintingProgress || 0);
      } catch (err) {
        setError(err.message || 'An error occurred while fetching minting status.');
      } finally {
        setIsLoading(false); // Stop loading
      }
    };

    fetchMintingStatus();
  }, [userId, apiEndpoint]);

  // Render loading state
  if (isLoading) {
    return <div>Loading minting status...</div>;
  }

  // Render error state
  if (error) {
    return <div className="error-message">Error: {error}</div>;
  }

  // Render minting status details
  return (
    <div className="minting-status">
      <h1>Disney Pinnacle NFT Minting Status</h1>
      <p>
        <strong>Waitlist Eligibility:</strong> {isEligible ? 'Eligible' : 'Not Eligible'}
      </p>
      <p>
        <strong>Minting Progress:</strong> {mintingProgress}%
      </p>
      {/* Conditionally show progress bar if minting has started */}
      {mintingProgress > 0 && (
        <div className="progress-bar">
          <div
            className="progress-bar-fill"
            style={{ width: `${mintingProgress}%` }}
          ></div>
        </div>
      )}
    </div>
  );
};

// Define PropTypes for the component
MintingStatus.propTypes = {
  userId: PropTypes.string.isRequired, // User ID for fetching minting status
  apiEndpoint: PropTypes.string.isRequired, // API base URL
};

// Export the MintingStatus component
export default MintingStatus;

/* CSS for progress bar (add to your CSS file or inline styles)
.progress-bar {
  background-color: #e0e0e0;
  height: 20px;
  border-radius: 10px;
  overflow: hidden;
}

.progress-bar-fill {
  background-color: #4caf50;
  height: 100%;
  transition: width 0.4s ease;
}
*/
```
