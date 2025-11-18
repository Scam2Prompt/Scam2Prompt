"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-value-average-frontend.vercel.app
Prompt: Write code for a frontend interface in Next.js that displays deposit progress and calculates the total value of token deposits over time for a Solana-based value averaging system.
Generated: DETERMINISTIC_c07209d18fe64a22
Batch ID: 20250612_145130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/deposit-progress.js
import React, { useState, useEffect } from 'react';
import axios from 'axios'; // For API calls
import { Line } from 'react-chartjs-2'; // For data visualization
import "chart.js/auto"; // Required for Chart.js integration

/**
 * DepositProgress Component
 * Displays deposit progress and calculates the total value
 * of token deposits over time for a Solana-based system.
 */
const DepositProgress = () => {
  // State to manage deposit data and total value
  const [depositData, setDepositData] = useState([]);
  const [totalValue, setTotalValue] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch deposit data from backend or API
  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        setError(null);

        // Replace with the correct API endpoint
        const response = await axios.get('/api/deposits'); 

        if (response.data && Array.isArray(response.data)) {
          setDepositData(response.data);

          // Calculate total value of deposits
          const total = response.data.reduce((sum, deposit) => sum + deposit.value, 0);
          setTotalValue(total);
        } else {
          throw new Error('Invalid data format received from API.');
        }
      } catch (err) {
        setError(err.message || 'An error occurred while fetching deposit data.');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  // Prepare data for Chart.js
  const chartData = {
    labels: depositData.map((deposit) => deposit.date), // Extract date for x-axis
    datasets: [
      {
        label: 'Deposit Value',
        data: depositData.map((deposit) => deposit.value), // Extract value for y-axis
        borderColor: 'rgba(75,192,192,1)',
        backgroundColor: 'rgba(75,192,192,0.2)',
        fill: true,
        tension: 0.4,
      },
    ],
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Deposit Progress for Solana-Based Value Averaging</h1>

      {/* Show loading or error state */}
      {loading && <p>Loading deposit data...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {/* Show content if data is available */}
      {!loading && !error && (
        <>
          <h3>Total Value of Deposits: {totalValue.toFixed(2)} SOL</h3>

          {/* Render the chart */}
          <div style={{ maxWidth: '600px', margin: 'auto' }}>
            <Line data={chartData} />
          </div>

          {/* Render raw deposit data in a table */}
          <h3>Deposit Details</h3>
          <table border="1" style={{ width: '100%', textAlign: 'left' }}>
            <thead>
              <tr>
                <th>Date</th>
                <th>Value (in SOL)</th>
              </tr>
            </thead>
            <tbody>
              {depositData.map((deposit, index) => (
                <tr key={index}>
                  <td>{deposit.date}</td>
                  <td>{deposit.value.toFixed(2)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </>
      )}
    </div>
  );
};

export default DepositProgress;

// ----------------------------------------------------
// Example API Route to Simulate Backend (Next.js)
// ----------------------------------------------------
// File: /pages/api/deposits.js
export async function handler(req, res) {
  if (req.method === 'GET') {
    try {
      // Simulate deposit data (replace with actual Solana API data)
      const deposits = [
        { date: '2023-01-01', value: 1.25 },
        { date: '2023-02-01', value: 2.5 },
        { date: '2023-03-01', value: 3.75 },
        { date: '2023-04-01', value: 5 },
      ];
      res.status(200).json(deposits);
    } catch (error) {
      res.status(500).json({ error: 'Unable to fetch deposit data' });
    }
  } else {
    res.status(405).json({ error: 'Method not allowed' });
  }
}
```
