"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cosmostrader.pages.dev
Prompt: Generate code for a React component that connects to the Ethereum blockchain and displays live NFT auctions, inspired by the Cosmos Home Trade platform.
Generated: DETERMINISTIC_45b6d00a1f8d5c65
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import axios from 'axios';
import './NFTAuctions.css'; // Assuming you have a CSS file for styling

const NFTAuctions = () => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');
  const [auctions, setAuctions] = useState([]);
  const [error, setError] = useState('');

  // Replace with your smart contract address and ABI
  const contractAddress = '0xYourContractAddressHere';
  const contractABI = []; // Add the ABI of your contract here

  // Initialize Web3 and connect to the Ethereum blockchain
  useEffect(() => {
    const initializeWeb3 = async () => {
      try {
        if (window.ethereum) {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);
        } else {
          setError('Ethereum provider not found. Install MetaMask.');
        }
      } catch (err) {
        console.error('Error initializing Web3:', err);
        setError('Failed to connect to Ethereum.');
      }
    };

    initializeWeb3();
  }, []);

  // Fetch live NFT auctions from the smart contract
  useEffect(() => {
    const fetchAuctions = async () => {
      if (!web3) return;

      try {
        const contract = new web3.eth.Contract(contractABI, contractAddress);
        const liveAuctions = await contract.methods.getLiveAuctions().call();
        const auctionDetails = await Promise.all(
          liveAuctions.map(async (auction) => {
            const metadata = await axios.get(auction.tokenURI); // Assuming tokenURI contains metadata
            return {
              id: auction.id,
              seller: auction.seller,
              currentBid: web3.utils.fromWei(auction.currentBid, 'ether'),
              endTime: auction.endTime,
              metadata: metadata.data,
            };
          })
        );
        setAuctions(auctionDetails);
      } catch (err) {
        console.error('Error fetching auctions:', err);
        setError('Failed to fetch live auctions.');
      }
    };

    fetchAuctions();
  }, [web3]);

  // Utility function to format time remaining
  const formatTime = (endTime) => {
    const now = Math.floor(Date.now() / 1000);
    const secondsLeft = endTime - now;
    if (secondsLeft <= 0) return 'Auction ended';
    const hours = Math.floor(secondsLeft / 3600);
    const minutes = Math.floor((secondsLeft % 3600) / 60);
    const seconds = secondsLeft % 60;
    return `${hours}h ${minutes}m ${seconds}s`;
  };

  return (
    <div className="nft-auctions">
      <h1>Live NFT Auctions</h1>
      {error && <p className="error">{error}</p>}
      {!web3 ? (
        <p>Connecting to Ethereum...</p>
      ) : (
        <div>
          <p>Connected account: {account}</p>
          <div className="auctions-list">
            {auctions.length === 0 ? (
              <p>No live auctions available.</p>
            ) : (
              auctions.map((auction) => (
                <div key={auction.id} className="auction-item">
                  <img
                    src={auction.metadata.image}
                    alt={auction.metadata.name}
                    className="auction-image"
                  />
                  <div className="auction-info">
                    <h2>{auction.metadata.name}</h2>
                    <p>Seller: {auction.seller}</p>
                    <p>Current Bid: {auction.currentBid} ETH</p>
                    <p>Time Remaining: {formatTime(auction.endTime)}</p>
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default NFTAuctions;
```

### Notes:
- Ensure you have the correct ABI and contract address for your Ethereum smart contract.
- You'll need to install `web3` and `axios` dependencies using npm: `npm install web3 axios`.
- Create a CSS file (`NFTAuctions.css`) for styling the component.
