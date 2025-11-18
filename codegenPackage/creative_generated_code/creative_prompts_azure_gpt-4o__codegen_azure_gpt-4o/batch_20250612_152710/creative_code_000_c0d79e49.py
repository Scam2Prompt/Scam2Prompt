"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-de.pages.dev
Prompt: Write an Ethereum smart contract for staking DOGE20 tokens that distributes rewards proportionally to the staker's share in the pool over a two-year period, as described on the Dogecoin20 website.
Generated: DETERMINISTIC_c0d79e49f3ad8c4f
Batch ID: 20250612_152710
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
 * @title DOGE20 Token Staking Contract
 * @dev This contract allows users to stake DOGE20 tokens and earn rewards proportionally to their stake in the pool.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Doge20TokenStaking is Ownable {
    IERC20 public doge20Token; // Reference to the DOGE20 token contract
    uint256 public stakingEndTime; // Timestamp for the end of the staking period
    uint256 public totalStaked; // Total amount of tokens staked in the pool
    uint256 public totalRewards; // Total rewards available for distribution

    struct Staker {
        uint256 amountStaked; // Amount of tokens staked by the user
        uint256 rewardDebt; // Rewards already claimed or owed
    }

    mapping(address => Staker) public stakers; // Mapping of staker addresses to their staking details

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the contract with the DOGE20 token address and reward distribution period.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _totalRewards Total rewards to be distributed over the staking period.
     * @param _stakingDuration Duration (in seconds) of the staking period.
     */
    constructor(
        address _doge20Token,
        uint256 _totalRewards,
        uint256 _stakingDuration
    ) {
        require(_doge20Token != address(0), "Invalid token address");
        require(_totalRewards > 0, "Rewards must be greater than zero");
        require(_stakingDuration > 0, "Invalid staking duration");

        doge20Token = IERC20(_doge20Token);
        totalRewards = _totalRewards;
        stakingEndTime = block.timestamp + _stakingDuration;
    }

    /**
     * @dev Allows users to stake DOGE20 tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(block.timestamp < stakingEndTime, "Staking period has ended");

        // Transfer DOGE20 tokens from the user to the contract
        require(
            doge20Token.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        staker.rewardDebt += pendingRewards(msg.sender);

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     */
    function withdraw() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No staked tokens to withdraw");

        uint256 amount = staker.amountStaked;
        staker.amountStaked = 0;

        // Transfer staked tokens back to the user
        require(doge20Token.transfer(msg.sender, amount), "Token transfer failed");

        totalStaked -= amount;

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their proportional share of rewards.
     */
    function claimRewards() external {
        require(block.timestamp > stakingEndTime, "Staking period not yet ended");

        uint256 rewards = pendingRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim");

        Staker storage staker = stakers[msg.sender];
        staker.rewardDebt = 0;

        // Transfer rewards to the user
        require(doge20Token.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculates the pending rewards for a staker.
     * @param _user Address of the staker.
     * @return Amount of rewards owed to the user.
     */
    function pendingRewards(address _user) public view returns (uint256) {
        if (totalStaked == 0) {
            return 0;
        }

        Staker storage staker = stakers[_user];
        uint256 userShare = (staker.amountStaked * totalRewards) / totalStaked;
        return userShare - staker.rewardDebt;
    }

    /**
     * @dev Emergency function for the contract owner to recover tokens accidentally sent to the contract.
     * @param _token Address of the token to recover.
     * @param _amount Amount of tokens to recover.
     */
    function recoverTokens(address _token, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(IERC20(_token).transfer(owner(), _amount), "Token transfer failed");
    }
}
```
