"""
Generated Code Metadata:
========================
Original URL: https://etherfi.vercel.app
Prompt: Generate a smart contract code snippet for handling eETH staking and community allocation adjustments as described on the Ether.fi website.
Generated: DETERMINISTIC_ea6759de2cac1421
Batch ID: 20250622_211011
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

/**
 * @title EtherFiStaking
 * @dev Smart contract for handling eETH staking and community allocation adjustments.
 */
contract EtherFiStaking {
    // State variables
    address public owner; // Contract owner
    uint256 public totalStaked; // Total amount of eETH staked
    uint256 public communityAllocation; // Community allocation percentage (e.g., 10% = 1000)

    mapping(address => uint256) public stakedBalances; // Tracks staked balances for each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event CommunityAllocationUpdated(uint256 newAllocation);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor
    constructor(uint256 initialCommunityAllocation) {
        require(initialCommunityAllocation <= 10000, "Allocation must be <= 100%");
        owner = msg.sender;
        communityAllocation = initialCommunityAllocation;
    }

    /**
     * @dev Allows users to stake eETH.
     * @param amount The amount of eETH to stake.
     */
    function stake(uint256 amount) external payable {
        require(amount > 0, "Stake amount must be greater than zero");
        require(msg.value == amount, "Sent value must match stake amount");

        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake eETH.
     * @param amount The amount of eETH to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer the unstaked amount back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Updates the community allocation percentage.
     * @param newAllocation The new community allocation percentage (e.g., 10% = 1000).
     */
    function updateCommunityAllocation(uint256 newAllocation) external onlyOwner {
        require(newAllocation <= 10000, "Allocation must be <= 100%");
        communityAllocation = newAllocation;

        emit CommunityAllocationUpdated(newAllocation);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
