"""
Generated Code Metadata:
========================
Original URL: https://smartordinalwallet.pages.dev
Prompt: Create a code for a farm/pool feature on the Smartdappchain to manage user funds and balance.
Generated: DETERMINISTIC_db17410a79773490
Batch ID: 20250622_205842
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FarmPool
 * @dev A smart contract to manage user funds and balances for a farming/pooling feature.
 */
contract FarmPool is Ownable {
    // Struct to hold user information
    struct UserInfo {
        uint256 amount;     // Amount of tokens the user has deposited
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping of user addresses to their information
    mapping(address => UserInfo) public userInfo;

    // Total amount of tokens staked in the pool
    uint256 public totalStaked;

    // ERC20 token used for staking
    IERC20 public stakingToken;

    // Reward per block for stakers
    uint256 public rewardPerBlock;

    // Total rewards distributed
    uint256 public totalRewards;

    // Event emitted when a user deposits tokens
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdraw(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event ClaimRewards(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the staking token and reward rate.
     * @param _stakingToken Address of the ERC20 token to be staked.
     * @param _rewardPerBlock Amount of rewards distributed per block.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardPerBlock) {
        stakingToken = _stakingToken;
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Deposit tokens into the farm pool.
     * @param _amount Amount of tokens to deposit.
     */
    function deposit(uint256 _amount) external {
        require(_amount > 0, "Deposit amount must be greater than 0");

        // Update user information
        UserInfo storage user = userInfo[msg.sender];
        user.amount += _amount;
        totalStaked += _amount;

        // Transfer tokens from user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        emit Deposit(msg.sender, _amount);
    }

    /**
     * @dev Withdraw tokens from the farm pool.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");

        // Update user information
        user.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Withdraw(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards for the user.
     */
    function claimRewards() external {
        UserInfo storage user = userInfo[msg.sender];
        uint256 pendingRewards = calculatePendingRewards(msg.sender);

        require(pendingRewards > 0, "No rewards to claim");

        // Update total rewards
        totalRewards += pendingRewards;

        // Transfer rewards to the user
        require(stakingToken.transfer(msg.sender, pendingRewards), "Transfer failed");

        emit ClaimRewards(msg.sender, pendingRewards);
    }

    /**
     * @dev Calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards for the user.
     */
    function calculatePendingRewards(address _user) internal view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        // Assuming rewards are calculated based on the amount staked and the reward rate
        return (user.amount * rewardPerBlock) - user.rewardDebt;
    }

    /**
     * @dev Update the reward per block.
     * @param _rewardPerBlock New reward per block.
     */
    function updateRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Emergency withdraw function to withdraw tokens without claiming rewards.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(stakingToken.transfer(msg.sender, balance), "Transfer failed");
    }
}
```
