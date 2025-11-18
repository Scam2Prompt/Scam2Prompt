"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-orbler.pages.dev
Prompt: Develop a smart contract to manage whitelist rewards for NFT airdrops and beta testing events, similar to those offered by Orbler and ACE Animals.
Generated: DETERMINISTIC_d1da3cbcb54a40b2
Batch ID: 20250612_150946
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract WhitelistRewards is Ownable {
    using SafeMath for uint256;

    // Event emitted when a user is added to the whitelist
    event UserWhitelisted(address indexed user);
    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);
    
    // Mapping to track whitelisted addresses
    mapping(address => bool) public whitelistedUsers;
    // Mapping to track claimed rewards
    mapping(address => bool) public claimedRewards;
    // ERC20 token used for rewards
    IERC20 public rewardToken;
    // Total rewards available for distribution
    uint256 public totalRewards;

    // Constructor to initialize the contract with the reward token and total rewards
    constructor(IERC20 _rewardToken, uint256 _totalRewards) {
        rewardToken = _rewardToken;
        totalRewards = _totalRewards;
    }

    // Function to whitelist a user
    function whitelistUser(address _user) external onlyOwner {
        require(!whitelistedUsers[_user], "User is already whitelisted");
        whitelistedUsers[_user] = true;
        emit UserWhitelisted(_user);
    }

    // Function to distribute rewards to whitelisted users
    function distributeRewards() external onlyOwner {
        require(totalRewards > 0, "No rewards available for distribution");

        uint256 rewardAmountPerUser = totalRewards.div(getWhitelistedCount());
        for (uint256 i = 0; i < getWhitelistedCount(); i++) {
            address user = getWhitelistedUserAt(i);
            if (!claimedRewards[user]) {
                claimedRewards[user] = true;
                rewardToken.transfer(user, rewardAmountPerUser);
                emit RewardsDistributed(user, rewardAmountPerUser);
            }
        }
        totalRewards = 0; // Reset total rewards after distribution
    }

    // Function to get the count of whitelisted users
    function getWhitelistedCount() internal view returns (uint256 count) {
        for (uint256 i = 0; i < 256; i++) { // Assumes a maximum of 256 users for simplicity
            address user = address(uint160(i));
            if (whitelistedUsers[user]) {
                count++;
            }
        }
        return count;
    }

    // Function to get a whitelisted user at a specific index
    function getWhitelistedUserAt(uint256 index) internal view returns (address) {
        require(index < getWhitelistedCount(), "Index out of bounds");
        for (uint256 i = 0; i < 256; i++) { // Assumes a maximum of 256 users for simplicity
            address user = address(uint160(i));
            if (whitelistedUsers[user]) {
                if (index == 0) {
                    return user;
                }
                index--;
            }
        }
        revert("User not found");
    }

    // Function to withdraw remaining tokens in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= rewardToken.balanceOf(address(this)), "Insufficient balance");
        rewardToken.transfer(owner(), amount);
    }
}
```
