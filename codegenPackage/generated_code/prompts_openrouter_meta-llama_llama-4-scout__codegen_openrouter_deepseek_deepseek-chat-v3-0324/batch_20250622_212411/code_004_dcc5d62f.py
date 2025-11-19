"""
Generated Code Metadata:
========================
Original URL: https://dclinvest-sa.com
Prompt: Create a JavaScript function to visualize the performance of a mutual fund strategy, similar to those developed and advised by DCL Invest for private and institutional clients.
Generated: DETERMINISTIC_dcc5d62feded5cec
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Visualizes mutual fund performance data with interactive charts
 * @param {Object} options - Configuration options
 * @param {Array} options.data - Performance data points
 * @param {string} options.containerId - DOM element ID for chart container
 * @param {string} [options.title="Mutual Fund Performance"] - Chart title
 * @param {string} [options.yAxisLabel="Growth (%)"] - Y-axis label
 * @param {string} [options.theme="light"] - Chart theme ('light' or 'dark')
 * @throws {Error} If required parameters are missing or invalid
 */
function visualizeFundPerformance(options) {
    // Validate required parameters
    if (!options || !options.data || !options.containerId) {
        throw new Error('Missing required parameters: data and containerId');
    }

    if (!Array.isArray(options.data) || options.data.length === 0) {
        throw new Error('Data must be a non-empty array');
    }

    const container = document.getElementById(options.containerId);
    if (!container) {
        throw new Error(`Container element with ID '${options.containerId}' not found`);
    }

    // Set default values
    const config = {
        title: options.title || "Mutual Fund Performance",
        yAxisLabel: options.yAxisLabel || "Growth (%)",
        theme: options.theme || "light",
        data: options.data
    };

    // Prepare chart container
    container.innerHTML = '';
    container.style.width = '100%';
    container.style.height = '500px';

    // Initialize chart
    try {
        const chart = new Chart(container, {
            type: 'line',
            data: {
                labels: config.data.map(item => item.date),
                datasets: [{
                    label: 'Fund Performance',
                    data: config.data.map(item => item.value),
                    borderColor: config.theme === 'dark' ? '#4bc0c0' : '#3e95cd',
                    backgroundColor: config.theme === 'dark' ? 'rgba(75, 192, 192, 0.2)' : 'rgba(54, 162, 235, 0.2)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    title: {
                        display: true,
                        text: config.title,
                        font: {
                            size: 18
                        },
                        color: config.theme === 'dark' ? '#ffffff' : '#333333'
                    },
                    tooltip: {
                        mode: 'index',
                        intersect: false,
                        backgroundColor: config.theme === 'dark' ? 'rgba(0, 0, 0, 0.8)' : 'rgba(255, 255, 255, 0.9)',
                        titleColor: config.theme === 'dark' ? '#ffffff' : '#333333',
                        bodyColor: config.theme === 'dark' ? '#ffffff' : '#333333',
                        borderColor: config.theme === 'dark' ? '#444444' : '#dddddd',
                        borderWidth: 1
                    },
                    legend: {
                        display: false
                    }
                },
                scales: {
                    x: {
                        grid: {
                            color: config.theme === 'dark' ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
                        },
                        ticks: {
                            color: config.theme === 'dark' ? '#ffffff' : '#666666'
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: config.yAxisLabel,
                            color: config.theme === 'dark' ? '#ffffff' : '#666666'
                        },
                        grid: {
                            color: config.theme === 'dark' ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
                        },
                        ticks: {
                            color: config.theme === 'dark' ? '#ffffff' : '#666666',
                            callback: function(value) {
                                return value + '%';
                            }
                        }
                    }
                },
                interaction: {
                    mode: 'nearest',
                    axis: 'x',
                    intersect: false
                }
            }
        });

        return chart;
    } catch (error) {
        console.error('Error initializing chart:', error);
        container.innerHTML = `<div class="error-message">Error displaying chart: ${error.message}</div>`;
        throw error;
    }
}

// Example usage:
/*
const sampleData = [
    { date: '2020-01', value: 100 },
    { date: '2020-02', value: 105 },
    { date: '2020-03', value: 98 },
    { date: '2020-04', value: 110 },
    { date: '2020-05', value: 115 },
    { date: '2020-06', value: 120 }
];

visualizeFundPerformance({
    data: sampleData,
    containerId: 'chart-container',
    title: 'DCL Invest Strategy Performance',
    yAxisLabel: 'Portfolio Growth (%)',
    theme: 'light'
});
*/
```
