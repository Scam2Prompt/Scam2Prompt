"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dpai-migrate.pages.dev
Prompt: Develop a DApp interface that integrates Scalia's cryptocurrency-based domain service, allowing users to securely purchase and manage domains.
Generated: DETERMINISTIC_9e64082701d5b2e3
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/*
  Scalia Domain Service DApp Interface
  Allows users to securely purchase and manage cryptocurrency-based domains.
  This example assumes integration with a smart contract deployed on Ethereum.
*/

import Web3 from 'web3';
import { useState, useEffect } from 'react';
import ScaliaDomainServiceABI from './ScaliaDomainServiceABI.json'; // Replace with the correct ABI file

// Constants
const CONTRACT_ADDRESS = '0x1234567890abcdef1234567890abcdef12345678'; // Replace with actual deployed contract address

function DomainServiceDApp() {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');
  const [contract, setContract] = useState(null);
  const [domainName, setDomainName] = useState('');
  const [statusMessage, setStatusMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // Initialize Web3 and setup connection
  useEffect(() => {
    async function initializeWeb3() {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);

        try {
          const accounts = await web3Instance.eth.requestAccounts();
          setAccount(accounts[0]);
          const contractInstance = new web3Instance.eth.Contract(
            ScaliaDomainServiceABI,
            CONTRACT_ADDRESS
          );
          setContract(contractInstance);
        } catch (error) {
          console.error('Error connecting to Ethereum:', error);
          setStatusMessage('Failed to connect to Ethereum. Please ensure your wallet is properly configured.');
        }
      } else {
        setStatusMessage('Ethereum provider (e.g., MetaMask) not detected. Please install a wallet extension.');
      }
    }
    initializeWeb3();
  }, []);

  // Handle domain purchase
  async function purchaseDomain() {
    if (!contract || !domainName.trim()) {
      setStatusMessage('Invalid input or contract not initialized.');
      return;
    }

    setIsLoading(true);
    setStatusMessage('');

    try {
      const response = await contract.methods.purchaseDomain(domainName).send({ from: account });
      setStatusMessage(`Domain "${domainName}" successfully purchased! Transaction hash: ${response.transactionHash}`);
    } catch (error) {
      console.error('Error purchasing domain:', error);
      setStatusMessage('Failed to purchase domain. Please check the domain name or try again.');
    } finally {
      setIsLoading(false);
    }
  }

  // Handle domain query
  async function queryDomainOwner() {
    if (!contract || !domainName.trim()) {
      setStatusMessage('Invalid input or contract not initialized.');
      return;
    }

    setIsLoading(true);
    setStatusMessage('');

    try {
      const owner = await contract.methods.getDomainOwner(domainName).call();
      if (owner === '0x0000000000000000000000000000000000000000') {
        setStatusMessage(`Domain "${domainName}" is not registered.`);
      } else {
        setStatusMessage(`Domain "${domainName}" is owned by: ${owner}`);
      }
    } catch (error) {
      console.error('Error querying domain owner:', error);
      setStatusMessage('Failed to retrieve domain ownership information.');
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <div style={{ padding: '20px' }}>
      <h1>Scalia Domain Service</h1>
      <p>Connected Wallet: {account || 'Not connected'}</p>

      <div style={{ marginBottom: '10px' }}>
        <input
          type="text"
          placeholder="Enter domain name (e.g., example.crypto)"
          value={domainName}
          onChange={(e) => setDomainName(e.target.value)}
          style={{ padding: '10px', width: '300px' }}
        />
      </div>

      <div style={{ marginBottom: '10px' }}>
        <button onClick={purchaseDomain} disabled={isLoading || !account} style={{ padding: '10px', marginRight: '10px' }}>
          Purchase Domain
        </button>
        <button onClick={queryDomainOwner} disabled={isLoading || !account} style={{ padding: '10px' }}>
          Query Domain Owner
        </button>
      </div>

      {statusMessage && <p>{statusMessage}</p>}
      {isLoading && <p>Loading...</p>}
    </div>
  );
}

export default DomainServiceDApp;
```
