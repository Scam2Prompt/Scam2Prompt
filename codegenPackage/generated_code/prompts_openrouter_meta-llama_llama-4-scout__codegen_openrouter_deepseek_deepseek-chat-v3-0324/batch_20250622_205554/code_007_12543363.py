"""
Generated Code Metadata:
========================
Original URL: https://energiadosertao.blogspot.com
Prompt: Design a basic web application using a library like React or Angular to display real-time data on solar panel system performance, including energy production, consumption, and storage.
Generated: DETERMINISTIC_12543363399146c5
Batch ID: 20250622_205554
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/solar/performance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// SolarPanelDashboard.js - React component for displaying solar panel performance data
import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const SolarPanelDashboard = () => {
  const [performanceData, setPerformanceData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch real-time data from API
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('https://api.example.com/solar/performance');
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        const data = await response.json();
        setPerformanceData(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setIsLoading(false);
      }
    };

    // Initial fetch
    fetchData();

    // Set up polling for real-time updates
    const intervalId = setInterval(fetchData, 30000); // Update every 30 seconds

    // Clean up interval on component unmount
    return () => clearInterval(intervalId);
  }, []);

  // Calculate summary statistics
  const calculateSummary = () => {
    if (performanceData.length === 0) return null;

    const latest = performanceData[performanceData.length - 1];
    return {
      production: latest.production,
      consumption: latest.consumption,
      storage: latest.storage,
      efficiency: ((latest.production / (latest.consumption + latest.storage)) * 100).toFixed(2)
    };
  };

  const summary = calculateSummary();

  if (isLoading) {
    return <div className="loading">Loading solar performance data...</div>;
  }

  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  return (
    <div className="solar-dashboard">
      <h1>Solar Panel Performance Dashboard</h1>
      
      {/* Summary Cards */}
      <div className="summary-cards">
        <div className="card">
          <h3>Energy Production</h3>
          <p>{summary?.production || 0} kWh</p>
        </div>
        <div className="card">
          <h3>Energy Consumption</h3>
          <p>{summary?.consumption || 0} kWh</p>
        </div>
        <div className="card">
          <h3>Battery Storage</h3>
          <p>{summary?.storage || 0} kWh</p>
        </div>
        <div className="card">
          <h3>System Efficiency</h3>
          <p>{summary?.efficiency || 0}%</p>
        </div>
      </div>

      {/* Performance Chart */}
      <div className="chart-container">
        <h2>Performance Over Time</h2>
        <ResponsiveContainer width="100%" height={400}>
          <LineChart
            data={performanceData}
            margin={{ top: 20, right: 30, left: 20, bottom: 20 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis 
              dataKey="timestamp" 
              tickFormatter={(timestamp) => new Date(timestamp).toLocaleTimeString()}
            />
            <YAxis label={{ value: 'kWh', angle: -90, position: 'insideLeft' }} />
            <Tooltip 
              formatter={(value) => [`${value} kWh`, '']}
              labelFormatter={(timestamp) => `Time: ${new Date(timestamp).toLocaleTimeString()}`}
            />
            <Legend />
            <Line type="monotone" dataKey="production" stroke="#8884d8" activeDot={{ r: 8 }} />
            <Line type="monotone" dataKey="consumption" stroke="#82ca9d" />
            <Line type="monotone" dataKey="storage" stroke="#ffc658" />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default SolarPanelDashboard;
```

```css
/* SolarDashboard.css - Styles for the solar panel dashboard */
.solar-dashboard {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.solar-dashboard h1 {
  color: #2c3e50;
  text-align: center;
  margin-bottom: 30px;
}

.summary-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.card {
  background: #fff;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.card h3 {
  color: #7f8c8d;
  margin-top: 0;
}

.card p {
  font-size: 24px;
  font-weight: bold;
  color: #2c3e50;
  margin-bottom: 0;
}

.chart-container {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.chart-container h2 {
  color: #2c3e50;
  margin-top: 0;
}

.loading, .error {
  text-align: center;
  padding: 20px;
  font-size: 18px;
}

.loading {
  color: #3498db;
}

.error {
  color: #e74c3c;
}
```

```javascript
// App.js - Main application entry point
import React from 'react';
import SolarPanelDashboard from './SolarPanelDashboard';
import './SolarDashboard.css';

function App() {
  return (
    <div className="App">
      <SolarPanelDashboard />
    </div>
  );
}

export default App;
```

```javascript
// index.js - React application bootstrap
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```
