"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamasksupport.vercel.app
Prompt: Generate code to interact with MetaMask for securely storing and retrieving NFTs in a gallery format. Include functionality for displaying metadata of the stored NFTs.
Generated: DETERMINISTIC_59c94365cf32eba6
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';

// Ensure to have MetaMask installed and connected
if (typeof window.ethereum === 'undefined') {
    alert('Please install MetaMask to use this app');
}

// NFT Gallery component
const NFTGallery = () => {
    const [account, setAccount] = useState('');
    const [nfts, setNfts] = useState([]);
    const [loading, setLoading] = useState(true);

    // Initialize Web3 and fetch the account
    useEffect(() => {
        const init = async () => {
            try {
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                const web3 = new Web3(window.ethereum);
                const accounts = await web3.eth.getAccounts();
                setAccount(accounts[0]);
            } catch (error) {
                console.error('Error connecting to MetaMask', error);
                alert('Could not connect to MetaMask. Please try again.');
            }
        };

        init();
    }, []);

    // Function to fetch NFTs based on the connected account
    const fetchNFTs = async () => {
        try {
            const provider = new ethers.providers.Web3Provider(window.ethereum);
            const nftContract = new ethers.Contract( 
                'YOUR_NFT_CONTRACT_ADDRESS', // Replace with your NFT contract address
                [
                    'function balanceOf(address owner) view returns (uint256)',
                    'function tokenOfOwnerByIndex(address owner, uint256 index) view returns (uint256)',
                    'function tokenURI(uint256 tokenId) view returns (string)',
                ],
                provider
            );

            const balance = await nftContract.balanceOf(account);
            const nftsArray = [];

            for (let i = 0; i < balance; i++) {
                const tokenId = await nftContract.tokenOfOwnerByIndex(account, i);
                const tokenURI = await nftContract.tokenURI(tokenId);
                const response = await fetch(tokenURI);
                const metadata = await response.json();
                
                nftsArray.push({
                    id: tokenId.toString(),
                    image: metadata.image,
                    name: metadata.name,
                    description: metadata.description,
                });
            }

            setNfts(nftsArray);
            setLoading(false);
        } catch (error) {
            console.error('Error fetching NFTs', error);
            alert('Could not fetch NFTs. Please try again later.');
            setLoading(false);
        }
    };

    useEffect(() => {
        if (account) {
            fetchNFTs();
        }
    }, [account]);

    return (
        <div>
            <h1>NFT Gallery</h1>
            {loading ? (
                <p>Loading NFTs...</p>
            ) : (
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))', gap: '16px' }}>
                    {nfts.map((nft) => (
                        <div key={nft.id} style={{ border: '1px solid #ddd', padding: '10px', borderRadius: '8px' }}>
                            <img src={nft.image} alt={nft.name} style={{ width: '100%', borderRadius: '8px' }} />
                            <h3>{nft.name}</h3>
                            <p>{nft.description}</p>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default NFTGallery;
```

### Notes:
- Replace `'YOUR_NFT_CONTRACT_ADDRESS'` with the actual NFT contract address you want to interact with.
- Ensure that the contract ABI is correct and matches the functions being called in the code.
- Remember to handle CORS issues when fetching metadata from various NFT platforms.
- This code assumes that the metadata returned from the NFTs has properties `image`, `name`, and `description`. Adjust as necessary based on your specific NFT metadata structure.
