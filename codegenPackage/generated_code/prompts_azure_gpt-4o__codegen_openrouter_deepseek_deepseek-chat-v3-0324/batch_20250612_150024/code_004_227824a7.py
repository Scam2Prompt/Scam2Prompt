"""
Generated Code Metadata:
========================
Original URL: https://interface-git-fork-chenxsan-bugfix-fix-scroll-top-uniswap.vercel.app
Prompt: Write a script to enable JavaScript functionality for a decentralized exchange interface, similar to the Uniswap Interface.
Generated: DETERMINISTIC_227824a74792629e
Batch ID: 20250612_150024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
/**
 * Decentralized Exchange Interface Script
 * Provides core functionality for a DEX interface similar to Uniswap
 */

// Import required libraries (assuming ES modules)
import { ethers } from 'ethers';
import { abi as ERC20_ABI } from './erc20.json';
import { abi as EXCHANGE_ABI } from './exchange.json';

// Configuration
const CONFIG = {
  defaultProvider: 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID',
  exchangeAddress: '0xEXCHANGE_CONTRACT_ADDRESS',
  defaultSlippage: 0.5, // 0.5%
  defaultDeadline: 20, // 20 minutes
};

// Global state
const state = {
  provider: null,
  signer: null,
  account: null,
  tokens: {},
  balances: {},
  exchange: null,
  initialized: false,
};

/**
 * Initialize the DEX interface
 * @param {Object} options - Initialization options
 * @param {string} [options.providerUrl] - Custom provider URL
 * @param {boolean} [options.connectWallet] - Whether to connect wallet on init
 */
export async function initDEX(options = {}) {
  try {
    // Initialize provider
    const providerUrl = options.providerUrl || CONFIG.defaultProvider;
    state.provider = new ethers.providers.JsonRpcProvider(providerUrl);

    // Initialize exchange contract
    state.exchange = new ethers.Contract(
      CONFIG.exchangeAddress,
      EXCHANGE_ABI,
      state.provider
    );

    // Connect wallet if requested
    if (options.connectWallet) {
      await connectWallet();
    }

    state.initialized = true;
    console.log('DEX interface initialized');
  } catch (error) {
    console.error('Failed to initialize DEX interface:', error);
    throw error;
  }
}

/**
 * Connect user's wallet
 */
export async function connectWallet() {
  try {
    if (!window.ethereum) {
      throw new Error('No Ethereum provider found');
    }

    // Request account access
    const accounts = await window.ethereum.request({
      method: 'eth_requestAccounts',
    });

    state.account = accounts[0];
    state.signer = new ethers.providers.Web3Provider(window.ethereum).getSigner();

    // Update exchange contract with signer
    state.exchange = state.exchange.connect(state.signer);

    // Listen for account changes
    window.ethereum.on('accountsChanged', (newAccounts) => {
      state.account = newAccounts[0] || null;
      if (state.account) {
        console.log('Account changed:', state.account);
        // Trigger UI update
        if (typeof onAccountChanged === 'function') {
          onAccountChanged(state.account);
        }
      } else {
        console.log('Account disconnected');
      }
    });

    console.log('Wallet connected:', state.account);
    return state.account;
  } catch (error) {
    console.error('Failed to connect wallet:', error);
    throw error;
  }
}

/**
 * Get token balance for current account
 * @param {string} tokenAddress - Token contract address
 */
export async function getTokenBalance(tokenAddress) {
  if (!state.initialized) throw new Error('DEX not initialized');
  if (!state.account) throw new Error('No account connected');

  try {
    const tokenContract = new ethers.Contract(
      tokenAddress,
      ERC20_ABI,
      state.signer || state.provider
    );

    const balance = await tokenContract.balanceOf(state.account);
    state.balances[tokenAddress] = balance;

    return balance;
  } catch (error) {
    console.error(`Failed to get balance for token ${tokenAddress}:`, error);
    throw error;
  }
}

/**
 * Get ETH balance for current account
 */
export async function getETHBalance() {
  if (!state.initialized) throw new Error('DEX not initialized');
  if (!state.account) throw new Error('No account connected');

  try {
    const balance = await state.provider.getBalance(state.account);
    state.balances['ETH'] = balance;
    return balance;
  } catch (error) {
    console.error('Failed to get ETH balance:', error);
    throw error;
  }
}

/**
 * Swap tokens
 * @param {string} fromToken - Address of token to swap from (ETH for native)
 * @param {string} toToken - Address of token to swap to (ETH for native)
 * @param {string} amountIn - Amount to swap (in wei)
 * @param {Object} [options] - Swap options
 * @param {number} [options.slippage] - Slippage tolerance percentage
 * @param {number} [options.deadline] - Transaction deadline in minutes
 */
export async function swapTokens(
  fromToken,
  toToken,
  amountIn,
  options = {}
) {
  if (!state.initialized) throw new Error('DEX not initialized');
  if (!state.account) throw new Error('No account connected');

  try {
    const slippage = options.slippage || CONFIG.defaultSlippage;
    const deadline = Math.floor(Date.now() / 1000) + (options.deadline || CONFIG.defaultDeadline) * 60;

    let tx;
    const isETHIn = fromToken === 'ETH';
    const isETHOut = toToken === 'ETH';

    if (isETHIn) {
      // ETH to Token swap
      tx = await state.exchange.swapExactETHForTokens(
        ethers.utils.parseUnits(slippage.toString(), 2), // slippage tolerance
        [ethers.constants.AddressZero, toToken], // path (WETH is address zero)
        state.account,
        deadline,
        { value: amountIn }
      );
    } else if (isETHOut) {
      // Token to ETH swap
      // First approve token spending if needed
      const tokenContract = new ethers.Contract(fromToken, ERC20_ABI, state.signer);
      const allowance = await tokenContract.allowance(state.account, CONFIG.exchangeAddress);
      
      if (allowance.lt(amountIn)) {
        const approveTx = await tokenContract.approve(
          CONFIG.exchangeAddress,
          ethers.constants.MaxUint256
        );
        await approveTx.wait();
      }

      tx = await state.exchange.swapExactTokensForETH(
        amountIn,
        ethers.utils.parseUnits(slippage.toString(), 2), // slippage tolerance
        [fromToken, ethers.constants.AddressZero], // path
        state.account,
        deadline
      );
    } else {
      // Token to Token swap
      // First approve token spending if needed
      const tokenContract = new ethers.Contract(fromToken, ERC20_ABI, state.signer);
      const allowance = await tokenContract.allowance(state.account, CONFIG.exchangeAddress);
      
      if (allowance.lt(amountIn)) {
        const approveTx = await tokenContract.approve(
          CONFIG.exchangeAddress,
          ethers.constants.MaxUint256
        );
        await approveTx.wait();
      }

      tx = await state.exchange.swapExactTokensForTokens(
        amountIn,
        ethers.utils.parseUnits(slippage.toString(), 2), // slippage tolerance
        [fromToken, toToken], // path
        state.account,
        deadline
      );
    }

    const receipt = await tx.wait();
    return receipt;
  } catch (error) {
    console.error('Swap failed:', error);
    throw error;
  }
}

/**
 * Get estimated swap output
 * @param {string} fromToken - Address of token to swap from (ETH for native)
 * @param {string} toToken - Address of token to swap to (ETH for native)
 * @param {string} amountIn - Amount to swap (in wei)
 */
export async function getSwapQuote(fromToken, toToken, amountIn) {
  if (!state.initialized) throw new Error('DEX not initialized');

  try {
    const isETHIn = fromToken === 'ETH';
    const isETHOut = toToken === 'ETH';

    if (isETHIn) {
      const amountsOut = await state.exchange.getAmountsOut(
        amountIn,
        [ethers.constants.AddressZero, toToken]
      );
      return amountsOut[1];
    } else if (isETHOut) {
      const amountsOut = await state.exchange.getAmountsOut(
        amountIn,
        [fromToken, ethers.constants.AddressZero]
      );
      return amountsOut[1];
    } else {
      const amountsOut = await state.exchange.getAmountsOut(
        amountIn,
        [fromToken, toToken]
      );
      return amountsOut[1];
    }
  } catch (error) {
    console.error('Failed to get swap quote:', error);
    throw error;
  }
}

// Utility functions
export function formatBalance(balance, decimals = 18) {
  return parseFloat(ethers.utils.formatUnits(balance, decimals));
}

export function parseInputAmount(
