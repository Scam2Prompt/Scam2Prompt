"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogclaim.pages.dev
Prompt: Write a smart contract in Solidity for staking $FROP tokens with a reward distribution mechanism similar to the one described on the Popo The Frog webpage. Ensure the contract supports multiple blockchain networks like BNB Chain, Ethereum, and Polygon.
Generated: DETERMINISTIC_16d7c9be18f288fb
Batch ID: 20250612_151648
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
 * @title StakingContract for $FROP Tokens
 * @dev This smart contract allows users to stake $FROP tokens and earn rewards.
 * It is compatible with multiple EVM-based networks like BNB Chain, Ethereum, and Polygon.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract FROPStaking is Ownable, ReentrancyGuard {
    // $FROP Token contract interface
    IERC20 public immutable fropToken;

    // Reward rate per block (modifiable by the owner)
    uint256 public rewardRatePerBlock;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // User staking information
    struct Staker {
        uint256 amountStaked;
        uint256 lastRewardBlock;
        uint256 pendingRewards;
    }

    // Mapping of user addresses to their staking info
    mapping(address => Staker) public stakers;

    // Events to track activity
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);
    event RewardRateUpdated(uint256 newRewardRate);

    /**
     * @dev Constructor initializes the contract with the $FROP token address and reward rate.
     * @param _fropToken Address of the $FROP token contract.
     * @param _rewardRatePerBlock Initial reward rate distributed per block.
     */
    constructor(IERC20 _fropToken, uint256 _rewardRatePerBlock) {
        require(address(_fropToken) != address(0), "Invalid token address");
        require(_rewardRatePerBlock > 0, "Reward rate must be greater than zero");

        fropToken = _fropToken;
        rewardRatePerBlock = _rewardRatePerBlock;
    }

    /**
     * @dev Allows users to stake $FROP tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(fropToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Update rewards for the user before modifying their state
        _updateRewards(msg.sender);

        // Transfer $FROP tokens from the user to the contract
        fropToken.transferFrom(msg.sender, address(this), _amount);

        // Update staking information
        stakers[msg.sender].amountStaked += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their $FROP tokens and claim rewards.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakers[msg.sender].amountStaked >= _amount, "Insufficient staked amount");

        // Update rewards for the user before modifying their state
        _updateRewards(msg.sender);

        // Update staking information
        stakers[msg.sender].amountStaked -= _amount;
        totalStaked -= _amount;

        // Transfer $FROP tokens back to the user
        fropToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their pending rewards.
     */
    function claimRewards() external nonReentrant {
        _updateRewards(msg.sender);
        uint256 rewards = stakers[msg.sender].pendingRewards;
        require(rewards > 0, "No rewards available");

        // Reset pending rewards
        stakers[msg.sender].pendingRewards = 0;

        // Transfer rewards to the user
        fropToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Updates the reward rate per block. Callable only by the contract owner.
     * @param _newRewardRate New reward rate per block.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRatePerBlock = _newRewardRate;

        emit RewardRateUpdated(_newRewardRate);
    }

    /**
     * @dev Internal function to update rewards for a staker.
     * @param _user Address of the staker.
     */
    function _updateRewards(address _user) internal {
        Staker storage staker = stakers[_user];
        if (staker.amountStaked > 0) {
            uint256 blocksPassed = block.number - staker.lastRewardBlock;
            uint256 rewards = blocksPassed * rewardRatePerBlock * staker.amountStaked / totalStaked;
            staker.pendingRewards += rewards;
        }
        staker.lastRewardBlock = block.number;
    }

    /**
     * @dev Retrieves the pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards for the user.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Staker memory staker = stakers[_user];
        if (staker.amountStaked > 0) {
            uint256 blocksPassed = block.number - staker.lastRewardBlock;
            uint256 rewards = blocksPassed * rewardRatePerBlock * staker.amountStaked / totalStaked;
            return staker.pendingRewards + rewards;
        }
        return 0;
    }
}
```
