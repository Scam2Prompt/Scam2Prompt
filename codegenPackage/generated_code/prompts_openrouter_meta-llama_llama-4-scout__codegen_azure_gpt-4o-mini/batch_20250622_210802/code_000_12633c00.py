"""
Generated Code Metadata:
========================
Original URL: https://get-mutatiofiles.pages.dev
Prompt: Write a Solidity function to wrap MUTATIO NFTs (ERC1155) to $FLIES (ERC20) tokens in a 1:1 ratio.
Generated: DETERMINISTIC_12633c0019cc436e
Batch ID: 20250622_210802
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

// Importing the ERC1155 interface
import "@openzeppelin/contracts/token/ERC1155/IERC1155.sol";
// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
// Importing the Ownable contract for access control
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract to wrap MUTATIO NFTs to $FLIES tokens
contract MutatioWrapper is Ownable {
    // Address of the ERC1155 MUTATIO contract
    IERC1155 public mutatioNFT;
    // Address of the ERC20 $FLIES token contract
    IERC20 public fliesToken;

    // Event emitted when NFTs are wrapped
    event Wrapped(address indexed user, uint256 indexed tokenId, uint256 amount);

    // Constructor to set the addresses of the NFT and token contracts
    constructor(address _mutatioNFT, address _fliesToken) {
        require(_mutatioNFT != address(0), "Invalid MUTATIO NFT address");
        require(_fliesToken != address(0), "Invalid $FLIES token address");
        
        mutatioNFT = IERC1155(_mutatioNFT);
        fliesToken = IERC20(_fliesToken);
    }

    // Function to wrap MUTATIO NFTs to $FLIES tokens
    function wrap(uint256 tokenId, uint256 amount) external {
        // Check if the user has enough NFTs to wrap
        require(mutatioNFT.balanceOf(msg.sender, tokenId) >= amount, "Insufficient NFT balance");

        // Transfer the NFTs from the user to this contract
        mutatioNFT.safeTransferFrom(msg.sender, address(this), tokenId, amount, "");

        // Transfer the equivalent amount of $FLIES tokens to the user
        require(fliesToken.balanceOf(address(this)) >= amount, "Insufficient $FLIES balance in contract");
        fliesToken.transfer(msg.sender, amount);

        // Emit the wrap event
        emit Wrapped(msg.sender, tokenId, amount);
    }

    // Function to withdraw any ERC20 tokens from the contract (only owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to withdraw any ERC1155 tokens from the contract (only owner)
    function withdrawNFTs(uint256 tokenId, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        mutatioNFT.safeTransferFrom(address(this), msg.sender, tokenId, amount, "");
    }
}
```
