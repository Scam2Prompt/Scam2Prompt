"""
Generated Code Metadata:
========================
Original URL: https://pepe-buy.pages.dev
Prompt: Develop a JavaScript-based frontend interface for purchasing and staking $PEPU tokens, integrating payment methods like ETH, USDT, and BNB.
Generated: DETERMINISTIC_f62a382492ccfe39
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries (assuming this is a React project)
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
import axios from 'axios';
import './App.css';

// Contract ABIs (simplified for example)
const PEPU_TOKEN_ABI = [
  // ERC20 standard functions
  "function balanceOf(address owner) view returns (uint256)",
  "function transfer(address to, uint256 amount) returns (bool)",
  "function approve(address spender, uint256 amount) returns (bool)",
  "function allowance(address owner, address spender) view returns (uint256)",
  // Staking functions
  "function stake(uint256 amount) public",
  "function unstake(uint256 amount) public",
  "function getStakedAmount(address user) public view returns (uint256)",
  "function getRewards(address user) public view returns (uint256)",
  "function claimRewards() public"
];

const TOKEN_SALE_ABI = [
  "function buyTokensWithETH() payable",
  "function buyTokensWithUSDT(uint256 amount)",
  "function buyTokensWithBNB(uint256 amount)",
  "function getTokenPrice() view returns (uint256)"
];

// Contract addresses (example values)
const CONTRACT_ADDRESSES = {
  PEPU_TOKEN: "0x123...",
  TOKEN_SALE: "0x456...",
  USDT: "0x789...",
  BNB: "0xabc..."
};

// Payment options
const PAYMENT_OPTIONS = [
  { value: 'eth', label: 'ETH' },
  { value: 'usdt', label: 'USDT' },
  { value: 'bnb', label: 'BNB' }
];

const App = () => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState(0);
  const [stakedAmount, setStakedAmount] = useState(0);
  const [rewards, setRewards] = useState(0);
  const [paymentMethod, setPaymentMethod] = useState('eth');
  const [amount, setAmount] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  // Initialize Web3 and contracts
  useEffect(() => {
    const init = async () => {
      try {
        if (window.ethereum) {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);
          
          await window.ethereum.enable();
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);
          
          loadContractData(web3Instance, accounts[0]);
        } else {
          setError('Please install MetaMask or another Web3 provider');
        }
      } catch (err) {
        setError(`Error connecting to wallet: ${err.message}`);
      }
    };
    
    init();
    
    // Listen for account changes
    if (window.ethereum) {
      window.ethereum.on('accountsChanged', (accounts) => {
        setAccount(accounts[0]);
        if (web3) loadContractData(web3, accounts[0]);
      });
    }
    
    return () => {
      if (window.ethereum) {
        window.ethereum.removeListener('accountsChanged');
      }
    };
  }, []);

  const loadContractData = async (web3Instance, account) => {
    try {
      const pepuToken = new web3Instance.eth.Contract(PEPU_TOKEN_ABI, CONTRACT_ADDRESSES.PEPU_TOKEN);
      
      const balance = await pepuToken.methods.balanceOf(account).call();
      setBalance(web3Instance.utils.fromWei(balance, 'ether'));
      
      const staked = await pepuToken.methods.getStakedAmount(account).call();
      setStakedAmount(web3Instance.utils.fromWei(staked, 'ether'));
      
      const rewards = await pepuToken.methods.getRewards(account).call();
      setRewards(web3Instance.utils.fromWei(rewards, 'ether'));
    } catch (err) {
      setError(`Error loading contract data: ${err.message}`);
    }
  };

  const handleBuyTokens = async () => {
    if (!amount || isNaN(amount) || Number(amount) <= 0) {
      setError('Please enter a valid amount');
      return;
    }
    
    setLoading(true);
    setError('');
    setSuccess('');
    
    try {
      const tokenSale = new web3.eth.Contract(TOKEN_SALE_ABI, CONTRACT_ADDRESSES.TOKEN_SALE);
      const amountWei = web3.utils.toWei(amount, 'ether');
      
      switch (paymentMethod) {
        case 'eth':
          await tokenSale.methods.buyTokensWithETH().send({
            from: account,
            value: amountWei
          });
          break;
          
        case 'usdt':
          const usdtContract = new web3.eth.Contract(PEPU_TOKEN_ABI, CONTRACT_ADDRESSES.USDT);
          await usdtContract.methods.approve(CONTRACT_ADDRESSES.TOKEN_SALE, amountWei).send({ from: account });
          await tokenSale.methods.buyTokensWithUSDT(amountWei).send({ from: account });
          break;
          
        case 'bnb':
          const bnbContract = new web3.eth.Contract(PEPU_TOKEN_ABI, CONTRACT_ADDRESSES.BNB);
          await bnbContract.methods.approve(CONTRACT_ADDRESSES.TOKEN_SALE, amountWei).send({ from: account });
          await tokenSale.methods.buyTokensWithBNB(amountWei).send({ from: account });
          break;
          
        default:
          throw new Error('Invalid payment method');
      }
      
      setSuccess('Tokens purchased successfully!');
      loadContractData(web3, account);
    } catch (err) {
      setError(`Error purchasing tokens: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleStake = async () => {
    if (!amount || isNaN(amount) || Number(amount) <= 0) {
      setError('Please enter a valid amount');
      return;
    }
    
    if (Number(amount) > Number(balance)) {
      setError('Insufficient balance');
      return;
    }
    
    setLoading(true);
    setError('');
    setSuccess('');
    
    try {
      const pepuToken = new web3.eth.Contract(PEPU_TOKEN_ABI, CONTRACT_ADDRESSES.PEPU_TOKEN);
      const amountWei = web3.utils.toWei(amount, 'ether');
      
      await pepuToken.methods.approve(CONTRACT_ADDRESSES.PEPU_TOKEN, amountWei).send({ from: account });
      await pepuToken.methods.stake(amountWei).send({ from: account });
      
      setSuccess('Tokens staked successfully!');
      loadContractData(web3, account);
    } catch (err) {
      setError(`Error staking tokens: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleUnstake = async () => {
    if (!amount || isNaN(amount) || Number(amount) <= 0) {
      setError('Please enter a valid amount');
      return;
    }
    
    if (Number(amount) > Number(stakedAmount)) {
      setError('Insufficient staked amount');
      return;
    }
    
    setLoading(true);
    setError('');
    setSuccess('');
    
    try {
      const pepuToken = new web3.eth.Contract(PEPU_TOKEN_ABI, CONTRACT_ADDRESSES.PEPU_TOKEN);
      const amountWei = web3.utils.toWei(amount, 'ether');
      
      await pepuToken.methods.unstake(amountWei).send({ from: account });
      
      setSuccess('Tokens unstaked successfully!');
      loadContractData(web3, account);
    } catch (err) {
      setError(`Error unstaking tokens: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleClaimRewards = async () => {
    setLoading(true);
    setError('');
    setSuccess('');
    
    try {
      const pepuToken = new web3.eth.Contract(PEPU_TOKEN_ABI, CONTRACT_ADDRESSES.PEPU_TOKEN);
      
      await pepuToken.methods.claimRewards().send({ from: account });
      
      setSuccess('Rewards claimed successfully!');
      loadContractData(web3, account);
    } catch (err) {
      setError(`Error claiming rewards: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header>
        <h1>$PEPU Token Staking</h1>
        {account ? (
          <p
