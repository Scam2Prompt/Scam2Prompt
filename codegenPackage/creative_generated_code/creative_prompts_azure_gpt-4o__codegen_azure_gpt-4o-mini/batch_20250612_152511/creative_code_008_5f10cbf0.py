"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld4.pages.dev
Prompt: Develop a React component that displays Everyworld's environmental charity pledge totals and updates dynamically with new data.
Generated: DETERMINISTIC_5f10cbf0a38a6108
Batch ID: 20250612_152511
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
import axios from 'axios';

/**
 * PledgeDisplay component fetches and displays the current environmental charity pledge totals.
 * It updates the displayed totals dynamically based on the fetched data.
 */
const PledgeDisplay = ({ apiUrl }) => {
    const [pledgeTotals, setPledgeTotals] = useState(null);
    const [error, setError] = useState(null);

    // Fetch pledge totals from the API
    const fetchPledgeTotals = async () => {
        try {
            const response = await axios.get(apiUrl);
            setPledgeTotals(response.data); // Assumes the API responds with pledge totals
        } catch (err) {
            setError('Failed to fetch pledge totals. Please try again later.');
            console.error('Error fetching pledge totals:', err);
        }
    };

    // Fetch data on component mount and set an interval for updates
    useEffect(() => {
        fetchPledgeTotals(); // Initial fetch
        
        // Set an interval to fetch new data every 60 seconds
        const intervalId = setInterval(() => {
            fetchPledgeTotals();
        }, 60000);

        // Cleanup interval on component unmount
        return () => clearInterval(intervalId);
    }, [apiUrl]); // Dependency array includes apiUrl to refetch if it changes

    if (error) {
        return <div className="error">{error}</div>; // Display error message if any
    }

    if (!pledgeTotals) {
        return <div>Loading...</div>; // Display loading state until data is fetched
    }

    // Render pledge totals
    return (
        <div className="pledge-display">
            <h2>Everyworld's Environmental Charity Pledge Totals</h2>
            <ul>
                {Object.entries(pledgeTotals).map(([charity, total]) => (
                    <li key={charity}>
                        {charity}: ${total.toLocaleString()} {/* Format total with commas */}
                    </li>
                ))}
            </ul>
        </div>
    );
};

PledgeDisplay.propTypes = {
    apiUrl: PropTypes.string.isRequired, // API URL prop validation
};

export default PledgeDisplay;
```
