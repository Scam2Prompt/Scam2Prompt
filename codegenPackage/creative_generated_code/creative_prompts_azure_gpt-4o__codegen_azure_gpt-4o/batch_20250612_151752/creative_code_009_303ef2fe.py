"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.jp
Prompt: Create a tool in JavaScript to visualize the daily compounding performance of CAKE rewards in PancakeSwap's Syrup Pool, similar to the data shared on the website.
Generated: DETERMINISTIC_303ef2fed7fcfa15
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// PancakeSwap CAKE Rewards Visualizer
// This script calculates and visualizes the daily compounding performance of CAKE rewards.
// Ensure you include this script in a web page with an HTML canvas element for visualization.

// Constants
const initialInvestment = 1000; // Initial amount in CAKE
const dailyAPR = 0.05; // Daily APR (5% for example, adjust as needed)
const daysToVisualize = 30; // Number of days to visualize
const canvasId = "visualizationCanvas"; // ID of the HTML Canvas element

// Function to calculate daily compounding rewards
function calculateDailyCompoundingPerformance(initialAmount, apr, days) {
    const rewards = [];
    let balance = initialAmount;

    for (let day = 1; day <= days; day++) {
        const dailyReward = balance * apr;
        balance += dailyReward;
        rewards.push({
            day: day,
            balance: balance,
            dailyReward: dailyReward,
        });
    }

    return rewards;
}

// Function to visualize performance
function visualizePerformance(rewards, canvasId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) {
        console.error(`Canvas element with ID '${canvasId}' not found.`);
        return;
    }

    const ctx = canvas.getContext("2d");
    canvas.width = 800;
    canvas.height = 400;

    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Chart settings
    const padding = 50;
    const chartWidth = canvas.width - padding * 2;
    const chartHeight = canvas.height - padding * 2;

    // Find max balance for scaling purposes
    const maxBalance = Math.max(...rewards.map((reward) => reward.balance));

    // Draw axes
    ctx.strokeStyle = "#000";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(padding, padding);
    ctx.lineTo(padding, canvas.height - padding);
    ctx.lineTo(canvas.width - padding, canvas.height - padding);
    ctx.stroke();

    // Plot data points
    ctx.strokeStyle = "#00f";
    ctx.lineWidth = 2;
    ctx.beginPath();

    rewards.forEach((reward, index) => {
        const x = padding + (index / (rewards.length - 1)) * chartWidth;
        const y =
            canvas.height -
            padding -
            (reward.balance / maxBalance) * chartHeight;

        if (index === 0) {
            ctx.moveTo(x, y);
        } else {
            ctx.lineTo(x, y);
        }
    });

    ctx.stroke();

    // Add labels and axis descriptions
    ctx.fillStyle = "#000";
    ctx.font = "14px Arial";
    ctx.fillText("Days", canvas.width / 2, canvas.height - padding / 2);
    ctx.fillText(
        "Balance (CAKE)",
        padding / 2,
        canvas.height / 2
    );
}

// Main Function
function main() {
    try {
        // Calculate rewards
        const rewards = calculateDailyCompoundingPerformance(
            initialInvestment,
            dailyAPR,
            daysToVisualize
        );

        // Visualize results
        visualizePerformance(rewards, canvasId);
    } catch (error) {
        console.error("An error occurred while generating the visualization:", error);
    }
}

// Run the main function once DOM is loaded
document.addEventListener("DOMContentLoaded", main);
```

**HTML needed for the above script to work:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PancakeSwap CAKE Rewards Visualizer</title>
</head>
<body>
    <canvas id="visualizationCanvas"></canvas>
    <script src="visualizer.js"></script>
</body>
</html>
```
