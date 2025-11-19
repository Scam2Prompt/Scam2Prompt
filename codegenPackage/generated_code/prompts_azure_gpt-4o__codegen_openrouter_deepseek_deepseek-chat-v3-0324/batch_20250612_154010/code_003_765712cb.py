"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-pepe.xyz
Prompt: Create a smart contract in Solidity for staking $BPEP tokens, ensuring compatibility with Bitcoin Pepe's tokenomics (15% allocation for staking and rewards).
Generated: DETERMINISTIC_765712cb0d9360bf
Batch ID: 20250612_154010
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

contract BPEPStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // The BPEP token contract
    IERC20 public bpepToken;

    // Total amount of BPEP tokens staked
    uint256 public totalStaked;

    // Reward rate (percentage per year)
    uint256 public rewardRate = 15; // 15% annual reward

    // Precision factor for reward calculations
    uint256 public constant PRECISION_FACTOR = 1e18;

    // Mapping of staker addresses to their staking info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    constructor(address _bpepToken) {
        require(_bpepToken != address(0), "BPEP token address cannot be zero");
        bpepToken = IERC20(_bpepToken);
    }

    /**
     * @notice Stake BPEP tokens to earn rewards
     * @param amount The amount of BPEP tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];

        // Claim any pending rewards before staking
        if (staker.amountStaked > 0) {
            _claimRewards();
        }

        // Transfer BPEP tokens from user to this contract
        bpepToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update staker's information
        staker.amountStaked += amount;
        staker.lastStakedTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake BPEP tokens and claim rewards
     * @param amount The amount of BPEP tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Claim any pending rewards before unstaking
        _claimRewards();

        // Update staker's information
        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Transfer BPEP tokens back to user
        bpepToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        require(stakers[msg.sender].amountStaked > 0, "No staked amount");
        _claimRewards();
    }

    /**
     * @dev Internal function to calculate and transfer rewards
     */
    function _claimRewards() internal {
        Staker storage staker = stakers[msg.sender];
        uint256 pendingRewards = calculatePendingRewards(msg.sender);

        if (pendingRewards > 0) {
            // Update reward debt
            staker.rewardDebt += pendingRewards;

            // Transfer rewards to staker
            bpepToken.safeTransfer(msg.sender, pendingRewards);

            emit RewardClaimed(msg.sender, pendingRewards);
        }

        // Update last staked time for future reward calculations
        staker.lastStakedTime = block.timestamp;
    }

    /**
     * @notice Calculate pending rewards for a staker
     * @param stakerAddress The address of the staker
     * @return The amount of pending rewards
     */
    function calculatePendingRewards(address stakerAddress) public view returns (uint256) {
        Staker memory staker = stakers[stakerAddress];
        if (staker.amountStaked == 0) return 0;

        uint256 timeElapsed = block.timestamp - staker.lastStakedTime;
        uint256 annualReward = (staker.amountStaked * rewardRate) / 100;
        uint256 pendingRewards = (annualReward * timeElapsed) / 365 days;

        return pendingRewards;
    }

    /**
     * @notice Update the reward rate (only callable by owner)
     * @param newRate The new reward rate (percentage per year)
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate <= 15, "Reward rate cannot exceed 15%");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @notice Emergency function to recover any ERC20 tokens sent to the contract
     * @param tokenAddress The address of the token to recover
     * @param amount The amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(bpepToken), "Cannot withdraw BPEP tokens");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
