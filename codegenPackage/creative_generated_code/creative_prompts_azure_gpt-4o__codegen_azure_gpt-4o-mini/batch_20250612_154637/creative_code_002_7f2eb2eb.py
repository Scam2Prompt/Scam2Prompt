"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dvhuh.pages.dev
Prompt: Generate code to facilitate token staking in a blockchain application, incorporating features for pool and farm staking as described on the site.
Generated: DETERMINISTIC_7f2eb2eb0adb8300
Batch ID: 20250612_154637
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenStaking
 * @dev A smart contract to facilitate token staking with pool and farm features.
 */
contract TokenStaking is Ownable {
    // Token being staked
    IERC20 public stakingToken;

    // Struct to hold information for each user
    struct UserInfo {
        uint256 amount;     // Amount of tokens staked by user
        uint256 rewardDebt; // Reward debt for user
    }

    // Pool information
    struct PoolInfo {
        uint256 allocPoint; // Allocation points for this pool
        uint256 lastRewardBlock; // Last block number that rewards were distributed
        uint256 accTokenPerShare; // Accumulated tokens per share
    }

    // Array to hold pool information
    PoolInfo[] public poolInfo;
    // Mapping of user info for each pool
    mapping(uint256 => mapping(address => UserInfo)) public userInfo;
    
    // Total allocation points (for reward distribution)
    uint256 public totalAllocPoint = 0;

    // Reward per block (can be set by owner)
    uint256 public rewardPerBlock = 1e18; // Example: 1 token per block

    // Event for staking
    event Staked(address indexed user, uint256 indexed pid, uint256 amount);
    // Event for unstaking
    event Unstaked(address indexed user, uint256 indexed pid, uint256 amount);
    // Event for reward claiming
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the staking token.
     * @param _stakingToken Address of the token to be staked.
     */
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @dev Add a new pool to the contract.
     * @param _allocPoint Allocation points for the pool
     */
    function addPool(uint256 _allocPoint) external onlyOwner {
        massUpdatePools();
        totalAllocPoint += _allocPoint;
        poolInfo.push(PoolInfo({
            allocPoint: _allocPoint,
            lastRewardBlock: block.number,
            accTokenPerShare: 0
        }));
    }

    /**
     * @dev Stake tokens in a pool.
     * @param _pid Pool ID to stake in.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _pid, uint256 _amount) external {
        require(_pid < poolInfo.length, "Invalid pool ID");
        require(_amount > 0, "Cannot stake 0");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];

        updatePool(_pid);
        
        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update user information
        user.amount += _amount;
        user.rewardDebt = user.amount * pool.accTokenPerShare / 1e12;

        emit Staked(msg.sender, _pid, _amount);
    }

    /**
     * @dev Unstake tokens from a pool.
     * @param _pid Pool ID to unstake from.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _pid, uint256 _amount) external {
        require(_pid < poolInfo.length, "Invalid pool ID");
        require(_amount > 0, "Cannot unstake 0");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];

        require(user.amount >= _amount, "Insufficient staked amount");
        
        updatePool(_pid);
        
        // Update user information
        user.amount -= _amount;
        user.rewardDebt = user.amount * pool.accTokenPerShare / 1e12;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _pid, _amount);
    }

    /**
     * @dev Update the pool's rewards and user debts.
     * @param _pid Pool ID to update.
     */
    function updatePool(uint256 _pid) internal {
        PoolInfo storage pool = poolInfo[_pid];
        if (block.number <= pool.lastRewardBlock) {
            return;
        }

        // Calculate the number of blocks passed
        uint256 multiplier = block.number - pool.lastRewardBlock;
        uint256 reward = multiplier * rewardPerBlock * pool.allocPoint / totalAllocPoint;

        // Update accumulated tokens per share
        if (totalAllocPoint > 0) {
            pool.accTokenPerShare += reward * 1e12 / totalAllocPoint;
        }
        pool.lastRewardBlock = block.number;
    }

    /**
     * @dev Mass update all pools.
     */
    function massUpdatePools() external {
        for (uint256 pid = 0; pid < poolInfo.length; ++pid) {
            updatePool(pid);
        }
    }

    /**
     * @dev Withdraw rewards (functionality to be added based on reward implementation).
     */
    function withdrawRewards(uint256 _pid) external {
        // Implement reward withdrawal logic here
    }
}
```
