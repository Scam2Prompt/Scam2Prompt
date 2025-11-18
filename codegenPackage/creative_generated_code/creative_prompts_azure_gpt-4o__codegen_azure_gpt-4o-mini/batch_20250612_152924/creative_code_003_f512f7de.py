"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-in.pages.dev
Prompt: Develop a smart contract in Solidity for staking $GBTC tokens, incorporating gamified staking mechanics and exponential reward calculations as described in Green Bitcoin's platform.
Generated: DETERMINISTIC_f512f7de54f6ae77
Batch ID: 20250612_152924
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

// Importing the SafeERC20 library for safe transfer of ERC20 tokens.
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GBTCStaking is Ownable {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // ERC20 token being staked
    IERC20 public gbtcToken;

    // Staker struct to hold staked balance and reward debt
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for exponential calculation
    }

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward multiplier for exponential growth (example: 1.05 for 5% per period)
    uint256 public rewardMultiplier;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _gbtcToken, uint256 _rewardMultiplier) {
        gbtcToken = _gbtcToken;
        rewardMultiplier = _rewardMultiplier;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Update staker information
        Staker storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        gbtcToken.safeTransferFrom(msg.sender, address(this), _amount);
        
        // Update total staked and staker's amount
        staker.amount = staker.amount.add(_amount);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked balance");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Transfer tokens back to the user
        staker.amount = staker.amount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);
        
        gbtcToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards based on staked amount and exponential growth
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);

        uint256 reward = staker.rewardDebt; // Calculate the total rewards for the user

        // Reset the user's reward debt
        staker.rewardDebt = 0;

        // Transfer rewards to the user
        gbtcToken.safeTransfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update rewards
    function _updateRewards(address _user) internal {
        Staker storage staker = stakers[_user];
        if (staker.amount > 0) {
            uint256 pendingReward = staker.amount.mul(rewardMultiplier).div(1e18);
            staker.rewardDebt = staker.rewardDebt.add(pendingReward);
        }
    }

    // Function to change the reward multiplier (only owner can change)
    function changeRewardMultiplier(uint256 _newMultiplier) external onlyOwner {
        rewardMultiplier = _newMultiplier;
    }
}
```
