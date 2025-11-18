"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xambush.top
Prompt: Write a smart contract in Solidity for an ERC721A token inspired by Azuki's decentralized anime brand, including features for minting and transferring tokens.
Generated: DETERMINISTIC_cbb421cba45a8002
Batch ID: 20250612_155015
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

// Import the ERC721A contract
import "./ERC721A.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract AzukiAnime is ERC721A, Ownable {
    // Base URI for the token metadata
    string private _baseTokenURI;

    // Event to emit when a new token is minted
    event TokenMinted(address indexed to, uint256 tokenId);

    // Constructor to set the token name and symbol
    constructor(string memory name, string memory symbol, string memory baseURI) 
        ERC721A(name, symbol) 
    {
        _baseTokenURI = baseURI;
    }

    // Function to mint tokens
    function mint(uint256 quantity) external onlyOwner {
        require(quantity > 0, "Quantity must be greater than zero");
        require(quantity + totalSupply() <= maxSupply(), "Exceeds max supply");
        
        // Mint the tokens to the caller
        _mint(msg.sender, quantity);
        emit TokenMinted(msg.sender, quantity);
    }

    // Function to set the base URI for token metadata
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    // Override the _baseURI function from ERC721A to return the base URI
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to transfer a token from one address to another
    function transferToken(address from, address to, uint256 tokenId) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");
        require(to != address(0), "Transfer to zero address");
        
        // Transfer the token
        _transfer(from, to, tokenId);
    }

    // Function to safely transfer a token with additional data
    function safeTransferToken(address from, address to, uint256 tokenId, bytes memory data) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");
        require(to != address(0), "Transfer to zero address");

        // Safe transfer of the token
        _safeTransfer(from, to, tokenId, data);
    }

    // Function to get total supply (inherited from ERC721A)
    function maxSupply() public pure returns (uint256) {
        return 10000; // Set the maximum supply of tokens
    }

    // Override supportsInterface to include ERC721A's interface
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721A) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
