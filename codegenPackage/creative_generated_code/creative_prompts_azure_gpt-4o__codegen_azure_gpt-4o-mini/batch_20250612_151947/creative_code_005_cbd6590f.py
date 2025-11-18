"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegraph.live
Prompt: Create a dashboard using React.js to visualize user progress and rewards across the tiers (M1-M8) as described on https://thegraph.live.
Generated: DETERMINISTIC_cbd6590f37ec1932
Batch ID: 20250612_151947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.thegraph.com/subgraphs/name/your-subgraph-name": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';
import './Dashboard.css'; // Custom CSS for the dashboard

// Define the Dashboard component
const Dashboard = () => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Fetch user progress and rewards data from the API
    const fetchData = async () => {
        try {
            const response = await axios.get('https://api.thegraph.com/subgraphs/name/your-subgraph-name');
            setData(response.data); // Assuming response.data contains the relevant information
        } catch (err) {
            setError('Error fetching data. Please try again later.');
            console.error('Data fetching error:', err);
        } finally {
            setLoading(false);
        }
    };

    // Use useEffect to fetch data on component mount
    useEffect(() => {
        fetchData();
    }, []);

    // Prepare chart data and options
    const prepareChartData = () => {
        if (!data.length) return {};

        const labels = data.map(item => item.tier); // Assuming 'tier' is a property in data
        const progressData = data.map(item => item.progress); // Assuming 'progress' is a property in data
        const rewardsData = data.map(item => item.rewards); // Assuming 'rewards' is a property in data

        return {
            labels,
            datasets: [
                {
                    label: 'User Progress',
                    data: progressData,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    fill: false,
                },
                {
                    label: 'Rewards',
                    data: rewardsData,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    fill: false,
                }
            ]
        };
    };

    // Render loading state or error message
    if (loading) return <div>Loading...</div>;
    if (error) return <div className="error">{error}</div>;

    return (
        <div className="dashboard">
            <h1>User Progress and Rewards Dashboard</h1>
            <Line data={prepareChartData()} options={{
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                    },
                },
            }} />
        </div>
    );
};

// Export the Dashboard component
export default Dashboard;
```

```css
/* Dashboard.css */
.dashboard {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.dashboard h1 {
    text-align: center;
    color: #333;
}

.error {
    color: red;
    text-align: center;
}
```
