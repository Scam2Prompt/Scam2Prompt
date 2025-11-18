"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mystrikingly.com
Prompt: Generate code for adding coupon functionality to an e-commerce store using Strikingly's platform.
Generated: DETERMINISTIC_9834d9415ff5b2ea
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { useState } from 'react';
import axios from 'axios';

// Coupon Component
const Coupon = () => {
    // State to hold coupon code and response message
    const [couponCode, setCouponCode] = useState('');
    const [message, setMessage] = useState('');

    // Handler for coupon code change
    const handleInputChange = (event) => {
        setCouponCode(event.target.value);
    };

    // Function to validate and apply coupon
    const applyCoupon = async () => {
        try {
            // Check if coupon code is not empty
            if (!couponCode.trim()) {
                throw new Error('Coupon code cannot be empty.');
            }

            // Send request to the server to validate the coupon code
            const response = await axios.post('/api/apply-coupon', { code: couponCode });

            // Check if the response is successful
            if (response.data.success) {
                setMessage(`Coupon applied successfully! Discount: ${response.data.discount}`);
            } else {
                setMessage(`Failed to apply coupon: ${response.data.message}`);
            }
        } catch (error) {
            // Handle error and update the message state
            console.error('Error applying coupon:', error);
            setMessage(`Error: ${error.message}`);
        }
    };

    return (
        <div className="coupon-container">
            <h2>Apply Coupon</h2>
            <input
                type="text"
                placeholder="Enter your coupon code"
                value={couponCode}
                onChange={handleInputChange}
                className="coupon-input"
            />
            <button onClick={applyCoupon} className="apply-button">
                Apply Coupon
            </button>
            {message && <p className="message">{message}</p>}
        </div>
    );
};

export default Coupon;

// Server-side API endpoint (Node.js with Express)

// Import necessary libraries
import express from 'express';

const router = express.Router();

// Mock coupon data (In a real application, this would be a database lookup)
const coupons = {
    'SAVE10': { discount: '10%', valid: true },
    'FREESHIP': { discount: 'Free Shipping', valid: true },
};

// API endpoint to apply coupon
router.post('/apply-coupon', (req, res) => {
    const { code } = req.body;

    // Validate input
    if (!code) {
        return res.status(400).json({ success: false, message: 'Coupon code is required.' });
    }

    // Check if coupon exists and is valid
    if (coupons[code]) {
        return res.json({ success: true, discount: coupons[code].discount });
    } else {
        return res.status(404).json({ success: false, message: 'Coupon code not valid.' });
    }
});

export default router;
```

This code provides a simple React component for applying a coupon code and a corresponding Express API endpoint to validate the coupon code. Both parts include error handling and user feedback.
