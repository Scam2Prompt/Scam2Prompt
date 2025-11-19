"""
Generated Code Metadata:
========================
Original URL: https://web3-connect-wallet.webflow.io
Prompt: Design a basic user interface component in code that shows a user's Web3 account details, including account ID and balance, similar to the layout on the webpage.
Generated: DETERMINISTIC_1a277a0ddb61efd7
Batch ID: 20250622_204931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { ethers } from 'ethers';

/**
 * Web3AccountDetails - Displays a user's Web3 account details including account ID and balance.
 * 
 * @param {Object} props - Component props
 * @param {string} props.provider - Web3 provider instance
 * @param {string} [props.theme='light'] - Theme for the component ('light' or 'dark')
 * @returns {JSX.Element} React component
 */
const Web3AccountDetails = ({ provider, theme = 'light' }) => {
  const [account, setAccount] = useState(null);
  const [balance, setBalance] = useState('0');
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchAccountDetails = async () => {
      try {
        setIsLoading(true);
        setError(null);

        // Request account access if needed
        const accounts = await provider.send('eth_requestAccounts', []);
        if (!accounts || accounts.length === 0) {
          throw new Error('No accounts found');
        }

        const selectedAccount = accounts[0];
        setAccount(selectedAccount);

        // Get balance
        const balanceWei = await provider.getBalance(selectedAccount);
        const balanceEth = ethers.utils.formatEther(balanceWei);
        setBalance(balanceEth);
      } catch (err) {
        console.error('Error fetching account details:', err);
        setError(err.message || 'Failed to load account details');
      } finally {
        setIsLoading(false);
      }
    };

    if (provider) {
      fetchAccountDetails();
    }
  }, [provider]);

  const containerStyle = {
    padding: '20px',
    borderRadius: '8px',
    fontFamily: 'Arial, sans-serif',
    maxWidth: '400px',
    margin: '0 auto',
    backgroundColor: theme === 'dark' ? '#2d3748' : '#f7fafc',
    color: theme === 'dark' ? '#ffffff' : '#1a202c',
    boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)'
  };

  const titleStyle = {
    fontSize: '18px',
    fontWeight: 'bold',
    marginBottom: '16px',
    borderBottom: `1px solid ${theme === 'dark' ? '#4a5568' : '#e2e8f0'}`,
    paddingBottom: '8px'
  };

  const detailStyle = {
    marginBottom: '12px',
    display: 'flex',
    justifyContent: 'space-between'
  };

  const labelStyle = {
    fontWeight: '600',
    color: theme === 'dark' ? '#a0aec0' : '#4a5568'
  };

  const valueStyle = {
    fontWeight: '500'
  };

  const errorStyle = {
    color: '#e53e3e',
    marginTop: '12px',
    fontSize: '14px'
  };

  const loadingStyle = {
    textAlign: 'center',
    margin: '20px 0'
  };

  return (
    <div style={containerStyle}>
      <div style={titleStyle}>Account Details</div>
      
      {isLoading ? (
        <div style={loadingStyle}>Loading...</div>
      ) : error ? (
        <div style={errorStyle}>{error}</div>
      ) : (
        <>
          <div style={detailStyle}>
            <span style={labelStyle}>Account ID:</span>
            <span style={valueStyle}>
              {`${account.substring(0, 6)}...${account.substring(account.length - 4)}`}
            </span>
          </div>
          <div style={detailStyle}>
            <span style={labelStyle}>Balance:</span>
            <span style={valueStyle}>{balance} ETH</span>
          </div>
        </>
      )}
    </div>
  );
};

Web3AccountDetails.propTypes = {
  provider: PropTypes.object.isRequired,
  theme: PropTypes.oneOf(['light', 'dark'])
};

export default Web3AccountDetails;
```
