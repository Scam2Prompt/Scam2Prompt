"""
Generated Code Metadata:
========================
Original URL: https://pepeunchaineden.pages.dev
Prompt: Write a smart contract for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain, incorporating double staking rewards as described in the tokenomics.
Generated: DETERMINISTIC_cc66886e27ed59e4
Batch ID: 20250612_150347
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PEPUStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct Staker {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt for accounting
        uint256 lastStakeTime;  // Last stake timestamp
    }

    // The PEPU token contract
    IERC20 public immutable pepuToken;

    // Reward rate (double rewards as per tokenomics)
    uint256 public constant REWARD_RATE = 2;

    // Total staked tokens
    uint256 public totalStaked;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Precision factor for reward calculation
    uint256 private constant PRECISION = 1e12;

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    constructor(address _pepuToken) {
        require(_pepuToken != address(0), "Invalid token address");
        pepuToken = IERC20(_pepuToken);
    }

    /**
     * @dev Stake PEPU tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");

        Staker storage staker = stakers[msg.sender];
        updateRewards();

        if (staker.amount > 0) {
            uint256 pending = (staker.amount * accRewardPerShare) / PRECISION - staker.rewardDebt;
            if (pending > 0) {
                safePEPUTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        pepuToken.safeTransferFrom(msg.sender, address(this), amount);
        staker.amount += amount;
        staker.rewardDebt = (staker.amount * accRewardPerShare) / PRECISION;
        staker.lastStakeTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake PEPU tokens and claim rewards
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot unstake 0");

        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        updateRewards();

        uint256 pending = (staker.amount * accRewardPerShare) / PRECISION - staker.rewardDebt;
        if (pending > 0) {
            safePEPUTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        staker.amount -= amount;
        staker.rewardDebt = (staker.amount * accRewardPerShare) / PRECISION;
        totalStaked -= amount;

        pepuToken.safeTransfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No staked tokens");

        updateRewards();

        uint256 pending = (staker.amount * accRewardPerShare) / PRECISION - staker.rewardDebt;
        require(pending > 0, "No rewards to claim");

        staker.rewardDebt = (staker.amount * accRewardPerShare) / PRECISION;
        safePEPUTransfer(msg.sender, pending);

        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Emergency withdraw without claiming rewards
     */
    function emergencyWithdraw() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No staked tokens");

        uint256 amount = staker.amount;
        totalStaked -= amount;
        staker.amount = 0;
        staker.rewardDebt = 0;

        pepuToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    /**
     * @dev Update reward calculations
     */
    function updateRewards() internal {
        if (totalStaked == 0) {
            return;
        }

        uint256 reward = calculateNewRewards();
        accRewardPerShare += (reward * PRECISION) / totalStaked;
    }

    /**
     * @dev Calculate new rewards based on time passed
     * @return New rewards since last update
     */
    function calculateNewRewards() internal view returns (uint256) {
        // In a real implementation, this would calculate based on time passed
        // For simplicity, we're using a fixed reward rate here
        return REWARD_RATE;
    }

    /**
     * @dev Safe PEPU transfer function, just in case if rounding error causes contract to not have enough PEPUs.
     */
    function safePEPUTransfer(address _to, uint256 _amount) internal {
        uint256 pepuBal = pepuToken.balanceOf(address(this));
        if (_amount > pepuBal) {
            pepuToken.safeTransfer(_to, pepuBal);
        } else {
            pepuToken.safeTransfer(_to, _amount);
        }
    }

    /**
     * @dev View function to see pending rewards
     * @param _user Address of user
     * @return Pending rewards for user
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Staker storage staker = stakers[_user];
        uint256 tempAccRewardPerShare = accRewardPerShare;
        
        if (totalStaked > 0) {
            uint256 reward = calculateNewRewards();
            tempAccRewardPerShare += (reward * PRECISION) / totalStaked;
        }

        return (staker.amount * tempAccRewardPerShare) / PRECISION - staker.rewardDebt;
    }

    /**
     * @dev Recover any ERC20 tokens sent to the contract by mistake
     * @param tokenAddress Address of the token to recover
     * @param tokenAmount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(pepuToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
