"""
Generated Code Metadata:
========================
Original URL: https://iensooa.pages.dev
Prompt: Generate an example of how to implement opt-in notification preferences for a web3 app using Web3Inbox and standard Sign In With Ethereum (SIWE) messages.
Generated: DETERMINISTIC_e76e870535c7151f
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { SignInWithEthereum } from 'siwe';
import Web3Inbox from 'web3-inbox';

// Define the NotificationPreferences component
const NotificationPreferences = () => {
    // State variables for user address and notification preferences
    const [userAddress, setUserAddress] = useState(null);
    const [preferences, setPreferences] = useState({
        email: false,
        sms: false,
        push: false,
    });

    // Initialize Web3Inbox
    const inbox = new Web3Inbox();

    // Function to handle Ethereum sign-in
    const handleSignIn = async () => {
        try {
            // Request account access
            const provider = new ethers.providers.Web3Provider(window.ethereum);
            await provider.send("eth_requestAccounts", []);
            const signer = provider.getSigner();
            const address = await signer.getAddress();
            setUserAddress(address);

            // Create SIWE message
            const message = new SignInWithEthereum({
                domain: window.location.hostname,
                address: address,
                statement: "Sign in to manage your notification preferences.",
                uri: window.location.origin,
                version: '1',
                chainId: 1, // Mainnet
            });

            // Sign the message
            const signature = await signer.signMessage(message.prepareMessage());
            await inbox.signIn(address, signature);
        } catch (error) {
            console.error("Sign-in error:", error);
            alert("Failed to sign in. Please try again.");
        }
    };

    // Function to handle preference changes
    const handlePreferenceChange = (event) => {
        const { name, checked } = event.target;
        setPreferences((prev) => ({
            ...prev,
            [name]: checked,
        }));
    };

    // Function to save preferences
    const savePreferences = async () => {
        if (!userAddress) {
            alert("You must be signed in to save preferences.");
            return;
        }

        try {
            // Save preferences to the backend or blockchain
            await inbox.savePreferences(userAddress, preferences);
            alert("Preferences saved successfully!");
        } catch (error) {
            console.error("Error saving preferences:", error);
            alert("Failed to save preferences. Please try again.");
        }
    };

    // Effect to load user preferences on sign-in
    useEffect(() => {
        const loadPreferences = async () => {
            if (userAddress) {
                try {
                    const userPreferences = await inbox.getPreferences(userAddress);
                    setPreferences(userPreferences);
                } catch (error) {
                    console.error("Error loading preferences:", error);
                }
            }
        };
        loadPreferences();
    }, [userAddress]);

    return (
        <div>
            <h1>Notification Preferences</h1>
            <button onClick={handleSignIn}>Sign In with Ethereum</button>
            <form>
                <label>
                    <input
                        type="checkbox"
                        name="email"
                        checked={preferences.email}
                        onChange={handlePreferenceChange}
                    />
                    Email Notifications
                </label>
                <label>
                    <input
                        type="checkbox"
                        name="sms"
                        checked={preferences.sms}
                        onChange={handlePreferenceChange}
                    />
                    SMS Notifications
                </label>
                <label>
                    <input
                        type="checkbox"
                        name="push"
                        checked={preferences.push}
                        onChange={handlePreferenceChange}
                    />
                    Push Notifications
                </label>
                <button type="button" onClick={savePreferences}>
                    Save Preferences
                </button>
            </form>
        </div>
    );
};

export default NotificationPreferences;
```
