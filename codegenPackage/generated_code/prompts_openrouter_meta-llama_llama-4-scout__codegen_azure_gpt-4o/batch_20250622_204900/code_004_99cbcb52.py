"""
Generated Code Metadata:
========================
Original URL: https://pira.pages.dev
Prompt: Create a data visualization code in JavaScript to display the airdrop distribution and vesting schedules for a specific airdrop on Avalaunch, such as the AVAX airdrop.
Generated: DETERMINISTIC_99cbcb52339a1b16
Batch ID: 20250622_204900
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries (assuming you are using a module bundler like Webpack or Parcel)
// You can install Chart.js via npm: `npm install chart.js`
import Chart from 'chart.js/auto';

// Function to create the airdrop distribution and vesting schedule visualization
function createAirdropChart(canvasId, airdropData) {
  // Validate input data
  if (!airdropData || !Array.isArray(airdropData.distribution) || !Array.isArray(airdropData.vesting)) {
    console.error("Invalid airdrop data provided.");
    return;
  }

  // Extract data for the chart
  const distributionLabels = airdropData.distribution.map(item => item.label);
  const distributionValues = airdropData.distribution.map(item => item.value);

  const vestingLabels = airdropData.vesting.map(item => item.date);
  const vestingValues = airdropData.vesting.map(item => item.amount);

  // Create the chart
  const ctx = document.getElementById(canvasId).getContext('2d');
  const chart = new Chart(ctx, {
    type: 'bar', // Bar chart for distribution
    data: {
      labels: distributionLabels,
      datasets: [
        {
          label: 'Airdrop Distribution',
          data: distributionValues,
          backgroundColor: 'rgba(75, 192, 192, 0.6)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1,
        },
        {
          label: 'Vesting Schedule',
          data: vestingValues,
          backgroundColor: 'rgba(153, 102, 255, 0.6)',
          borderColor: 'rgba(153, 102, 255, 1)',
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        tooltip: {
          callbacks: {
            label: function (context) {
              return `${context.dataset.label}: ${context.raw}`;
            },
          },
        },
      },
      scales: {
        x: {
          title: {
            display: true,
            text: 'Categories / Dates',
          },
        },
        y: {
          title: {
            display: true,
            text: 'Amount',
          },
          beginAtZero: true,
        },
      },
    },
  });

  return chart;
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  // Example airdrop data
  const airdropData = {
    distribution: [
      { label: 'Community', value: 5000 },
      { label: 'Team', value: 3000 },
      { label: 'Advisors', value: 2000 },
    ],
    vesting: [
      { date: '2023-01-01', amount: 1000 },
      { date: '2023-06-01', amount: 2000 },
      { date: '2024-01-01', amount: 3000 },
    ],
  };

  // Create the chart
  createAirdropChart('airdropChart', airdropData);
});
```

```html
<!-- HTML structure -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Airdrop Visualization</title>
  <script src="path/to/your/javascript/file.js" defer></script>
</head>
<body>
  <h1>Airdrop Distribution and Vesting Schedule</h1>
  <canvas id="airdropChart" width="800" height="400"></canvas>
</body>
</html>
```
