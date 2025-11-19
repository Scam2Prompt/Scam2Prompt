"""
Generated Code Metadata:
========================
Original URL: https://pepe-buy.pages.dev
Prompt: Write a Solidity function to calculate and distribute staking rewards for $PEPU tokens, ensuring compatibility with the tokenomics described on the Pepe Unchained site.
Generated: DETERMINISTIC_40327b415dafc74c
Batch ID: 20250612_151347
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title StakingRewardsCalculator
 * @author [Your Name]
 * @notice Calculates and distributes staking rewards for $PEPU tokens.
 */
contract StakingRewardsCalculator {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward claims
    mapping(address => uint256) public lastClaimTimestamps;

    // $PEPU token contract
    IERC20 public pepuToken;

    // Rewards per second
    uint256 public rewardsPerSecond;

    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _pepuToken $PEPU token contract address
     * @param _rewardsPerSecond Rewards per second
     */
    constructor(address _pepuToken, uint256 _rewardsPerSecond) public {
        require(_pepuToken != address(0), "Invalid token address");
        pepuToken = IERC20(_pepuToken);
        rewardsPerSecond = _rewardsPerSecond;
    }

    /**
     * @dev Updates user staking balance
     * @param _user User address
     * @param _newBalance New staking balance
     */
    function updateStakingBalance(address _user, uint256 _newBalance) public {
        require(_user != address(0), "Invalid user address");
        stakingBalances[_user] = _newBalance;
    }

    /**
     * @dev Calculates and distributes staking rewards for a user
     * @param _user User address
     */
    function distributeRewards(address _user) public {
        require(_user != address(0), "Invalid user address");
        uint256 currentBalance = stakingBalances[_user];
        require(currentBalance > 0, "User has no staking balance");

        uint256 lastClaimTimestamp = lastClaimTimestamps[_user];
        uint256 secondsSinceLastClaim = block.timestamp.sub(lastClaimTimestamp);

        // Calculate rewards
        uint256 rewards = secondsSinceLastClaim.mul(rewardsPerSecond).mul(currentBalance).div(1e18);

        // Update last claim timestamp
        lastClaimTimestamps[_user] = block.timestamp;

        // Distribute rewards
        pepuToken.transfer(_user, rewards);
        totalRewardsDistributed = totalRewardsDistributed.add(rewards);

        emit RewardsDistributed(_user, rewards);
    }

    /**
     * @dev Withdraws staking balance and pending rewards
     * @param _user User address
     */
    function withdrawStakingBalance(address _user) public {
        require(_user != address(0), "Invalid user address");
        uint256 currentBalance = stakingBalances[_user];
        require(currentBalance > 0, "User has no staking balance");

        // Distribute pending rewards
        distributeRewards(_user);

        // Withdraw staking balance
        stakingBalances[_user] = 0;
        pepuToken.transfer(_user, currentBalance);
    }
}
```
