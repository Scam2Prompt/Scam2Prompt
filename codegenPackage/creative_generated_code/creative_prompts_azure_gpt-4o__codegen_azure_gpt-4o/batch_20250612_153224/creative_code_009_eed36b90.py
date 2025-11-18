"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1-dv2.pages.dev
Prompt: Provide an example of deploying a TIP-4 NFT collection with metadata customization and trading support on Oasis.Gallery using Venom's developer tools.
Generated: DETERMINISTIC_eed36b90f0c49885
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0 <0.9.0;

// Import the required TIP-4 interfaces for NFTs and metadata.
import "@broxus/tip4/contracts/TIP4_4/TIP4_4Collection.sol";
import "@broxus/tip4/contracts/TIP4_4/TIP4_4NFT.sol";

// Import the Venom tools for advanced NFT trading features.
import "@venom/venom-tools/contracts/TradingSupport.sol";

// TIP-4 NFT Collection Contract with Metadata Customization and Trading Support
contract CustomNFTCollection is TIP4_4Collection {
    // Metadata base URI for all NFTs in the collection
    string public baseURI;

    // Event emitted when a new NFT is created
    event NFTCreated(address indexed nftAddress, uint256 indexed tokenId);

    // Constructor to initialize the collection
    constructor(
        string memory _name, 
        string memory _symbol, 
        string memory _baseURI
    ) TIP4_4Collection(_name, _symbol) {
        // Set the base URI for metadata
        baseURI = _baseURI;
    }

    /**
     * @dev Function to mint a new NFT in the collection.
     * @param recipient Address that will own the newly minted NFT.
     * @param metadataURI Custom metadata URI for the NFT.
     */
    function mintNFT(address recipient, string memory metadataURI) external {
        // Generate a unique tokenId based on the current NFT count
        uint256 tokenId = _totalSupply + 1;

        // Deploy a new NFT contract
        address nftAddress = _deployNFT(
            recipient, 
            tokenId,
            metadataURI
        );

        // Emit the NFT creation event
        emit NFTCreated(nftAddress, tokenId);
    }

    /**
     * @dev Internal function to deploy an NFT contract.
     * @param recipient Address that will own the NFT.
     * @param tokenId Unique ID for the NFT.
     * @param metadataURI URI for the NFT metadata.
     * @return Address of the deployed NFT contract.
     */
    function _deployNFT(
        address recipient, 
        uint256 tokenId, 
        string memory metadataURI
    ) internal returns (address) {
        // Deploy the TIP-4.4 NFT contract
        TIP4_4NFT newNFT = new TIP4_4NFT(
            recipient,
            address(this),
            tokenId,
            metadataURI
        );

        // Return the deployed NFT contract address
        return address(newNFT);
    }

    /**
     * @dev Function to update the base URI of the collection.
     * @param newBaseURI The new base URI to set.
     */
    function updateBaseURI(string memory newBaseURI) external onlyOwner {
        baseURI = newBaseURI;
    }
}
```
