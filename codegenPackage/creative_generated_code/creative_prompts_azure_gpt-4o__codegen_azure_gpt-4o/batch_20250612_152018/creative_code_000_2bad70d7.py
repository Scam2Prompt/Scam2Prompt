"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asx-capital.pages.dev
Prompt: Write a smart contract in Solidity that enables staking of the $ASX token and distributes rewards in $USDC based on the yield-bearing mechanics described on the ASX Capital website.
Generated: DETERMINISTIC_2bad70d7de873dab
Batch ID: 20250612_152018
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

// Importing OpenZeppelin libraries for ERC20 token interface and safe math operations
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking $ASX tokens and distributing rewards in $USDC
contract ASXStaking is Ownable {
    using SafeERC20 for IERC20;

    // ERC20 token contracts
    IERC20 public immutable ASXToken;
    IERC20 public immutable USDCToken;

    // Reward rate per second (e.g., yield rate)
    uint256 public rewardRate;

    // Store staking information for each user
    struct Staker {
        uint256 amountStaked; // Total amount of $ASX tokens staked
        uint256 lastUpdated; // Last timestamp of staking/reward update
        uint256 pendingRewards; // Accumulated $USDC rewards not yet withdrawn
    }

    // Mapping to track staker data
    mapping(address => Staker) public stakers;

    // Events for transparency
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardCollected(address indexed user, uint256 reward);

    constructor(IERC20 _ASXToken, IERC20 _USDCToken, uint256 _rewardRate) {
        require(address(_ASXToken) != address(0), "Invalid ASX token address");
        require(address(_USDCToken) != address(0), "Invalid USDC token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        ASXToken = _ASXToken;
        USDCToken = _USDCToken;
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards for the user before performing certain actions
    modifier updateRewards(address _account) {
        Staker storage staker = stakers[_account];

        if (staker.amountStaked > 0) {
            // Calculate pending rewards based on elapsed time and reward rate
            uint256 timeElapsed = block.timestamp - staker.lastUpdated;
            staker.pendingRewards += (timeElapsed * staker.amountStaked * rewardRate) / 1e18;
        }

        // Update the timestamp
        staker.lastUpdated = block.timestamp;
        _;
    }

    // Function to stake $ASX tokens
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer $ASX tokens from user to the contract
        ASXToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update staker data
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked $ASX tokens
    function withdraw(uint256 _amount) external updateRewards(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(staker.amountStaked >= _amount, "Insufficient staked balance");

        // Update staker data
        staker.amountStaked -= _amount;

        // Transfer $ASX tokens back to the user
        ASXToken.safeTransfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim accumulated $USDC rewards
    function claimRewards() external updateRewards(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        uint256 rewardsToClaim = staker.pendingRewards;
        require(rewardsToClaim > 0, "No rewards available to claim");

        // Reset pending rewards
        staker.pendingRewards = 0;

        // Transfer $USDC rewards to the user
        USDCToken.safeTransfer(msg.sender, rewardsToClaim);

        emit RewardCollected(msg.sender, rewardsToClaim);
    }

    // Owner function to update the reward rate
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }

    // Emergency function to withdraw tokens stuck in the contract
    function emergencyWithdraw(address _tokenAddress, uint256 _amount) external onlyOwner {
        IERC20(_tokenAddress).safeTransfer(owner(), _amount);
    }
}
```
