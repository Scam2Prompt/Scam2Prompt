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
  "https://api.example.com/optimism-voting-results": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/chart.js": {
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
  <title>Optimism Proposal Voting Results</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script> <!-- Chart.js library -->
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    canvas {
      max-width: 800px;
      margin: 0 auto;
    }
  </style>
</head>
<body>
  <h1>Optimism Proposal Voting Results</h1>
  <p>Select a proposal to view the results:</p>
  <select id="proposalSelect">
    <!-- Dropdown options will be dynamically populated -->
  </select>
  <canvas id="votingChart"></canvas> <!-- Chart container -->

  <script>
    // Mock API Function to Fetch Proposals and Voting Data from Agora
    async function fetchVotingData() {
      try {
        // Replace this URL with the actual API endpoint if available
        const response = await fetch('https://api.example.com/optimism-voting-results');
        if (!response.ok) {
          throw new Error(`Failed to fetch data: ${response.statusText}`);
        }
        return await response.json();
      } catch (error) {
        console.error('Error fetching voting data:', error);
        alert('Failed to load voting data. Please try again later.');
      }
    }

    // Function to Update the Chart with Selected Proposal Data
    function updateChart(chart, data) {
      chart.data.labels = ['For', 'Against'];
      chart.data.datasets[0].data = [data.forVotes, data.againstVotes];
      chart.update();
    }

    // Main Function to Initialize the Application
    async function init() {
      const votingData = await fetchVotingData();
      if (!votingData || !votingData.proposals) return;

      const proposalSelect = document.getElementById('proposalSelect');
      const ctx = document.getElementById('votingChart').getContext('2d');

      // Populate Dropdown with Proposals
      votingData.proposals.forEach((proposal, index) => {
        const option = document.createElement('option');
        option.value = index;
        option.textContent = proposal.title;
        proposalSelect.appendChild(option);
      });

      // Initialize Chart.js Pie Chart
      const chart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ['For', 'Against'],
          datasets: [{
            label: 'Votes',
            data: [0, 0],
            backgroundColor: ['#4CAF50', '#F44336'], // Green for "For", Red for "Against"
            borderWidth: 1
          }]
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: 'top'
            },
            tooltip: {
              callbacks: {
                label: (tooltipItem) => `${tooltipItem.label}: ${tooltipItem.raw.toLocaleString()}`
              }
            }
          }
        }
      });

      // Event Listener to Update Chart on Proposal Selection
      proposalSelect.addEventListener('change', (event) => {
        const selectedProposal = votingData.proposals[event.target.value];
        updateChart(chart, selectedProposal.votes);
      });

      // Automatically Select and Display the First Proposal
      if (votingData.proposals.length > 0) {
        proposalSelect.value = 0;
        updateChart(chart, votingData.proposals[0].votes);
      }
    }

    // Run the Initialization Function on Page Load
    window.onload = init;
  </script>
</body>
</html>
```
