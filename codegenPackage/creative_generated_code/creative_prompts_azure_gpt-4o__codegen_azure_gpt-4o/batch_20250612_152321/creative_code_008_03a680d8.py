"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-6s6.pages.dev
Prompt: Create a smart contract in Solidity for the $FROP token that includes features for staking, rewards distribution, and multichain compatibility.
Generated: DETERMINISTIC_03a680d8c9b56f4e
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title FROP Token Smart Contract
 * @dev ERC20 token with staking, rewards distribution, and multichain compatibility
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract FROPToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track staking balances
    mapping(address => uint256) private stakingBalances;
    // Mapping to track last reward claim timestamps
    mapping(address => uint256) private lastRewardClaimTimestamp;
    // Total staked amount
    uint256 public totalStaked;
    // Reward rate per second (can be updated by the owner)
    uint256 public rewardRate;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor to initialize the token name, symbol, and reward rate.
     */
    constructor() ERC20("FROP Token", "FROP") {
        rewardRate = 1 ether; // Example: 1 token rewarded per second for staking
        _mint(msg.sender, 1_000_000 ether); // Mint initial supply
    }

    /**
     * @dev Allows users to stake tokens to earn rewards.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update rewards for the staker
        _updateRewards(msg.sender);

        // Transfer the tokens from the user to the contract for staking
        _transfer(msg.sender, address(this), amount);

        // Update staking balance and total staked amount
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their tokens and claim rewards.
     */
    function unstake() external {
        uint256 stakedAmount = stakingBalances[msg.sender];
        require(stakedAmount > 0, "No tokens staked");

        // Update rewards for the staker
        _updateRewards(msg.sender);

        // Reset staked amount for the user
        stakingBalances[msg.sender] = 0;
        totalStaked = totalStaked.sub(stakedAmount);

        // Transfer staked tokens back to the user
        _transfer(address(this), msg.sender, stakedAmount);

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Allows users to claim their staking rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param newRate The new reward rate per second.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than 0");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Calculates and distributes staking rewards to the user.
     * @param staker The address of the staker.
     */
    function _updateRewards(address staker) internal {
        uint256 stakedAmount = stakingBalances[staker];
        if (stakedAmount == 0) {
            lastRewardClaimTimestamp[staker] = block.timestamp;
            return;
        }

        // Calculate rewards based on the time elapsed
        uint256 elapsedTime = block.timestamp.sub(lastRewardClaimTimestamp[staker]);
        uint256 rewards = stakedAmount.mul(rewardRate).mul(elapsedTime).div(1 ether);

        // Update last reward claim timestamp
        lastRewardClaimTimestamp[staker] = block.timestamp;

        if (rewards > 0) {
            // Mint the rewards and transfer to the user
            _mint(staker, rewards);
            emit RewardsClaimed(staker, rewards);
        }
    }

    /**
     * @dev Returns the staking balance of a user.
     * @param user The address of the user.
     * @return The staking balance of the user.
     */
    function stakingBalance(address user) external view returns (uint256) {
        return stakingBalances[user];
    }

    /**
     * @dev Returns the pending rewards for a user.
     * @param user The address of the user.
     * @return The pending rewards for the user.
     */
    function pendingRewards(address user) external view returns (uint256) {
        uint256 stakedAmount = stakingBalances[user];
        if (stakedAmount == 0) {
            return 0;
        }

        uint256 elapsedTime = block.timestamp.sub(lastRewardClaimTimestamp[user]);
        uint256 rewards = stakedAmount.mul(rewardRate).mul(elapsedTime).div(1 ether);
        return rewards;
    }
}
```
