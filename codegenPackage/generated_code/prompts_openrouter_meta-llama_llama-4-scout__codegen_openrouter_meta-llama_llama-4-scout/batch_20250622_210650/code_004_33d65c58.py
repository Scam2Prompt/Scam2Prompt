"""
Generated Code Metadata:
========================
Original URL: https://strategikorp.com
Prompt: "Create a JavaScript function to visualize the results of a business strategy plan, similar to how Strategik Corporation presents their 'Resultados Destacados' (Highlighted Results)."
Generated: DETERMINISTIC_33d65c582ddda854
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Visualize the results of a business strategy plan.
 * 
 * @param {Object} data - The data to visualize, containing 'metric', 'target', and 'actual' values.
 * @param {string} data.metric - The name of the metric (e.g., 'Revenue Growth', 'Customer Acquisition').
 * @param {number} data.target - The target value for the metric.
 * @param {number} data.actual - The actual value achieved for the metric.
 * @param {string} [containerId='visualization-container'] - The ID of the container element to render the visualization in.
 */
function visualizeStrategyResults(data, containerId = 'visualization-container') {
    // Check if the data is valid
    if (!Array.isArray(data) || data.length === 0) {
        throw new Error('Invalid data: expected a non-empty array of objects');
    }

    // Validate each data point
    data.forEach((point, index) => {
        if (typeof point.metric !== 'string' || typeof point.target !== 'number' || typeof point.actual !== 'number') {
            throw new Error(`Invalid data at index ${index}: expected { metric: string, target: number, actual: number }`);
        }
    });

    // Create the container element if it doesn't exist
    const container = document.getElementById(containerId);
    if (!container) {
        throw new Error(`Container element with ID '${containerId}' not found`);
    }

    // Render the visualization
    const visualizationHtml = data.map((point) => {
        const percentage = ((point.actual - point.target) / point.target) * 100;
        const color = percentage >= 0 ? 'green' : 'red';
        return `
            <div class="metric-visualization">
                <span>${point.metric}</span>
                <span>Target: ${point.target.toLocaleString()}</span>
                <span>Actual: ${point.actual.toLocaleString()}</span>
                <span style="color: ${color}">${percentage.toFixed(2)}%</span>
            </div>
        `;
    }).join('');

    container.innerHTML = visualizationHtml;
}

// Example usage
const data = [
    { metric: 'Revenue Growth', target: 100000, actual: 120000 },
    { metric: 'Customer Acquisition', target: 1000, actual: 900 },
];

try {
    visualizeStrategyResults(data);
} catch (error) {
    console.error(error.message);
}
```
