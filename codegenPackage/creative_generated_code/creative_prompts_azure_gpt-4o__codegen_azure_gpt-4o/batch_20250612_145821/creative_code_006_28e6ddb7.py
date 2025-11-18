"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-pepeunchained.pages.dev
Prompt: Provide an example of how to implement double staking rewards for $PEPU tokens on Layer 2 using Solidity.
Generated: DETERMINISTIC_28e6ddb74bcb7220
Batch ID: 20250612_145821
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
 * @title Double Staking Rewards Contract for $PEPU Tokens
 * @dev Implements a staking mechanism with double rewards for $PEPU holders.
 *      Users stake their $PEPU tokens to earn rewards in two separate reward tokens.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DoubleStakingRewards is Ownable, ReentrancyGuard {
    // Token interfaces
    IERC20 public pepuToken;        // The staking token
    IERC20 public rewardToken1;     // First reward token
    IERC20 public rewardToken2;     // Second reward token

    // Staking data structure
    struct Stake {
        uint256 amount;             // Amount of staked tokens
        uint256 rewardDebt1;        // Reward debt for reward token 1
        uint256 rewardDebt2;        // Reward debt for reward token 2
    }

    uint256 public rewardsPerBlock1; // Rewards per block for reward token 1
    uint256 public rewardsPerBlock2; // Rewards per block for reward token 2

    uint256 public lastRewardBlock;  // Last block that rewards were calculated
    uint256 public accRewardPerShare1; // Accumulated rewards per share for reward token 1
    uint256 public accRewardPerShare2; // Accumulated rewards per share for reward token 2

    mapping(address => Stake) public stakes; // Mapping of user addresses to stakes
    uint256 public totalStaked;             // Total amount of tokens staked

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward1, uint256 reward2);

    // Constructor
    constructor(
        address _pepuToken,
        address _rewardToken1,
        address _rewardToken2,
        uint256 _rewardsPerBlock1,
        uint256 _rewardsPerBlock2
    ) {
        pepuToken = IERC20(_pepuToken);
        rewardToken1 = IERC20(_rewardToken1);
        rewardToken2 = IERC20(_rewardToken2);
        rewardsPerBlock1 = _rewardsPerBlock1;
        rewardsPerBlock2 = _rewardsPerBlock2;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Update the reward variables.
     */
    function updatePool() internal {
        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 multiplier = block.number - lastRewardBlock;
        uint256 reward1 = multiplier * rewardsPerBlock1;
        uint256 reward2 = multiplier * rewardsPerBlock2;

        accRewardPerShare1 += (reward1 * 1e12) / totalStaked;
        accRewardPerShare2 += (reward2 * 1e12) / totalStaked;

        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake $PEPU tokens in the contract.
     * @param _amount Amount of $PEPU tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake 0 tokens");

        updatePool();

        Stake storage user = stakes[msg.sender];

        // If there is an existing stake, calculate pending rewards
        if (user.amount > 0) {
            uint256 pending1 = (user.amount * accRewardPerShare1) / 1e12 - user.rewardDebt1;
            uint256 pending2 = (user.amount * accRewardPerShare2) / 1e12 - user.rewardDebt2;

            if (pending1 > 0) {
                rewardToken1.transfer(msg.sender, pending1);
            }
            if (pending2 > 0) {
                rewardToken2.transfer(msg.sender, pending2);
            }
        }

        // Transfer tokens and update user's stake
        pepuToken.transferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.rewardDebt1 = (user.amount * accRewardPerShare1) / 1e12;
        user.rewardDebt2 = (user.amount * accRewardPerShare2) / 1e12;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked $PEPU tokens and claim rewards.
     * @param _amount Amount of $PEPU tokens to withdraw.
     */
    function withdraw(uint256 _amount) external nonReentrant {
        Stake storage user = stakes[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds staked amount");

        updatePool();

        uint256 pending1 = (user.amount * accRewardPerShare1) / 1e12 - user.rewardDebt1;
        uint256 pending2 = (user.amount * accRewardPerShare2) / 1e12 - user.rewardDebt2;

        if (pending1 > 0) {
            rewardToken1.transfer(msg.sender, pending1);
        }
        if (pending2 > 0) {
            rewardToken2.transfer(msg.sender, pending2);
        }

        if (_amount > 0) {
            user.amount -= _amount;
            pepuToken.transfer(msg.sender, _amount);
            totalStaked -= _amount;
        }

        user.rewardDebt1 = (user.amount * accRewardPerShare1) / 1e12;
        user.rewardDebt2 = (user.amount * accRewardPerShare2) / 1e12;

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards without withdrawing staked tokens.
     */
    function claimRewards() external nonReentrant {
        Stake storage user = stakes[msg.sender];

        updatePool();

        uint256 pending1 = (user.amount * accRewardPerShare1) / 1e12 - user.rewardDebt1;
        uint256 pending2 = (user.amount * accRewardPerShare2) / 1e12 - user.rewardDebt2;

        require(pending1 > 0 || pending2 > 0, "No rewards to claim");

        if (pending1 > 0) {
            rewardToken1.transfer(msg.sender, pending1);
        }
        if (pending2 > 0) {
            rewardToken2.transfer(msg.sender, pending2);
        }

        user.rewardDebt1 = (user.amount * accRewardPerShare1) / 1e12;
        user.rewardDebt2 = (user.amount * accRewardPerShare2) / 1e12;

        emit RewardsClaimed(msg.sender, pending1, pending2);
    }

    /**
     * @dev Update reward rates. Only owner can call this.
     * @param _rewardsPerBlock1 New reward rate for reward token 1.
     * @param _rewardsPerBlock2 New reward rate for reward token 2.
     */
    function updateRewardRates(uint256 _rewardsPerBlock1, uint256 _rewardsPerBlock2) external onlyOwner {
        updatePool();
        rewardsPerBlock1 = _rewardsPerBlock1;
        rewardsPerBlock2 = _rewardsPerBlock2;
    }
}
```
