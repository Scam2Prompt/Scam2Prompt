"""
Generated Code Metadata:
========================
Original URL: https://nodeissuesfix.com
Prompt: Write JavaScript code to initialize a Web3 DApp with multichain support and fetch cryptocurrency prices using Coinlib.
Generated: DETERMINISTIC_233f31cb2edb97f6
Batch ID: 20250612_150135
URLs Found: 7
Malicious URLs: 0

Oracle Results:
{
  "https://coinlib.io/api/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://polygonscan.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://polygon-rpc.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bscscan.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://etherscan.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
// Import required libraries
import Web3 from 'web3';
import axios from 'axios';

// Supported chains configuration
const CHAINS = {
  ETHEREUM: {
    id: 1,
    name: 'Ethereum',
    rpcUrl: 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID',
    symbol: 'ETH',
    explorer: 'https://etherscan.io'
  },
  BINANCE_SMART_CHAIN: {
    id: 56,
    name: 'Binance Smart Chain',
    rpcUrl: 'https://bsc-dataseed.binance.org/',
    symbol: 'BNB',
    explorer: 'https://bscscan.com'
  },
  POLYGON: {
    id: 137,
    name: 'Polygon',
    rpcUrl: 'https://polygon-rpc.com/',
    symbol: 'MATIC',
    explorer: 'https://polygonscan.com'
  }
};

// Coinlib API configuration
const COINLIB_API = {
  baseUrl: 'https://coinlib.io/api/v1',
  apiKey: 'YOUR_COINLIB_API_KEY' // Replace with your actual API key
};

class MultiChainDApp {
  constructor() {
    this.web3 = null;
    this.currentChain = null;
    this.userAddress = null;
  }

  /**
   * Initialize Web3 connection for a specific chain
   * @param {string} chainName - Name of the chain to connect to
   * @returns {Promise<void>}
   */
  async initWeb3(chainName) {
    try {
      const chainConfig = CHAINS[chainName];
      if (!chainConfig) {
        throw new Error(`Unsupported chain: ${chainName}`);
      }

      if (window.ethereum) {
        // Modern dapp browsers
        this.web3 = new Web3(window.ethereum);
        try {
          // Request account access
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          this.userAddress = (await this.web3.eth.getAccounts())[0];
        } catch (error) {
          throw new Error('User denied account access');
        }
      } else if (window.web3) {
        // Legacy dapp browsers
        this.web3 = new Web3(window.web3.currentProvider);
        this.userAddress = (await this.web3.eth.getAccounts())[0];
      } else {
        // Fallback to RPC provider
        this.web3 = new Web3(new Web3.providers.HttpProvider(chainConfig.rpcUrl));
      }

      this.currentChain = chainConfig;
      console.log(`Connected to ${chainConfig.name} with address: ${this.userAddress || 'No address (read-only)'}`);
    } catch (error) {
      console.error('Error initializing Web3:', error);
      throw error;
    }
  }

  /**
   * Switch to a different blockchain network
   * @param {string} chainName - Name of the chain to switch to
   * @returns {Promise<void>}
   */
  async switchChain(chainName) {
    try {
      await this.initWeb3(chainName);
    } catch (error) {
      console.error('Error switching chains:', error);
      throw error;
    }
  }

  /**
   * Fetch cryptocurrency prices from Coinlib API
   * @param {string[]} symbols - Array of cryptocurrency symbols to fetch prices for
   * @param {string} [preferredCurrency='USD'] - Preferred fiat currency for price
   * @returns {Promise<Object>} - Object with symbol-price pairs
   */
  async fetchCryptoPrices(symbols, preferredCurrency = 'USD') {
    try {
      if (!symbols || symbols.length === 0) {
        throw new Error('No symbols provided');
      }

      const symbolString = symbols.join(',');
      const url = `${COINLIB_API.baseUrl}/coin?key=${COINLIB_API.apiKey}&pref=${preferredCurrency}&symbol=${symbolString}`;

      const response = await axios.get(url);
      if (response.status !== 200) {
        throw new Error(`Coinlib API error: ${response.statusText}`);
      }

      const prices = {};
      response.data.coins.forEach(coin => {
        prices[coin.symbol] = {
          price: coin.price,
          marketCap: coin.market_cap,
          change24h: coin.delta_24h,
          currency: preferredCurrency
        };
      });

      return prices;
    } catch (error) {
      console.error('Error fetching crypto prices:', error);
      throw error;
    }
  }

  /**
   * Get the native token balance of the connected wallet
   * @returns {Promise<string>} - Balance in wei
   */
  async getNativeTokenBalance() {
    try {
      if (!this.web3 || !this.userAddress) {
        throw new Error('Web3 not initialized or no user address available');
      }

      const balance = await this.web3.eth.getBalance(this.userAddress);
      return balance;
    } catch (error) {
      console.error('Error fetching native token balance:', error);
      throw error;
    }
  }

  /**
   * Convert wei to ether (or other native token units)
   * @param {string} weiAmount - Amount in wei
   * @param {number} [decimals=18] - Number of decimal places
   * @returns {string} - Converted amount
   */
  fromWei(weiAmount, decimals = 18) {
    try {
      return this.web3.utils.fromWei(weiAmount, 'ether');
    } catch (error) {
      console.error('Error converting from wei:', error);
      throw error;
    }
  }
}

// Example usage:
// const dapp = new MultiChainDApp();
// await dapp.initWeb3('ETHEREUM');
// const prices = await dapp.fetchCryptoPrices(['BTC', 'ETH', 'BNB']);
// const balance = await dapp.getNativeTokenBalance();
// console.log('Prices:', prices);
// console.log('Balance:', dapp.fromWei(balance));
```
