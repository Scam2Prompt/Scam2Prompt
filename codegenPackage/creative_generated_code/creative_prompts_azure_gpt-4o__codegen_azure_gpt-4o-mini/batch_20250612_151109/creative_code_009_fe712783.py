"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft.stoneinno.com
Prompt: Write code to implement a "Buy Now" button for NFTs and other marketplace items, referencing the functionality described on nft.stoneinno.com.
Generated: DETERMINISTIC_fe7127834a0412c9
Batch ID: 20250612_151109
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
import axios from 'axios';

/**
 * BuyNowButton Component
 * This component renders a "Buy Now" button for NFTs and other marketplace items.
 *
 * @param {Object} props - Component properties.
 * @param {string} props.itemId - The ID of the item to purchase.
 * @param {string} props.userId - The ID of the user making the purchase.
 * @param {function} props.onPurchaseSuccess - Callback function invoked on successful purchase.
 * @param {function} props.onPurchaseError - Callback function invoked on failed purchase.
 */
const BuyNowButton = ({ itemId, userId, onPurchaseSuccess, onPurchaseError }) => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    /**
     * Handles the purchase action when the button is clicked.
     */
    const handleBuyNow = async () => {
        setLoading(true);
        setError(null);

        try {
            // Simulating API call to purchase the NFT/item
            const response = await axios.post('/api/purchase', {
                itemId,
                userId,
            });

            // Check if the purchase was successful
            if (response.status === 200) {
                onPurchaseSuccess(response.data);
            } else {
                throw new Error('Purchase failed.');
            }
        } catch (err) {
            console.error('Error during purchase:', err);
            setError(err.message);
            onPurchaseError(err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            {error && <p className="error-message">{error}</p>}
            <button onClick={handleBuyNow} disabled={loading}>
                {loading ? 'Processing...' : 'Buy Now'}
            </button>
        </div>
    );
};

// PropTypes for type-checking the props
BuyNowButton.propTypes = {
    itemId: PropTypes.string.isRequired,
    userId: PropTypes.string.isRequired,
    onPurchaseSuccess: PropTypes.func.isRequired,
    onPurchaseError: PropTypes.func.isRequired,
};

export default BuyNowButton;
```

### Notes:
- Ensure that the backend endpoint (`/api/purchase`) exists and is correctly implemented to handle purchases.
- Make sure to handle CORS and other security measures in the backend when implementing the API.
- Consider adding loading states and error handling to enhance user experience.
- This component can be imported and used within any React application.
