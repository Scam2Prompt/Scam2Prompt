"""
Generated Code Metadata:
========================
Original URL: https://graph-protocol.vercel.app
Prompt: Provide an example of how to connect a wallet to a Web3 dApp built using the Graph Protocol on the Mumbai Testnet.
Generated: DETERMINISTIC_a742129f8f845f54
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { useEffect, useState } from 'react';
import Web3 from 'web3';
import { useQuery } from '@apollo/client';
import { gql } from 'graphql-tag';

// Define the GraphQL query to fetch data
const GET_DATA_QUERY = gql`
  query {
    yourDataEntity {
      id
      value
    }
  }
`;

// Define the WalletConnection component
const WalletConnection = () => {
  const [account, setAccount] = useState(null);
  const [web3, setWeb3] = useState(null);
  const { loading, error, data } = useQuery(GET_DATA_QUERY);

  // Function to connect to the wallet
  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);

        // Initialize Web3 instance
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);
      } catch (error) {
        console.error("Error connecting to wallet:", error);
      }
    } else {
      alert('Please install MetaMask to use this dApp');
    }
  };

  // Effect to handle wallet connection on component mount
  useEffect(() => {
    if (window.ethereum) {
      window.ethereum.on('accountsChanged', (accounts) => {
        setAccount(accounts[0]);
      });
    }
  }, []);

  return (
    <div>
      <h1>Connect to Wallet</h1>
      <button onClick={connectWallet}>Connect Wallet</button>
      {account && <p>Connected Account: {account}</p>}
      {loading && <p>Loading data...</p>}
      {error && <p>Error fetching data: {error.message}</p>}
      {data && (
        <div>
          <h2>Data from The Graph:</h2>
          <ul>
            {data.yourDataEntity.map(item => (
              <li key={item.id}>{item.value}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default WalletConnection;
```
