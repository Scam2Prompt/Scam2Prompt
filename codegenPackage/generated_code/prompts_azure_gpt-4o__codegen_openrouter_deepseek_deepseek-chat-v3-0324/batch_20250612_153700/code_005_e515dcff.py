"""
Generated Code Metadata:
========================
Original URL: https://furies-mystery.pages.dev
Prompt: Provide an example of a decentralized application (dApp) interface that allows users to connect their wallet, view $MYSTERY token holdings, and execute swaps using the Uniswap API.
Generated: DETERMINISTIC_e515dcff0c151a4e
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { abi as MYSTERY_ABI } from './MysteryTokenABI.json';
import { abi as UNISWAP_ROUTER_ABI } from '@uniswap/v2-periphery/build/UniswapV2Router02.json';

// Contract addresses (replace with actual addresses)
const MYSTERY_TOKEN_ADDRESS = '0x...';
const UNISWAP_ROUTER_ADDRESS = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D';

const App = () => {
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);
  const [account, setAccount] = useState('');
  const [mysteryBalance, setMysteryBalance] = useState('0');
  const [swapAmount, setSwapAmount] = useState('');
  const [tokenToReceive, setTokenToReceive] = useState('ETH');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  // Initialize provider when component mounts
  useEffect(() => {
    if (window.ethereum) {
      const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
      setProvider(web3Provider);
    } else {
      setError('Please install MetaMask or another Web3 provider');
    }
  }, []);

  // Connect wallet handler
  const connectWallet = async () => {
    try {
      setIsLoading(true);
      setError('');
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = web3Provider.getSigner();
      const address = await signer.getAddress();
      
      setProvider(web3Provider);
      setSigner(signer);
      setAccount(address);
      await fetchMysteryBalance(signer);
    } catch (err) {
      setError('Failed to connect wallet: ' + err.message);
    } finally {
      setIsLoading(false);
    }
  };

  // Fetch $MYSTERY token balance
  const fetchMysteryBalance = async (signer) => {
    try {
      const mysteryToken = new ethers.Contract(MYSTERY_TOKEN_ADDRESS, MYSTERY_ABI, signer);
      const balance = await mysteryToken.balanceOf(account);
      setMysteryBalance(ethers.utils.formatUnits(balance, 18)); // Assuming 18 decimals
    } catch (err) {
      setError('Failed to fetch balance: ' + err.message);
    }
  };

  // Execute swap on Uniswap
  const executeSwap = async () => {
    if (!signer || !swapAmount) return;
    
    try {
      setIsLoading(true);
      setError('');
      
      const uniswapRouter = new ethers.Contract(
        UNISWAP_ROUTER_ADDRESS,
        UNISWAP_ROUTER_ABI,
        signer
      );

      const mysteryToken = new ethers.Contract(MYSTERY_TOKEN_ADDRESS, MYSTERY_ABI, signer);
      const amountIn = ethers.utils.parseUnits(swapAmount, 18);
      
      // Approve token spending first
      const approveTx = await mysteryToken.approve(UNISWAP_ROUTER_ADDRESS, amountIn);
      await approveTx.wait();

      // Set up swap parameters
      const path = [MYSTERY_TOKEN_ADDRESS, ethers.constants.AddressZero]; // MYSTERY to ETH
      const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // 20 minutes from now
      
      // Execute swap
      const swapTx = await uniswapRouter.swapExactTokensForETH(
        amountIn,
        0, // Minimum amount out (slippage protection would be better in production)
        path,
        account,
        deadline
      );
      
      await swapTx.wait();
      await fetchMysteryBalance(signer); // Refresh balance
    } catch (err) {
      setError('Swap failed: ' + err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app">
      <header>
        <h1>$MYSTERY Token Swap</h1>
      </header>

      <main>
        {!account ? (
          <button onClick={connectWallet} disabled={isLoading}>
            {isLoading ? 'Connecting...' : 'Connect Wallet'}
          </button>
        ) : (
          <div className="wallet-info">
            <p>Connected: {`${account.substring(0, 6)}...${account.substring(38)}`}</p>
            <p>$MYSTERY Balance: {mysteryBalance}</p>
          </div>
        )}

        <div className="swap-container">
          <h2>Swap $MYSTERY</h2>
          <div className="swap-input">
            <input
              type="number"
              value={swapAmount}
              onChange={(e) => setSwapAmount(e.target.value)}
              placeholder="Amount"
              disabled={!account}
            />
            <span>$MYSTERY</span>
          </div>
          <div className="swap-output">
            <input
              type="text"
              value={tokenToReceive}
              onChange={(e) => setTokenToReceive(e.target.value)}
              disabled
            />
          </div>
          <button
            onClick={executeSwap}
            disabled={!account || !swapAmount || isLoading}
          >
            {isLoading ? 'Processing...' : 'Swap'}
          </button>
        </div>

        {error && <p className="error">{error}</p>}
      </main>
    </div>
  );
};

export default App;
```
