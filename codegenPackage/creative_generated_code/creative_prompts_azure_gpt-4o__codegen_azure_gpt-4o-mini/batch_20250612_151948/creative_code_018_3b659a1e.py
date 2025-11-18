"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Generate code for a dApp that allows users to mint and trade NFTs, following the standards described on Ethereum.org.
Generated: DETERMINISTIC_3b659a1e2b630c6a
Batch ID: 20250612_151948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing ERC721 standard from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFTContract is an ERC721 token for minting and trading NFTs
contract NFTContract is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to token URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("MyNFT", "MNFT") {}

    /**
     * @dev Mint a new NFT.
     * @param tokenURI The URI for the NFT metadata.
     */
    function mintNFT(string memory tokenURI) external onlyOwner {
        uint256 newTokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        // Mint the NFT to the caller's address
        _mint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        emit NFTMinted(msg.sender, newTokenId, tokenURI);
    }

    /**
     * @dev Set the token URI for a given token ID.
     * @param tokenId The ID of the token.
     * @param tokenURI The URI for the NFT metadata.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "ERC721Metadata: URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Get the token URI for a given token ID.
     * @param tokenId The ID of the token.
     * @return The token URI.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Override transferFrom to include additional checks or functionality.
     * @param from The current owner of the token.
     * @param to The new owner of the token.
     * @param tokenId The ID of the token to transfer.
     */
    function transferFrom(address from, address to, uint256 tokenId) public override {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: transfer caller is not owner nor approved");
        _transfer(from, to, tokenId);
    }

    /**
     * @dev Override safeTransferFrom to include additional checks or functionality.
     * @param from The current owner of the token.
     * @param to The new owner of the token.
     * @param tokenId The ID of the token to transfer.
     * @param _data Additional data to pass along with the transfer.
     */
    function safeTransferFrom(address from, address to, uint256 tokenId, bytes memory _data) public override {
        transferFrom(from, to, tokenId);
        require(_checkOnERC721Received(from, to, tokenId, _data), "ERC721: transfer to non ERC721Receiver implementer");
    }
}
```

```javascript
// Frontend code (using web3.js and React)
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import NFTContract from './NFTContract.json'; // Import the compiled NFT contract

const App = () => {
    const [account, setAccount] = useState('');
    const [contract, setContract] = useState(null);
    const [tokenURI, setTokenURI] = useState('');
    const [message, setMessage] = useState('');

    useEffect(() => {
        const init = async () => {
            // Connect to Ethereum
            const web3 = new Web3(window.ethereum);
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            const accounts = await web3.eth.getAccounts();
            setAccount(accounts[0]);

            // Set up contract
            const networkId = await web3.eth.net.getId();
            const deployedNetwork = NFTContract.networks[networkId];
            const instance = new web3.eth.Contract(
                NFTContract.abi,
                deployedNetwork && deployedNetwork.address,
            );
            setContract(instance);
        };
        init();
    }, []);

    const mintNFT = async () => {
        try {
            await contract.methods.mintNFT(tokenURI).send({ from: account });
            setMessage('NFT minted successfully!');
        } catch (error) {
            console.error(error);
            setMessage('Error minting NFT. Check console for details.');
        }
    };

    return (
        <div>
            <h1>NFT Minting dApp</h1>
            <p>Connected account: {account}</p>
            <input
                type="text"
                placeholder="Enter Token URI"
                value={tokenURI}
                onChange={(e) => setTokenURI(e.target.value)}
            />
            <button onClick={mintNFT}>Mint NFT</button>
            <p>{message}</p>
        </div>
    );
};

export default App;
```
