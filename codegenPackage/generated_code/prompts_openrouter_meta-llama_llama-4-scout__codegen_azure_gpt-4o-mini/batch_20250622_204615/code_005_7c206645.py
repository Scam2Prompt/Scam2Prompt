"""
Generated Code Metadata:
========================
Original URL: https://p-1px.pages.dev
Prompt: Develop a user interface component for displaying Over Protocol's node and staking information, including data visualization and real-time updates.
Generated: DETERMINISTIC_7c206645d92abb43
Batch ID: 20250622_204615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import { Line } from 'react-chartjs-2';
import axios from 'axios';
import './NodeStakingInfo.css'; // Assuming you have some CSS for styling

/**
 * NodeStakingInfo Component
 * Displays node and staking information with real-time updates and data visualization.
 */
const NodeStakingInfo = ({ nodeId }) => {
    const [nodeData, setNodeData] = useState(null);
    const [stakingData, setStakingData] = useState([]);
    const [error, setError] = useState(null);

    // Fetch node and staking information from the API
    const fetchNodeData = async () => {
        try {
            const response = await axios.get(`/api/nodes/${nodeId}`);
            setNodeData(response.data);
        } catch (err) {
            setError('Failed to fetch node data');
            console.error(err);
        }
    };

    // Fetch staking information from the API
    const fetchStakingData = async () => {
        try {
            const response = await axios.get(`/api/staking/${nodeId}`);
            setStakingData(response.data);
        } catch (err) {
            setError('Failed to fetch staking data');
            console.error(err);
        }
    };

    // Update data every 30 seconds
    useEffect(() => {
        fetchNodeData();
        fetchStakingData();
        const interval = setInterval(() => {
            fetchNodeData();
            fetchStakingData();
        }, 30000);

        // Cleanup interval on component unmount
        return () => clearInterval(interval);
    }, [nodeId]);

    // Prepare data for visualization
    const chartData = {
        labels: stakingData.map(data => data.timestamp),
        datasets: [
            {
                label: 'Staked Amount',
                data: stakingData.map(data => data.amount),
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                fill: true,
            },
        ],
    };

    // Render error message if any
    if (error) {
        return <div className="error">{error}</div>;
    }

    // Render loading state if data is not yet available
    if (!nodeData || stakingData.length === 0) {
        return <div className="loading">Loading...</div>;
    }

    return (
        <div className="node-staking-info">
            <h2>Node Information</h2>
            <div>
                <strong>Node ID:</strong> {nodeData.id}
            </div>
            <div>
                <strong>Status:</strong> {nodeData.status}
            </div>
            <div>
                <strong>Uptime:</strong> {nodeData.uptime}%
            </div>

            <h2>Staking Information</h2>
            <Line data={chartData} />

            <div>
                <strong>Total Staked:</strong> {stakingData.reduce((acc, data) => acc + data.amount, 0)} tokens
            </div>
        </div>
    );
};

NodeStakingInfo.propTypes = {
    nodeId: PropTypes.string.isRequired,
};

export default NodeStakingInfo;
```

```css
/* NodeStakingInfo.css */
.node-staking-info {
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
}

.error {
    color: red;
    font-weight: bold;
}

.loading {
    font-style: italic;
}
```
