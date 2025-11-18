"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rockketpool.github.io
Prompt: Write a smart contract that automates the distribution of staking rewards from Rocket Pool to multiple users based on their rETH holdings.
Generated: DETERMINISTIC_0937d85fbbd5ee0b
Batch ID: 20250612_145223
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

// Smart contract to distribute staking rewards based on rETH holdings.

interface IRocketPoolToken {
    function balanceOf(address account) external view returns (uint256);
    function totalSupply() external view returns (uint256);
}

contract StakingRewardsDistributor {
    // Address of the rETH token contract
    address public rETHContract;

    // Owner of the contract
    address public owner;

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 totalRewards, uint256 timestamp);

    // Event emitted when the owner is updated
    event OwnerUpdated(address indexed oldOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized: caller is not the owner");
        _;
    }

    constructor(address _rETHContract) {
        require(_rETHContract != address(0), "Invalid rETH contract address");
        rETHContract = _rETHContract;
        owner = msg.sender; // Set contract deployer as owner
    }

    // Update owner of the contract
    function updateOwner(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        emit OwnerUpdated(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Distributes staking rewards to all holders of rETH.
     * Each holder receives rewards proportional to their rETH holdings.
     */
    function distributeRewards() external payable onlyOwner {
        require(msg.value > 0, "No rewards to distribute");

        IRocketPoolToken rETH = IRocketPoolToken(rETHContract);

        // Fetch total supply of rETH
        uint256 totalSupply = rETH.totalSupply();
        require(totalSupply > 0, "No rETH supply to distribute rewards");

        // Loop through all rETH holders to distribute rewards
        // WARNING: This approach assumes the contract has a manageable list of known holders.
        address[] memory holders = getHolders(); // This function must be implemented off-chain or with external oracles.
        uint256 totalRewards = msg.value;

        for (uint256 i = 0; i < holders.length; i++) {
            address holder = holders[i];
            uint256 holderBalance = rETH.balanceOf(holder);

            // Calculate the share of rewards for the current holder
            uint256 reward = (totalRewards * holderBalance) / totalSupply;

            // Send the reward to the holder
            (bool success, ) = holder.call{value: reward}("");
            require(success, "Reward transfer failed");
        }

        emit RewardsDistributed(totalRewards, block.timestamp);
    }

    /**
     * @notice Placeholder for off-chain or oracle-based solution to fetch rETH holders.
     * In production, this should be replaced with a reliable external mechanism.
     */
    function getHolders() internal view returns (address[] memory) {
        revert("Holder fetching not implemented");
    }

    // Fallback function to prevent accidental ETH transfers
    fallback() external payable {
        revert("Fallback function: ETH transfers not allowed");
    }

    // Receive function to handle direct ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
