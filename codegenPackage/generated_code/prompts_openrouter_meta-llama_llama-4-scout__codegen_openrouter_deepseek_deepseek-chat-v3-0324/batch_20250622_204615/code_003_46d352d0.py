"""
Generated Code Metadata:
========================
Original URL: https://solnarize-in.pages.dev
Prompt: Design a simple smart contract in Solidity to manage token allocations and transactions for a project like Solnarize, including functions for buying and claiming tokens.
Generated: DETERMINISTIC_46d352d0ded40b25
Batch ID: 20250622_204615
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract SolnarizeTokenManager is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public tokenPrice;
    uint256 public totalTokensForSale;
    uint256 public tokensSold;
    uint256 public claimStartTime;
    bool public saleActive;

    mapping(address => uint256) public allocations;
    mapping(address => bool) public hasClaimed;

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event TokensClaimed(address indexed claimant, uint256 amount);
    event SaleStatusChanged(bool isActive);
    event TokenPriceUpdated(uint256 newPrice);
    event TokensWithdrawn(uint256 amount);

    constructor(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _totalTokensForSale,
        uint256 _claimStartTime
    ) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_totalTokensForSale > 0, "Total tokens for sale must be greater than zero");

        token = IERC20(_tokenAddress);
        tokenPrice = _tokenPrice;
        totalTokensForSale = _totalTokensForSale;
        claimStartTime = _claimStartTime;
        saleActive = false;
    }

    modifier whenSaleActive() {
        require(saleActive, "Sale is not active");
        _;
    }

    modifier whenClaimingActive() {
        require(block.timestamp >= claimStartTime, "Claiming has not started yet");
        _;
    }

    function buyTokens() external payable whenSaleActive nonReentrant {
        require(msg.value > 0, "Must send ETH to buy tokens");
        uint256 tokenAmount = msg.value / tokenPrice;
        require(tokenAmount > 0, "Insufficient ETH sent");
        require(tokensSold + tokenAmount <= totalTokensForSale, "Not enough tokens left for sale");

        allocations[msg.sender] += tokenAmount;
        tokensSold += tokenAmount;

        emit TokensPurchased(msg.sender, tokenAmount, msg.value);
    }

    function claimTokens() external whenClaimingActive nonReentrant {
        require(allocations[msg.sender] > 0, "No tokens allocated");
        require(!hasClaimed[msg.sender], "Tokens already claimed");

        uint256 amount = allocations[msg.sender];
        hasClaimed[msg.sender] = true;

        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensClaimed(msg.sender, amount);
    }

    function toggleSaleStatus() external onlyOwner {
        saleActive = !saleActive;
        emit SaleStatusChanged(saleActive);
    }

    function setTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Token price must be greater than zero");
        tokenPrice = _newPrice;
        emit TokenPriceUpdated(_newPrice);
    }

    function withdrawTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner(), balance), "Token transfer failed");
        emit TokensWithdrawn(balance);
    }

    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(owner()).transfer(balance);
    }

    function updateClaimStartTime(uint256 _newTime) external onlyOwner {
        claimStartTime = _newTime;
    }

    function getClaimableAmount(address _user) external view returns (uint256) {
        if (block.timestamp < claimStartTime || hasClaimed[_user]) {
            return 0;
        }
        return allocations[_user];
    }
}
```
