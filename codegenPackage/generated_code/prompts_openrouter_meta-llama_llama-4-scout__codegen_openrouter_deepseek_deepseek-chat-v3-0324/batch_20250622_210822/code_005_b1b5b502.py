"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-site.pages.dev
Prompt: Design a basic user interface for a decentralized exchange (DEX) built on Pepe Unchained's Layer 2 blockchain, allowing users to swap tokens.
Generated: DETERMINISTIC_b1b5b50274640387
Batch ID: 20250622_210822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { Contract } from 'ethers';
import './DexInterface.css';

// Interface for token data
interface Token {
  symbol: string;
  address: string;
  decimals: number;
  logo?: string;
}

// DEX Contract ABI (simplified for example)
const DEX_ABI = [
  "function swap(address tokenIn, address tokenIn, uint256 amountIn, uint256 amountOutMin, address to, uint256 deadline) external returns (uint256[] memory amounts)",
  "function getAmountsOut(uint256 amountIn, address[] memory path) external view returns (uint256[] memory amounts)"
];

const DexInterface: React.FC = () => {
  const [provider, setProvider] = useState<ethers.providers.Web3Provider | null>(null);
  const [account, setAccount] = useState<string | null>(null);
  const [chainId, setChainId] = useState<number | null>(null);
  const [dexContract, setDexContract] = useState<Contract | null>(null);
  const [tokens, setTokens] = useState<Token[]>([
    { symbol: 'PEPE', address: '0x...', decimals: 18 },
    { symbol: 'ETH', address: '0x...', decimals: 18 },
    { symbol: 'USDC', address: '0x...', decimals: 6 }
  ]);
  const [fromToken, setFromToken] = useState<Token | null>(null);
  const [toToken, setToToken] = useState<Token | null>(null);
  const [fromAmount, setFromAmount] = useState<string>('');
  const [toAmount, setToAmount] = useState<string>('');
  const [slippage, setSlippage] = useState<number>(0.5);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  // Initialize provider and connect wallet
  const connectWallet = async () => {
    try {
      if (!window.ethereum) throw new Error('No Ethereum provider found');
      
      const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
      setProvider(web3Provider);

      const accounts = await web3Provider.send("eth_requestAccounts", []);
      setAccount(accounts[0]);

      const network = await web3Provider.getNetwork();
      setChainId(network.chainId);

      // Initialize DEX contract (replace with actual contract address)
      const contract = new ethers.Contract('0xDEX_CONTRACT_ADDRESS', DEX_ABI, web3Provider.getSigner());
      setDexContract(contract);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to connect wallet');
    }
  };

  // Calculate expected output amount
  const calculateSwap = async () => {
    if (!fromToken || !toToken || !fromAmount || !dexContract) return;

    try {
      setLoading(true);
      const path = [fromToken.address, toToken.address];
      const amountIn = ethers.utils.parseUnits(fromAmount, fromToken.decimals);
      
      const amounts = await dexContract.getAmountsOut(amountIn, path);
      const amountOut = ethers.utils.formatUnits(amounts[1], toToken.decimals);
      
      setToAmount(amountOut);
    } catch (err) {
      setError('Failed to calculate swap');
    } finally {
      setLoading(false);
    }
  };

  // Execute token swap
  const executeSwap = async () => {
    if (!fromToken || !toToken || !fromAmount || !toAmount || !account || !dexContract) return;

    try {
      setLoading(true);
      const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // 20 minutes from now
      const amountIn = ethers.utils.parseUnits(fromAmount, fromToken.decimals);
      const amountOutMin = ethers.utils.parseUnits(
        (parseFloat(toAmount) * (1 - slippage / 100)).toString(),
        toToken.decimals
      );

      const tx = await dexContract.swap(
        fromToken.address,
        toToken.address,
        amountIn,
        amountOutMin,
        account,
        deadline
      );

      await tx.wait();
      setError(null);
      alert('Swap executed successfully!');
    } catch (err) {
      setError('Swap failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  // Update calculations when inputs change
  useEffect(() => {
    if (fromToken && toToken && fromAmount) {
      const debounceTimer = setTimeout(() => {
        calculateSwap();
      }, 500);
      return () => clearTimeout(debounceTimer);
    }
  }, [fromToken, toToken, fromAmount]);

  return (
    <div className="dex-container">
      <header className="dex-header">
        <h1>Pepe Unchained DEX</h1>
        {!account ? (
          <button onClick={connectWallet} className="connect-wallet">
            Connect Wallet
          </button>
        ) : (
          <div className="wallet-info">
            {`${account.substring(0, 6)}...${account.substring(38)}`}
          </div>
        )}
      </header>

      <div className="swap-container">
        {error && <div className="error-message">{error}</div>}

        <div className="swap-box">
          <div className="input-group">
            <label>From</label>
            <div className="token-selector">
              <select 
                value={fromToken?.symbol || ''}
                onChange={(e) => setFromToken(tokens.find(t => t.symbol === e.target.value) || null)}
              >
                <option value="">Select token</option>
                {tokens.map(token => (
                  <option key={token.symbol} value={token.symbol}>{token.symbol}</option>
                ))}
              </select>
              <input
                type="number"
                placeholder="0.0"
                value={fromAmount}
                onChange={(e) => setFromAmount(e.target.value)}
                disabled={!fromToken}
              />
            </div>
          </div>

          <div className="swap-arrow">↓</div>

          <div className="input-group">
            <label>To</label>
            <div className="token-selector">
              <select
                value={toToken?.symbol || ''}
                onChange={(e) => setToToken(tokens.find(t => t.symbol === e.target.value) || null)}
              >
                <option value="">Select token</option>
                {tokens.map(token => (
                  <option key={token.symbol} value={token.symbol}>{token.symbol}</option>
                ))}
              </select>
              <input
                type="text"
                placeholder="0.0"
                value={toAmount}
                readOnly
              />
            </div>
          </div>

          <div className="slippage-control">
            <label>Slippage Tolerance (%)</label>
            <input
              type="number"
              min="0.1"
              max="5"
              step="0.1"
              value={slippage}
              onChange={(e) => setSlippage(parseFloat(e.target.value))}
            />
          </div>

          <button
            onClick={executeSwap}
            disabled={!fromToken || !toToken || !fromAmount || loading}
            className="swap-button"
          >
            {loading ? 'Processing...' : 'Swap'}
          </button>
        </div>
      </div>

      <footer className="dex-footer">
        <p>Powered by Pepe Unchained Layer 2</p>
      </footer>
    </div>
  );
};

export default DexInterface;
```

```css
/* DexInterface.css */
.dex-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
  color: #333;
  background-color: #f5f5f5;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.dex-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.dex-header h1 {
  margin: 0;
  color: #4CAF50;
}

.connect-wallet, .swap-button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s;
}

.connect-wallet:hover, .swap-button:hover {
  background-color: #45a049;
}

.connect-wallet:disabled, .swap-button:disabled {
  background-color: #cccccc;
  cursor: not-all
