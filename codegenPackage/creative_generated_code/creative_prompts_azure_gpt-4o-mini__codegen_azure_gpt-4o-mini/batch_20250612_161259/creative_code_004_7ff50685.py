"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-badge.vercel.app
Prompt: How do I utilize SuiBadge's features to enhance user engagement in my Sui Connect Wallet app?
Generated: DETERMINISTIC_7ff50685f23368a5
Batch ID: 20250612_161259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import React, { useEffect, useState } from 'react';
import { SuiBadge } from 'sui-badge-sdk'; // Make sure to install the Sui Badge SDK
import { useWallet } from 'sui-connect-wallet'; // Import the Sui Connect Wallet hook

// Define the BadgeComponent
const BadgeComponent = () => {
    const { wallet, connect, disconnect } = useWallet(); // Get wallet functions
    const [badges, setBadges] = useState([]); // State to store user badges
    const [loading, setLoading] = useState(true); // State for loading status
    const [error, setError] = useState(null); // State to handle errors

    // Function to fetch badges for the connected user
    const fetchBadges = async () => {
        try {
            setLoading(true); // Set loading state
            if (!wallet) throw new Error("Wallet not connected."); // Error if no wallet is connected

            // Fetch badges from SuiBadge SDK
            const userBadges = await SuiBadge.getUserBadges(wallet.address);
            setBadges(userBadges); // Update state with fetched badges
        } catch (err) {
            console.error("Error fetching badges:", err); // Log error for debugging
            setError(err.message); // Update error state
        } finally {
            setLoading(false); // Reset loading state
        }
    };

    // Effect to fetch badges when wallet changes
    useEffect(() => {
        if (wallet) {
            fetchBadges(); // Fetch badges if wallet is connected
        } else {
            setBadges([]); // Reset badges if wallet is disconnected
        }
    }, [wallet]);

    // Rendering loading, error, or badges
    return (
        <div className="badge-component">
            <h2>User Badges</h2>
            {loading && <p>Loading badges...</p>} {/* Loading indicator */}
            {error && <p style={{ color: 'red' }}>{error}</p>} {/* Error message */}
            <ul>
                {badges.length > 0 ? (
                    badges.map((badge, index) => (
                        <li key={index}>
                            <img src={badge.image} alt={badge.name} /> {/* Badge image */}
                            <span>{badge.name}</span> {/* Badge name */}
                        </li>
                    ))
                ) : (
                    <p>No badges found.</p> // Message if no badges exist
                )}
            </ul>
            <button onClick={connect}>Connect Wallet</button> {/* Button to connect wallet */}
            <button onClick={disconnect}>Disconnect Wallet</button> {/* Button to disconnect wallet */}
        </div>
    );
};

// Export the BadgeComponent for use in other parts of the app
export default BadgeComponent;
```
