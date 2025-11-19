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
// Import required libraries
import React, { useState, useEffect } from 'react';
import { PieChart, Pie, Cell, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

// Mock data for airdrop distribution and vesting schedules
const airdropData = [
  { name: 'Public Sale', value: 40 },
  { name: 'Team', value: 20 },
  { name: 'Advisors', value: 10 },
  { name: 'Ecosystem', value: 20 },
  { name: 'Reserve', value: 10 },
];

const vestingData = [
  { month: 'Month 1', unlocked: 10, locked: 90 },
  { month: 'Month 3', unlocked: 20, locked: 80 },
  { month: 'Month 6', unlocked: 30, locked: 70 },
  { month: 'Month 9', unlocked: 50, locked: 50 },
  { month: 'Month 12', unlocked: 100, locked: 0 },
];

// Color palette for charts
const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884D8'];

// Component for Airdrop Distribution Pie Chart
const AirdropDistributionChart = () => {
  return (
    <div className="chart-container">
      <h2>AVAX Airdrop Distribution</h2>
      <ResponsiveContainer width="100%" height={400}>
        <PieChart>
          <Pie
            data={airdropData}
            cx="50%"
            cy="50%"
            labelLine={false}
            label={({ name, percent }) => `${name}: ${(percent * 100).toFixed(0)}%`}
            outerRadius={150}
            fill="#8884d8"
            dataKey="value"
          >
            {airdropData.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip formatter={(value) => [`${value}%`, 'Percentage']} />
          <Legend />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
};

// Component for Vesting Schedule Bar Chart
const VestingScheduleChart = () => {
  return (
    <div className="chart-container">
      <h2>AVAX Vesting Schedule</h2>
      <ResponsiveContainer width="100%" height={400}>
        <BarChart
          data={vestingData}
          margin={{
            top: 20,
            right: 30,
            left: 20,
            bottom: 5,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="month" />
          <YAxis label={{ value: 'Percentage', angle: -90, position: 'insideLeft' }} />
          <Tooltip formatter={(value) => [`${value}%`, 'Percentage']} />
          <Legend />
          <Bar dataKey="unlocked" stackId="a" fill="#82ca9d" name="Unlocked" />
          <Bar dataKey="locked" stackId="a" fill="#8884d8" name="Locked" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

// Main App Component
const AvalaunchAirdropVisualization = () => {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Simulate API fetch
    const fetchData = async () => {
      try {
        // In a real app, you would fetch data from an API here
        await new Promise(resolve => setTimeout(resolve, 1000));
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <div className="loading">Loading data...</div>;
  }

  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  return (
    <div className="avalaunch-airdrop">
      <h1>AVAX Airdrop Analytics</h1>
      <div className="charts-grid">
        <AirdropDistributionChart />
        <VestingScheduleChart />
      </div>
    </div>
  );
};

export default AvalaunchAirdropVisualization;

// CSS styles (could be moved to a separate file)
const styles = `
  .avalaunch-airdrop {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
  }
  
  .charts-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 30px;
  }
  
  .chart-container {
    background: white;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  }
  
  h1, h2 {
    color: #333;
  }
  
  h1 {
    text-align: center;
    margin-bottom: 30px;
  }
  
  .loading, .error {
    text-align: center;
    padding: 50px;
    font-size: 18px;
  }
  
  .error {
    color: #ff4444;
  }
`;

// Add styles to the document
const styleElement = document.createElement('style');
styleElement.innerHTML = styles;
document.head.appendChild(styleElement);
```
