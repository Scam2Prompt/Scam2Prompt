"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snapshot-ethosmobileorg.pages.dev
Prompt: Create a smart contract function that facilitates the minting of NFTs for a limited-supply product, referencing the ethOS phone minting process.
Generated: DETERMINISTIC_e20c72546674495c
Batch ID: 20250612_153526
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

/**
 * @title LimitedSupplyNFTMinting
 * @dev This contract allows for the minting of NFTs with a limited supply.
 */
contract LimitedSupplyNFTMinting {
    // Address of the contract owner
    address public owner;

    // Maximum supply of NFTs
    uint256 public maxSupply;

    // Total number of NFTs minted so far
    uint256 public totalMinted;

    // Mapping to keep track of minted NFTs for each address
    mapping(address => uint256) public mintedTokens;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed recipient, uint256 tokenId);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    // Modifier to ensure minting does not exceed supply
    modifier canMint() {
        require(totalMinted < maxSupply, "No more NFTs left to mint.");
        _;
    }

    /**
     * @dev Constructor initializes the contract with a maximum NFT supply
     * @param _maxSupply Maximum number of NFTs that can be minted
     */
    constructor(uint256 _maxSupply) {
        require(_maxSupply > 0, "Max supply must be greater than 0.");
        owner = msg.sender;
        maxSupply = _maxSupply;
    }

    /**
     * @dev Function to mint a new NFT
     * @notice Only callable as long as total minted is less than maxSupply
     */
    function mintNFT() external canMint {
        // Increment the total minted counter
        totalMinted++;

        // Assign the minted token ID (sequentially based on totalMinted)
        uint256 tokenId = totalMinted;

        // Update the count of NFTs minted for the recipient
        mintedTokens[msg.sender]++;

        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId);
    }

    /**
     * @dev Function for the owner to modify max supply (if necessary)
     * @param _newMaxSupply New maximum supply for NFTs
     */
    function setMaxSupply(uint256 _newMaxSupply) external onlyOwner {
        require(_newMaxSupply > totalMinted, "New max supply must exceed current total minted.");
        maxSupply = _newMaxSupply;
    }
}
```
