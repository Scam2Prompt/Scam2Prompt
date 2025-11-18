"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phi-f1z.pages.dev
Prompt: Write code to implement a feature in a dApp that lets users showcase their Phi Cred NFTs in various formats, such as text, images, or videos.
Generated: DETERMINISTIC_34249019d9293edd
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s production-ready JavaScript code for the requested feature, built using the Web3.js library and a front-end framework like React.js for a typical dApp environment:

```javascript
import React, { useEffect, useState } from "react";
import Web3 from "web3";

// Contract ABI and Address for the Phi Cred NFT
const PHI_CRED_NFT_ABI = [
  // Define the ABI here (simplified for brevity)
];
const PHI_CRED_NFT_ADDRESS = "0xYourContractAddressHere";

const ShowcaseNFT = () => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);
  const [contract, setContract] = useState(null);
  const [nfts, setNfts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Initialize Web3 and Contract
  useEffect(() => {
    const initializeWeb3 = async () => {
      try {
        // Check if MetaMask is available
        if (window.ethereum) {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);

          // Request account access
          const accounts = await window.ethereum.request({
            method: "eth_requestAccounts",
          });
          setAccount(accounts[0]);

          // Instantiate the contract
          const contractInstance = new web3Instance.eth.Contract(
            PHI_CRED_NFT_ABI,
            PHI_CRED_NFT_ADDRESS
          );
          setContract(contractInstance);
        } else {
          throw new Error("MetaMask not detected. Please install MetaMask.");
        }
      } catch (err) {
        setError(err.message);
      }
    };

    initializeWeb3();
  }, []);

  // Fetch NFTs owned by the user
  const fetchNFTs = async () => {
    if (!contract || !account) return;

    try {
      setLoading(true);
      setError("");

      // Call the smart contract's method to fetch NFT IDs owned by the user
      const tokenIds = await contract.methods.tokensOfOwner(account).call();

      // Fetch metadata for each token (assuming a `tokenURI` function exists)
      const nftPromises = tokenIds.map(async (tokenId) => {
        const tokenURI = await contract.methods.tokenURI(tokenId).call();
        const response = await fetch(tokenURI);
        const metadata = await response.json();
        return { tokenId, metadata };
      });

      const fetchedNFTs = await Promise.all(nftPromises);
      setNfts(fetchedNFTs);
    } catch (err) {
      setError("Failed to fetch NFTs: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (contract && account) {
      fetchNFTs();
    }
  }, [contract, account]);

  return (
    <div className="showcase-container">
      <h1>Showcase Your Phi Cred NFTs</h1>
      {error && <p className="error">{error}</p>}
      {loading ? (
        <p>Loading your NFTs...</p>
      ) : (
        <div className="nft-grid">
          {nfts.map((nft) => (
            <div key={nft.tokenId} className="nft-card">
              {/* Showcase NFTs in various formats */}
              <h2>Token ID: {nft.tokenId}</h2>
              {nft.metadata.image && (
                <img
                  src={nft.metadata.image}
                  alt={`NFT Token ID ${nft.tokenId}`}
                  className="nft-image"
                />
              )}
              {nft.metadata.video && (
                <video
                  src={nft.metadata.video}
                  controls
                  className="nft-video"
                />
              )}
              {nft.metadata.description && (
                <p className="nft-description">{nft.metadata.description}</p>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ShowcaseNFT;
```

### Key Points:
- **`tokensOfOwner`**: A placeholder method should exist in the smart contract that provides the list of token IDs owned by the user.
- **`tokenURI`**: A standard method in ERC-721 contracts to fetch the metadata URL for a given token ID.
- **React**: Used to create the front-end structure for showcasing NFTs.

Ensure the smart contract fulfills the required methods (`tokensOfOwner` and `tokenURI`) and that the metadata contains fields like `image`, `video`, and `description`.
