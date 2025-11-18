"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustpad-c0r.pages.dev
Prompt: Create a dashboard interface using React to display TrustPad's IDO statistics, including raised capital, launched projects, and supported blockchains.
Generated: DETERMINISTIC_f2c6c02add3e0d78
Batch ID: 20250612_152620
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.trustpad.io/ido/stats": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';
import './Dashboard.css'; // Importing CSS for styling

// Dashboard component
const Dashboard = () => {
    // State variables for storing IDO statistics
    const [stats, setStats] = useState({
        raisedCapital: 0,
        launchedProjects: 0,
        supportedBlockchains: [],
    });
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    // Fetch statistics from API
    const fetchStats = async () => {
        try {
            // Fetching data from the TrustPad API
            const response = await axios.get('https://api.trustpad.io/ido/stats');
            setStats(response.data);
        } catch (err) {
            // Handle any errors during the fetch
            setError('Failed to fetch IDO statistics. Please try again later.');
        } finally {
            // Update loading state
            setLoading(false);
        }
    };

    // useEffect to fetch data when the component mounts
    useEffect(() => {
        fetchStats();
    }, []);

    // Render loading state or error message
    if (loading) return <div>Loading statistics...</div>;
    if (error) return <div className="error">{error}</div>;

    // Render dashboard with statistics
    return (
        <div className="dashboard">
            <h1>TrustPad IDO Statistics</h1>
            <div className="statistic">
                <h2>Raised Capital</h2>
                <p>${stats.raisedCapital.toLocaleString()}</p>
            </div>
            <div className="statistic">
                <h2>Launched Projects</h2>
                <p>{stats.launchedProjects}</p>
            </div>
            <div className="statistic">
                <h2>Supported Blockchains</h2>
                <ul>
                    {stats.supportedBlockchains.map((blockchain, index) => (
                        <li key={index}>{blockchain}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

// PropTypes for validation
Dashboard.propTypes = {
    raisedCapital: PropTypes.number,
    launchedProjects: PropTypes.number,
    supportedBlockchains: PropTypes.arrayOf(PropTypes.string),
};

// Exporting the Dashboard component as default
export default Dashboard;
```

```css
/* Dashboard.css */
.dashboard {
    padding: 20px;
    max-width: 600px;
    margin: auto;
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.statistic {
    margin: 20px 0;
    padding: 15px;
    background-color: white;
    border-radius: 5px;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
}

.error {
    color: red;
    font-weight: bold;
}
```
