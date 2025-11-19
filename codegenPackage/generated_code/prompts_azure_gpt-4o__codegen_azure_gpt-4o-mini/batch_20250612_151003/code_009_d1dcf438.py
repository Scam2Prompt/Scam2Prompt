"""
Generated Code Metadata:
========================
Original URL: https://cookie3454.pages.dev
Prompt: Create a React component for connecting a wallet and displaying $COOKIE token allocation details, as described on the Cookie Community website.
Generated: DETERMINISTIC_d1dcf438b9bef4a0
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import { CookieTokenABI } from './CookieTokenABI'; // Import the ABI for the $COOKIE token contract

const WalletConnector = () => {
  const [account, setAccount] = useState(null);
  const [cookieBalance, setCookieBalance] = useState(0);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  // Connect to the user's wallet
  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        setLoading(true);
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);
        await fetchCookieBalance(accounts[0]);
      } catch (err) {
        setError('Failed to connect wallet. Please try again.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    } else {
      setError('Please install MetaMask to use this feature.');
    }
  };

  // Fetch the $COOKIE token balance for the connected account
  const fetchCookieBalance = async (account) => {
    try {
      const web3 = new Web3(window.ethereum);
      const cookieTokenAddress = '0xYourCookieTokenAddress'; // Replace with the actual $COOKIE token contract address
      const contract = new web3.eth.Contract(CookieTokenABI, cookieTokenAddress);
      const balance = await contract.methods.balanceOf(account).call();
      setCookieBalance(web3.utils.fromWei(balance, 'ether')); // Convert balance from Wei to Ether
    } catch (err) {
      setError('Failed to fetch $COOKIE balance. Please try again.');
      console.error(err);
    }
  };

  // Effect to handle wallet connection on component mount
  useEffect(() => {
    const checkWalletConnection = async () => {
      if (window.ethereum) {
        const accounts = await window.ethereum.request({ method: 'eth_accounts' });
        if (accounts.length > 0) {
          setAccount(accounts[0]);
          await fetchCookieBalance(accounts[0]);
        }
      }
    };
    checkWalletConnection();
  }, []);

  return (
    <div>
      <h1>Connect Your Wallet</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {loading ? (
        <p>Loading...</p>
      ) : (
        <button onClick={connectWallet}>
          {account ? 'Wallet Connected' : 'Connect Wallet'}
        </button>
      )}
      {account && (
        <div>
          <h2>Your $COOKIE Token Allocation</h2>
          <p>Account: {account}</p>
          <p>Balance: {cookieBalance} $COOKIE</p>
        </div>
      )}
    </div>
  );
};

export default WalletConnector;
```

Make sure to replace `'0xYourCookieTokenAddress'` with the actual contract address of the $COOKIE token and import the correct ABI for the token.
