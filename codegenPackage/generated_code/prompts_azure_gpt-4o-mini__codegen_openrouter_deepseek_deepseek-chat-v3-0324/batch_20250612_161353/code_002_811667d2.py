"""
Generated Code Metadata:
========================
Original URL: https://pablo-defis.web.app
Prompt: Create a Solidity smart contract that implements the staking protocol described in the Pablo ecosystem, ensuring revenue sharing in both $PABLO tokens and USDT.
Generated: DETERMINISTIC_811667d2a87196b4
Batch ID: 20250612_161353
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

contract PabloStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to represent a staker's information
    struct StakerInfo {
        uint256 amount; // Amount of PABLO tokens staked
        uint256 rewardDebtPablo; // Reward debt for PABLO
        uint256 rewardDebtUsdt; // Reward debt for USDT
        uint256 lastStakeTime; // Timestamp of last stake
    }

    // Staking token (PABLO)
    IERC20 public immutable stakingToken;
    
    // Reward tokens (PABLO and USDT)
    IERC20 public immutable rewardTokenPablo;
    IERC20 public immutable rewardTokenUsdt;

    // Total staked amount
    uint256 public totalStaked;

    // Reward distribution parameters
    uint256 public rewardPerBlockPablo;
    uint256 public rewardPerBlockUsdt;
    uint256 public lastRewardBlock;

    // Accumulated rewards per share
    uint256 public accRewardPerSharePablo;
    uint256 public accRewardPerShareUsdt;

    // Staking duration parameters
    uint256 public constant MIN_STAKE_DURATION = 7 days;
    uint256 public constant MAX_STAKE_DURATION = 365 days;

    // Mapping of staker addresses to their info
    mapping(address => StakerInfo) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 pabloAmount, uint256 usdtAmount);
    event RewardParametersUpdated(uint256 pabloPerBlock, uint256 usdtPerBlock);

    constructor(
        address _stakingToken,
        address _rewardTokenPablo,
        address _rewardTokenUsdt,
        uint256 _rewardPerBlockPablo,
        uint256 _rewardPerBlockUsdt
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardTokenPablo != address(0), "Invalid PABLO reward token address");
        require(_rewardTokenUsdt != address(0), "Invalid USDT reward token address");

        stakingToken = IERC20(_stakingToken);
        rewardTokenPablo = IERC20(_rewardTokenPablo);
        rewardTokenUsdt = IERC20(_rewardTokenUsdt);
        rewardPerBlockPablo = _rewardPerBlockPablo;
        rewardPerBlockUsdt = _rewardPerBlockUsdt;
        lastRewardBlock = block.number;
    }

    // Update reward variables
    function updatePool() internal {
        if (block.number <= lastRewardBlock) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocksSinceLastReward = block.number - lastRewardBlock;
        uint256 pabloReward = blocksSinceLastReward * rewardPerBlockPablo;
        uint256 usdtReward = blocksSinceLastReward * rewardPerBlockUsdt;

        accRewardPerSharePablo += (pabloReward * 1e12) / totalStaked;
        accRewardPerShareUsdt += (usdtReward * 1e12) / totalStaked;
        lastRewardBlock = block.number;
    }

    // Stake PABLO tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake 0 tokens");
        
        updatePool();
        
        StakerInfo storage staker = stakers[msg.sender];
        
        // Claim pending rewards if already staking
        if (staker.amount > 0) {
            _claimRewards();
        }

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
        
        // Update staker info
        staker.amount += _amount;
        staker.rewardDebtPablo = (staker.amount * accRewardPerSharePablo) / 1e12;
        staker.rewardDebtUsdt = (staker.amount * accRewardPerShareUsdt) / 1e12;
        staker.lastStakeTime = block.timestamp;
        
        // Update total staked
        totalStaked += _amount;
        
        emit Staked(msg.sender, _amount);
    }

    // Unstake PABLO tokens
    function unstake(uint256 _amount) external nonReentrant {
        StakerInfo storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");
        require(
            block.timestamp >= staker.lastStakeTime + MIN_STAKE_DURATION,
            "Minimum stake duration not reached"
        );

        updatePool();
        _claimRewards();

        // Calculate early unstake penalty if applicable
        uint256 penalty = 0;
        if (block.timestamp < staker.lastStakeTime + MAX_STAKE_DURATION) {
            penalty = (_amount * 10) / 100; // 10% penalty for early unstake
        }

        uint256 amountToTransfer = _amount - penalty;
        
        // Update staker info
        staker.amount -= _amount;
        staker.rewardDebtPablo = (staker.amount * accRewardPerSharePablo) / 1e12;
        staker.rewardDebtUsdt = (staker.amount * accRewardPerShareUsdt) / 1e12;
        
        // Update total staked
        totalStaked -= _amount;
        
        // Transfer tokens back to user
        if (amountToTransfer > 0) {
            stakingToken.safeTransfer(msg.sender, amountToTransfer);
        }
        
        // Burn penalty tokens if any
        if (penalty > 0) {
            stakingToken.safeTransfer(address(0xdead), penalty);
        }
        
        emit Unstaked(msg.sender, _amount);
    }

    // Claim rewards
    function claimRewards() external nonReentrant {
        updatePool();
        _claimRewards();
    }

    // Internal function to claim rewards
    function _claimRewards() internal {
        StakerInfo storage staker = stakers[msg.sender];
        if (staker.amount == 0) return;

        uint256 pendingPablo = (staker.amount * accRewardPerSharePablo) / 1e12 - staker.rewardDebtPablo;
        uint256 pendingUsdt = (staker.amount * accRewardPerShareUsdt) / 1e12 - staker.rewardDebtUsdt;

        if (pendingPablo > 0) {
            rewardTokenPablo.safeTransfer(msg.sender, pendingPablo);
        }
        if (pendingUsdt > 0) {
            rewardTokenUsdt.safeTransfer(msg.sender, pendingUsdt);
        }

        staker.rewardDebtPablo = (staker.amount * accRewardPerSharePablo) / 1e12;
        staker.rewardDebtUsdt = (staker.amount * accRewardPerShareUsdt) / 1e12;

        emit RewardClaimed(msg.sender, pendingPablo, pendingUsdt);
    }

    // Update reward distribution parameters (owner only)
    function updateRewardParameters(uint256 _pabloPerBlock, uint256 _usdtPerBlock) external onlyOwner {
        updatePool();
        rewardPerBlockPablo = _pabloPerBlock;
        rewardPerBlockUsdt = _usdtPerBlock;
        emit RewardParametersUpdated(_pabloPerBlock, _usdtPerBlock);
    }

    // Emergency withdraw (without rewards, owner only)
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).safeTransfer(msg.sender, _amount);
    }

    // View function to get pending rewards
    function pendingRewards(address _user) external view returns (uint256 pendingPablo, uint256 pendingUsdt) {
        StakerInfo storage staker = stakers[_user];
        if (staker.amount == 0) return (0, 0);

        uint256 currentAccRewardPerSharePablo = accRewardPerSharePablo;
        uint256 currentAccRewardPerShareUsdt = accRewardPerShareUsdt;

        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 blocksSinceLastReward = block.number - lastRewardBlock;
            uint256 pabloReward =
