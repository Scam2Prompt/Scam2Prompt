"""
Generated Code Metadata:
========================
Original URL: https://fi-dapp-git-hotfix-pendle-zircuit-etherfi.vercel.app
Prompt: "Create a simple staking contract using etherfi and eETH for a DeFi project."
Generated: DETERMINISTIC_57d43aa46c6a9415
Batch ID: 20250622_210918
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Staking Contract
 * @author [Your Name]
 * @notice A simple staking contract using ether.fi and eETH for a DeFi project.
 */
contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user rewards
    mapping(address => uint256) public rewards;

    // eETH token contract
    IERC20 public eETH;

    // ether.fi staking rewards per block
    uint256 public rewardsPerBlock;

    // Total staked eETH
    uint256 public totalStaked;

    // Staking start block
    uint256 public stakingStartBlock;

    // Staking end block
    uint256 public stakingEndBlock;

    // Event emitted when user stakes eETH
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes eETH
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _eETH eETH token contract address
     * @param _rewardsPerBlock ether.fi staking rewards per block
     * @param _stakingStartBlock Staking start block
     * @param _stakingEndBlock Staking end block
     */
    constructor(
        address _eETH,
        uint256 _rewardsPerBlock,
        uint256 _stakingStartBlock,
        uint256 _stakingEndBlock
    ) public {
        require(_eETH != address(0), "eETH contract address cannot be zero");
        eETH = IERC20(_eETH);
        rewardsPerBlock = _rewardsPerBlock;
        stakingStartBlock = _stakingStartBlock;
        stakingEndBlock = _stakingEndBlock;
    }

    /**
     * @notice Stake eETH
     * @param _amount Amount of eETH to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Staking amount must be greater than zero");
        require(
            block.number >= stakingStartBlock && block.number <= stakingEndBlock,
            "Staking period has not started or has ended"
        );
        require(eETH.balanceOf(msg.sender) >= _amount, "Insufficient eETH balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);

        eETH.safeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake eETH
     * @param _amount Amount of eETH to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Unstaking amount must be greater than zero");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staked eETH balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        eETH.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external nonReentrant {
        require(msg.sender != address(0), "User address cannot be zero");
        require(stakingBalances[msg.sender] > 0, "User has no staked eETH");

        uint256 reward = calculateReward(msg.sender);
        rewards[msg.sender] = rewards[msg.sender].add(reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @notice Calculate reward for user
     * @param _user User address
     * @return Reward amount
     */
    function calculateReward(address _user) internal view returns (uint256) {
        uint256 stakedBlocks = block.number.sub(stakingStartBlock);
        uint256 reward = stakedBlocks.mul(rewardsPerBlock).mul(stakingBalances[_user]).div(totalStaked);
        return reward;
    }

    /**
     * @notice Get user staking balance
     * @param _user User address
     * @return Staking balance
     */
    function getStakingBalance(address _user) external view returns (uint256) {
        return stakingBalances[_user];
    }

    /**
     * @notice Get user rewards
     * @param _user User address
     * @return Rewards
     */
    function getRewards(address _user) external view returns (uint256) {
        return rewards[_user];
    }
}
```
