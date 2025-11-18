"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burnfi.pages.dev
Prompt: Create a smart contract in Solidity that implements the reward distribution mechanism for $build holders, including proof minting and reflection as outlined in the BurnedFi burn rules.
Generated: DETERMINISTIC_e03f58a3434150b6
Batch ID: 20250612_152410
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
 * @title RewardDistribution
 * @dev A smart contract for distributing rewards to $BUILD holders with proof minting and reflection mechanism.
 * Implements BurnedFi burn rules.
 */
contract RewardDistribution {
    // State variables
    address public owner; // Owner of the contract
    uint256 public totalSupply; // Total supply of $BUILD tokens
    mapping(address => uint256) public balances; // Mapping to track $BUILD token balances
    mapping(address => uint256) public reflectionBalances; // Mapping to track reflection balances
    uint256 public reflectionPool; // Reflection pool amount
    uint256 public burnRate; // Burn rate in percentage (e.g., 2 for 2%)
    uint256 public mintRate; // Mint rate in percentage (e.g., 1 for 1%)

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Burn(address indexed from, uint256 value);
    event Mint(address indexed to, uint256 value);
    event ReflectionDistributed(uint256 value);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor
    constructor(uint256 _initialSupply, uint256 _burnRate, uint256 _mintRate) {
        owner = msg.sender;
        totalSupply = _initialSupply;
        balances[owner] = _initialSupply;
        burnRate = _burnRate;
        mintRate = _mintRate;
    }

    /**
     * @dev Transfer $BUILD tokens from one address to another.
     * Automatically burns a percentage and distributes reflections.
     * @param to Address to transfer to.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address to, uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        require(to != address(0), "Invalid recipient address");

        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 mintAmount = (amount * mintRate) / 100;
        uint256 transferAmount = amount - burnAmount;

        // Burn tokens
        balances[msg.sender] -= amount;
        totalSupply -= burnAmount;
        reflectionPool += burnAmount;
        emit Burn(msg.sender, burnAmount);

        // Mint new tokens
        totalSupply += mintAmount;
        balances[to] += mintAmount;
        emit Mint(to, mintAmount);

        // Transfer tokens
        balances[to] += transferAmount;
        emit Transfer(msg.sender, to, transferAmount);

        // Distribute reflections
        distributeReflections();
    }

    /**
     * @dev Distribute reflection pool to all $BUILD holders proportionally.
     */
    function distributeReflections() private {
        require(reflectionPool > 0, "Reflection pool is empty");
        uint256 totalDistributed = reflectionPool;
        reflectionPool = 0;

        for (uint256 i = 0; i < totalSupply; i++) {
            address holder = address(uint160(i)); // Simulated holder address for this example
            uint256 holderBalance = balances[holder];
            if (holderBalance > 0) {
                uint256 reflectionShare = (totalDistributed * holderBalance) / totalSupply;
                reflectionBalances[holder] += reflectionShare;
            }
        }

        emit ReflectionDistributed(totalDistributed);
    }

    /**
     * @dev Allow the owner to update the burn rate.
     * @param _burnRate New burn rate percentage.
     */
    function updateBurnRate(uint256 _burnRate) external onlyOwner {
        burnRate = _burnRate;
    }

    /**
     * @dev Allow the owner to update the mint rate.
     * @param _mintRate New mint rate percentage.
     */
    function updateMintRate(uint256 _mintRate) external onlyOwner {
        mintRate = _mintRate;
    }

    /**
     * @dev Withdraw reflections for the sender.
     */
    function withdrawReflections() external {
        uint256 reflectionAmount = reflectionBalances[msg.sender];
        require(reflectionAmount > 0, "No reflections to withdraw");

        reflectionBalances[msg.sender] = 0;
        balances[msg.sender] += reflectionAmount;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external {
        revert("ETH transfers not supported");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("ETH transfers not supported");
    }
}
```
