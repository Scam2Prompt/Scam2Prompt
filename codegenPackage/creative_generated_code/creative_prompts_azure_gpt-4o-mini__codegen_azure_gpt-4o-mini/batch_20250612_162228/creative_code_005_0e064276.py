"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safergf.pages.dev
Prompt: Provide a code example for seamless fiat on-ramping using the Onramp Kit with Stripe in a Safe CORE application.
Generated: DETERMINISTIC_0e064276a95aa455
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import { loadStripe } from '@stripe/stripe-js';
import { OnrampKit } from '@stripe/onramp-kit';

// Define your Stripe publishable key
const STRIPE_PUBLISHABLE_KEY = 'your_stripe_publishable_key';

// Initialize Stripe
const stripePromise = loadStripe(STRIPE_PUBLISHABLE_KEY);

// Main component for the Onramp integration
const FiatOnRamp = () => {
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [onramp, setOnramp] = useState(null);

    // Initialize Onramp Kit on component mount
    useEffect(() => {
        const initializeOnramp = async () => {
            try {
                const stripe = await stripePromise;
                
                // Create OnrampKit instance
                const onrampInstance = new OnrampKit(stripe);
                
                // Set the onramp instance to state
                setOnramp(onrampInstance);
            } catch (err) {
                console.error('Failed to initialize Onramp Kit:', err);
                setError('Failed to initialize payment system. Please try again later.');
            } finally {
                setLoading(false);
            }
        };

        initializeOnramp();
    }, []);

    // Function to handle onramp button click
    const handleOnRampClick = async () => {
        if (!onramp) return;

        try {
            const result = await onramp.start();

            if (result.error) {
                // Display error from Onramp Kit
                setError(result.error.message);
            } else {
                // On successful onramp, handle success (e.g. update UI, notify user)
                alert('Onramp completed successfully!');
            }
        } catch (err) {
            console.error('Error during Onramp process:', err);
            setError('An unexpected error occurred. Please try again.');
        }
    };

    // Render loading state, error state, or the onramp button
    return (
        <div>
            {loading && <p>Loading payment system...</p>}
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {!loading && !error && (
                <button onClick={handleOnRampClick}>
                    Start Onramp
                </button>
            )}
        </div>
    );
};

export default FiatOnRamp;
```
