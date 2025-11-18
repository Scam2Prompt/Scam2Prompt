"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ddlnft.top
Prompt: Generate code to integrate Doodles NFT features into a web application, allowing users to log in via MetaMask and explore the Doodleverse.
Generated: DETERMINISTIC_5764083535abf7c8
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3'; // Web3.js for blockchain interaction
import detectEthereumProvider from '@metamask/detect-provider'; // Detect MetaMask provider
import React, { useEffect, useState } from 'react';

// Smart contract ABI and address for Doodles NFT (replace with actual values)
const DOODLES_CONTRACT_ABI = []; // Add the Doodles NFT contract ABI here
const DOODLES_CONTRACT_ADDRESS = ''; // Add the Doodles NFT contract address here

// Main App Component
const DoodleverseApp = () => {
  const [userAddress, setUserAddress] = useState(null);
  const [web3, setWeb3] = useState(null);
  const [nftData, setNftData] = useState([]);

  // Function to initialize Web3 and MetaMask login
  const initializeWeb3 = async () => {
    try {
      // Detect MetaMask provider
      const provider = await detectEthereumProvider();
      if (!provider) {
        alert('Please install MetaMask to use this application.');
        return;
      }

      // Set Web3 instance
      const web3Instance = new Web3(provider);
      setWeb3(web3Instance);

      // Request account access
      const accounts = await provider.request({ method: 'eth_requestAccounts' });
      setUserAddress(accounts[0]);
    } catch (error) {
      console.error('Error initializing Web3:', error);
      alert('Failed to connect to MetaMask. Please try again.');
    }
  };

  // Function to fetch Doodles NFTs owned by the user
  const fetchDoodlesNFTs = async () => {
    try {
      if (!web3 || !userAddress) {
        alert('Please connect to MetaMask first.');
        return;
      }

      // Instantiate Doodles NFT contract
      const contract = new web3.eth.Contract(DOODLES_CONTRACT_ABI, DOODLES_CONTRACT_ADDRESS);

      // Call contract method to get NFTs owned by the user (replace with actual method)
      const ownedTokens = await contract.methods.tokensOfOwner(userAddress).call();

      // Fetch metadata for each token (replace with actual logic)
      const tokenMetadataPromises = ownedTokens.map(async (tokenId) => {
        const tokenURI = await contract.methods.tokenURI(tokenId).call();
        const response = await fetch(tokenURI);
        return response.json();
      });

      const metadata = await Promise.all(tokenMetadataPromises);
      setNftData(metadata);
    } catch (error) {
      console.error('Error fetching NFTs:', error);
      alert('Failed to fetch Doodles NFTs. Please try again.');
    }
  };

  // Log out function
  const logout = () => {
    setUserAddress(null);
    setNftData([]);
  };

  // Effect to auto-connect if MetaMask is already logged in
  useEffect(() => {
    const checkConnection = async () => {
      const provider = await detectEthereumProvider();
      if (provider && provider.selectedAddress) {
        setUserAddress(provider.selectedAddress);
        setWeb3(new Web3(provider));
      }
    };
    checkConnection();
  }, []);

  // UI rendering
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Welcome to the Doodleverse</h1>
      {!userAddress ? (
        <button onClick={initializeWeb3} style={{ padding: '10px', fontSize: '16px' }}>
          Connect MetaMask
        </button>
      ) : (
        <div>
          <p>Logged in as: {userAddress}</p>
          <button onClick={fetchDoodlesNFTs} style={{ padding: '10px', fontSize: '16px', marginRight: '10px' }}>
            Explore Your Doodles
          </button>
          <button onClick={logout} style={{ padding: '10px', fontSize: '16px' }}>
            Logout
          </button>
          <div style={{ marginTop: '20px' }}>
            {nftData.length > 0 ? (
              nftData.map((nft, index) => (
                <div key={index} style={{ border: '1px solid #ccc', padding: '10px', marginBottom: '10px' }}>
                  <img src={nft.image} alt={nft.name} style={{ maxWidth: '200px' }} />
                  <h3>{nft.name}</h3>
                  <p>{nft.description}</p>
                </div>
              ))
            ) : (
              <p>No Doodles NFTs found.</p>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default DoodleverseApp;
```
