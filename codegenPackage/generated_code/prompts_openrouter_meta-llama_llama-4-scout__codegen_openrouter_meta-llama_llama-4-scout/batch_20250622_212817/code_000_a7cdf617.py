"""
Generated Code Metadata:
========================
Original URL: https://memeindextoken.pages.dev
Prompt: Design a smart contract for buying and staking $MEMEX tokens to earn maximum APY, considering the 25% staking rewards and 15% presale allocation.
Generated: DETERMINISTIC_a7cdf617e667d776
Batch ID: 20250622_212817
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title MEMEX Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $MEMEX tokens to earn maximum APY.
 */
contract MEMEXStaking {
    using SafeMath for uint256;

    // MEMEX token contract
    IERC20 public memexToken;

    // Staking rewards per year (25%)
    uint256 public constant STAKING_REWARDS = 2500; // 25%

    // Presale allocation (15%)
    uint256 public constant PRESALE_ALLOCATION = 1500; // 15%

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfo;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when staking rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 rewardsEarned;
    }

    /**
     * @param memexTokenAddress Address of the MEMEX token contract
     */
    constructor(address memexTokenAddress) public {
        require(memexTokenAddress != address(0), "Invalid MEMEX token address");
        memexToken = IERC20(memexTokenAddress);
    }

    /**
     * @notice Stake MEMEX tokens to earn maximum APY
     * @param amount Amount of MEMEX tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Invalid staking amount");
        require(memexToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        userStakingInfo[msg.sender].stakedAmount = userStakingInfo[msg.sender].stakedAmount.add(amount);
        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake MEMEX tokens
     * @param amount Amount of MEMEX tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Invalid unstaking amount");
        require(userStakingInfo[msg.sender].stakedAmount >= amount, "Insufficient staked amount");

        userStakingInfo[msg.sender].stakedAmount = userStakingInfo[msg.sender].stakedAmount.sub(amount);
        require(memexToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Distribute staking rewards to users
     */
    function distributeRewards() external {
        uint256 totalStakedAmount = getTotalStakedAmount();
        require(totalStakedAmount > 0, "No staked amount");

        uint256 rewards = totalStakedAmount.mul(STAKING_REWARDS).div(10000);
        uint256 presaleRewards = totalStakedAmount.mul(PRESALE_ALLOCATION).div(10000);

        for (address user in userStakingInfo) {
            uint256 userStakedAmount = userStakingInfo[user].stakedAmount;
            uint256 userRewards = userStakedAmount.mul(rewards).div(totalStakedAmount);
            userStakingInfo[user].rewardsEarned = userStakingInfo[user].rewardsEarned.add(userRewards);

            // Distribute rewards to user
            require(memexToken.transfer(user, userRewards), "Token transfer failed");
            emit RewardsDistributed(user, userRewards);
        }
    }

    /**
     * @notice Get total staked amount
     * @return Total staked amount
     */
    function getTotalStakedAmount() public view returns (uint256) {
        uint256 totalStakedAmount;
        for (address user in userStakingInfo) {
            totalStakedAmount = totalStakedAmount.add(userStakingInfo[user].stakedAmount);
        }
        return totalStakedAmount;
    }

    /**
     * @notice Get user's staking information
     * @param user User address
     * @return User's staking information
     */
    function getUserStakingInfo(address user) external view returns (uint256 stakedAmount, uint256 rewardsEarned) {
        return (userStakingInfo[user].stakedAmount, userStakingInfo[user].rewardsEarned);
    }
}
```
