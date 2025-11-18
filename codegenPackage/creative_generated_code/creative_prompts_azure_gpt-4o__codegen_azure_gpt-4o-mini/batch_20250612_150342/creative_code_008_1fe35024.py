"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefy.pages.dev
Prompt: Create a dashboard using React.js and the Beefy Finance API to display real-time vault statistics and earnings.
Generated: DETERMINISTIC_1fe35024af65afaa
Batch ID: 20250612_150342
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.beefy.finance/vaults": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import React, { useEffect, useState } from 'react';
import axios from 'axios';

// Dashboard component to display vault statistics
const Dashboard = () => {
  // State to hold vault data
  const [vaultData, setVaultData] = useState([]);
  // State to handle loading state
  const [loading, setLoading] = useState(true);
  // State to handle errors
  const [error, setError] = useState(null);

  // Function to fetch vault data from Beefy Finance API
  const fetchVaultData = async () => {
    try {
      // Set loading to true before fetching data
      setLoading(true);
      // Make API call to Beefy Finance
      const response = await axios.get('https://api.beefy.finance/vaults');
      // Update state with fetched data
      setVaultData(response.data);
    } catch (err) {
      // Set error if fetching fails
      setError(err.message);
    } finally {
      // Set loading to false after fetching
      setLoading(false);
    }
  };

  // useEffect to fetch data on component mount
  useEffect(() => {
    fetchVaultData();
  }, []);

  // Render loading, error, or vault data
  return (
    <div>
      <h1>Beefy Finance Dashboard</h1>
      {loading && <p>Loading vault data...</p>}
      {error && <p>Error: {error}</p>}
      {vaultData.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Vault Name</th>
              <th>APY (%)</th>
              <th>Total Deposited</th>
              <th>Total Earned</th>
            </tr>
          </thead>
          <tbody>
            {vaultData.map((vault) => (
              <tr key={vault.id}>
                <td>{vault.name}</td>
                <td>{vault.apy.toFixed(2)}</td>
                <td>{vault.totalDeposited.toLocaleString()}</td>
                <td>{vault.totalEarned.toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

// Export Dashboard component
export default Dashboard;
```

### Additional Notes
- Ensure you have the `axios` library installed in your project. You can add it by running `npm install axios`.
- This code fetches real-time data from the Beefy Finance API and displays it in a simple HTML table format. Adjust the API endpoint and data structure based on the actual API response if necessary.
