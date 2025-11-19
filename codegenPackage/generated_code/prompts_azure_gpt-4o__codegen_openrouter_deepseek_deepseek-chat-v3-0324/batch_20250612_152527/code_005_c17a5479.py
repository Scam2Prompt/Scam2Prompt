"""
Generated Code Metadata:
========================
Original URL: https://nft-mantanetwork-8pv.pages.dev
Prompt: Develop a web interface that allows users to connect their wallet, check eligibility, and mint a Golden Treasure Shovel NFT within the Manta Network ecosystem.
Generated: DETERMINISTIC_c17a5479de865396
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import required libraries and types
import { ethers } from 'ethers';
import React, { useState, useEffect } from 'react';
import './App.css';

// Interface for the NFT contract
interface NFTContract {
  connect: (provider: ethers.providers.Web3Provider) => ethers.Contract;
  mint: (address: string) => Promise<any>;
  isEligible: (address: string) => Promise<boolean>;
}

// App component
const App: React.FC = () => {
  const [walletAddress, setWalletAddress] = useState<string>('');
  const [isConnected, setIsConnected] = useState<boolean>(false);
  const [isEligible, setIsEligible] = useState<boolean>(false);
  const [isMinting, setIsMinting] = useState<boolean>(false);
  const [mintSuccess, setMintSuccess] = useState<boolean>(false);
  const [error, setError] = useState<string>('');

  // NFT contract configuration
  const NFT_CONTRACT_ADDRESS = '0x...'; // Replace with actual contract address
  const NFT_ABI = [/* ABI of the NFT contract */];

  // Initialize contract
  const nftContract: NFTContract = {
    connect: (provider) => new ethers.Contract(NFT_CONTRACT_ADDRESS, NFT_ABI, provider.getSigner()),
    mint: async (address) => {
      const provider = new ethers.providers.Web3Provider((window as any).ethereum);
      const contract = nftContract.connect(provider);
      return await contract.mint(address);
    },
    isEligible: async (address) => {
      const provider = new ethers.providers.Web3Provider((window as any).ethereum);
      const contract = nftContract.connect(provider);
      return await contract.isEligible(address);
    }
  };

  // Check if wallet is connected
  const checkWalletConnection = async () => {
    if ((window as any).ethereum) {
      try {
        const accounts = await (window as any).ethereum.request({ method: 'eth_accounts' });
        if (accounts.length > 0) {
          setWalletAddress(accounts[0]);
          setIsConnected(true);
          checkEligibility(accounts[0]);
        }
      } catch (err) {
        console.error('Error checking wallet connection:', err);
      }
    }
  };

  // Connect wallet
  const connectWallet = async () => {
    if ((window as any).ethereum) {
      try {
        const accounts = await (window as any).ethereum.request({ method: 'eth_requestAccounts' });
        setWalletAddress(accounts[0]);
        setIsConnected(true);
        checkEligibility(accounts[0]);
      } catch (err) {
        setError('Failed to connect wallet');
        console.error('Error connecting wallet:', err);
      }
    } else {
      setError('Please install MetaMask or another Ethereum wallet');
    }
  };

  // Check eligibility
  const checkEligibility = async (address: string) => {
    try {
      const eligible = await nftContract.isEligible(address);
      setIsEligible(eligible);
    } catch (err) {
      setError('Failed to check eligibility');
      console.error('Error checking eligibility:', err);
    }
  };

  // Mint NFT
  const mintNFT = async () => {
    if (!walletAddress) return;
    
    setIsMinting(true);
    setError('');
    
    try {
      const tx = await nftContract.mint(walletAddress);
      await tx.wait();
      setMintSuccess(true);
    } catch (err) {
      setError('Failed to mint NFT');
      console.error('Error minting NFT:', err);
    } finally {
      setIsMinting(false);
    }
  };

  // Check wallet connection on component mount
  useEffect(() => {
    checkWalletConnection();
    
    // Listen for account changes
    if ((window as any).ethereum) {
      (window as any).ethereum.on('accountsChanged', (accounts: string[]) => {
        if (accounts.length > 0) {
          setWalletAddress(accounts[0]);
          checkEligibility(accounts[0]);
        } else {
          setWalletAddress('');
          setIsConnected(false);
          setIsEligible(false);
        }
      });
    }
    
    return () => {
      if ((window as any).ethereum) {
        (window as any).ethereum.removeListener('accountsChanged', () => {});
      }
    };
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Golden Treasure Shovel NFT</h1>
        <p>Mint your exclusive Golden Treasure Shovel on Manta Network</p>
        
        {!isConnected ? (
          <button onClick={connectWallet} className="connect-button">
            Connect Wallet
          </button>
        ) : (
          <div className="wallet-info">
            <p>Connected: {walletAddress.substring(0, 6)}...{walletAddress.substring(walletAddress.length - 4)}</p>
            
            {isEligible ? (
              <div className="mint-section">
                {!mintSuccess ? (
                  <button 
                    onClick={mintNFT} 
                    disabled={isMinting}
                    className="mint-button"
                  >
                    {isMinting ? 'Minting...' : 'Mint NFT'}
                  </button>
                ) : (
                  <p className="success-message">NFT minted successfully!</p>
                )}
              </div>
            ) : (
              <p className="eligibility-message">You are not eligible to mint this NFT</p>
            )}
          </div>
        )}
        
        {error && <p className="error-message">{error}</p>}
      </header>
    </div>
  );
};

export default App;
```

```css
/* App.css */
.App {
  text-align: center;
  min-height: 100vh;
  background-color: #282c34;
  color: white;
  padding: 20px;
}

.App-header {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.connect-button, .mint-button {
  background-color: #61dafb;
  border: none;
  color: #282c34;
  padding: 12px 24px;
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
  margin: 10px;
  transition: background-color 0.3s;
}

.connect-button:hover, .mint-button:hover {
  background-color: #4fa8d3;
}

.connect-button:disabled, .mint-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.wallet-info {
  margin: 20px 0;
  padding: 15px;
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
}

.error-message {
  color: #ff6b6b;
  margin-top: 15px;
}

.success-message {
  color: #51cf66;
  margin-top: 15px;
}

.eligibility-message {
  color: #fcc419;
  margin-top: 15px;
}
```
