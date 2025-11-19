"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-moments-git-feature-burn-freshdrops.vercel.app
Prompt: How do I implement a burn feature for NFTs in my crypto project, based on the concepts from Crypto Moments?
Generated: DETERMINISTIC_6dfa4ab79a29c1b4
Batch ID: 20250612_162508
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

// Importing OpenZeppelin Contracts for ERC721
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CryptoMomentsNFT
 * @dev This contract implements an NFT with a burn feature.
 */
contract CryptoMomentsNFT is ERC721Burnable, Ownable {
    uint256 private _tokenIdCounter;

    // Event emitted when a new NFT is minted
    event Minted(address indexed owner, uint256 indexed tokenId);

    /**
     * @dev Constructor for initializing the NFT contract
     * @param name Name of the NFT collection
     * @param symbol Symbol of the NFT collection
     */
    constructor(string memory name, string memory symbol) 
        ERC721(name, symbol) {
        _tokenIdCounter = 0; // Initialize token ID counter
    }

    /**
     * @dev Mint a new NFT to the specified address
     * @param to The address to mint the NFT to
     * @return tokenId The ID of the minted token
     */
    function mint(address to) external onlyOwner returns (uint256) {
        require(to != address(0), "Invalid address");

        _tokenIdCounter++; // Increment token ID counter
        uint256 tokenId = _tokenIdCounter;

        _mint(to, tokenId); // Mint the NFT
        emit Minted(to, tokenId); // Emit the mint event

        return tokenId;
    }

    /**
     * @dev Override the burn function to include additional checks or logic if needed
     * @param tokenId The ID of the token to burn
     */
    function burn(uint256 tokenId) public override {
        // Additional checks can be added here if necessary
        require(_isApprovedOrOwner(_msgSender(), tokenId), "Caller is not owner nor approved");

        super.burn(tokenId); // Call the burn function from ERC721Burnable
    }

    /**
     * @dev Returns the current token ID counter (for external use, if necessary)
     * @return tokenIdCounter The current token ID counter
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _tokenIdCounter;
    }
}
```

### Notes:
- This Solidity contract implements a simple NFT minting and burning feature using OpenZeppelin's ERC721 and ERC721Burnable contracts.
- The contract owner can mint new NFTs, and users can burn (destroy) their NFTs if they own them or are approved to do so.
- Proper error handling is done using require statements to ensure valid operations.
