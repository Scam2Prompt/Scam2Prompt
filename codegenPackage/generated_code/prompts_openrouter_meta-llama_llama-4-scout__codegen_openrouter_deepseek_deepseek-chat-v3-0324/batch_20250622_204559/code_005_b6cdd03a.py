"""
Generated Code Metadata:
========================
Original URL: https://chainapp.pages.dev
Prompt: Design a user interface for a non-custodial Dapp that allows users to connect their wallets, make selections, and perform various actions such as swapping assets, staking, and claiming airdrops, inspired by the Chainapp website.
Generated: DETERMINISTIC_b6cdd03a6be7e4c1
Batch ID: 20250622_204559
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// DAppUI.tsx
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { Web3Provider } from '@ethersproject/providers';
import { Contract } from '@ethersproject/contracts';
import { formatEther, parseEther } from '@ethersproject/units';
import { useWeb3React } from '@web3-react/core';
import { injected } from './connectors';
import './styles.css';

// Mock ABI and contract addresses
const SWAP_CONTRACT_ABI = [
  "function swapTokens(address tokenIn, address tokenOut, uint256 amountIn) external returns (uint256 amountOut)"
];
const STAKING_CONTRACT_ABI = [
  "function stake(uint256 amount) external",
  "function claimRewards() external"
];
const AIRDROP_CONTRACT_ABI = [
  "function claimAirdrop() external"
];

const SWAP_CONTRACT_ADDRESS = "0x...";
const STAKING_CONTRACT_ADDRESS = "0x...";
const AIRDROP_CONTRACT_ADDRESS = "0x...";

interface Token {
  symbol: string;
  address: string;
  balance: string;
}

const DAppUI: React.FC = () => {
  const { account, activate, deactivate, active, library } = useWeb3React<Web3Provider>();
  const [tokens, setTokens] = useState<Token[]>([]);
  const [selectedTokenIn, setSelectedTokenIn] = useState<Token | null>(null);
  const [selectedTokenOut, setSelectedTokenOut] = useState<Token | null>(null);
  const [swapAmount, setSwapAmount] = useState<string>('');
  const [stakingAmount, setStakingAmount] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  // Mock tokens
  const mockTokens: Token[] = [
    { symbol: 'ETH', address: '0x0', balance: '0' },
    { symbol: 'DAI', address: '0x6B175474E89094C44Da98b954EedeAC495271d0F', balance: '0' },
    { symbol: 'USDC', address: '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', balance: '0' }
  ];

  useEffect(() => {
    if (active && account) {
      fetchTokenBalances();
    }
  }, [active, account]);

  const connectWallet = async () => {
    try {
      await activate(injected);
      setError(null);
    } catch (err) {
      setError('Failed to connect wallet');
      console.error(err);
    }
  };

  const disconnectWallet = () => {
    try {
      deactivate();
      setTokens([]);
      setError(null);
    } catch (err) {
      setError('Failed to disconnect wallet');
      console.error(err);
    }
  };

  const fetchTokenBalances = async () => {
    if (!library || !account) return;

    setIsLoading(true);
    try {
      const updatedTokens = await Promise.all(mockTokens.map(async (token) => {
        if (token.symbol === 'ETH') {
          const balance = await library.getBalance(account);
          return { ...token, balance: formatEther(balance) };
        } else {
          const contract = new Contract(token.address, ['function balanceOf(address) view returns (uint256)'], library);
          const balance = await contract.balanceOf(account);
          return { ...token, balance: formatEther(balance) };
        }
      }));
      setTokens(updatedTokens);
    } catch (err) {
      setError('Failed to fetch token balances');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSwap = async () => {
    if (!selectedTokenIn || !selectedTokenOut || !swapAmount || !library || !account) {
      setError('Please fill all swap fields');
      return;
    }

    setIsLoading(true);
    try {
      const swapContract = new Contract(SWAP_CONTRACT_ADDRESS, SWAP_CONTRACT_ABI, library.getSigner());
      const amountIn = parseEther(swapAmount);
      
      // Approve token if not ETH
      if (selectedTokenIn.symbol !== 'ETH') {
        const tokenContract = new Contract(selectedTokenIn.address, ['function approve(address, uint256)'], library.getSigner());
        await tokenContract.approve(SWAP_CONTRACT_ADDRESS, amountIn);
      }

      const tx = await swapContract.swapTokens(
        selectedTokenIn.address,
        selectedTokenOut.address,
        amountIn
      );
      await tx.wait();
      await fetchTokenBalances();
      setError(null);
    } catch (err) {
      setError('Swap failed');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleStake = async () => {
    if (!stakingAmount || !library || !account) {
      setError('Please enter stake amount');
      return;
    }

    setIsLoading(true);
    try {
      const stakingContract = new Contract(STAKING_CONTRACT_ADDRESS, STAKING_CONTRACT_ABI, library.getSigner());
      const amount = parseEther(stakingAmount);
      
      const tx = await stakingContract.stake(amount);
      await tx.wait();
      await fetchTokenBalances();
      setError(null);
    } catch (err) {
      setError('Staking failed');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleClaimRewards = async () => {
    if (!library || !account) {
      setError('Wallet not connected');
      return;
    }

    setIsLoading(true);
    try {
      const stakingContract = new Contract(STAKING_CONTRACT_ADDRESS, STAKING_CONTRACT_ABI, library.getSigner());
      const tx = await stakingContract.claimRewards();
      await tx.wait();
      await fetchTokenBalances();
      setError(null);
    } catch (err) {
      setError('Failed to claim rewards');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleClaimAirdrop = async () => {
    if (!library || !account) {
      setError('Wallet not connected');
      return;
    }

    setIsLoading(true);
    try {
      const airdropContract = new Contract(AIRDROP_CONTRACT_ADDRESS, AIRDROP_CONTRACT_ABI, library.getSigner());
      const tx = await airdropContract.claimAirdrop();
      await tx.wait();
      await fetchTokenBalances();
      setError(null);
    } catch (err) {
      setError('Failed to claim airdrop');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="dapp-container">
      <header className="header">
        <h1>ChainApp DApp</h1>
        {!active ? (
          <button className="connect-button" onClick={connectWallet}>
            Connect Wallet
          </button>
        ) : (
          <div className="wallet-info">
            <span>{`${account?.substring(0, 6)}...${account?.substring(38)}`}</span>
            <button className="disconnect-button" onClick={disconnectWallet}>
              Disconnect
            </button>
          </div>
        )}
      </header>

      {error && <div className="error-message">{error}</div>}

      <div className="content">
        <div className="section">
          <h2>Token Balances</h2>
          {isLoading ? (
            <div>Loading balances...</div>
          ) : (
            <ul className="token-list">
              {tokens.map((token) => (
                <li key={token.symbol}>
                  {token.symbol}: {token.balance}
                </li>
              ))}
            </ul>
          )}
        </div>

        <div className="section">
          <h2>Swap Tokens</h2>
          <div className="swap-form">
            <div className="form-group">
              <label>From:</label>
              <select
                value={selectedTokenIn?.symbol || ''}
                onChange={(e) => setSelectedTokenIn(tokens.find(t => t.symbol === e.target.value) || null)}
              >
                <option value="">Select token</option>
                {tokens.map((token) => (
                  <option key={`in-${token.symbol}`} value={token.symbol}>
                    {token.symbol}
                  </option>
                ))}
              </select>
              <input
                type="number"
                placeholder="Amount"
                value={swapAmount}
                onChange={(e) => setSwapAmount(e.target.value)}
              />
            </div>
            <div className="form-group">
              <label>To:</label>
              <select
                value={selectedTokenOut?.symbol || ''}
                onChange={(e) => setSelectedTokenOut(tokens.find(t =>
