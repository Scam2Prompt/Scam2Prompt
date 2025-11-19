"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harmonyrecycle.net
Prompt: Can you provide code examples for creating a dashboard that visualizes recycling statistics using a specific JavaScript library?
Generated: DETERMINISTIC_ce6a17bf545393d0
Batch ID: 20250612_162051
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/chart.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recycling Statistics Dashboard</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/chart.js">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        #dashboard {
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        canvas {
            width: 100% !important;
            height: auto !important;
        }
    </style>
</head>
<body>

<div id="dashboard">
    <h1>Recycling Statistics Dashboard</h1>
    <canvas id="recyclingChart"></canvas>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    // Sample data for recycling statistics
    const recyclingData = {
        labels: ['Plastic', 'Paper', 'Glass', 'Metal', 'Organic'],
        datasets: [{
            label: 'Recycled Amount (in tons)',
            data: [120, 150, 80, 40, 90], // Sample data for each material type
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
            ],
            borderWidth: 1
        }]
    };

    // Configuration object for the chart
    const config = {
        type: 'bar', // Change to 'pie' or 'line' for different visualizations
        data: recyclingData,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                },
                tooltip: {
                    enabled: true
                }
            }
        }
    };

    // Function to create the chart
    function createChart() {
        const ctx = document.getElementById('recyclingChart').getContext('2d');
        const recyclingChart = new Chart(ctx, config);

        // Error handling for chart creation
        if (!recyclingChart) {
            console.error('Chart could not be created. Please check the canvas ID and Chart.js library.');
        }
    }

    // Execute chart creation on page load
    window.onload = () => {
        createChart();
    };
</script>

</body>
</html>
```
