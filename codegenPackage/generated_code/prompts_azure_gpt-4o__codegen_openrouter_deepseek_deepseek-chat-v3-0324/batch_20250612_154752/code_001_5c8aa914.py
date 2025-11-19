"""
Generated Code Metadata:
========================
Original URL: https://yetiouro.co
Prompt: Create a smart contract in Solidity that incorporates staking and yield farming mechanisms, aligning with Yeti Ouro's tokenomics and roadmap goals.
Generated: DETERMINISTIC_5c8aa914ae22c75a
Batch ID: 20250612_154752
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

contract YetiOuroStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to represent user staking information
    struct UserInfo {
        uint256 amount;     // How many tokens the user has staked
        uint256 rewardDebt; // Reward debt for yield calculation
        uint256 lastStakeTime; // Timestamp of last stake
    }

    // The YETI token contract
    IERC20 public immutable yetiToken;
    
    // The reward token contract (could be same as staking token)
    IERC20 public immutable rewardToken;
    
    // Reward rate per block (in wei)
    uint256 public rewardPerBlock;
    
    // Total tokens staked
    uint256 public totalStaked;
    
    // Accumulated rewards per share (scaled by 1e12)
    uint256 public accRewardPerShare;
    
    // Last block number that rewards were calculated
    uint256 public lastRewardBlock;
    
    // Lockup period in seconds (0 for no lockup)
    uint256 public lockupPeriod;
    
    // Precision factor for reward calculation
    uint256 private constant PRECISION = 1e12;
    
    // Mapping from user address to user info
    mapping(address => UserInfo) public userInfo;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event LockupPeriodUpdated(uint256 newPeriod);

    constructor(
        IERC20 _yetiToken,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _lockupPeriod
    ) {
        require(address(_yetiToken) != address(0), "Invalid token address");
        yetiToken = _yetiToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        lockupPeriod = _lockupPeriod;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Update reward variables to reflect current state
     */
    function updatePool() public {
        if (block.number <= lastRewardBlock) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocksSinceLastReward = block.number - lastRewardBlock;
        uint256 reward = blocksSinceLastReward * rewardPerBlock;

        accRewardPerShare += (reward * PRECISION) / totalStaked;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake tokens to earn rewards
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake 0");

        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / PRECISION - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        yetiToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION;
        user.lastStakeTime = block.timestamp;
        totalStaked += _amount;

        emit Deposit(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens and claim rewards
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");
        require(block.timestamp >= user.lastStakeTime + lockupPeriod, "Tokens are locked");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / PRECISION - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        user.amount -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION;
        totalStaked -= _amount;

        yetiToken.safeTransfer(msg.sender, _amount);
        emit Withdraw(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards without withdrawing staked tokens
     */
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / PRECISION - user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION;
        safeRewardTransfer(msg.sender, pending);

        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Emergency withdraw without caring about rewards
     */
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(block.timestamp >= user.lastStakeTime + lockupPeriod, "Tokens are locked");

        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");

        totalStaked -= amount;
        user.amount = 0;
        user.rewardDebt = 0;

        yetiToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    /**
     * @dev Safe reward transfer function, just in case if rounding error causes pool to not have enough rewards
     */
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        if (_amount > rewardBalance) {
            rewardToken.safeTransfer(_to, rewardBalance);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }

    /**
     * @dev Update the reward rate per block
     * @param _rewardPerBlock New reward rate per block
     */
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        updatePool();
        rewardPerBlock = _rewardPerBlock;
        emit RewardRateUpdated(_rewardPerBlock);
    }

    /**
     * @dev Update the lockup period
     * @param _lockupPeriod New lockup period in seconds
     */
    function setLockupPeriod(uint256 _lockupPeriod) external onlyOwner {
        lockupPeriod = _lockupPeriod;
        emit LockupPeriodUpdated(_lockupPeriod);
    }

    /**
     * @dev View function to see pending rewards for a user
     * @param _user User address
     * @return Pending rewards for user
     */
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 blocksSinceLastReward = block.number - lastRewardBlock;
            uint256 reward = blocksSinceLastReward * rewardPerBlock;
            currentAccRewardPerShare += (reward * PRECISION) / totalStaked;
        }
        
        return (user.amount * currentAccRewardPerShare) / PRECISION - user.rewardDebt;
    }

    /**
     * @dev Recover any ERC20 tokens accidentally sent to this contract
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(yetiToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
