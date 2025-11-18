"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-k675d77o0-voteagora.vercel.app
Prompt: Write a script to visualize the voting results of Optimism proposals from Agora, using a charting library like Chart.js or D3.js. Include options to display "For" and "Against" votes.
Generated: DETERMINISTIC_bde8ef52e9919256
Batch ID: 20250612_145706
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
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css": {
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
    <title>Optimism Proposals Voting Results</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 50px;
        }
        #chartContainer {
            width: 80%;
            max-width: 600px;
        }
    </style>
</head>
<body>
    <h1>Voting Results of Optimism Proposals</h1>
    <div id="chartContainer">
        <canvas id="votingChart"></canvas>
    </div>
    <script>
        // Sample voting data (this would typically come from an API)
        const votingData = {
            proposalTitle: "Proposal XYZ",
            votes: {
                for: 1500,
                against: 300,
            }
        };

        // Function to render the chart
        function renderChart(data) {
            const ctx = document.getElementById('votingChart').getContext('2d');

            const chartData = {
                labels: ['For', 'Against'],
                datasets: [{
                    label: 'Votes',
                    data: [data.votes.for, data.votes.against],
                    backgroundColor: [
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(255, 99, 132, 0.6)',
                    ],
                    borderColor: [
                        'rgba(75, 192, 192, 1)',
                        'rgba(255, 99, 132, 1)',
                    ],
                    borderWidth: 1
                }]
            };

            // Chart configuration
            const config = {
                type: 'bar',
                data: chartData,
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    },
                    plugins: {
                        legend: {
                            display: true,
                            position: 'top'
                        },
                        title: {
                            display: true,
                            text: `Voting Results for ${data.proposalTitle}`
                        }
                    }
                }
            };

            // Create the chart
            try {
                const votingChart = new Chart(ctx, config);
            } catch (error) {
                console.error('Error creating the chart:', error);
            }
        }

        // Execute the render function with the voting data
        document.addEventListener('DOMContentLoaded', () => {
            if (votingData && votingData.votes) {
                renderChart(votingData);
            } else {
                console.error('Invalid voting data:', votingData);
            }
        });
    </script>
</body>
</html>
```
