"""
Generated Code Metadata:
========================
Original URL: https://btcetfcoinn.pages.dev
Prompt: Develop a DApp interface for buying and staking BTCETF tokens, including wallet connection functionality and presale purchase options using ETH, BNB, or USDT.
Generated: DETERMINISTIC_4223fd4d49045619
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

// Contract ABIs (replace with actual contract ABIs)
const BTCETF_ABI = [/* BTCETF Token ABI */];
const PRESALE_ABI = [/* Presale Contract ABI */];
const STAKING_ABI = [/* Staking Contract ABI */];

// Contract addresses (replace with actual addresses)
const BTCETF_ADDRESS = '0x...';
const PRESALE_ADDRESS = '0x...';
const STAKING_ADDRESS = '0x...';

// Supported networks
const SUPPORTED_NETWORKS = {
  1: 'Ethereum Mainnet',
  56: 'Binance Smart Chain',
  97: 'Binance Smart Chain Testnet'
};

const App = () => {
  const [web3, setWeb3] = useState(null);
  const [provider, setProvider] = useState(null);
  const [account, setAccount] = useState('');
  const [chainId, setChainId] = useState('');
  const [balance, setBalance] = useState('0');
  const [btcetfBalance, setBtcetfBalance] = useState('0');
  const [stakedAmount, setStakedAmount] = useState('0');
  const [rewards, setRewards] = useState('0');
  const [presaleAmount, setPresaleAmount] = useState('');
  const [stakeAmount, setStakeAmount] = useState('');
  const [unstakeAmount, setUnstakeAmount] = useState('');
  const [selectedToken, setSelectedToken] = useState('ETH');
  const [isLoading, setIsLoading] = useState(false);

  // Initialize Web3 and provider
  const initWeb3 = async () => {
    if (window.ethereum) {
      try {
        const web3Instance = new Web3(window.ethereum);
        const providerInstance = new ethers.providers.Web3Provider(window.ethereum);
        
        setWeb3(web3Instance);
        setProvider(providerInstance);
        
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);
        
        // Get chain ID
        const chainId = await web3Instance.eth.getChainId();
        setChainId(chainId);
        
        // Set up event listeners
        window.ethereum.on('accountsChanged', handleAccountsChanged);
        window.ethereum.on('chainChanged', handleChainChanged);
        
        // Load initial data
        loadAccountData();
      } catch (error) {
        console.error('Error initializing Web3:', error);
        toast.error('Failed to connect wallet');
      }
    } else {
      toast.error('Please install MetaMask or another Web3 provider');
    }
  };

  // Handle account changes
  const handleAccountsChanged = (accounts) => {
    if (accounts.length === 0) {
      toast.info('Please connect to MetaMask');
    } else {
      setAccount(accounts[0]);
      loadAccountData();
    }
  };

  // Handle chain changes
  const handleChainChanged = (chainId) => {
    window.location.reload();
  };

  // Load account data
  const loadAccountData = async () => {
    if (!web3 || !account) return;
    
    try {
      setIsLoading(true);
      
      // Get native token balance
      const nativeBalance = await web3.eth.getBalance(account);
      setBalance(web3.utils.fromWei(nativeBalance, 'ether'));
      
      // Get BTCETF token balance
      const btcetfContract = new web3.eth.Contract(BTCETF_ABI, BTCETF_ADDRESS);
      const btcetfBalance = await btcetfContract.methods.balanceOf(account).call();
      setBtcetfBalance(web3.utils.fromWei(btcetfBalance, 'ether'));
      
      // Get staking info
      const stakingContract = new web3.eth.Contract(STAKING_ABI, STAKING_ADDRESS);
      const staked = await stakingContract.methods.stakedAmount(account).call();
      setStakedAmount(web3.utils.fromWei(staked, 'ether'));
      
      const reward = await stakingContract.methods.calculateRewards(account).call();
      setRewards(web3.utils.fromWei(reward, 'ether'));
      
    } catch (error) {
      console.error('Error loading account data:', error);
      toast.error('Failed to load account data');
    } finally {
      setIsLoading(false);
    }
  };

  // Buy tokens in presale
  const buyPresaleTokens = async () => {
    if (!web3 || !account || !presaleAmount || parseFloat(presaleAmount) <= 0) {
      toast.error('Please enter a valid amount');
      return;
    }
    
    try {
      setIsLoading(true);
      const presaleContract = new web3.eth.Contract(PRESALE_ABI, PRESALE_ADDRESS);
      const amountWei = web3.utils.toWei(presaleAmount, 'ether');
      
      let tx;
      if (selectedToken === 'ETH') {
        tx = await presaleContract.methods.buyWithETH().send({
          from: account,
          value: amountWei
        });
      } else {
        // For BNB or USDT, we would need to approve and call buyWithToken
        // This is simplified - actual implementation would need token contract interaction
        toast.error('Token purchase not implemented yet');
        return;
      }
      
      toast.success('Purchase successful!');
      loadAccountData();
    } catch (error) {
      console.error('Error buying tokens:', error);
      toast.error('Purchase failed');
    } finally {
      setIsLoading(false);
    }
  };

  // Stake tokens
  const stakeTokens = async () => {
    if (!web3 || !account || !stakeAmount || parseFloat(stakeAmount) <= 0) {
      toast.error('Please enter a valid amount');
      return;
    }
    
    try {
      setIsLoading(true);
      const stakingContract = new web3.eth.Contract(STAKING_ABI, STAKING_ADDRESS);
      const btcetfContract = new web3.eth.Contract(BTCETF_ABI, BTCETF_ADDRESS);
      
      const amountWei = web3.utils.toWei(stakeAmount, 'ether');
      
      // Approve staking contract to spend tokens
      await btcetfContract.methods.approve(STAKING_ADDRESS, amountWei).send({ from: account });
      
      // Stake tokens
      await stakingContract.methods.stake(amountWei).send({ from: account });
      
      toast.success('Tokens staked successfully!');
      loadAccountData();
    } catch (error) {
      console.error('Error staking tokens:', error);
      toast.error('Staking failed');
    } finally {
      setIsLoading(false);
    }
  };

  // Unstake tokens
  const unstakeTokens = async () => {
    if (!web3 || !account || !unstakeAmount || parseFloat(unstakeAmount) <= 0) {
      toast.error('Please enter a valid amount');
      return;
    }
    
    try {
      setIsLoading(true);
      const stakingContract = new web3.eth.Contract(STAKING_ABI, STAKING_ADDRESS);
      const amountWei = web3.utils.toWei(unstakeAmount, 'ether');
      
      await stakingContract.methods.unstake(amountWei).send({ from: account });
      
      toast.success('Tokens unstaked successfully!');
      loadAccountData();
    } catch (error) {
      console.error('Error unstaking tokens:', error);
      toast.error('Unstaking failed');
    } finally {
      setIsLoading(false);
    }
  };

  // Claim rewards
  const claimRewards = async () => {
    if (!web3 || !account) return;
    
    try {
      setIsLoading(true);
      const stakingContract = new web3.eth.Contract(STAKING_ABI, STAKING_ADDRESS);
      
      await stakingContract.methods.claimRewards().send({ from: account });
      
      toast.success('Rewards claimed successfully!');
      loadAccountData();
    } catch (error) {
      console.error('Error claiming rewards:', error);
      toast.error('Claim failed');
    } finally {
      setIsLoading(false);
    }
  };

  // Format network name
  const getNetworkName = () => {
    return SUPPORTED_NETWORKS[chainId] || `Unknown Network (${chainId})`;
  };

  return (
    <div className="app">
      <ToastContainer position="top-right" autoClose={5000} />
      
      <header>
        <h1>BTCETF DApp</h1>
        {account ? (
          <div className="wallet-info">
            <span>{account.substring(0, 6
