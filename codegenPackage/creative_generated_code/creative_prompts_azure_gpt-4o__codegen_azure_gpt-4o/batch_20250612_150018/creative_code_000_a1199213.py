"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltrove.com
Prompt: Write a smart contract in Solidity for creating unique NFTs, ensuring security and transparency, as described by Atravaraazen's services.
Generated: DETERMINISTIC_a119921387e6468d
Batch ID: 20250612_150018
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

// Importing OpenZeppelin's ERC721 standard and utility contracts for NFTs
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol"; // To restrict certain functions to the owner only
import "@openzeppelin/contracts/utils/Counters.sol"; // For safe incrementing of token IDs

contract UniqueNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds; // Counter to keep track of the next token ID

    // Event to log the creation of a new NFT for transparency
    event NFTCreated(uint256 tokenId, string tokenURI, address owner);

    // Constructor to initialize the NFT contract with a name and symbol
    constructor() ERC721("UniqueNFT", "UNFT") {}

    /**
     * @notice Function to mint a new NFT.
     * @dev Only the contract owner can mint NFTs.
     * @param recipient Address to receive the newly minted NFT.
     * @param tokenURI URI pointing to the metadata of the NFT.
     * @return tokenId The ID of the newly minted NFT.
     */
    function createNFT(address recipient, string memory tokenURI) public onlyOwner returns (uint256) {
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");
        require(recipient != address(0), "Recipient cannot be the zero address");

        _tokenIds.increment(); // Increment the token ID
        uint256 newItemId = _tokenIds.current(); // Get the new token ID

        // Mint the new NFT and set its metadata URI
        _mint(recipient, newItemId);
        _setTokenURI(newItemId, tokenURI);

        // Emit event for transparency
        emit NFTCreated(newItemId, tokenURI, recipient);

        return newItemId;
    }

    /**
     * @notice Function to get the total number of NFTs minted so far.
     * @return count The total number of NFTs minted.
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIds.current();
    }

    /**
     * @notice Function to withdraw Ether from the contract.
     * @dev Only the contract owner can withdraw Ether.
     */
    function withdraw() public onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback and receive functions to handle accidental Ether transfers
    receive() external payable {}

    fallback() external payable {}
}
```

This is a complete Solidity smart contract for creating unique NFTs, following the ERC721 standard. It includes features such as minting, metadata handling, and event logging for transparency, along with proper error handling and best practices for security.
