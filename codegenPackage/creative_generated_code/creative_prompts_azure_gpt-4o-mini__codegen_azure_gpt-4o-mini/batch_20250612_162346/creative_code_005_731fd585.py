"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dodgecoiin20.pages.dev
Prompt: Create a Solidity contract that mimics the DOGE20 staking mechanism, distributing rewards based on the percentage of tokens staked.
Generated: DETERMINISTIC_731fd585bd5ce8cf
Batch ID: 20250612_162346
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

// Import OpenZeppelin's SafeERC20 and IERC20 interfaces for safe token operations
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for a staking mechanism that distributes rewards based on staked tokens
contract DOGE20Staking is Ownable {
    using SafeERC20 for IERC20;

    // Struct to represent info of each staker
    struct StakerInfo {
        uint256 amountStaked; // Amount of tokens staked
        uint256 rewardDebt;    // Reward debt for the staker
    }

    // State variables
    IERC20 public stakingToken; // The token that will be staked
    uint256 public totalStaked;  // Total amount staked in the contract
    uint256 public rewardPerToken; // Reward per token staked
    uint256 public totalRewards; // Total rewards available for distribution

    // Mapping of address to StakerInfo
    mapping(address => StakerInfo) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardAdded(uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to set the staking token address
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer tokens to the contract
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update total staked amount and staker's info
        StakerInfo storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        StakerInfo storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked balance");

        // Update total staked amount and staker's info
        staker.amountStaked -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the staker
        stakingToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to add rewards to the pool
    function addReward(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        totalRewards += _amount;
        rewardPerToken += _amount / totalStaked; // Update reward per token

        emit RewardAdded(_amount);
    }

    // Function to claim accrued rewards
    function claimReward() external {
        StakerInfo storage staker = stakers[msg.sender];
        uint256 pendingReward = (staker.amountStaked * rewardPerToken) - staker.rewardDebt;

        require(pendingReward > 0, "No rewards to claim");
        require(totalRewards >= pendingReward, "Not enough rewards available");

        // Transfer the pending reward to the staker
        totalRewards -= pendingReward;
        staker.rewardDebt = (staker.amountStaked * rewardPerToken); // Update reward debt

        payable(msg.sender).transfer(pendingReward); // Assuming rewards are in Ether

        emit RewardClaimed(msg.sender, pendingReward);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
