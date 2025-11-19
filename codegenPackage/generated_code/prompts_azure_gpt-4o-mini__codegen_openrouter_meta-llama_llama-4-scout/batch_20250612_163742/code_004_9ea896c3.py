"""
Generated Code Metadata:
========================
Original URL: https://alixa.tech
Prompt: Provide an example of how to claim rewards and restake bonds using Alixa's bonding system in a smart contract.
Generated: DETERMINISTIC_9ea896c396ac03fb
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title Alixa Bonding System Contract
 * @author [Your Name]
 * @notice This contract provides functionality for claiming rewards and restaking bonds using Alixa's bonding system.
 */
contract AlixaBondingSystem {
    using SafeMath for uint256;

    // Mapping of user addresses to their bonding information
    mapping (address => BondingInfo) public bondingInfos;

    // Mapping of bond IDs to their respective bond information
    mapping (uint256 => Bond) public bonds;

    // Total number of bonds
    uint256 public totalBonds;

    // Address of the reward token
    IERC20 public rewardToken;

    // Address of the bond token
    IERC20 public bondToken;

    /**
     * @dev Struct representing bonding information for a user
     */
    struct BondingInfo {
        uint256[] bondIds;
        uint256 totalStaked;
        uint256 totalRewards;
    }

    /**
     * @dev Struct representing a bond
     */
    struct Bond {
        uint256 id;
        address user;
        uint256 amount;
        uint256 reward;
        bool isClaimed;
    }

    /**
     * @dev Constructor for the AlixaBondingSystem contract
     * @param _rewardToken Address of the reward token
     * @param _bondToken Address of the bond token
     */
    constructor(IERC20 _rewardToken, IERC20 _bondToken) public {
        rewardToken = _rewardToken;
        bondToken = _bondToken;
    }

    /**
     * @dev Function to create a new bond
     * @param _amount Amount of bond token to stake
     */
    function createBond(uint256 _amount) public {
        require(_amount > 0, "Invalid bond amount");

        // Transfer bond tokens from user to contract
        require(bondToken.transferFrom(msg.sender, address(this), _amount), "Failed to transfer bond tokens");

        // Create a new bond
        Bond memory newBond;
        newBond.id = ++totalBonds;
        newBond.user = msg.sender;
        newBond.amount = _amount;
        newBond.reward = _amount.mul(10); // Assuming 10% reward for simplicity
        newBond.isClaimed = false;

        // Store the new bond
        bonds[totalBonds] = newBond;

        // Update user's bonding information
        bondingInfos[msg.sender].bondIds.push(totalBonds);
        bondingInfos[msg.sender].totalStaked = bondingInfos[msg.sender].totalStaked.add(_amount);
    }

    /**
     * @dev Function to claim rewards and restake bonds
     * @param _bondId ID of the bond to claim rewards and restake
     */
    function claimRewardsAndRestake(uint256 _bondId) public {
        require(bonds[_bondId].user == msg.sender, "Invalid bond owner");
        require(!bonds[_bondId].isClaimed, "Bond already claimed");

        // Calculate reward
        uint256 reward = bonds[_bondId].reward;

        // Update bond status
        bonds[_bondId].isClaimed = true;

        // Transfer reward tokens to user
        require(rewardToken.transfer(msg.sender, reward), "Failed to transfer reward tokens");

        // Update user's bonding information
        bondingInfos[msg.sender].totalRewards = bondingInfos[msg.sender].totalRewards.add(reward);

        // Restake bond
        restakeBond(_bondId);
    }

    /**
     * @dev Function to restake a bond
     * @param _bondId ID of the bond to restake
     */
    function restakeBond(uint256 _bondId) internal {
        // Get bond details
        Bond memory bond = bonds[_bondId];

        // Restake bond by transferring bond tokens back to the user
        require(bondToken.transfer(bond.user, bond.amount), "Failed to transfer bond tokens");

        // Update user's bonding information
        bondingInfos[bond.user].totalStaked = bondingInfos[bond.user].totalStaked.add(bond.amount);
    }

    /**
     * @dev Function to get user's bonding information
     * @param _user Address of the user
     * @return BondingInfo struct containing user's bonding information
     */
    function getBondingInfo(address _user) public view returns (BondingInfo memory) {
        return bondingInfos[_user];
    }
}
```
