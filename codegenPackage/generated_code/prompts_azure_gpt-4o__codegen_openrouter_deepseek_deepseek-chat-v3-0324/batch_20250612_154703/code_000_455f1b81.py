"""
Generated Code Metadata:
========================
Original URL: https://web3portal.com
Prompt: Write a script that demonstrates how to integrate a Web3-based decentralized service into a browser extension, specifically referencing the principles of freedom, privacy, and ownership described on Lume Web.
Generated: DETERMINISTIC_455f1b8186d2bcd0
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// background.js - Background script for the browser extension

// Import necessary Web3 libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Error handling class for Web3 operations
class Web3Error extends Error {
  constructor(message) {
    super(message);
    this.name = 'Web3Error';
  }
}

// Main Web3 service class
class LumeWeb3Service {
  constructor() {
    this.provider = null;
    this.web3 = null;
    this.ethersProvider = null;
    this.connected = false;
    this.userAddress = null;
  }

  /**
   * Initialize Web3 provider with user's wallet
   * @param {string} providerUrl - Optional provider URL (defaults to window.ethereum)
   * @throws {Web3Error} If Web3 initialization fails
   */
  async initWeb3(providerUrl = null) {
    try {
      if (window.ethereum && !providerUrl) {
        // Use MetaMask/injected provider
        this.provider = window.ethereum;
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        this.web3 = new Web3(window.ethereum);
        this.ethersProvider = new ethers.providers.Web3Provider(window.ethereum);
      } else if (providerUrl) {
        // Use custom provider
        this.provider = new Web3.providers.HttpProvider(providerUrl);
        this.web3 = new Web3(this.provider);
        this.ethersProvider = new ethers.providers.JsonRpcProvider(providerUrl);
      } else {
        throw new Web3Error('No Ethereum provider detected');
      }

      // Get user address
      const accounts = await this.web3.eth.getAccounts();
      this.userAddress = accounts[0];
      this.connected = true;

      // Set up event listeners
      if (window.ethereum) {
        window.ethereum.on('accountsChanged', (accounts) => {
          this.userAddress = accounts[0] || null;
          chrome.runtime.sendMessage({ type: 'ACCOUNT_CHANGED', address: this.userAddress });
        });

        window.ethereum.on('chainChanged', () => {
          window.location.reload();
        });
      }

      return this.userAddress;
    } catch (error) {
      console.error('Web3 initialization error:', error);
      throw new Web3Error(`Failed to initialize Web3: ${error.message}`);
    }
  }

  /**
   * Get user's Ethereum address
   * @returns {string|null} User's address or null if not connected
   */
  getAddress() {
    return this.userAddress;
  }

  /**
   * Sign a message with user's wallet
   * @param {string} message - Message to sign
   * @returns {Promise<string>} Signed message
   * @throws {Web3Error} If signing fails
   */
  async signMessage(message) {
    if (!this.connected) {
      throw new Web3Error('Wallet not connected');
    }

    try {
      if (this.ethersProvider) {
        const signer = this.ethersProvider.getSigner();
        return await signer.signMessage(message);
      } else {
        return await this.web3.eth.personal.sign(message, this.userAddress, '');
      }
    } catch (error) {
      console.error('Message signing error:', error);
      throw new Web3Error(`Failed to sign message: ${error.message}`);
    }
  }

  /**
   * Verify a signed message
   * @param {string} message - Original message
   * @param {string} signature - Signed message
   * @returns {Promise<string>} Recovered address
   * @throws {Web3Error} If verification fails
   */
  async verifyMessage(message, signature) {
    try {
      if (this.ethersProvider) {
        return ethers.utils.verifyMessage(message, signature);
      } else {
        return this.web3.eth.accounts.recover(message, signature);
      }
    } catch (error) {
      console.error('Message verification error:', error);
      throw new Web3Error(`Failed to verify message: ${error.message}`);
    }
  }

  /**
   * Encrypt data with user's public key
   * @param {string} data - Data to encrypt
   * @returns {Promise<string>} Encrypted data
   * @throws {Web3Error} If encryption fails
   */
  async encryptData(data) {
    if (!this.connected) {
      throw new Web3Error('Wallet not connected');
    }

    try {
      const publicKey = await this.web3.eth.getEncryptionPublicKey(this.userAddress);
      return this.web3.eth.encrypt(data, publicKey);
    } catch (error) {
      console.error('Data encryption error:', error);
      throw new Web3Error(`Failed to encrypt data: ${error.message}`);
    }
  }

  /**
   * Decrypt data with user's private key
   * @param {string} encryptedData - Encrypted data
   * @returns {Promise<string>} Decrypted data
   * @throws {Web3Error} If decryption fails
   */
  async decryptData(encryptedData) {
    if (!this.connected) {
      throw new Web3Error('Wallet not connected');
    }

    try {
      return await this.web3.eth.decrypt(encryptedData, this.userAddress);
    } catch (error) {
      console.error('Data decryption error:', error);
      throw new Web3Error(`Failed to decrypt data: ${error.message}`);
    }
  }
}

// Initialize the service
const lumeWeb3Service = new LumeWeb3Service();

// Message handler for extension
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  (async () => {
    try {
      switch (request.type) {
        case 'INIT_WEB3':
          const address = await lumeWeb3Service.initWeb3(request.providerUrl);
          sendResponse({ success: true, address });
          break;
        case 'GET_ADDRESS':
          sendResponse({ address: lumeWeb3Service.getAddress() });
          break;
        case 'SIGN_MESSAGE':
          const signature = await lumeWeb3Service.signMessage(request.message);
          sendResponse({ success: true, signature });
          break;
        case 'VERIFY_MESSAGE':
          const recoveredAddress = await lumeWeb3Service.verifyMessage(request.message, request.signature);
          sendResponse({ success: true, address: recoveredAddress });
          break;
        case 'ENCRYPT_DATA':
          const encryptedData = await lumeWeb3Service.encryptData(request.data);
          sendResponse({ success: true, encryptedData });
          break;
        case 'DECRYPT_DATA':
          const decryptedData = await lumeWeb3Service.decryptData(request.encryptedData);
          sendResponse({ success: true, decryptedData });
          break;
        default:
          sendResponse({ success: false, error: 'Unknown message type' });
      }
    } catch (error) {
      console.error('Message handler error:', error);
      sendResponse({ success: false, error: error.message });
    }
  })();

  // Return true to indicate async response
  return true;
});

// Content script communication
chrome.runtime.onConnect.addListener((port) => {
  port.onMessage.addListener((msg) => {
    if (msg.type === 'PING') {
      port.postMessage({ type: 'PONG', web3Connected: lumeWeb3Service.connected });
    }
  });
});
```

```javascript
// content.js - Content script for the browser extension

// Connect to the background script
const port = chrome.runtime.connect({ name: 'lume-web3-connection' });

// Send ping to check Web3 connection status
port.postMessage({ type: 'PING' });

// Listen for responses
port.onMessage.addListener((msg) => {
  if (msg.type === 'PONG') {
    console.log('Web3 connection status:', msg.web3Connected);
  }
});

// Expose limited API to web page
window.addEventListener('message', (event) => {
  // Only accept messages from our window
  if (event.source !== window) return;

  // Handle messages requesting Web3 functionality
  if (event.data.type && event.data.type.startsWith('LUME_WEB3_')) {
    chrome.runtime.sendMessage(
      {
        type: event.data.type.replace('LUME_WEB3_', ''),
        ...event.data.payload
      },
      (response) => {
        window.postMessage(
          {
            type: `${event.data.type}_RESPONSE`,
            payload: response
          },
          '*'
        );
      }
    );
  }
});

// Inject provider detection
function injectProviderDetection() {
  const script = document.createElement('script');
  script.textContent = `
    if (typeof window.lumeWeb3Detected === 'undefined') {
      window.lumeWeb3Detected = true;
      window.addEventListener('message', (event) => {
        if (event.data.type === 'LUME_WEB3_DETECT') {
          window.postMessage({
            type: 'LUME_WEB3_DETECT_RESPONSE',
            detected: true
