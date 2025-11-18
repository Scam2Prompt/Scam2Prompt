"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismdashboard.xyz
Prompt: Write JavaScript code to pull wallet analytics data from Optimistic Etherscan and render it in a searchable table format.
Generated: DETERMINISTIC_9b972f9b81c26c7b
Batch ID: 20250612_151932
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.optimistic.etherscan.io/api": {
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
// Import necessary libraries
import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { Table, Input } from 'antd';

// Constants for API endpoint and the Ethereum wallet address
const API_KEY = 'YOUR_ETHERSCAN_API_KEY'; // Replace with your Etherscan API key
const ETHERSCAN_API_URL = 'https://api.optimistic.etherscan.io/api';
const WALLET_ADDRESS = 'YOUR_WALLET_ADDRESS'; // Replace with the wallet address you want to analyze

// Functional component for displaying wallet analytics data
const WalletAnalytics = () => {
  const [data, setData] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  // Fetch wallet transaction data from Optimistic Etherscan API
  const fetchWalletData = async () => {
    try {
      const response = await axios.get(ETHERSCAN_API_URL, {
        params: {
          module: 'account',
          action: 'txlist',
          address: WALLET_ADDRESS,
          startblock: 0,
          endblock: 99999999,
          sort: 'desc',
          apikey: API_KEY,
        },
      });
      
      // Check for a successful response and set the data state
      if (response.data.status === '1') {
        setData(response.data.result);
      } else {
        throw new Error(response.data.message);
      }
      
    } catch (error) {
      console.error('Error fetching wallet data:', error);
      alert('Failed to fetch wallet data. Please try again later.');
    }
  };

  // Effect to fetch data on component mount
  useEffect(() => {
    fetchWalletData();
  }, []);

  // Function to handle search input change
  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };

  // Filter data based on search term
  const filteredData = data.filter((transaction) => 
    transaction.hash.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div>
      <h1>Wallet Analytics</h1>
      <Input
        placeholder="Search by transaction hash"
        value={searchTerm}
        onChange={handleSearchChange}
        style={{ marginBottom: '20px', width: '300px' }}
      />
      <Table 
        dataSource={filteredData} 
        rowKey="hash" 
        pagination={{ pageSize: 10 }}
      >
        <Table.Column title="Transaction Hash" dataIndex="hash" />
        <Table.Column title="Block Number" dataIndex="blockNumber" />
        <Table.Column title="Timestamp" dataIndex="timeStamp" render={(timestamp) => new Date(timestamp * 1000).toLocaleString()} />
        <Table.Column title="From" dataIndex="from" />
        <Table.Column title="To" dataIndex="to" />
        <Table.Column title="Value" dataIndex="value" render={(value) => `${(value / 1e18).toFixed(4)} ETH`} />
      </Table>
    </div>
  );
};

export default WalletAnalytics;
```

### Instructions:
- Ensure to replace `YOUR_ETHERSCAN_API_KEY` with a valid Optimistic Etherscan API key.
- Replace `YOUR_WALLET_ADDRESS` with the address of the wallet you want to analyze.
- This code uses React and Ant Design for rendering the table. Make sure to install these libraries with `npm install axios antd react` if they are not already installed in your project.
- Include this component in your main application file to render it.
