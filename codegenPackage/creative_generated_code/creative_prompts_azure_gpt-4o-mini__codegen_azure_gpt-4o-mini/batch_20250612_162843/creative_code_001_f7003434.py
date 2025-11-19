"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pikmisobakilive.com
Prompt: Write a code snippet to create a button for users to claim rewards after winning a free spin in a TON-based application.
Generated: DETERMINISTIC_f7003434c4a72b63
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import PropTypes from 'prop-types';

// Button component for claiming rewards
const ClaimRewardButton = ({ onClaimReward }) => {
    // State to manage loading status and error messages
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    // Handler for button click event
    const handleClaimReward = async () => {
        setIsLoading(true);
        setError(null); // Reset error message

        try {
            // Simulate an API call to claim the reward
            const response = await onClaimReward();
            
            // Check if response is successful
            if (!response.success) {
                throw new Error(response.message || 'Failed to claim reward');
            }

            // Notify user of successful claim (could be replaced with a toast notification)
            alert('Reward claimed successfully!');
        } catch (err) {
            // Set error message to be displayed
            setError(err.message);
        } finally {
            // Reset loading state
            setIsLoading(false);
        }
    };

    return (
        <div>
            <button 
                onClick={handleClaimReward} 
                disabled={isLoading} 
                className="claim-reward-button"
            >
                {isLoading ? 'Claiming...' : 'Claim Reward'}
            </button>
            {error && <p className="error-message">{error}</p>}
        </div>
    );
};

// Prop type validation
ClaimRewardButton.propTypes = {
    onClaimReward: PropTypes.func.isRequired,
};

export default ClaimRewardButton;
```
