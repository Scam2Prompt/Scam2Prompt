"""
Generated Code Metadata:
========================
Original URL: https://ipblockchain.pages.dev
Prompt: "Design a smart contract using Story's modular smart contract protocol to tokenize a creative work and make it programmable on the Story Network."
Generated: DETERMINISTIC_83fdd8ce5261fae2
Batch ID: 20250622_204843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary interfaces and libraries from the Story modular smart contract protocol
import "@storyprotocol/contracts/token/ERC721.sol";
import "@storyprotocol/contracts/utils/Context.sol";
import "@storyprotocol/contracts/utils/Strings.sol";

// Defining the SmartContract for tokenizing creative works
contract CreativeWorkToken is Context, ERC721 {
    using Strings for uint256;

    // State variables
    string private _baseTokenURI; // Base URI for the token metadata
    uint256 private _tokenCounter; // Counter for the token IDs

    // Event emitted when a new token is minted
    event TokenMinted(address indexed owner, uint256 indexed tokenId);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
        _tokenCounter = 0;
    }

    // Function to mint a new token
    function mintToken(address to) external {
        require(to != address(0), "Invalid address: cannot mint to the zero address");

        // Increment the token counter to get a new token ID
        _tokenCounter++;
        uint256 newTokenId = _tokenCounter;

        // Mint the new token
        _mint(to, newTokenId);

        // Emit the TokenMinted event
        emit TokenMinted(to, newTokenId);
    }

    // Function to return the base URI for the token metadata
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to get the current token counter
    function getCurrentTokenCount() external view returns (uint256) {
        return _tokenCounter;
    }

    // Function to update the base URI (only owner can call this)
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        _baseTokenURI = newBaseURI;
    }

    // Function to safely transfer tokens with error handling
    function safeTransferToken(address from, address to, uint256 tokenId) external {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "Caller is not owner nor approved");
        require(to != address(0), "Invalid address: cannot transfer to the zero address");

        // Safe transfer of the token
        _safeTransfer(from, to, tokenId, "");
    }

    // Function to get the token URI for a specific token ID
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return string(abi.encodePacked(_baseURI(), tokenId.toString()));
    }
}
```
