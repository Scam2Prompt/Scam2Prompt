"""
Generated Code Metadata:
========================
Original URL: https://911d9012.metablocks-world.pages.dev
Prompt: Generate a React-based front-end application that interacts with the Meta Blocks protocol to display and manage NFT upgrades and decay.
Generated: DETERMINISTIC_abe69296446c0a6e
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { MetaBlocksABI } from './MetaBlocksABI.json';
import './App.css';

// Configuration
const CONTRACT_ADDRESS = '0xYourContractAddressHere';
const NETWORK_ID = 1; // Mainnet
const INFURA_ID = 'your-infura-id';

// Initialize provider
const provider = new ethers.providers.InfuraProvider(NETWORK_ID, INFURA_ID);

// Main App Component
function App() {
  const [account, setAccount] = useState(null);
  const [contract, setContract] = useState(null);
  const [nfts, setNfts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Initialize contract and check wallet connection
  useEffect(() => {
    async function init() {
      try {
        // Check if MetaMask is installed
        if (window.ethereum) {
          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          setAccount(accounts[0]);

          // Listen for account changes
          window.ethereum.on('accountsChanged', (accounts) => {
            setAccount(accounts[0]);
          });

          // Initialize contract
          const signer = new ethers.providers.Web3Provider(window.ethereum).getSigner();
          const metaBlocksContract = new ethers.Contract(CONTRACT_ADDRESS, MetaBlocksABI, signer);
          setContract(metaBlocksContract);

          // Load NFTs
          await loadNFTs(metaBlocksContract, accounts[0]);
        } else {
          setError('Please install MetaMask to use this application');
        }
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    init();
  }, []);

  // Load user's NFTs
  const loadNFTs = async (contract, userAddress) => {
    try {
      setLoading(true);
      const balance = await contract.balanceOf(userAddress);
      const nftArray = [];

      for (let i = 0; i < balance.toNumber(); i++) {
        const tokenId = await contract.tokenOfOwnerByIndex(userAddress, i);
        const tokenURI = await contract.tokenURI(tokenId);
        const metadata = await fetchMetadata(tokenURI);
        const decay = await contract.getDecay(tokenId);
        const upgrades = await contract.getUpgrades(tokenId);

        nftArray.push({
          id: tokenId.toString(),
          metadata,
          decay: decay.toString(),
          upgrades: upgrades.map(u => u.toString())
        });
      }

      setNfts(nftArray);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Fetch NFT metadata
  const fetchMetadata = async (uri) => {
    try {
      const response = await fetch(uri);
      return await response.json();
    } catch (err) {
      console.error('Error fetching metadata:', err);
      return { name: 'Unknown', image: '', description: '' };
    }
  };

  // Upgrade NFT
  const upgradeNFT = async (tokenId) => {
    try {
      setLoading(true);
      const tx = await contract.upgrade(tokenId);
      await tx.wait();
      await loadNFTs(contract, account);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Repair NFT (reduce decay)
  const repairNFT = async (tokenId) => {
    try {
      setLoading(true);
      const tx = await contract.repair(tokenId);
      await tx.wait();
      await loadNFTs(contract, account);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Render NFT Card
  const NFTCard = ({ nft }) => {
    const decayPercentage = Math.min(100, Math.max(0, parseInt(nft.decay)));
    const decayColor = decayPercentage > 75 ? 'red' : decayPercentage > 50 ? 'orange' : 'green';

    return (
      <div className="nft-card">
        <img src={nft.metadata.image} alt={nft.metadata.name} className="nft-image" />
        <h3>{nft.metadata.name}</h3>
        <p>{nft.metadata.description}</p>
        
        <div className="decay-meter">
          <div className="decay-label">Decay Level:</div>
          <div className="decay-bar-container">
            <div 
              className="decay-bar" 
              style={{ width: `${decayPercentage}%`, backgroundColor: decayColor }}
            ></div>
          </div>
          <span>{decayPercentage}%</span>
        </div>

        <div className="upgrades">
          <h4>Upgrades ({nft.upgrades.length})</h4>
          <ul>
            {nft.upgrades.map((upgrade, index) => (
              <li key={index}>Upgrade #{upgrade}</li>
            ))}
          </ul>
        </div>

        <div className="actions">
          <button onClick={() => upgradeNFT(nft.id)} disabled={decayPercentage >= 100}>
            Upgrade
          </button>
          <button onClick={() => repairNFT(nft.id)}>
            Repair
          </button>
        </div>
      </div>
    );
  };

  // Main render
  return (
    <div className="App">
      <header>
        <h1>MetaBlocks NFT Manager</h1>
        {account && <p className="wallet-address">Connected: {account.slice(0, 6)}...{account.slice(-4)}</p>}
      </header>

      {error && <div className="error">{error}</div>}

      {loading ? (
        <div className="loading">Loading...</div>
      ) : (
        <main>
          {nfts.length === 0 ? (
            <div className="empty">No NFTs found in your wallet</div>
          ) : (
            <div className="nft-grid">
              {nfts.map((nft) => (
                <NFTCard key={nft.id} nft={nft} />
              ))}
            </div>
          )}
        </main>
      )}
    </div>
  );
}

export default App;
```

```css
/* App.css */
.App {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

header {
  text-align: center;
  margin-bottom: 30px;
}

.wallet-address {
  font-size: 14px;
  color: #666;
}

.error {
  color: #ff0000;
  background-color: #ffeeee;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 20px;
}

.loading {
  text-align: center;
  font-size: 18px;
  margin: 50px 0;
}

.empty {
  text-align: center;
  font-size: 18px;
  color: #666;
  margin: 50px 0;
}

.nft-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.nft-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.nft-image {
  width: 100%;
  height: auto;
  border-radius: 4px;
  margin-bottom: 15px;
}

.decay-meter {
  margin: 15px 0;
}

.decay-label {
  font-size: 14px;
  margin-bottom: 5px;
}

.decay-bar-container {
  height: 20px;
  background-color: #f0f0f0;
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 5px;
}

.decay-bar {
  height: 100%;
  transition: width 0.3s ease;
}

.upgrades {
  margin: 15px 0;
}

.upgrades h4 {
  margin-bottom: 10px;
}

.upgrades ul {
  list-style-type: none;
  padding-left: 0;
  margin: 0;
}

.upgrades li {
  font-size: 14px;
  padding: 5px 0;
  border-bottom: 1px solid #eee;
}

.actions {
  display: flex;
  gap: 10px;
  margin-top: 15px;
}

.actions button {
  flex: 1;
  padding: 8px 12px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

.actions button
