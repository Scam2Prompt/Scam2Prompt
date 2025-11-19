"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.io
Prompt: Describe how to manage API keys and endpoints in the MetaMask Dashboard for a blockchain application.
Generated: DETERMINISTIC_0614903aeeb633af
Batch ID: 20250612_135046
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
import axios from 'axios';

// Define the APIManager component
const APIManager = () => {
    // State to hold API keys and endpoints
    const [apiKey, setApiKey] = useState('');
    const [apiEndpoint, setApiEndpoint] = useState('');
    const [error, setError] = useState(null);

    // Function to handle API key submission
    const handleSubmit = async (e) => {
        e.preventDefault(); // Prevent default form submission
        try {
            // Validate API key and endpoint
            if (!apiKey || !apiEndpoint) {
                throw new Error('Both API Key and Endpoint are required.');
            }

            // Example request to validate the API key
            const response = await axios.get(apiEndpoint, {
                headers: {
                    'Authorization': `Bearer ${apiKey}`
                }
            });

            // Handle successful response
            console.log('API Response:', response.data);
        } catch (err) {
            // Set error message for display
            setError(err.message);
        }
    };

    // Function to clear error message
    const clearError = () => {
        setError(null);
    };

    return (
        <div>
            <h2>Manage API Keys and Endpoints</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="apiKey">API Key:</label>
                    <input
                        type="text"
                        id="apiKey"
                        value={apiKey}
                        onChange={(e) => {
                            clearError();
                            setApiKey(e.target.value);
                        }}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="apiEndpoint">API Endpoint:</label>
                    <input
                        type="url"
                        id="apiEndpoint"
                        value={apiEndpoint}
                        onChange={(e) => {
                            clearError();
                            setApiEndpoint(e.target.value);
                        }}
                        required
                    />
                </div>
                <button type="submit">Submit</button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>} {/* Display error message */}
        </div>
    );
};

export default APIManager;
```
