"""
Generated Code Metadata:
========================
Original URL: https://real-infected-mint.vercel.app
Prompt: Generate code to implement a token gating system for Real God and Real Zombie NFT holders to mint Real Infected Mint NFTs at specific prices.
Generated: DETERMINISTIC_146ee1e2f036bc3a
Batch ID: 20250622_205411
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract RealInfectedMint is Ownable {
    // Address of the Real God NFT contract
    IERC721 public realGodNFT;
    // Address of the Real Zombie NFT contract
    IERC721 public realZombieNFT;
    // Price for minting Real Infected Mint NFTs
    uint256 public mintPrice;
    // Mapping to track minted NFTs
    mapping(address => uint256) public mintedCount;

    // Event emitted when a mint occurs
    event Minted(address indexed user, uint256 tokenId);

    // Constructor to initialize the contract with NFT addresses and mint price
    constructor(
        address _realGodNFT,
        address _realZombieNFT,
        uint256 _mintPrice
    ) {
        realGodNFT = IERC721(_realGodNFT);
        realZombieNFT = IERC721(_realZombieNFT);
        mintPrice = _mintPrice;
    }

    // Function to mint Real Infected Mint NFTs
    function mint() external payable {
        // Check if the correct amount of Ether is sent
        require(msg.value == mintPrice, "Incorrect Ether value sent");

        // Check if the user holds at least one Real God or Real Zombie NFT
        require(
            hasRealGodNFT(msg.sender) || hasRealZombieNFT(msg.sender),
            "You must hold a Real God or Real Zombie NFT to mint"
        );

        // Increment the minted count for the user
        mintedCount[msg.sender] += 1;

        // Mint the Real Infected Mint NFT (implementation depends on your NFT contract)
        // Here we assume a function mintNFT exists in the contract
        uint256 tokenId = _mintNFT(msg.sender);

        // Emit the mint event
        emit Minted(msg.sender, tokenId);
    }

    // Internal function to check if the user holds Real God NFTs
    function hasRealGodNFT(address user) internal view returns (bool) {
        return IERC721Enumerable(address(realGodNFT)).balanceOf(user) > 0;
    }

    // Internal function to check if the user holds Real Zombie NFTs
    function hasRealZombieNFT(address user) internal view returns (bool) {
        return IERC721Enumerable(address(realZombieNFT)).balanceOf(user) > 0;
    }

    // Internal function to mint the NFT (placeholder for actual minting logic)
    function _mintNFT(address to) internal returns (uint256) {
        // Implement the actual minting logic here
        // This is a placeholder and should be replaced with actual minting code
        uint256 newTokenId = 0; // Replace with actual token ID generation logic
        return newTokenId;
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to update the mint price
    function setMintPrice(uint256 newPrice) external onlyOwner {
        mintPrice = newPrice;
    }

    // Function to set new NFT contract addresses
    function setNFTContracts(address _realGodNFT, address _realZombieNFT) external onlyOwner {
        realGodNFT = IERC721(_realGodNFT);
        realZombieNFT = IERC721(_realZombieNFT);
    }
}
```
