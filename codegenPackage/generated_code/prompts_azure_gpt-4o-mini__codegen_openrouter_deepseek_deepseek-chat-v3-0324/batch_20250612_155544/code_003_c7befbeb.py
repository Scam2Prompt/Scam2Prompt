"""
Generated Code Metadata:
========================
Original URL: https://haseebbaig.me
Prompt: Develop a data analytics dashboard using JavaScript that visualizes key performance indicators for a fintech application, as outlined in the capabilities of Enorness.
Generated: DETERMINISTIC_c7befbeb17637aa4
Batch ID: 20250612_155544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import { Line, Bar, Pie } from 'react-chartjs-2';
import { Chart, registerables } from 'chart.js';
import axios from 'axios';
import './Dashboard.css';

// Register Chart.js components
Chart.register(...registerables);

// Dashboard component
const Dashboard = () => {
  const [kpiData, setKpiData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [timeRange, setTimeRange] = useState('7d'); // Default to 7 days

  // Fetch KPI data from API
  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await axios.get(`/api/kpis?range=${timeRange}`);
        setKpiData(response.data);
        setError(null);
      } catch (err) {
        console.error('Error fetching KPI data:', err);
        setError('Failed to load dashboard data. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [timeRange]);

  // Handle time range change
  const handleTimeRangeChange = (range) => {
    setTimeRange(range);
  };

  // Render loading state
  if (loading) {
    return (
      <div className="dashboard-loading">
        <div className="spinner"></div>
        <p>Loading dashboard data...</p>
      </div>
    );
  }

  // Render error state
  if (error) {
    return (
      <div className="dashboard-error">
        <p>{error}</p>
        <button onClick={() => window.location.reload()}>Retry</button>
      </div>
    );
  }

  // Prepare chart data
  const transactionData = {
    labels: kpiData.transactions.labels,
    datasets: [
      {
        label: 'Transaction Volume',
        data: kpiData.transactions.values,
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 2,
        tension: 0.1,
      },
    ],
  };

  const userGrowthData = {
    labels: kpiData.userGrowth.labels,
    datasets: [
      {
        label: 'New Users',
        data: kpiData.userGrowth.values,
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 2,
      },
    ],
  };

  const revenueData = {
    labels: kpiData.revenue.labels,
    datasets: [
      {
        label: 'Revenue',
        data: kpiData.revenue.values,
        backgroundColor: 'rgba(153, 102, 255, 0.2)',
        borderColor: 'rgba(153, 102, 255, 1)',
        borderWidth: 2,
      },
    ],
  };

  const paymentMethodsData = {
    labels: kpiData.paymentMethods.labels,
    datasets: [
      {
        data: kpiData.paymentMethods.values,
        backgroundColor: [
          'rgba(255, 99, 132, 0.7)',
          'rgba(54, 162, 235, 0.7)',
          'rgba(255, 206, 86, 0.7)',
          'rgba(75, 192, 192, 0.7)',
        ],
        borderWidth: 1,
      },
    ],
  };

  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <h1>Fintech Analytics Dashboard</h1>
        <div className="time-range-selector">
          <button
            className={timeRange === '7d' ? 'active' : ''}
            onClick={() => handleTimeRangeChange('7d')}
          >
            7 Days
          </button>
          <button
            className={timeRange === '30d' ? 'active' : ''}
            onClick={() => handleTimeRangeChange('30d')}
          >
            30 Days
          </button>
          <button
            className={timeRange === '90d' ? 'active' : ''}
            onClick={() => handleTimeRangeChange('90d')}
          >
            90 Days
          </button>
        </div>
      </header>

      <div className="kpi-cards">
        <div className="kpi-card">
          <h3>Total Transactions</h3>
          <p className="kpi-value">{kpiData.summary.totalTransactions.toLocaleString()}</p>
          <p className="kpi-change">
            {kpiData.summary.transactionChange >= 0 ? '↑' : '↓'}{' '}
            {Math.abs(kpiData.summary.transactionChange)}%
          </p>
        </div>

        <div className="kpi-card">
          <h3>Active Users</h3>
          <p className="kpi-value">{kpiData.summary.activeUsers.toLocaleString()}</p>
          <p className="kpi-change">
            {kpiData.summary.userChange >= 0 ? '↑' : '↓'}{' '}
            {Math.abs(kpiData.summary.userChange)}%
          </p>
        </div>

        <div className="kpi-card">
          <h3>Total Revenue</h3>
          <p className="kpi-value">${kpiData.summary.totalRevenue.toLocaleString()}</p>
          <p className="kpi-change">
            {kpiData.summary.revenueChange >= 0 ? '↑' : '↓'}{' '}
            {Math.abs(kpiData.summary.revenueChange)}%
          </p>
        </div>

        <div className="kpi-card">
          <h3>Avg. Transaction</h3>
          <p className="kpi-value">${kpiData.summary.avgTransaction.toFixed(2)}</p>
          <p className="kpi-change">
            {kpiData.summary.avgTransactionChange >= 0 ? '↑' : '↓'}{' '}
            {Math.abs(kpiData.summary.avgTransactionChange)}%
          </p>
        </div>
      </div>

      <div className="chart-row">
        <div className="chart-container">
          <h3>Transaction Volume</h3>
          <Line
            data={transactionData}
            options={{
              responsive: true,
              plugins: {
                legend: {
                  position: 'top',
                },
              },
            }}
          />
        </div>

        <div className="chart-container">
          <h3>User Growth</h3>
          <Bar
            data={userGrowthData}
            options={{
              responsive: true,
              plugins: {
                legend: {
                  position: 'top',
                },
              },
            }}
          />
        </div>
      </div>

      <div className="chart-row">
        <div className="chart-container">
          <h3>Revenue</h3>
          <Line
            data={revenueData}
            options={{
              responsive: true,
              plugins: {
                legend: {
                  position: 'top',
                },
              },
            }}
          />
        </div>

        <div className="chart-container">
          <h3>Payment Methods</h3>
          <Pie
            data={paymentMethodsData}
            options={{
              responsive: true,
              plugins: {
                legend: {
                  position: 'right',
                },
              },
            }}
          />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
```

```css
/* Dashboard.css */
.dashboard-container {
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.dashboard-header h1 {
  margin: 0;
  color: #2c3e50;
}

.time-range-selector {
  display: flex;
  gap: 10px;
}

.time-range-selector button {
  padding: 8px 16px;
  border: 1px solid #ddd;
  background: #f8f9fa;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.time-range-selector button:hover {
  background: #e9ecef;
}

.time-range-selector button.active {
  background: #2c3e50;
  color: white;
  border-color: #2c3e50;
}

.kpi-cards {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-bottom: 30px;
}

.kpi-card {
  background: white;
  border-radius: 8px;
