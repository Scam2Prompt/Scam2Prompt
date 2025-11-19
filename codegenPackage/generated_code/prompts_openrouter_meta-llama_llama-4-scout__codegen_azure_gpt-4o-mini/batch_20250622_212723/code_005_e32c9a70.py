"""
Generated Code Metadata:
========================
Original URL: https://worldmobile-token.pages.dev
Prompt: "Create a staking mechanism for WMTx that allocates rewards to node operators and World Mobile products, using a non-custodial vault for secure management."
Generated: DETERMINISTIC_e32c9a700aabe66d
Batch ID: 20250622_212723
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Interface for the WMTx token
interface IWMTx is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Staking contract for WMTx rewards allocation
contract WMTxStaking is Ownable, ReentrancyGuard {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of WMTx staked
    uint256 public totalStaked;

    // Reward token contract
    IWMTx public wmtxToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last block number that rewards were distributed
    uint256 public lastRewardBlock;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IWMTx _wmtxToken, uint256 _rewardPerBlock) {
        wmtxToken = _wmtxToken;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    // Function to stake WMTx tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(wmtxToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Update staker information
        stakers[msg.sender].amountStaked += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake WMTx tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].amountStaked >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Update staker information
        stakers[msg.sender].amountStaked -= amount;
        totalStaked -= amount;

        // Transfer the staked amount back to the user
        require(wmtxToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        _updateRewards(msg.sender);
        uint256 reward = stakers[msg.sender].rewardDebt;

        require(reward > 0, "No rewards to claim");
        stakers[msg.sender].rewardDebt = 0;

        // Mint and transfer rewards to the user
        wmtxToken.mint(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a staker
    function _updateRewards(address staker) internal {
        uint256 blocksPassed = block.number - lastRewardBlock;
        if (blocksPassed > 0 && totalStaked > 0) {
            uint256 reward = blocksPassed * rewardPerBlock;
            stakers[staker].rewardDebt += (reward * stakers[staker].amountStaked) / totalStaked;
        }
        lastRewardBlock = block.number;
    }

    // Function to set a new reward per block (only owner)
    function setRewardPerBlock(uint256 newRewardPerBlock) external onlyOwner {
        _updateRewards(address(0)); // Update rewards for all stakers
        rewardPerBlock = newRewardPerBlock;
    }
}
```
