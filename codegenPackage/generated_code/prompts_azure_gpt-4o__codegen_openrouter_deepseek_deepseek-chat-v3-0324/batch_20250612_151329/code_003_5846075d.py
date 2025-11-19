"""
Generated Code Metadata:
========================
Original URL: https://bnvxhjdghdg.pages.dev
Prompt: Provide code for implementing a "Connect Wallet" button using ethers.js that interacts with an NFT marketplace, inspired by the Azuki Elementals site.
Generated: DETERMINISTIC_5846075de2a4c399
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import { ethers } from 'ethers';
import { useState, useEffect } from 'react';

// NFT Marketplace Contract ABI (simplified for example)
const NFT_MARKETPLACE_ABI = [
  "function balanceOf(address owner) view returns (uint256)",
  "function getOwnedNFTs(address owner) view returns (uint256[] memory)"
];

// Contract address (replace with actual contract address)
const NFT_MARKETPLACE_ADDRESS = "0x123...abc";

const ConnectWalletButton = () => {
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);
  const [account, setAccount] = useState(null);
  const [nftBalance, setNftBalance] = useState(0);
  const [error, setError] = useState(null);
  const [isConnecting, setIsConnecting] = useState(false);

  // Check if wallet is connected on component mount
  useEffect(() => {
    const checkWalletConnection = async () => {
      if (window.ethereum) {
        try {
          const accounts = await window.ethereum.request({ method: 'eth_accounts' });
          if (accounts.length > 0) {
            await connectWallet();
          }
        } catch (err) {
          console.error("Error checking wallet connection:", err);
        }
      }
    };

    checkWalletConnection();
  }, []);

  // Handle account changes
  useEffect(() => {
    if (window.ethereum) {
      window.ethereum.on('accountsChanged', (accounts) => {
        if (accounts.length === 0) {
          // Wallet disconnected
          setAccount(null);
          setSigner(null);
          setNftBalance(0);
        } else {
          // Account changed
          setAccount(accounts[0]);
          updateSignerAndBalance();
        }
      });

      window.ethereum.on('chainChanged', () => {
        window.location.reload();
      });
    }

    return () => {
      if (window.ethereum) {
        window.ethereum.removeListener('accountsChanged');
        window.ethereum.removeListener('chainChanged');
      }
    };
  }, [provider]);

  const updateSignerAndBalance = async () => {
    if (provider && account) {
      const newSigner = provider.getSigner();
      setSigner(newSigner);
      await fetchNFTBalance(newSigner);
    }
  };

  const fetchNFTBalance = async (currentSigner) => {
    try {
      const contract = new ethers.Contract(
        NFT_MARKETPLACE_ADDRESS,
        NFT_MARKETPLACE_ABI,
        currentSigner
      );
      const balance = await contract.balanceOf(account);
      setNftBalance(balance.toNumber());
    } catch (err) {
      console.error("Error fetching NFT balance:", err);
      setError("Failed to fetch NFT balance");
    }
  };

  const connectWallet = async () => {
    setIsConnecting(true);
    setError(null);

    try {
      if (!window.ethereum) {
        throw new Error("No Ethereum provider detected");
      }

      const newProvider = new ethers.providers.Web3Provider(window.ethereum);
      setProvider(newProvider);

      const accounts = await newProvider.send("eth_requestAccounts", []);
      setAccount(accounts[0]);

      const newSigner = newProvider.getSigner();
      setSigner(newSigner);

      await fetchNFTBalance(newSigner);
    } catch (err) {
      console.error("Error connecting wallet:", err);
      setError(err.message || "Failed to connect wallet");
    } finally {
      setIsConnecting(false);
    }
  };

  const disconnectWallet = () => {
    setAccount(null);
    setSigner(null);
    setProvider(null);
    setNftBalance(0);
  };

  const shortenAddress = (addr) => {
    return `${addr.substring(0, 6)}...${addr.substring(addr.length - 4)}`;
  };

  return (
    <div className="wallet-container">
      {error && <div className="error-message">{error}</div>}
      
      {account ? (
        <div className="wallet-connected">
          <span className="wallet-address">{shortenAddress(account)}</span>
          {nftBalance > 0 && (
            <span className="nft-count">{nftBalance} NFT{nftBalance !== 1 ? 's' : ''}</span>
          )}
          <button onClick={disconnectWallet} className="disconnect-button">
            Disconnect
          </button>
        </div>
      ) : (
        <button 
          onClick={connectWallet} 
          className="connect-button"
          disabled={isConnecting}
        >
          {isConnecting ? 'Connecting...' : 'Connect Wallet'}
        </button>
      )}
    </div>
  );
};

export default ConnectWalletButton;
```
