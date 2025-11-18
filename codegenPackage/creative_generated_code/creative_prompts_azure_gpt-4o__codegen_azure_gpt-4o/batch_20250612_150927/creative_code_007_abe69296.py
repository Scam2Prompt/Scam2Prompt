"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://911d9012.metablocks-world.pages.dev
Prompt: Generate a React-based front-end application that interacts with the Meta Blocks protocol to display and manage NFT upgrades and decay.
Generated: DETERMINISTIC_abe69296446c0a6e
Batch ID: 20250612_150927
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.metablocks.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.metablocks.example.com`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// File: src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';

// Render the React application
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// File: src/App.js
import React, { useState, useEffect } from 'react';
import NftManager from './components/NftManager';
import './App.css';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Meta Blocks NFT Manager</h1>
      </header>
      <main>
        <NftManager />
      </main>
    </div>
  );
};

export default App;

// File: src/components/NftManager.js
import React, { useState, useEffect } from 'react';
import { getNftDetails, upgradeNft, decayNft } from '../services/metaBlocksApi';
import './NftManager.css';

const NftManager = () => {
  const [nfts, setNfts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch NFT details on component mount
  useEffect(() => {
    const fetchNfts = async () => {
      try {
        const nftData = await getNftDetails();
        setNfts(nftData);
      } catch (err) {
        setError('Failed to load NFT data.');
      } finally {
        setLoading(false);
      }
    };
    fetchNfts();
  }, []);

  // Handle NFT upgrade
  const handleUpgrade = async (nftId) => {
    try {
      const updatedNft = await upgradeNft(nftId);
      setNfts((prevNfts) =>
        prevNfts.map((nft) => (nft.id === nftId ? updatedNft : nft))
      );
    } catch (err) {
      alert('Failed to upgrade NFT.');
    }
  };

  // Handle NFT decay
  const handleDecay = async (nftId) => {
    try {
      const updatedNft = await decayNft(nftId);
      setNfts((prevNfts) =>
        prevNfts.map((nft) => (nft.id === nftId ? updatedNft : nft))
      );
    } catch (err) {
      alert('Failed to decay NFT.');
    }
  };

  if (loading) {
    return <p>Loading NFTs...</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <div className="NftManager">
      <h2>Manage NFTs</h2>
      <ul>
        {nfts.map((nft) => (
          <li key={nft.id}>
            <h3>{nft.name}</h3>
            <p>Level: {nft.level}</p>
            <p>Status: {nft.status}</p>
            <button onClick={() => handleUpgrade(nft.id)}>Upgrade</button>
            <button onClick={() => handleDecay(nft.id)}>Decay</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NftManager;

// File: src/services/metaBlocksApi.js
import axios from 'axios';

// Base API URL (replace with your Meta Blocks endpoint)
const API_BASE_URL = 'https://api.metablocks.example.com';

/**
 * Get details of all NFTs
 * @returns {Promise<Array>} List of NFTs
 */
export const getNftDetails = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/nfts`);
    return response.data;
  } catch (err) {
    throw new Error('Error fetching NFT details.');
  }
};

/**
 * Upgrade an NFT
 * @param {string} nftId - The ID of the NFT to upgrade
 * @returns {Promise<Object>} Updated NFT data
 */
export const upgradeNft = async (nftId) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/nfts/${nftId}/upgrade`);
    return response.data;
  } catch (err) {
    throw new Error('Error upgrading NFT.');
  }
};

/**
 * Decay an NFT
 * @param {string} nftId - The ID of the NFT to decay
 * @returns {Promise<Object>} Updated NFT data
 */
export const decayNft = async (nftId) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/nfts/${nftId}/decay`);
    return response.data;
  } catch (err) {
    throw new Error('Error decaying NFT.');
  }
};

// File: src/App.css
.App {
  text-align: center;
}

.App-header {
  background-color: #282c34;
  padding: 20px;
  color: white;
}

// File: src/components/NftManager.css
.NftManager ul {
  list-style: none;
  padding: 0;
}

.NftManager li {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px 0;
}

.NftManager button {
  margin: 5px;
}

// File: src/index.css
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
}
```

This code follows React best practices, is well-documented, and includes error handling for API requests. Replace `https://api.metablocks.example.com` with your actual Meta Blocks API URL.
