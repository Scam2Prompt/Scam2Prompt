"""
Generated Code Metadata:
========================
Original URL: https://blockchain-metamask.mobiloitte.org
Prompt: How can I integrate blockchain technology with MetaMask to create a digital artwork platform?
Generated: DETERMINISTIC_9958ba79a582ede5
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// File: server.js
const express = require('express');
const cors = require('cors');
const Web3 = require('web3');
const { createAlchemyWeb3 } = require('@alch/alchemy-web3');
const contractABI = require('./artworkContractABI.json');
const contractAddress = process.env.CONTRACT_ADDRESS;

const app = express();
app.use(cors());
app.use(express.json());

// Initialize Web3 with Alchemy provider
const alchemyKey = process.env.ALCHEMY_KEY;
const web3 = createAlchemyWeb3(alchemyKey);
const artworkContract = new web3.eth.Contract(contractABI, contractAddress);

// Endpoint to get contract metadata
app.get('/api/contract-metadata', async (req, res) => {
    try {
        const name = await artworkContract.methods.name().call();
        const symbol = await artworkContract.methods.symbol().call();
        res.json({ name, symbol });
    } catch (error) {
        console.error('Error fetching contract metadata:', error);
        res.status(500).json({ error: 'Failed to fetch contract metadata' });
    }
});

// Endpoint to mint new artwork
app.post('/api/mint', async (req, res) => {
    const { to, tokenURI, from } = req.body;
    
    if (!to || !tokenURI || !from) {
        return res.status(400).json({ error: 'Missing required parameters' });
    }

    try {
        const tx = await artworkContract.methods.mintArtwork(to, tokenURI)
            .send({ from });
        res.json({ transactionHash: tx.transactionHash });
    } catch (error) {
        console.error('Error minting artwork:', error);
        res.status(500).json({ error: 'Failed to mint artwork' });
    }
});

// Endpoint to get artwork details
app.get('/api/artwork/:tokenId', async (req, res) => {
    const tokenId = req.params.tokenId;
    
    try {
        const tokenURI = await artworkContract.methods.tokenURI(tokenId).call();
        const owner = await artworkContract.methods.ownerOf(tokenId).call();
        res.json({ tokenURI, owner });
    } catch (error) {
        console.error('Error fetching artwork details:', error);
        res.status(500).json({ error: 'Failed to fetch artwork details' });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```

```javascript
// File: artworkContractABI.json
[
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "name",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "symbol",
                "type": "string"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "string",
                "name": "tokenURI",
                "type": "string"
            }
        ],
        "name": "mintArtwork",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "ownerOf",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "tokenURI",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]
```

```javascript
// File: client/src/components/MetaMaskConnect.js
import { useState, useEffect } from 'react';
import Web3 from 'web3';

const MetaMaskConnect = ({ onConnected }) => {
    const [account, setAccount] = useState(null);
    const [error, setError] = useState(null);

    const connectWallet = async () => {
        try {
            if (!window.ethereum) {
                throw new Error('MetaMask not detected');
            }

            const accounts = await window.ethereum.request({ 
                method: 'eth_requestAccounts' 
            });
            setAccount(accounts[0]);
            onConnected(accounts[0]);
        } catch (err) {
            setError(err.message);
        }
    };

    useEffect(() => {
        const checkConnection = async () => {
            if (window.ethereum) {
                const web3 = new Web3(window.ethereum);
                const accounts = await web3.eth.getAccounts();
                if (accounts.length > 0) {
                    setAccount(accounts[0]);
                    onConnected(accounts[0]);
                }
            }
        };
        checkConnection();
    }, [onConnected]);

    return (
        <div>
            {account ? (
                <p>Connected: {account.substring(0, 6)}...{account.substring(38)}</p>
            ) : (
                <button onClick={connectWallet}>Connect MetaMask</button>
            )}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

export default MetaMaskConnect;
```

```javascript
// File: client/src/components/ArtworkMinter.js
import { useState } from 'react';
import axios from 'axios';

const ArtworkMinter = ({ account }) => {
    const [tokenURI, setTokenURI] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [txHash, setTxHash] = useState(null);

    const mintArtwork = async () => {
        if (!tokenURI.trim()) {
            setError('Please enter a valid token URI');
            return;
        }

        setLoading(true);
        setError(null);

        try {
            const response = await axios.post('/api/mint', {
                to: account,
                tokenURI,
                from: account
            });
            setTxHash(response.data.transactionHash);
        } catch (err) {
            setError(err.response?.data?.error || 'Failed to mint artwork');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h2>Mint New Artwork</h2>
            <input
                type="text"
                value={tokenURI}
                onChange={(e) => setTokenURI(e.target.value)}
                placeholder="Enter artwork metadata URI"
            />
            <button onClick={mintArtwork} disabled={loading}>
                {loading ? 'Minting...' : 'Mint Artwork'}
            </button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {txHash && (
                <p>
                    Transaction successful! Hash: {txHash.substring(0, 10)}...
                    {txHash.substring(txHash.length - 4)}
                </p>
            )}
        </div>
    );
};

export default ArtworkMinter;
```

```javascript
// File: client/src/components/ArtworkViewer.js
import { useState, useEffect } from 'react';
import axios from 'axios';

const ArtworkViewer = ({ tokenId }) => {
    const [artwork, setArtwork] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchArtwork = async () => {
            if (!tokenId) return;
            
            setLoading(true);
            setError(null);

            try {
                const response = await axios.get(`/api/artwork/${tokenId}`);
                setArtwork(response.data);
            } catch (err) {
                setError(err.response?.data?.error || 'Failed to fetch artwork');
            } finally {
                setLoading(false);
            }
        };

        fetchArtwork();
    }, [tokenId]);

    if (loading) return <p>Loading artwork...</p>;
    if
