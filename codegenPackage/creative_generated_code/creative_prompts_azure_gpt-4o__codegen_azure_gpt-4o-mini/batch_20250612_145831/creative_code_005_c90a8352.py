"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartdefi-feg.pages.dev
Prompt: Write a React component that integrates with the FEG Migration Tool and displays the user's current FEG Stake V2 balance, along with a button to initiate migration to V3.
Generated: DETERMINISTIC_c90a83524d8d0b75
Batch ID: 20250612_145831
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

// Define a functional component for FEG Migration Tool
const FEGMigration = ({ apiUrl, userId }) => {
    // State to hold the user's FEG Stake V2 balance
    const [stakeV2Balance, setStakeV2Balance] = useState(0);
    // State to manage loading state
    const [loading, setLoading] = useState(true);
    // State to manage error messages
    const [error, setError] = useState(null);

    // Fetch the user's FEG Stake V2 balance from the API
    const fetchStakeBalance = async () => {
        try {
            const response = await fetch(`${apiUrl}/stake/v2/balance/${userId}`);
            if (!response.ok) {
                throw new Error(`Error: ${response.statusText}`);
            }
            const data = await response.json();
            setStakeV2Balance(data.balance); // Assuming the response contains the balance
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    // Function to initiate migration to V3
    const handleMigration = async () => {
        try {
            const response = await fetch(`${apiUrl}/stake/migrate/${userId}`, {
                method: 'POST',
            });
            if (!response.ok) {
                throw new Error(`Migration failed: ${response.statusText}`);
            }
            const result = await response.json();
            alert(`Migration successful: ${result.message}`);
        } catch (err) {
            alert(`Migration failed: ${err.message}`);
        }
    };

    // Use effect to fetch the balance on component mount
    useEffect(() => {
        fetchStakeBalance();
    }, [apiUrl, userId]); // Dependency array ensures it runs on change

    // Render loading state, error messages, or the balance and migration button
    return (
        <div>
            {loading && <p>Loading balance...</p>}
            {error && <p>Error: {error}</p>}
            {!loading && !error && (
                <>
                    <h2>Your FEG Stake V2 Balance: {stakeV2Balance}</h2>
                    <button onClick={handleMigration}>Migrate to V3</button>
                </>
            )}
        </div>
    );
};

// Prop types for validation
FEGMigration.propTypes = {
    apiUrl: PropTypes.string.isRequired, // URL of the API to fetch data
    userId: PropTypes.string.isRequired,  // User ID for fetching the balance
};

export default FEGMigration;
```
