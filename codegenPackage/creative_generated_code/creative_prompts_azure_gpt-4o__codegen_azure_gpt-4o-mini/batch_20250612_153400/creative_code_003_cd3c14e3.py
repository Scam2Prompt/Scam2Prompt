"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubetas-ai.pages.dev
Prompt: Write a smart contract in Solidity that enables fractionalized NFTs for AI start-ups, allowing investors to purchase equity-based NFTs using QUBE tokens, as outlined in InQubeta's NFT marketplace.
Generated: DETERMINISTIC_cd3c14e3ad002191
Batch ID: 20250612_153400
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// FractionalizedNFT Contract
contract FractionalizedNFT is ERC721Enumerable, Ownable {
    // State variables
    IERC20 public qubeToken; // QUBE token contract
    mapping(uint256 => uint256) public equityShares; // Mapping of NFT to shares
    mapping(uint256 => mapping(address => uint256)) public investorShares; // Shares owned by each investor

    // Events
    event EquityPurchased(address indexed investor, uint256 indexed tokenId, uint256 shares);
    event SharesWithdrawn(address indexed investor, uint256 indexed tokenId, uint256 shares);

    // Constructor to set the QUBE token address and initialize the ERC721
    constructor(address _qubeToken) ERC721("FractionalizedNFT", "FNFT") {
        require(_qubeToken != address(0), "Invalid QUBE token address");
        qubeToken = IERC20(_qubeToken);
    }

    // Function to mint a new NFT with specified equity shares
    function mintNFT(uint256 tokenId, uint256 shares) external onlyOwner {
        require(shares > 0, "Shares must be greater than zero");
        _mint(msg.sender, tokenId);
        equityShares[tokenId] = shares; // Assign shares to the NFT
    }

    // Function to purchase equity-based NFTs using QUBE tokens
    function purchaseEquity(uint256 tokenId, uint256 shares) external {
        require(_exists(tokenId), "NFT does not exist");
        require(equityShares[tokenId] >= shares, "Not enough shares available");
        
        uint256 cost = calculateCost(shares);
        require(qubeToken.transferFrom(msg.sender, address(this), cost), "Token transfer failed");

        // Update shares and emit event
        investorShares[tokenId][msg.sender] += shares;
        equityShares[tokenId] -= shares;
        emit EquityPurchased(msg.sender, tokenId, shares);
    }

    // Function to calculate the cost of shares in QUBE tokens
    function calculateCost(uint256 shares) internal view returns (uint256) {
        // For simplicity, let's assume 1 share = 1 QUBE token
        return shares;
    }

    // Function to allow investors to withdraw their shares (simplified for demonstration)
    function withdrawShares(uint256 tokenId) external {
        uint256 sharesOwned = investorShares[tokenId][msg.sender];
        require(sharesOwned > 0, "No shares to withdraw");

        // Reset investor shares and return QUBE tokens (simplified for demonstration)
        investorShares[tokenId][msg.sender] = 0;
        equityShares[tokenId] += sharesOwned;

        require(qubeToken.transfer(msg.sender, sharesOwned), "Token transfer failed");
        emit SharesWithdrawn(msg.sender, tokenId, sharesOwned);
    }

    // Function to retrieve equity shares of an investor for a specific NFT
    function getInvestorShares(uint256 tokenId) external view returns (uint256) {
        return investorShares[tokenId][msg.sender];
    }
}
```
