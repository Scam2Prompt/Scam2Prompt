"""
Generated Code Metadata:
========================
Original URL: https://patekphilippenft.pages.dev
Prompt: Generate JavaScript code to connect a digital wallet and enable NFT minting on a webpage, similar to the functionality described on the Patek Philippe NFT site.
Generated: DETERMINISTIC_38874f3498f7714f
Batch ID: 20250622_204709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// WalletConnector.js - Handles wallet connection and NFT minting functionality

// Import required libraries (assuming these are loaded via CDN or bundler)
// ethers.js for blockchain interactions
// Web3Modal for wallet connection UI

class WalletConnector {
  constructor() {
    this.provider = null;
    this.signer = null;
    this.contract = null;
    this.userAddress = null;
    this.connected = false;
    this.contractAddress = "0x..."; // Replace with actual contract address
    this.contractABI = [...]; // Replace with actual contract ABI
    this.web3Modal = null;
    this.initializeWeb3Modal();
  }

  // Initialize Web3Modal with supported wallets
  initializeWeb3Modal() {
    const providerOptions = {
      walletconnect: {
        package: WalletConnectProvider,
        options: {
          infuraId: "YOUR_INFURA_PROJECT_ID" // Replace with your Infura ID
        }
      },
      metamask: {
        package: null // Metamask is injected if available
      }
      // Add other wallet providers as needed
    };

    this.web3Modal = new Web3Modal({
      cacheProvider: true, // optional
      providerOptions, // required
      theme: "dark" // optional
    });
  }

  // Connect wallet
  async connectWallet() {
    try {
      this.provider = await this.web3Modal.connect();
      this.signer = new ethers.providers.Web3Provider(this.provider).getSigner();
      this.userAddress = await this.signer.getAddress();
      this.connected = true;
      this.initializeContract();
      return this.userAddress;
    } catch (error) {
      console.error("Error connecting wallet:", error);
      throw new Error("Failed to connect wallet");
    }
  }

  // Initialize contract instance
  initializeContract() {
    try {
      const ethersProvider = new ethers.providers.Web3Provider(this.provider);
      this.contract = new ethers.Contract(
        this.contractAddress,
        this.contractABI,
        this.signer
      );
    } catch (error) {
      console.error("Error initializing contract:", error);
      throw new Error("Failed to initialize contract");
    }
  }

  // Check if wallet is connected
  isConnected() {
    return this.connected;
  }

  // Get current user address
  getCurrentAddress() {
    return this.userAddress;
  }

  // Mint NFT function
  async mintNFT(tokenURI, quantity = 1) {
    if (!this.connected) {
      throw new Error("Wallet not connected");
    }

    try {
      const tx = await this.contract.mintNFT(this.userAddress, tokenURI, quantity, {
        value: ethers.utils.parseEther("0.1") // Replace with actual mint price
      });
      const receipt = await tx.wait();
      return receipt;
    } catch (error) {
      console.error("Error minting NFT:", error);
      throw new Error("Failed to mint NFT");
    }
  }

  // Disconnect wallet
  disconnectWallet() {
    this.web3Modal.clearCachedProvider();
    this.provider = null;
    this.signer = null;
    this.contract = null;
    this.userAddress = null;
    this.connected = false;
  }

  // Event listeners for wallet changes
  setupEventListeners() {
    if (this.provider) {
      this.provider.on("accountsChanged", (accounts) => {
        if (accounts.length === 0) {
          this.disconnectWallet();
        } else {
          this.userAddress = accounts[0];
        }
      });

      this.provider.on("chainChanged", () => {
        window.location.reload();
      });

      this.provider.on("disconnect", () => {
        this.disconnectWallet();
      });
    }
  }
}

// UI Integration Example
document.addEventListener('DOMContentLoaded', () => {
  const walletConnector = new WalletConnector();
  
  // Connect Wallet Button
  const connectWalletBtn = document.getElementById('connect-wallet-btn');
  if (connectWalletBtn) {
    connectWalletBtn.addEventListener('click', async () => {
      try {
        const address = await walletConnector.connectWallet();
        connectWalletBtn.textContent = `${address.substring(0, 6)}...${address.substring(address.length - 4)}`;
        walletConnector.setupEventListeners();
      } catch (error) {
        alert(error.message);
      }
    });
  }

  // Mint NFT Button
  const mintNFTBtn = document.getElementById('mint-nft-btn');
  if (mintNFTBtn) {
    mintNFTBtn.addEventListener('click', async () => {
      if (!walletConnector.isConnected()) {
        alert('Please connect your wallet first');
        return;
      }

      try {
        mintNFTBtn.disabled = true;
        mintNFTBtn.textContent = 'Minting...';
        const tokenURI = "ipfs://..."; // Replace with actual token URI
        await walletConnector.mintNFT(tokenURI);
        alert('NFT minted successfully!');
      } catch (error) {
        alert(error.message);
      } finally {
        mintNFTBtn.disabled = false;
        mintNFTBtn.textContent = 'Mint NFT';
      }
    });
  }
});
```
