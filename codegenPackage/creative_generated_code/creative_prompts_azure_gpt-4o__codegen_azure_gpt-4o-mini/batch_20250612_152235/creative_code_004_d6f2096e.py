"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decrypt-nft.pages.dev
Prompt: Develop a smart contract in Solidity to manage the distribution of unique NFTs, ensuring eligibility verification and one-NFT-per-user constraints as outlined on the Decrypt NFT page.
Generated: DETERMINISTIC_d6f2096e50b89eea
Batch ID: 20250612_152235
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract to manage unique NFTs distribution
contract UniqueNFT is ERC721Enumerable, Ownable {
    // Mapping to track NFT eligibility and distribution
    mapping(address => bool) public hasClaimed;
    // Event emitted when an NFT is minted
    event NFTMinted(address indexed recipient, uint256 tokenId);

    // Counter for the token IDs
    uint256 private _tokenIdCounter;

    // Constructor to set the NFT name and symbol
    constructor() ERC721("UniqueNFT", "UNFT") {}

    // Function to mint a new NFT
    function mintNFT() external {
        // Check if the user has already claimed an NFT
        require(!hasClaimed[msg.sender], "You have already claimed an NFT.");
        
        // Mint the NFT
        uint256 tokenId = _tokenIdCounter++;
        hasClaimed[msg.sender] = true;
        _mint(msg.sender, tokenId);

        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to see the current token count
    function getCurrentTokenId() external view returns (uint256) {
        return _tokenIdCounter;
    }

    // Function to withdraw any accidental Ether sent to the contract
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw tokens if they are mistakenly sent to this contract
    function withdrawERC20(address tokenAddress) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        token.transfer(owner(), balance);
    }
}

// Interface for ERC20 to allow token withdrawals
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
