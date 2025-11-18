"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blue-interface.netlify.app
Prompt: Recommend tools or libraries for visualizing earning analytics provided by the Morpho protocol in a React application.
Generated: DETERMINISTIC_c1b73228e663bf71
Batch ID: 20250612_155032
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: EarningAnalyticsChart.js

// Import necessary libraries and dependencies
import React from 'react';
import PropTypes from 'prop-types';
import { Chart } from 'react-chartjs-2'; // Chart.js is a powerful visualization library
import 'chart.js/auto'; // Import required modules for Chart.js
import { CircularProgress, Typography } from '@mui/material'; // Material-UI for styling and loader

/**
 * A React component for visualizing earning analytics data from the Morpho protocol.
 * @param {Object} props - The component props.
 * @param {boolean} props.isLoading - Indicates whether the data is still loading.
 * @param {Array} props.data - An array of analytics data objects.
 * @param {string} props.chartTitle - Title of the chart.
 */
const EarningAnalyticsChart = ({ isLoading, data, chartTitle }) => {
  // Error handling: If no data is provided, display a message
  if (!data || data.length === 0) {
    return <Typography variant="body1">No earning analytics data available.</Typography>;
  }

  // Prepare chart data structure for Chart.js
  const chartData = {
    labels: data.map((item) => item.date), // Map data dates for x-axis labels
    datasets: [
      {
        label: 'Earnings (in USD)',
        data: data.map((item) => item.earnings), // Map earnings for y-axis data points
        backgroundColor: 'rgba(75, 192, 192, 0.2)', // Light teal for bar background
        borderColor: 'rgba(75, 192, 192, 1)', // Teal for bar border
        borderWidth: 1, // Bar border width
      },
    ],
  };

  // Chart options to customize appearance
  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: true,
        position: 'top',
      },
      title: {
        display: !!chartTitle,
        text: chartTitle,
        font: {
          size: 16,
        },
      },
    },
    scales: {
      x: {
        title: {
          display: true,
          text: 'Date',
        },
      },
      y: {
        title: {
          display: true,
          text: 'Earnings (USD)',
        },
        beginAtZero: true,
      },
    },
  };

  // Render component
  return (
    <div style={{ width: '100%', height: '400px', position: 'relative' }}>
      {isLoading ? (
        <CircularProgress style={{ position: 'absolute', top: '50%', left: '50%' }} />
      ) : (
        <Chart type="bar" data={chartData} options={chartOptions} />
      )}
    </div>
  );
};

// Prop type validation for improved reliability
EarningAnalyticsChart.propTypes = {
  isLoading: PropTypes.bool.isRequired, // Loading state
  data: PropTypes.arrayOf(
    PropTypes.shape({
      date: PropTypes.string.isRequired, // Date field
      earnings: PropTypes.number.isRequired, // Earnings field
    })
  ).isRequired, // Analytics data array
  chartTitle: PropTypes.string, // Chart title (optional)
};

// Default props for optional properties
EarningAnalyticsChart.defaultProps = {
  chartTitle: 'Earning Analytics',
};

// Export the component for use in other parts of the application
export default EarningAnalyticsChart;
```
