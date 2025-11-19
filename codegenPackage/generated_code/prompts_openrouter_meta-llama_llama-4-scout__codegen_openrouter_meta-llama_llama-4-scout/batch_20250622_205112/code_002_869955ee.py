"""
Generated Code Metadata:
========================
Original URL: https://pushdtoken.pages.dev
Prompt: "Design a smart contract for a decentralized rewards program that incentivizes users to participate in the growth of a blockchain-based marketplace like Pushd."
Generated: DETERMINISTIC_869955eeb392f0bb
Batch ID: 20250622_205112
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Pushd Rewards Contract
 * @author [Your Name]
 * @notice A smart contract for a decentralized rewards program that incentivizes users to participate in the growth of a blockchain-based marketplace like Pushd.
 */
contract PushdRewards is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user addresses to their reward balances
    mapping(address => uint256) public rewardBalances;

    // Mapping of user addresses to their participation levels
    mapping(address => uint256) public participationLevels;

    // The ERC20 token used for rewards
    ERC20 public rewardsToken;

    // The address of the marketplace contract
    address public marketplaceContract;

    // The rate at which rewards are distributed per participation level
    uint256 public rewardRate;

    // Event emitted when a user earns rewards
    event RewardsEarned(address indexed user, uint256 amount);

    // Event emitted when a user's participation level is updated
    event ParticipationLevelUpdated(address indexed user, uint256 level);

    /**
     * @notice Initializes the PushdRewards contract
     * @param _rewardsToken The address of the ERC20 token used for rewards
     * @param _marketplaceContract The address of the marketplace contract
     * @param _rewardRate The rate at which rewards are distributed per participation level
     */
    constructor(ERC20 _rewardsToken, address _marketplaceContract, uint256 _rewardRate) {
        rewardsToken = _rewardsToken;
        marketplaceContract = _marketplaceContract;
        rewardRate = _rewardRate;
    }

    /**
     * @notice Updates a user's participation level
     * @param _user The address of the user
     * @param _level The new participation level
     */
    function updateParticipationLevel(address _user, uint256 _level) public {
        // Only the marketplace contract can update participation levels
        require(msg.sender == marketplaceContract, "Only the marketplace contract can update participation levels");

        participationLevels[_user] = _level;
        emit ParticipationLevelUpdated(_user, _level);
    }

    /**
     * @notice Calculates and distributes rewards to a user
     * @param _user The address of the user
     */
    function earnRewards(address _user) public nonReentrant {
        // Only the marketplace contract can trigger reward distribution
        require(msg.sender == marketplaceContract, "Only the marketplace contract can trigger reward distribution");

        uint256 participationLevel = participationLevels[_user];
        uint256 rewardAmount = participationLevel.mul(rewardRate);

        // Ensure the contract has sufficient rewards tokens
        require(rewardsToken.balanceOf(address(this)) >= rewardAmount, "Insufficient rewards tokens");

        rewardBalances[_user] = rewardBalances[_user].add(rewardAmount);
        rewardsToken.transfer(_user, rewardAmount);

        emit RewardsEarned(_user, rewardAmount);
    }

    /**
     * @notice Allows a user to claim their rewards
     */
    function claimRewards() public nonReentrant {
        uint256 rewardAmount = rewardBalances[msg.sender];

        // Ensure the user has earned rewards
        require(rewardAmount > 0, "No rewards to claim");

        rewardBalances[msg.sender] = 0;
        rewardsToken.transfer(msg.sender, rewardAmount);
    }

    /**
     * @notice Allows the owner to update the reward rate
     * @param _newRewardRate The new reward rate
     */
    function updateRewardRate(uint256 _newRewardRate) public {
        // Only the contract owner can update the reward rate
        require(msg.sender == owner(), "Only the contract owner can update the reward rate");

        rewardRate = _newRewardRate;
    }

    /**
     * @notice Allows the owner to transfer rewards tokens to the contract
     * @param _amount The amount of rewards tokens to transfer
     */
    function fundRewards(uint256 _amount) public {
        // Only the contract owner can fund rewards
        require(msg.sender == owner(), "Only the contract owner can fund rewards");

        rewardsToken.transferFrom(msg.sender, address(this), _amount);
    }

    /**
     * @notice Gets the contract owner
     * @return The address of the contract owner
     */
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
