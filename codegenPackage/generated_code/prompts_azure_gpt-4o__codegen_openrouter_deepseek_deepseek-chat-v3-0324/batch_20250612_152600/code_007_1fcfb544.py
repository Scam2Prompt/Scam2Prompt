"""
Generated Code Metadata:
========================
Original URL: https://appkit-laboratory-ibhc82bf8-reown-com.vercel.app
Prompt: Write a configuration script for AppKit using Ethers 5 as the driving library and enable SIWE functionality.
Generated: DETERMINISTIC_1fcfb544cf696772
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ethers } = require("ethers");
const { SiweMessage } = require("siwe");

// Configuration class for AppKit with SIWE functionality
class AppKitConfig {
  constructor() {
    this.provider = null;
    this.signer = null;
    this.siweMessage = null;
    this.domain = window.location.host;
    this.origin = window.location.origin;
    this.chainId = 1; // Default to Ethereum mainnet
    this.address = null;
  }

  /**
   * Initialize Ethers provider
   * @param {string} [rpcUrl] - Optional RPC URL, defaults to window.ethereum
   */
  async initProvider(rpcUrl) {
    try {
      if (window.ethereum && !rpcUrl) {
        this.provider = new ethers.providers.Web3Provider(window.ethereum);
        await window.ethereum.request({ method: 'eth_requestAccounts' });
      } else if (rpcUrl) {
        this.provider = new ethers.providers.JsonRpcProvider(rpcUrl);
      } else {
        throw new Error("No Ethereum provider found");
      }
      return this.provider;
    } catch (error) {
      console.error("Error initializing provider:", error);
      throw error;
    }
  }

  /**
   * Initialize signer
   */
  async initSigner() {
    if (!this.provider) {
      throw new Error("Provider not initialized");
    }
    this.signer = this.provider.getSigner();
    this.address = await this.signer.getAddress();
    this.chainId = await this.signer.getChainId();
    return this.signer;
  }

  /**
   * Create SIWE message
   * @param {string} statement - Optional statement to show user
   * @returns {SiweMessage} - Prepared SIWE message
   */
  createSiweMessage(statement = "Sign in with Ethereum") {
    if (!this.address) {
      throw new Error("Signer not initialized");
    }

    this.siweMessage = new SiweMessage({
      domain: this.domain,
      address: this.address,
      statement,
      uri: this.origin,
      version: "1",
      chainId: this.chainId,
    });

    return this.siweMessage;
  }

  /**
   * Sign SIWE message
   * @returns {Promise<string>} - Signed message
   */
  async signSiweMessage() {
    if (!this.siweMessage) {
      throw new Error("SIWE message not created");
    }
    if (!this.signer) {
      throw new Error("Signer not initialized");
    }

    const message = this.siweMessage.prepareMessage();
    const signature = await this.signer.signMessage(message);
    return { message, signature };
  }

  /**
   * Verify SIWE message
   * @param {string} message - Original message
   * @param {string} signature - Signature to verify
   * @returns {Promise<SiweMessage>} - Verified message
   */
  async verifySiweMessage(message, signature) {
    try {
      const siweMessage = new SiweMessage(message);
      await siweMessage.validate(signature);
      return siweMessage;
    } catch (error) {
      console.error("Error verifying SIWE message:", error);
      throw error;
    }
  }
}

// Export the configuration class
module.exports = AppKitConfig;
```
