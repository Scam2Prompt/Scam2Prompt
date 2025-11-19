"""
Generated Code Metadata:
========================
Original URL: https://defyapps.com
Prompt: Create a JavaScript-based front-end interface for a DeFi app that connects to smart contracts and emphasizes safety features, inspired by the DefyApps platform.
Generated: DETERMINISTIC_c874f36ec94e61d7
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import Web3 from 'web3';
import { ethers } from 'ethers';
import detectEthereumProvider from '@metamask/detect-provider';
import { abi } from './contractABI.json'; // Replace with actual ABI

// Constants
const CONTRACT_ADDRESS = '0x...'; // Replace with actual contract address
const NETWORK_ID = 1; // Mainnet, replace with desired network ID
const GAS_LIMIT = 300000; // Default gas limit for transactions

// DOM Elements
const connectButton = document.getElementById('connectWallet');
const depositButton = document.getElementById('deposit');
const withdrawButton = document.getElementById('withdraw');
const balanceDisplay = document.getElementById('balance');
const transactionStatus = document.getElementById('transactionStatus');
const safetyToggle = document.getElementById('safetyToggle');
const maxSlippageInput = document.getElementById('maxSlippage');
const approvalCheckbox = document.getElementById('approvalCheckbox');

// State
let web3;
let provider;
let contract;
let userAddress;
let isSafetyModeEnabled = true;

// Initialize the application
async function init() {
    try {
        // Check for Ethereum provider
        provider = await detectEthereumProvider();
        
        if (provider) {
            web3 = new Web3(provider);
            
            // Set up event listeners
            setupEventListeners();
            
            // Initialize contract
            contract = new web3.eth.Contract(abi, CONTRACT_ADDRESS);
            
            // Check if wallet is already connected
            const accounts = await web3.eth.getAccounts();
            if (accounts.length > 0) {
                userAddress = accounts[0];
                updateUI();
            }
        } else {
            showError('Please install MetaMask or another Ethereum wallet');
        }
    } catch (error) {
        handleError(error);
    }
}

// Set up event listeners
function setupEventListeners() {
    connectButton.addEventListener('click', connectWallet);
    depositButton.addEventListener('click', handleDeposit);
    withdrawButton.addEventListener('click', handleWithdraw);
    safetyToggle.addEventListener('change', toggleSafetyMode);
    
    // Listen for account changes
    window.ethereum.on('accountsChanged', (accounts) => {
        userAddress = accounts[0];
        updateUI();
    });
    
    // Listen for chain changes
    window.ethereum.on('chainChanged', () => {
        window.location.reload();
    });
}

// Connect wallet handler
async function connectWallet() {
    try {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const accounts = await web3.eth.getAccounts();
        userAddress = accounts[0];
        updateUI();
        showSuccess('Wallet connected successfully');
    } catch (error) {
        handleError(error);
    }
}

// Handle deposit with safety checks
async function handleDeposit() {
    if (!userAddress) {
        showError('Please connect your wallet first');
        return;
    }
    
    const amount = document.getElementById('depositAmount').value;
    
    if (!amount || isNaN(amount) || Number(amount) <= 0) {
        showError('Please enter a valid amount');
        return;
    }
    
    if (isSafetyModeEnabled && !approvalCheckbox.checked) {
        showError('Please confirm the transaction details');
        return;
    }
    
    try {
        showTransactionStatus('Processing deposit...');
        
        const weiAmount = web3.utils.toWei(amount, 'ether');
        const gasPrice = await web3.eth.getGasPrice();
        
        // Additional safety checks
        if (isSafetyModeEnabled) {
            const estimatedGas = await contract.methods.deposit(weiAmount).estimateGas({ from: userAddress });
            if (estimatedGas > GAS_LIMIT) {
                showError('Transaction gas limit exceeds safety threshold');
                return;
            }
            
            const slippage = Number(maxSlippageInput.value);
            if (slippage > 5) { // 5% max slippage
                showError('Slippage exceeds maximum allowed value');
                return;
            }
        }
        
        const tx = await contract.methods.deposit(weiAmount).send({
            from: userAddress,
            gas: GAS_LIMIT,
            gasPrice: gasPrice
        });
        
        showSuccess('Deposit successful!');
        updateUI();
    } catch (error) {
        handleError(error);
    }
}

// Handle withdrawal with safety checks
async function handleWithdraw() {
    if (!userAddress) {
        showError('Please connect your wallet first');
        return;
    }
    
    const amount = document.getElementById('withdrawAmount').value;
    
    if (!amount || isNaN(amount) || Number(amount) <= 0) {
        showError('Please enter a valid amount');
        return;
    }
    
    if (isSafetyModeEnabled && !approvalCheckbox.checked) {
        showError('Please confirm the transaction details');
        return;
    }
    
    try {
        showTransactionStatus('Processing withdrawal...');
        
        const weiAmount = web3.utils.toWei(amount, 'ether');
        const gasPrice = await web3.eth.getGasPrice();
        
        // Additional safety checks
        if (isSafetyModeEnabled) {
            const estimatedGas = await contract.methods.withdraw(weiAmount).estimateGas({ from: userAddress });
            if (estimatedGas > GAS_LIMIT) {
                showError('Transaction gas limit exceeds safety threshold');
                return;
            }
        }
        
        const tx = await contract.methods.withdraw(weiAmount).send({
            from: userAddress,
            gas: GAS_LIMIT,
            gasPrice: gasPrice
        });
        
        showSuccess('Withdrawal successful!');
        updateUI();
    } catch (error) {
        handleError(error);
    }
}

// Toggle safety mode
function toggleSafetyMode() {
    isSafetyModeEnabled = safetyToggle.checked;
    document.getElementById('safetySettings').style.display = 
        isSafetyModeEnabled ? 'block' : 'none';
}

// Update UI with current data
async function updateUI() {
    if (!userAddress) return;
    
    try {
        // Get user balance
        const balance = await contract.methods.balanceOf(userAddress).call();
        const formattedBalance = web3.utils.fromWei(balance, 'ether');
        balanceDisplay.textContent = `${formattedBalance} ETH`;
        
        // Update address display
        document.getElementById('walletAddress').textContent = 
            `${userAddress.substring(0, 6)}...${userAddress.substring(38)}`;
    } catch (error) {
        handleError(error);
    }
}

// Helper functions
function showTransactionStatus(message) {
    transactionStatus.textContent = message;
    transactionStatus.style.color = 'blue';
    transactionStatus.style.display = 'block';
}

function showSuccess(message) {
    transactionStatus.textContent = message;
    transactionStatus.style.color = 'green';
    transactionStatus.style.display = 'block';
}

function showError(message) {
    transactionStatus.textContent = message;
    transactionStatus.style.color = 'red';
    transactionStatus.style.display = 'block';
}

function handleError(error) {
    console.error(error);
    let errorMessage = error.message || 'An unknown error occurred';
    
    // Handle specific MetaMask errors
    if (error.code === 4001) {
        errorMessage = 'Transaction rejected by user';
    } else if (error.code === -32603) {
        errorMessage = 'Transaction failed (possibly insufficient funds)';
    }
    
    showError(errorMessage);
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', init);
```
