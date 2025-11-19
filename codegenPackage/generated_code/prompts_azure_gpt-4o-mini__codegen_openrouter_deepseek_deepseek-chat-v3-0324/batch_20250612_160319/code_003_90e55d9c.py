"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter.productsway.com
Prompt: Generate a React component for displaying account balance in a DApp, referencing the features mentioned on the Dapp Starter site.
Generated: DETERMINISTIC_90e55d9c25ba0a2e
Batch ID: 20250612_160319
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
import { useWeb3React } from '@web3-react/core';

/**
 * AccountBalance component displays the user's account balance in ETH.
 * 
 * Features:
 * - Fetches balance from connected wallet
 * - Auto-refreshes on account/network changes
 * - Displays formatted ETH value
 * - Handles loading and error states
 * 
 * @param {Object} props - Component props
 * @param {string} [props.className] - Additional CSS class names
 * @param {function} [props.onError] - Error callback handler
 */
const AccountBalance = ({ className = '', onError = () => {} }) => {
  const { account, library, chainId } = useWeb3React();
  const [balance, setBalance] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchBalance = async () => {
    if (!account || !library) {
      setBalance(null);
      return;
    }

    try {
      setIsLoading(true);
      setError(null);
      const balanceWei = await library.getBalance(account);
      const balanceEth = ethers.utils.formatEther(balanceWei);
      setBalance(parseFloat(balanceEth).toFixed(4));
    } catch (err) {
      console.error('Error fetching balance:', err);
      setError('Failed to fetch balance');
      onError(err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchBalance();
  }, [account, library, chainId]);

  return (
    <div className={`account-balance ${className}`}>
      {isLoading ? (
        <span className="balance-loading">Loading...</span>
      ) : error ? (
        <span className="balance-error">{error}</span>
      ) : balance !== null ? (
        <>
          <span className="balance-value">{balance}</span>
          <span className="balance-currency">ETH</span>
        </>
      ) : (
        <span className="balance-disconnected">Not connected</span>
      )}
    </div>
  );
};

AccountBalance.propTypes = {
  className: PropTypes.string,
  onError: PropTypes.func,
};

export default AccountBalance;
```
