"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-extra.fi
Prompt: Develop a dashboard using JavaScript that provides real-time analytics for portfolio performance, similar to Extra Finance's transparent analytics feature.
Generated: DETERMINISTIC_bda3b12f461cac4c
Batch ID: 20250612_153923
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/chart.js/3.7.0/chart.min.js": {
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
    <title>Portfolio Performance Dashboard</title>
    <link rel="stylesheet" href="styles.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/chart.js/3.7.0/chart.min.js"></script>
</head>
<body>
    <div class="dashboard">
        <h1>Portfolio Performance Dashboard</h1>
        <canvas id="portfolioChart" width="400" height="200"></canvas>
        <div id="error-message" class="error-message"></div>
    </div>

    <script>
        // Simulated portfolio data for demonstration purposes
        const portfolioData = [
            { date: '2023-01-01', value: 1000 },
            { date: '2023-02-01', value: 1100 },
            { date: '2023-03-01', value: 1200 },
            { date: '2023-04-01', value: 1300 },
            { date: '2023-05-01', value: 1250 },
            { date: '2023-06-01', value: 1400 }
        ];

        // Function to fetch portfolio data (mocked for this example)
        async function fetchPortfolioData() {
            try {
                // Simulate fetching data from an API
                return new Promise((resolve, reject) => {
                    setTimeout(() => {
                        // Randomly succeed or fail to simulate API behavior
                        Math.random() > 0.2 ? resolve(portfolioData) : reject("Failed to fetch data");
                    }, 1000);
                });
            } catch (error) {
                displayError(error);
            }
        }

        // Function to display error messages to the user
        function displayError(message) {
            const errorMessageElement = document.getElementById('error-message');
            errorMessageElement.textContent = message;
            errorMessageElement.style.display = 'block';
        }

        // Function to render the portfolio chart
        function renderChart(data) {
            const ctx = document.getElementById('portfolioChart').getContext('2d');
            const labels = data.map(item => item.date);
            const values = data.map(item => item.value);

            const chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Portfolio Value',
                        data: values,
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 2,
                        fill: false,
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Date'
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Value ($)'
                            }
                        }
                    }
                }
            });
        }

        // Main function to initialize the dashboard
        async function init() {
            try {
                const data = await fetchPortfolioData();
                renderChart(data);
            } catch (error) {
                displayError("An unexpected error occurred while initializing the dashboard.");
            }
        }

        // Initialize the dashboard on page load
        window.onload = init;
    </script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .dashboard {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .error-message {
            color: red;
            display: none;
            margin-top: 10px;
        }
    </style>
</body>
</html>
```
