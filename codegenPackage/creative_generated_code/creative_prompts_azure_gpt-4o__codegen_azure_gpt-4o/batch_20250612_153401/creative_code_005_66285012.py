"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://habit-tracker-ten-pearl.vercel.app
Prompt: Provide an example of integrating a chart library like Chart.js into a React habit tracker app to visualize habit completion trends over time.
Generated: DETERMINISTIC_662850122b810413
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary dependencies
import React, { useEffect, useRef } from "react";
import { Chart } from "chart.js";

// HabitChart component: Displays a chart with habit data over time
const HabitChart = ({ habitData }) => {
  // Use a ref to attach the chart to a canvas element
  const chartRef = useRef(null);

  // Effect to initialize and update the chart based on habitData
  useEffect(() => {
    if (!habitData || habitData.length === 0) return;

    // Extract labels (dates) and completion data from habitData
    const labels = habitData.map((entry) => entry.date);
    const data = habitData.map((entry) => entry.completions);

    // Define the chart configuration
    const chartConfig = {
      type: "line", // Line chart
      data: {
        labels,
        datasets: [
          {
            label: "Habit Completion Trends",
            data,
            borderColor: "rgba(75, 192, 192, 1)", // Line color
            backgroundColor: "rgba(75, 192, 192, 0.2)", // Fill under line
            borderWidth: 2,
            tension: 0.3, // Smooth curve for line
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            display: true,
            position: "top", // Display legend at the top
          },
        },
        scales: {
          x: {
            title: {
              display: true,
              text: "Date", // Label for the x-axis
            },
          },
          y: {
            title: {
              display: true,
              text: "Completions", // Label for the y-axis
            },
            beginAtZero: true, // Start y-axis at 0
          },
        },
      },
    };

    // Initialize the chart on the canvas
    const ctx = chartRef.current.getContext("2d");
    const chartInstance = new Chart(ctx, chartConfig);

    // Cleanup: Destroy the chart when the component unmounts or data changes
    return () => {
      chartInstance.destroy();
    };
  }, [habitData]);

  // Render the canvas element for the chart
  return (
    <div>
      <h2>Habit Completion Trends</h2>
      <canvas ref={chartRef}></canvas>
    </div>
  );
};

// Example usage of the HabitChart component
// Replace this with your app logic or data source
const ExampleHabitTracker = () => {
  // Sample habit data: Replace with dynamic sources as needed
  const sampleHabitData = [
    { date: "2023-10-01", completions: 5 },
    { date: "2023-10-02", completions: 3 },
    { date: "2023-10-03", completions: 6 },
    { date: "2023-10-04", completions: 7 },
    { date: "2023-10-05", completions: 4 },
  ];

  return (
    <div>
      <HabitChart habitData={sampleHabitData} />
    </div>
  );
};

export default ExampleHabitTracker;
```
