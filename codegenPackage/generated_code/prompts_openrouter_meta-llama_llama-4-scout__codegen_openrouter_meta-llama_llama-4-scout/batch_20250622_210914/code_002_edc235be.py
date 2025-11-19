"""
Generated Code Metadata:
========================
Original URL: https://scottytheaidapp.pages.dev
Prompt: Generate a smart contract code snippet in Solidity for distributing Scotty AI token rewards to users based on their share of the staking pool and annual returns percentage.
Generated: DETERMINISTIC_edc235beda88e7ef
Batch ID: 20250622_210914
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ScottyAI Token Rewards Distribution Contract
 * @author [Your Name]
 * @notice Distributes Scotty AI token rewards to users based on their share of the staking pool and annual returns percentage
 */
contract ScottyAIRewardsDistribution {
    using SafeMath for uint256;

    // Scotty AI token contract instance
    ERC20 public scottyToken;

    // Mapping of user staking balances
    mapping (address => uint256) public stakingBalances;

    // Mapping of user reward claims
    mapping (address => uint256) public rewardClaims;

    // Annual returns percentage (in basis points, e.g., 1000 = 10%)
    uint256 public annualReturnsPercentage;

    // Staking pool total
    uint256 public stakingPoolTotal;

    // Reward token distribution events
    event RewardsDistributed(address indexed user, uint256 rewardAmount);
    event StakingBalanceUpdated(address indexed user, uint256 newBalance);

    /**
     * @dev Constructor
     * @param _scottyToken Scotty AI token contract address
     * @param _annualReturnsPercentage Annual returns percentage (in basis points)
     */
    constructor(address _scottyToken, uint256 _annualReturnsPercentage) public {
        require(_scottyToken != address(0), "Scotty token contract address cannot be zero");
        require(_annualReturnsPercentage > 0, "Annual returns percentage must be greater than zero");

        scottyToken = ERC20(_scottyToken);
        annualReturnsPercentage = _annualReturnsPercentage;
    }

    /**
     * @dev Updates user staking balance
     * @param _user User address
     * @param _newBalance New staking balance
     */
    function updateStakingBalance(address _user, uint256 _newBalance) public onlyOwner {
        require(_user != address(0), "User address cannot be zero");
        require(_newBalance >= 0, "New staking balance must be non-negative");

        stakingBalances[_user] = _newBalance;
        stakingPoolTotal = stakingPoolTotal.add(_newBalance).sub(stakingBalances[_user]);
        emit StakingBalanceUpdated(_user, _newBalance);
    }

    /**
     * @dev Calculates user reward
     * @param _user User address
     * @return Reward amount
     */
    function calculateReward(address _user) public view returns (uint256) {
        uint256 userStakingBalance = stakingBalances[_user];
        uint256 reward = userStakingBalance.mul(annualReturnsPercentage).div(10000);
        return reward;
    }

    /**
     * @dev Distributes rewards to users
     * @param _users Array of user addresses
     */
    function distributeRewards(address[] memory _users) public onlyOwner {
        for (uint256 i = 0; i < _users.length; i++) {
            address user = _users[i];
            uint256 reward = calculateReward(user);

            // Check if user has a staking balance and reward amount is greater than zero
            if (stakingBalances[user] > 0 && reward > 0) {
                // Transfer reward tokens to user
                require(scottyToken.transfer(user, reward), "Reward token transfer failed");

                // Update user's reward claim
                rewardClaims[user] = rewardClaims[user].add(reward);

                emit RewardsDistributed(user, reward);
            }
        }
    }

    /**
     * @dev Modifier for only owner
     */
    modifier onlyOwner {
        require(msg.sender == owner(), "Only the owner can call this function");
        _;
    }

    /**
     * @dev Returns contract owner
     * @return Owner address
     */
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
