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

/**
 * @title BlindsightTokenSale
 * @dev A contract for purchasing Blindsight tokens and receiving rewards based on holdings.
 */
contract BlindsightTokenSale {
    // Token contract interface
    IERC20 public blindsightToken;

    // Owner of the contract
    address public owner;

    // Token price in wei (for simplicity, 1 token = 0.001 Ether)
    uint256 public tokenPrice = 1000000000000000; // 0.001 ETH

    // Mapping to track user balances for rewards
    mapping(address => uint256) public tokenHoldings;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed holder, uint256 rewardAmount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor: initialize the contract with token address and set the contract owner
    constructor(address _blindsightTokenAddress) {
        require(_blindsightTokenAddress != address(0), "Invalid token address");
        blindsightToken = IERC20(_blindsightTokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Allows users to purchase Blindsight tokens by sending Ether.
     * The number of tokens received is proportional to the Ether sent.
     */
    function buyTokens() external payable {
        require(msg.value > 0, "Must send Ether to purchase tokens");

        uint256 tokenAmount = (msg.value * 1 ether) / tokenPrice;
        require(blindsightToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens available for sale");

        // Transfer tokens to the buyer
        blindsightToken.transfer(msg.sender, tokenAmount);

        // Update the buyer's holdings
        tokenHoldings[msg.sender] += tokenAmount;

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Allows the owner to distribute rewards to token holders based on their holdings.
     * Rewards are proportional to the number of tokens held.
     * Assumes the reward tokens are already deposited in the contract.
     */
    function distributeRewards(uint256 totalRewardAmount) external onlyOwner {
        require(blindsightToken.balanceOf(address(this)) >= totalRewardAmount, "Not enough reward tokens available");

        uint256 totalTokens = blindsightToken.totalSupply();
        require(totalTokens > 0, "No tokens are held");

        for (uint i = 0; i < totalTokens; i++) {
            address tokenHolder = blindsightToken.holderAt(i);
            uint256 holderBalance = tokenHoldings[tokenHolder];
            uint256 reward = (holderBalance * totalRewardAmount) / totalTokens;

            blindsightToken.transfer(tokenHolder, reward);
            emit RewardDistributed(tokenHolder, reward);
        }
    }

    /**
     * @dev Allows the owner to withdraw Ether from the contract.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether available to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Failed to withdraw Ether");
    }
}

// Interface for the ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function totalSupply() external view returns (uint256);
    function holderAt(uint256 index) external view returns (address);
}
```
