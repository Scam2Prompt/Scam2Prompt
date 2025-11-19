"""
Generated Code Metadata:
========================
Original URL: https://marketplace-jesse-3on.pages.dev
Prompt: Create a Solidity contract that implements a presale mechanism with tiered pricing and a total supply limit, inspired by the JESSE presale model.
Generated: DETERMINISTIC_e0eaf8fa5d08f72f
Batch ID: 20250612_153401
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract JessePresale is Ownable, ReentrancyGuard {
    // Presale parameters
    uint256 public constant TIER1_PRICE = 0.05 ether; // Price per token in tier 1
    uint256 public constant TIER2_PRICE = 0.075 ether; // Price per token in tier 2
    uint256 public constant TIER3_PRICE = 0.1 ether; // Price per token in tier 3
    uint256 public constant MAX_SUPPLY = 1_000_000 ether; // Total token supply (assuming 18 decimals)
    uint256 public constant MIN_CONTRIBUTION = 0.01 ether;
    uint256 public constant MAX_CONTRIBUTION = 5 ether;

    // Presale state
    uint256 public totalSold;
    uint256 public startTime;
    uint256 public endTime;
    bool public isPresaleActive;
    IERC20 public token;

    // User contributions
    mapping(address => uint256) public contributions;
    mapping(address => uint256) public tokensPurchased;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 tier);
    event PresaleStarted(uint256 startTime, uint256 endTime);
    event PresaleEnded(uint256 endTime);
    event TokensClaimed(address indexed buyer, uint256 amount);

    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        token = IERC20(_tokenAddress);
    }

    modifier whenPresaleActive() {
        require(isPresaleActive, "Presale is not active");
        require(block.timestamp >= startTime, "Presale has not started");
        require(block.timestamp <= endTime, "Presale has ended");
        _;
    }

    function startPresale(uint256 _durationInHours) external onlyOwner {
        require(!isPresaleActive, "Presale is already active");
        startTime = block.timestamp;
        endTime = startTime + (_durationInHours * 1 hours);
        isPresaleActive = true;
        emit PresaleStarted(startTime, endTime);
    }

    function endPresale() external onlyOwner {
        require(isPresaleActive, "Presale is not active");
        isPresaleActive = false;
        endTime = block.timestamp;
        emit PresaleEnded(endTime);
    }

    function buyTokens(uint256 tier) external payable nonReentrant whenPresaleActive {
        require(tier >= 1 && tier <= 3, "Invalid tier");
        require(msg.value >= MIN_CONTRIBUTION, "Contribution too low");
        require(contributions[msg.sender] + msg.value <= MAX_CONTRIBUTION, "Exceeds max contribution");

        uint256 pricePerToken;
        if (tier == 1) {
            pricePerToken = TIER1_PRICE;
        } else if (tier == 2) {
            pricePerToken = TIER2_PRICE;
        } else {
            pricePerToken = TIER3_PRICE;
        }

        uint256 tokenAmount = (msg.value * 1 ether) / pricePerToken;
        require(totalSold + tokenAmount <= MAX_SUPPLY, "Exceeds max supply");

        contributions[msg.sender] += msg.value;
        tokensPurchased[msg.sender] += tokenAmount;
        totalSold += tokenAmount;

        emit TokensPurchased(msg.sender, tokenAmount, tier);
    }

    function claimTokens() external nonReentrant {
        require(!isPresaleActive, "Presale is still active");
        require(tokensPurchased[msg.sender] > 0, "No tokens to claim");

        uint256 amount = tokensPurchased[msg.sender];
        tokensPurchased[msg.sender] = 0;

        require(token.transfer(msg.sender, amount), "Token transfer failed");
        emit TokensClaimed(msg.sender, amount);
    }

    function withdrawFunds() external onlyOwner {
        require(!isPresaleActive, "Presale is still active");
        payable(owner()).transfer(address(this).balance);
    }

    function emergencyWithdrawTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        token.transfer(owner(), balance);
    }

    function getTokenAmount(uint256 ethAmount, uint256 tier) external pure returns (uint256) {
        require(tier >= 1 && tier <= 3, "Invalid tier");
        uint256 pricePerToken;
        if (tier == 1) {
            pricePerToken = TIER1_PRICE;
        } else if (tier == 2) {
            pricePerToken = TIER2_PRICE;
        } else {
            pricePerToken = TIER3_PRICE;
        }
        return (ethAmount * 1 ether) / pricePerToken;
    }
}
```
