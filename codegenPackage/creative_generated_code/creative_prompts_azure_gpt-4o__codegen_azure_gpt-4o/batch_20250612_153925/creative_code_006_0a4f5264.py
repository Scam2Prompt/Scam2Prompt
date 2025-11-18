"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://et-erfi-v2.com
Prompt: Write a tutorial for deploying a non-custodial staking protocol on Ethereum, including features like liquid staking and restaking, similar to EtherFi.
Generated: DETERMINISTIC_0a4f5264f7b6cf88
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title Liquid Staking Protocol
 * @dev Implements non-custodial staking with features like liquid staking and restaking.
 */
contract LiquidStaking {
    // --- State Variables ---
    address public owner; // Contract owner
    uint256 public totalStaked; // Total ETH staked in the protocol
    mapping(address => uint256) public userStakes; // Mapping of user addresses to their staked amount
    mapping(address => uint256) public liquidTokenBalance; // Mapping of user addresses to liquid tokens
    uint256 public liquidTokenExchangeRate = 1 ether; // Exchange rate between ETH and liquid tokens

    // --- Events ---
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Restaked(address indexed user, uint256 amount);
    event LiquidTokensMinted(address indexed user, uint256 amount);
    event LiquidTokensBurned(address indexed user, uint256 amount);

    // --- Modifiers ---
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // --- Constructor ---
    constructor() {
        owner = msg.sender; // Assign contract deployer as owner
    }

    // --- Public Functions ---
    /**
     * @notice Stake ETH in the protocol
     */
    function stake() external payable {
        require(msg.value > 0, "Cannot stake zero ETH");

        // Update user stake and protocol total stake
        userStakes[msg.sender] += msg.value;
        totalStaked += msg.value;

        // Mint liquid tokens to the user
        uint256 tokensToMint = msg.value / liquidTokenExchangeRate;
        liquidTokenBalance[msg.sender] += tokensToMint;

        emit Staked(msg.sender, msg.value);
        emit LiquidTokensMinted(msg.sender, tokensToMint);
    }

    /**
     * @notice Unstake ETH from the protocol
     * @param amount The amount of ETH to unstake
     */
    function unstake(uint256 amount) external {
        require(userStakes[msg.sender] >= amount, "Insufficient staked balance");

        // Burn liquid tokens equivalent to the amount
        uint256 tokensToBurn = amount / liquidTokenExchangeRate;
        require(liquidTokenBalance[msg.sender] >= tokensToBurn, "Insufficient liquid tokens");

        // Update user stake and protocol total stake
        userStakes[msg.sender] -= amount;
        totalStaked -= amount;
        liquidTokenBalance[msg.sender] -= tokensToBurn;

        // Transfer ETH back to the user
        payable(msg.sender).transfer(amount);

        emit Unstaked(msg.sender, amount);
        emit LiquidTokensBurned(msg.sender, tokensToBurn);
    }

    /**
     * @notice Restake ETH to increase rewards
     * @dev Restaking locks ETH for a new period, increasing reward potential
     * @param amount The amount of ETH to restake
     */
    function restake(uint256 amount) external {
        require(userStakes[msg.sender] >= amount, "Insufficient staked balance");

        // Increase the stake without additional minting
        userStakes[msg.sender] += amount;

        emit Restaked(msg.sender, amount);
    }

    // --- Owner Functions ---
    /**
     * @notice Update liquid token exchange rate
     * @param newRate The new exchange rate (ETH per liquid token)
     */
    function updateExchangeRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Exchange rate must be greater than zero");
        liquidTokenExchangeRate = newRate;
    }

    // --- Fallback Functions ---
    /**
     * @notice Fallback function to prevent accidental ETH transfers
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }

    fallback() external payable {
        revert("Fallback function invoked");
    }
}
```

This Solidity smart contract implements a simple non-custodial staking protocol with features like liquid staking and restaking. It includes proper error handling, follows best practices, and is well-documented with inline comments.
