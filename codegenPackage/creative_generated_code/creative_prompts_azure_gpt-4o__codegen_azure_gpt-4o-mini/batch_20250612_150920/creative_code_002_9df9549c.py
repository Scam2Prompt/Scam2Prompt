"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.construyerk.com
Prompt: Generate a script in JavaScript to visualize construction project milestones, including phases like foundation laying, brickwork, and final inspections, tailored for a construction company in Argentina.
Generated: DETERMINISTIC_9df9549c64992926
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Construction Project Milestones Visualization

// Import necessary libraries
import Chart from 'chart.js';

const milestonesData = [
    {
        phase: 'Foundation Laying',
        startDate: new Date('2023-01-01'),
        endDate: new Date('2023-01-15'),
    },
    {
        phase: 'Brickwork',
        startDate: new Date('2023-01-16'),
        endDate: new Date('2023-02-15'),
    },
    {
        phase: 'Roofing',
        startDate: new Date('2023-02-16'),
        endDate: new Date('2023-03-01'),
    },
    {
        phase: 'Electrical and Plumbing',
        startDate: new Date('2023-03-02'),
        endDate: new Date('2023-03-20'),
    },
    {
        phase: 'Final Inspections',
        startDate: new Date('2023-03-21'),
        endDate: new Date('2023-03-30'),
    }
];

// Function to calculate duration of each phase
const calculateDurations = (milestones) => {
    return milestones.map(milestone => ({
        phase: milestone.phase,
        duration: (milestone.endDate - milestone.startDate) / (1000 * 60 * 60 * 24), // Duration in days
    }));
};

// Function to render the chart
const renderChart = (data) => {
    const ctx = document.getElementById('milestonesChart').getContext('2d');

    // Destroy existing chart instance if it exists
    if (window.milestonesChart) {
        window.milestonesChart.destroy();
    }

    // Create a new chart instance
    window.milestonesChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.map(item => item.phase),
            datasets: [{
                label: 'Duration in Days',
                data: data.map(item => item.duration),
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Duration (Days)'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Construction Phase'
                    }
                }
            },
            plugins: {
                legend: {
                    display: true
                }
            }
        }
    });
};

// Error handling for rendering
try {
    const durations = calculateDurations(milestonesData);
    renderChart(durations);
} catch (error) {
    console.error('Error rendering the chart:', error);
}

// HTML structure for the canvas
document.body.innerHTML += `
    <div style="width: 80%; margin: auto;">
        <h2>Construction Project Milestones</h2>
        <canvas id="milestonesChart" width="400" height="200"></canvas>
    </div>
`;
```
