"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-xyz.pages.dev
Prompt: Provide an example of a smart contract that manages the staking and reward distribution for $SCOTTY tokens in a blockchain environment.
Generated: DETERMINISTIC_d496f44e608b3449
Batch ID: 20250612_162228
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Staking and Reward Distribution Contract for $SCOTTY tokens
 */
contract ScottyStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward claims
    mapping(address => uint256) public rewardClaims;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward per block
    uint256 public rewardPerBlock;

    // Reward distribution start block
    uint256 public rewardStartBlock;

    // Reward distribution end block
    uint256 public rewardEndBlock;

    // $SCOTTY token contract
    ERC20 public scottyToken;

    /**
     * @notice Constructor for the ScottyStaking contract
     * @param _scottyToken Address of the $SCOTTY token contract
     * @param _rewardPerBlock Reward per block
     * @param _rewardStartBlock Reward distribution start block
     * @param _rewardEndBlock Reward distribution end block
     */
    constructor(
        address _scottyToken,
        uint256 _rewardPerBlock,
        uint256 _rewardStartBlock,
        uint256 _rewardEndBlock
    ) {
        require(_scottyToken != address(0), "Invalid token address");
        require(_rewardPerBlock > 0, "Reward per block must be greater than 0");
        require(_rewardStartBlock < _rewardEndBlock, "Invalid reward period");

        scottyToken = ERC20(_scottyToken);
        rewardPerBlock = _rewardPerBlock;
        rewardStartBlock = _rewardStartBlock;
        rewardEndBlock = _rewardEndBlock;
    }

    /**
     * @notice Stake $SCOTTY tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than 0");
        require(scottyToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);

        // Transfer tokens to the contract
        scottyToken.transferFrom(msg.sender, address(this), _amount);
    }

    /**
     * @notice Unstake $SCOTTY tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than 0");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staked balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens back to the user
        scottyToken.transfer(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        rewardClaims[msg.sender] = block.number;
        scottyToken.transfer(msg.sender, rewards);
    }

    /**
     * @notice Calculate rewards for a user
     * @param _user Address of the user
     * @return Rewards for the user
     */
    function calculateRewards(address _user) public view returns (uint256) {
        uint256 stakedAmount = stakingBalances[_user];
        uint256 blocksElapsed = block.number.sub(rewardClaims[_user]);

        if (blocksElapsed > 0 && block.number >= rewardStartBlock && block.number <= rewardEndBlock) {
            uint256 rewards = stakedAmount.mul(rewardPerBlock).mul(blocksElapsed);
            return rewards;
        }

        return 0;
    }

    /**
     * @notice Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) external {
        require(msg.sender == owner(), "Only the owner can update the reward per block");
        require(_newRewardPerBlock > 0, "Reward per block must be greater than 0");

        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @notice Get the contract balance
     * @return Contract balance
     */
    function getContractBalance() public view returns (uint256) {
        return scottyToken.balanceOf(address(this));
    }

    // Owner function to transfer remaining tokens
    function transferRemainingTokens(address _recipient) external {
        require(msg.sender == owner(), "Only the owner can transfer remaining tokens");
        scottyToken.transfer(_recipient, getContractBalance());
    }
}
```
