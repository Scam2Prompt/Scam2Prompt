"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-app.pages.dev
Prompt: Provide an example of how to use ERC-20 tokens to implement a decentralized cloud mining platform, ensuring that mining credits are non-transferable and burned for mining power.
Generated: DETERMINISTIC_f3c3144d06268ed4
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation of a decentralized cloud mining platform using ERC-20 tokens in Solidity.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Decentralized Cloud Mining Platform
 * @dev Implements mining credits based on ERC-20 tokens.
 * Mining credits are non-transferable and burned for mining power.
 */
contract CloudMiningPlatform {
    // Basic ERC-20 implementation for mining credits
    string public name = "MiningCredits";
    string public symbol = "MCR";
    uint8 public decimals = 18;

    // Total supply of mining credits
    uint256 public totalSupply;

    // Mapping to store balances of users
    mapping(address => uint256) private balances;

    // Address of the owner (platform administrator)
    address public owner;

    // Event emitted when mining credits are burned for mining power
    event Burned(address indexed user, uint256 amount);

    // Modifier to restrict access to platform owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor that initializes the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to mint mining credits for a user.
     * @param _to Address of the user receiving mining credits.
     * @param _amount Amount of mining credits to mint.
     */
    function mint(address _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "Cannot mint to zero address");
        require(_amount > 0, "Mint amount must be greater than zero");

        balances[_to] += _amount;
        totalSupply += _amount;
    }

    /**
     * @dev Function to burn mining credits to activate mining power.
     * @param _amount Amount of mining credits to burn.
     */
    function burn(uint256 _amount) external {
        require(_amount > 0, "Burn amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient mining credits");

        // Deduct mining credits from sender
        balances[msg.sender] -= _amount;
        totalSupply -= _amount;

        // Emit burn event
        emit Burned(msg.sender, _amount);

        // Logic for mining power activation goes here
        // (e.g., allocating mining resources to the user)
    }

    /**
     * @dev Function to get the balance of mining credits for a user.
     * @param _user Address of the user.
     * @return Balance of mining credits for the user.
     */
    function balanceOf(address _user) external view returns (uint256) {
        return balances[_user];
    }

    /**
     * @dev Prevent transfer of mining credits.
     * Throws an error if the function is called.
     */
    function transfer(address, uint256) external pure {
        revert("Mining credits are non-transferable");
    }

    /**
     * @dev Prevent approval of mining credits for transfer.
     * Throws an error if the function is called.
     */
    function approve(address, uint256) external pure {
        revert("Mining credits are non-transferable");
    }

    /**
     * @dev Prevent transfer of mining credits via transferFrom.
     * Throws an error if the function is called.
     */
    function transferFrom(address, address, uint256) external pure {
        revert("Mining credits are non-transferable");
    }
}
```
