"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-homepage-kappa.vercel.app
Prompt: Provide code examples for displaying NFT ownership data on a Starknet-powered decentralized application using Starknet-React.
Generated: DETERMINISTIC_746e5eea55ceb4c7
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components from React and Starknet
import React, { useEffect, useState } from 'react';
import { useAccount } from 'starknet-react';
import { Contract } from 'starknet';
import { getNFTContractAddress, getNFTData } from './utils'; // Utility functions to get contract address and NFT data

const NFTDisplay = () => {
  // State to hold NFT ownership data
  const [nfts, setNfts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  // Get the current account from Starknet context
  const { account } = useAccount();

  // Fetch NFT ownership data on component mount or account change
  useEffect(() => {
    const fetchNFTs = async () => {
      try {
        setLoading(true);
        setError(null);

        // Ensure the account is connected
        if (!account) {
          throw new Error('No account connected');
        }

        // Get the NFT contract address
        const nftContractAddress = getNFTContractAddress();
        
        // Create a contract instance
        const nftContract = new Contract(nftContractAddress);

        // Fetch NFT data for the account
        const nftData = await getNFTData(nftContract, account);
        
        // Update state with fetched NFT data
        setNfts(nftData);
      } catch (err) {
        // Handle errors (e.g., connect issues, blockchain errors)
        setError(err.message || 'An error occurred');
      } finally {
        setLoading(false);
      }
    };

    fetchNFTs();
  }, [account]); // Rerun effect if the account changes

  // Render loading state, error message, or NFT list
  if (loading) return <p>Loading NFT data...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h1>Your NFTs</h1>
      <ul>
        {nfts.length === 0 ? (
          <li>No NFTs found for this account.</li>
        ) : (
          nfts.map((nft, index) => (
            <li key={index}>
              <img src={nft.image} alt={nft.name} />
              <p>Name: {nft.name}</p>
              <p>ID: {nft.id}</p>
            </li>
          ))
        )}
      </ul>
    </div>
  );
};

export default NFTDisplay;
```
