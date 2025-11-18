"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicstr6f6nebuy7tjlpjgzecshw3segkzgnu4rzkkzrr6hrawmofg4.ipfs.dweb.link
Prompt: Write a script to audit the smart contract for staking `wTAO` and receiving `rsTAO` rewards, ensuring compliance with security standards.
Generated: DETERMINISTIC_f4f4760393117313
Batch ID: 20250612_150228
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
 * @title Smart Contract Auditor for Staking wTAO and Receiving rsTAO Rewards
 * @notice This contract implements a basic staking mechanism with security best practices
 * @dev Ensure all interactions are compliant with OpenZeppelin standards and avoid common vulnerabilities
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is ReentrancyGuard, Ownable {
    // Events for logging activities
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Tokens
    IERC20 public wTAOToken; // Token to stake
    IERC20 public rsTAOToken; // Reward token

    // Staking variables
    uint256 public rewardRatePerBlock; // Reward rate per block
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) public balances; // User balances
    mapping(address => uint256) public lastUpdatedBlock; // Last block at which rewards were calculated for each user
    mapping(address => uint256) public rewardDebt; // Rewards already paid to the user

    /**
     * @dev Constructor to initialize staking and reward tokens
     * @param _wTAOToken Address of the token to stake
     * @param _rsTAOToken Address of the reward token
     * @param _rewardRatePerBlock Reward rate per block
     */
    constructor(
        address _wTAOToken,
        address _rsTAOToken,
        uint256 _rewardRatePerBlock
    ) {
        require(
            _wTAOToken != address(0) && _rsTAOToken != address(0),
            "Token addresses must be valid"
        );
        wTAOToken = IERC20(_wTAOToken);
        rsTAOToken = IERC20(_rsTAOToken);
        rewardRatePerBlock = _rewardRatePerBlock;
    }

    /**
     * @dev Stake wTAO tokens to earn rsTAO rewards
     * @param amount Amount of wTAO tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(
            wTAOToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update rewards for the user before staking
        _updateRewards(msg.sender);

        // Update staking balance and total staked
        balances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake wTAO tokens and claim pending rewards
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update rewards for the user before unstaking
        _updateRewards(msg.sender);

        // Update staking balance and total staked
        balances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer staked tokens and rewards to the user
        require(
            wTAOToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );
        uint256 pendingReward = rewardDebt[msg.sender];
        if (pendingReward > 0) {
            rewardDebt[msg.sender] = 0; // Reset reward debt
            require(
                rsTAOToken.transfer(msg.sender, pendingReward),
                "Reward transfer failed"
            );
            emit RewardPaid(msg.sender, pendingReward);
        }

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev View pending rewards for a staker
     * @param user Address of the user
     * @return Pending reward amount
     */
    function pendingReward(address user) external view returns (uint256) {
        uint256 blocksStaked = block.number - lastUpdatedBlock[user];
        uint256 accumulatedReward = (balances[user] * rewardRatePerBlock) *
            blocksStaked;
        return accumulatedReward + rewardDebt[user];
    }

    /**
     * @dev Update reward debt and last updated block for the user
     * @param user Address of the user
     */
    function _updateRewards(address user) internal {
        uint256 blocksStaked = block.number - lastUpdatedBlock[user];
        uint256 accumulatedReward = (balances[user] * rewardRatePerBlock) *
            blocksStaked;

        rewardDebt[user] += accumulatedReward;
        lastUpdatedBlock[user] = block.number;
    }

    /**
     * @dev Update the reward rate per block (Admin function)
     * @param _rewardRatePerBlock New reward rate per block
     */
    function updateRewardRate(uint256 _rewardRatePerBlock) external onlyOwner {
        require(_rewardRatePerBlock > 0, "Reward rate must be greater than zero");
        rewardRatePerBlock = _rewardRatePerBlock;
    }

    /**
     * @dev Emergency withdraw function for admin to recover tokens
     * @param token Address of the token to recover
     * @param amount Amount of tokens to recover
     */
    function emergencyWithdraw(address token, uint256 amount)
        external
        onlyOwner
    {
        require(
            IERC20(token).transfer(owner(), amount),
            "Emergency withdraw failed"
        );
    }
}
```
