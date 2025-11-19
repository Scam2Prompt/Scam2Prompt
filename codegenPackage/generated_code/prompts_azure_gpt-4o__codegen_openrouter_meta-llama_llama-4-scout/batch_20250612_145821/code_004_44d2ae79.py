"""
Generated Code Metadata:
========================
Original URL: https://nodeapp-serverlaunch.com
Prompt: Write a smart contract to enable staking and unstaking of tokens, including error handling for staking-related issues.
Generated: DETERMINISTIC_44d2ae79b8fc68be
Batch ID: 20250612_145821
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @author [Your Name]
 * @notice A simple staking contract that allows users to stake and unstake tokens.
 */
contract StakingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking balances
    mapping(address => uint256) private _stakingBalances;

    // Mapping of user staking rewards
    mapping(address => uint256) private _stakingRewards;

    // Token being staked
    IERC20 public stakingToken;

    // Total staked tokens
    uint256 public totalStaked;

    // Staking reward per block
    uint256 public rewardPerBlock;

    // Last reward update block
    uint256 public lastRewardUpdate;

    // Staking start block
    uint256 public stakingStartBlock;

    // Staking end block
    uint256 public stakingEndBlock;

    /**
     * @notice Constructor for StakingContract
     * @param _stakingToken Address of token being staked
     * @param _rewardPerBlock Reward per block
     * @param _stakingStartBlock Staking start block
     * @param _stakingEndBlock Staking end block
     */
    constructor(
        IERC20 _stakingToken,
        uint256 _rewardPerBlock,
        uint256 _stakingStartBlock,
        uint256 _stakingEndBlock
    ) {
        require(
            address(_stakingToken) != address(0),
            "Staking token address cannot be zero"
        );
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");
        require(
            _stakingEndBlock > _stakingStartBlock,
            "Staking end block must be greater than start block"
        );

        stakingToken = _stakingToken;
        rewardPerBlock = _rewardPerBlock;
        stakingStartBlock = _stakingStartBlock;
        stakingEndBlock = _stakingEndBlock;
        lastRewardUpdate = block.number;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(
            block.number >= stakingStartBlock && block.number <= stakingEndBlock,
            "Staking is not active"
        );
        require(_amount > 0, "Stake amount must be greater than zero");
        require(
            stakingToken.balanceOf(msg.sender) >= _amount,
            "Insufficient token balance"
        );

        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);

        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        _updateRewards(msg.sender);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(
            _stakingBalances[msg.sender] >= _amount,
            "Insufficient staked balance"
        );
        require(_amount > 0, "Unstake amount must be greater than zero");

        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        stakingToken.safeTransfer(msg.sender, _amount);

        _updateRewards(msg.sender);
    }

    /**
     * @notice Get staking balance of user
     * @param _user Address of user
     * @return Staking balance of user
     */
    function getStakingBalance(address _user) external view returns (uint256) {
        return _stakingBalances[_user];
    }

    /**
     * @notice Get staking rewards of user
     * @param _user Address of user
     * @return Staking rewards of user
     */
    function getStakingRewards(address _user) external view returns (uint256) {
        return _stakingRewards[_user];
    }

    /**
     * @notice Update rewards for user
     * @param _user Address of user
     */
    function _updateRewards(address _user) internal {
        uint256 pendingRewards = _calculateRewards(_user);
        _stakingRewards[_user] = _stakingRewards[_user].add(pendingRewards);
    }

    /**
     * @notice Calculate rewards for user
     * @param _user Address of user
     * @return Pending rewards for user
     */
    function _calculateRewards(address _user) internal view returns (uint256) {
        uint256 stakingBlocks = block.number.sub(lastRewardUpdate);
        uint256 userStakingBlocks = stakingBlocks.mul(_stakingBalances[_user]).div(
            totalStaked
        );
        return userStakingBlocks.mul(rewardPerBlock);
    }

    /**
     * @notice Update last reward update block
     */
    function _updateLastRewardUpdate() internal {
        lastRewardUpdate = block.number;
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        uint256 pendingRewards = _stakingRewards[msg.sender];
        require(pendingRewards > 0, "No rewards to claim");

        _stakingRewards[msg.sender] = 0;

        stakingToken.safeTransfer(msg.sender, pendingRewards);

        _updateLastRewardUpdate();
    }
}
```
