"""
Generated Code Metadata:
========================
Original URL: https://metamaskloghin.gitbook.io
Prompt: Design a user interface for a DApp that integrates with MetaMask, making it easy for users to interact with the application and perform transactions.
Generated: DETERMINISTIC_82e2b1dc4da309b9
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries and components
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import detectEthereumProvider from '@metamask/detect-provider';
import { Button, Card, Alert, Spinner } from 'react-bootstrap';
import './App.css';

// Main DApp component
const DApp = () => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);
  const [balance, setBalance] = useState('0');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  // Initialize Web3 and check for MetaMask
  useEffect(() => {
    const initWeb3 = async () => {
      try {
        const provider = await detectEthereumProvider();
        
        if (provider) {
          const web3Instance = new Web3(provider);
          setWeb3(web3Instance);

          // Listen for account changes
          window.ethereum.on('accountsChanged', (accounts) => {
            setAccount(accounts[0]);
            fetchBalance(accounts[0], web3Instance);
          });

          // Listen for chain changes
          window.ethereum.on('chainChanged', () => {
            window.location.reload();
          });
        } else {
          setError('Please install MetaMask to use this DApp.');
        }
      } catch (err) {
        setError('Failed to initialize Web3.');
        console.error(err);
      }
    };

    initWeb3();
  }, []);

  // Connect to MetaMask wallet
  const connectWallet = async () => {
    try {
      setLoading(true);
      setError(null);
      
      if (window.ethereum) {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);
        await fetchBalance(accounts[0], web3);
      } else {
        setError('MetaMask is not installed.');
      }
    } catch (err) {
      setError('Failed to connect to MetaMask.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Fetch user's balance
  const fetchBalance = async (account, web3Instance) => {
    try {
      if (account && web3Instance) {
        const balanceWei = await web3Instance.eth.getBalance(account);
        const balanceEth = web3Instance.utils.fromWei(balanceWei, 'ether');
        setBalance(balanceEth);
      }
    } catch (err) {
      setError('Failed to fetch balance.');
      console.error(err);
    }
  };

  // Example transaction function
  const sendTransaction = async () => {
    try {
      setLoading(true);
      setError(null);
      setSuccess(null);

      if (!account) {
        setError('Please connect your wallet first.');
        return;
      }

      const transaction = {
        from: account,
        to: '0x742d35Cc6634C0532925a3b844Bc454e4438f44e', // Example recipient address
        value: web3.utils.toWei('0.01', 'ether'),
      };

      const txHash = await web3.eth.sendTransaction(transaction);
      setSuccess(`Transaction successful! Hash: ${txHash.transactionHash}`);
    } catch (err) {
      setError('Transaction failed. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <Card className="dapp-card">
        <Card.Header>
          <h2>MetaMask DApp</h2>
        </Card.Header>
        <Card.Body>
          {error && <Alert variant="danger">{error}</Alert>}
          {success && <Alert variant="success">{success}</Alert>}

          {!account ? (
            <Button 
              variant="primary" 
              onClick={connectWallet}
              disabled={loading}
            >
              {loading ? (
                <>
                  <Spinner animation="border" size="sm" /> Connecting...
                </>
              ) : (
                'Connect MetaMask'
              )}
            </Button>
          ) : (
            <>
              <div className="account-info">
                <p><strong>Account:</strong> {account}</p>
                <p><strong>Balance:</strong> {balance} ETH</p>
              </div>
              
              <Button 
                variant="success" 
                onClick={sendTransaction}
                disabled={loading}
                className="mt-3"
              >
                {loading ? (
                  <>
                    <Spinner animation="border" size="sm" /> Processing...
                  </>
                ) : (
                  'Send 0.01 ETH'
                )}
              </Button>
            </>
          )}
        </Card.Body>
      </Card>
    </div>
  );
};

export default DApp;
```

```css
/* App.css */
.app-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f8f9fa;
}

.dapp-card {
  width: 100%;
  max-width: 500px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.account-info {
  background-color: #f8f9fa;
  padding: 15px;
  border-radius: 5px;
  margin-bottom: 20px;
}

.spinner-border {
  margin-right: 8px;
}
```
