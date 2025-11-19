"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blindsightofficial.pages.dev
Prompt: Create a function in Solidity that allows users to buy Blindsight tokens and receive rewards based on their holdings.
Generated: DETERMINISTIC_f2c4786ee81e5505
Batch ID: 20250612_140356
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Main contract for Blindsight token sale and rewards
contract BlindsightTokenSale {
    IERC20 public blindsightToken; // The ERC20 token contract
    address public owner; // Owner of the contract
    uint256 public tokenPrice; // Price per token in wei
    uint256 public totalSupply; // Total available tokens for sale

    // Mapping to keep track of user balances
    mapping(address => uint256) public userBalances;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);
    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 rewardAmount);

    // Constructor to initialize the contract
    constructor(IERC20 _blindsightToken, uint256 _tokenPrice, uint256 _totalSupply) {
        blindsightToken = _blindsightToken;
        tokenPrice = _tokenPrice;
        totalSupply = _totalSupply;
        owner = msg.sender;
    }

    // Modifier to restrict functions to the owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Function to buy tokens
    function buyTokens(uint256 _amount) external payable {
        // Calculate the cost of tokens
        uint256 cost = _amount * tokenPrice;
        require(msg.value >= cost, "Insufficient funds sent");
        require(totalSupply >= _amount, "Not enough tokens available");

        // Update total supply and user balance
        totalSupply -= _amount;
        userBalances[msg.sender] += _amount;

        // Transfer tokens to the buyer
        require(blindsightToken.transfer(msg.sender, _amount), "Token transfer failed");

        // Emit purchase event
        emit TokensPurchased(msg.sender, _amount);

        // If excess ether was sent, refund to the buyer
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }
    }

    // Function to distribute rewards based on user's holdings
    function distributeRewards() external {
        uint256 userBalance = userBalances[msg.sender];
        require(userBalance > 0, "No tokens held for rewards");

        // Calculate reward (example: 10% of user's balance)
        uint256 rewardAmount = userBalance / 10;

        // Ensure the contract has enough tokens to pay rewards
        require(blindsightToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance for rewards");

        // Transfer the reward to the user
        require(blindsightToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");

        // Emit rewards distribution event
        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    // Function to withdraw funds from the contract (only owner)
    function withdrawFunds() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens (only owner)
    function withdrawUnsoldTokens() external onlyOwner {
        require(totalSupply > 0, "No unsold tokens to withdraw");
        require(blindsightToken.transfer(owner, totalSupply), "Unsold token transfer failed");
        totalSupply = 0; // All tokens are withdrawn
    }

    // Fallback function to prevent accidental ether transfers
    receive() external payable {
        revert("Direct ether transfer not allowed");
    }
}
```
