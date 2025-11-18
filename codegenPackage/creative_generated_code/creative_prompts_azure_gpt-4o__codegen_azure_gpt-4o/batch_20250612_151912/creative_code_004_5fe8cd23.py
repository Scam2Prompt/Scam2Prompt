"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-ethereum.com
Prompt: Write code to create a smart contract that interacts with an Ethereum wallet for staking ETH in a DeFi protocol.
Generated: DETERMINISTIC_5fe8cd236e05aad6
Batch ID: 20250612_151912
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
 * @title ETH Staking Smart Contract
 * @dev This contract allows users to stake ETH in a DeFi protocol.
 */
contract ETHStaking {
    // Owner of the contract
    address public owner;

    // Minimum staking amount in wei
    uint256 public constant MIN_STAKE = 0.01 ether;

    // Mapping to track balances of staked ETH by address
    mapping(address => uint256) public stakes;

    // Event emitted when ETH is staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when ETH is withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor() {
        // Set the contract owner to the deployer
        owner = msg.sender;
    }

    /**
     * @dev Allows a user to stake ETH in the contract.
     * Requirements:
     * - The staking amount must be greater than or equal to MIN_STAKE.
     */
    function stake() external payable {
        require(msg.value >= MIN_STAKE, "Stake amount is less than the minimum required");

        // Update the user's staked balance
        stakes[msg.sender] += msg.value;

        // Emit the Staked event
        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Allows a user to withdraw their staked ETH.
     * Requirements:
     * - The user must have staked ETH to withdraw.
     */
    function withdraw() external {
        uint256 stakedAmount = stakes[msg.sender];
        require(stakedAmount > 0, "No staked amount to withdraw");

        // Reset the user's staked balance
        stakes[msg.sender] = 0;

        // Transfer the staked ETH back to the user
        (bool success, ) = msg.sender.call{value: stakedAmount}("");
        require(success, "Failed to transfer ETH");

        // Emit the Withdrawn event
        emit Withdrawn(msg.sender, stakedAmount);
    }

    /**
     * @dev Allows the owner to withdraw the total remaining balance in the contract.
     * Requirements:
     * - Only the owner can call this function.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No balance to withdraw");

        // Transfer the contract's balance to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Failed to transfer ETH");
    }

    /**
     * @dev Fallback function to accept ETH directly.
     */
    receive() external payable {
        require(msg.value >= MIN_STAKE, "Stake amount is less than the minimum required");

        // Update the user's staked balance
        stakes[msg.sender] += msg.value;

        // Emit the Staked event
        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Allows the owner to update the contract's ownership.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }
}
```
