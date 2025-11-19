"""
Generated Code Metadata:
========================
Original URL: https://euler.is
Prompt: Generate a code example for visualizing defect graphs and layer annotations in a web-based AM system, similar to Euler’s platform.
Generated: DETERMINISTIC_8286531423df5666
Batch ID: 20250622_205315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import { Chart } from 'react-chartjs-2';
import axios from 'axios';

// Define the main component for visualizing defect graphs
const DefectGraphVisualizer = () => {
    // State to hold defect data and loading status
    const [defectData, setDefectData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Fetch defect data from the API
    const fetchDefectData = async () => {
        try {
            const response = await axios.get('/api/defects'); // Replace with your API endpoint
            setDefectData(response.data);
        } catch (err) {
            setError('Error fetching defect data');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    // Use effect to fetch data on component mount
    useEffect(() => {
        fetchDefectData();
    }, []);

    // Prepare data for the chart
    const prepareChartData = () => {
        const labels = defectData.map(defect => defect.layer);
        const data = defectData.map(defect => defect.count);

        return {
            labels: labels,
            datasets: [
                {
                    label: 'Defect Count',
                    data: data,
                    backgroundColor: 'rgba(75, 192, 192, 0.6)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                },
            ],
        };
    };

    // Render loading state or error message
    if (loading) return <div>Loading...</div>;
    if (error) return <div>{error}</div>;

    // Render the chart
    return (
        <div>
            <h2>Defect Graph Visualization</h2>
            <Chart
                type="bar"
                data={prepareChartData()}
                options={{
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                        },
                    },
                }}
            />
        </div>
    );
};

// Export the component for use in other parts of the application
export default DefectGraphVisualizer;
```

```css
/* Add basic styles for the defect graph visualizer */
.defect-graph-container {
    width: 80%;
    margin: auto;
    padding: 20px;
}

h2 {
    text-align: center;
    color: #333;
}
```

```json
// Sample JSON response from the API for defect data
[
    { "layer": "Layer 1", "count": 10 },
    { "layer": "Layer 2", "count": 5 },
    { "layer": "Layer 3", "count": 8 },
    { "layer": "Layer 4", "count": 12 }
]
```

```html
<!-- Include this in your HTML file to load the React app -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Defect Graph Visualizer</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="root"></div>
    <script src="index.js"></script>
</body>
</html>
```

```javascript
// index.js - Entry point for the React application
import React from 'react';
import ReactDOM from 'react-dom';
import DefectGraphVisualizer from './DefectGraphVisualizer';

ReactDOM.render(
    <React.StrictMode>
        <DefectGraphVisualizer />
    </React.StrictMode>,
    document.getElementById('root')
);
```
