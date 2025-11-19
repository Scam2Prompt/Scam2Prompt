"""
Generated Code Metadata:
========================
Original URL: https://koalamemecoin.pages.dev
Prompt: Create a staking rewards system in Solidity for a cryptocurrency like KoalaKash, where VIP holders earn higher rewards and voting rights.
Generated: DETERMINISTIC_59bc0d3e00e0be38
Batch ID: 20250612_152240
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

contract KoalaKashStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 timeStaked;
        uint256 unclaimedRewards;
        bool isVIP;
    }

    // Staking token (KoalaKash)
    IERC20 public immutable stakingToken;

    // Reward distribution parameters
    uint256 public constant REWARD_RATE_BASE = 100; // 1% per period
    uint256 public constant REWARD_RATE_VIP = 150; // 1.5% per period
    uint256 public constant REWARD_PERIOD = 7 days;
    uint256 public constant MIN_STAKE_DURATION = 1 days;
    uint256 public constant VIP_STAKE_THRESHOLD = 10000 * 10**18; // 10,000 tokens

    // Voting parameters
    uint256 public totalVotes;
    mapping(address => uint256) public votes;
    mapping(uint256 => uint256) public proposalVotes;

    // Staking state
    uint256 public totalStaked;
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event VIPStatusChanged(address indexed user, bool isVIP);
    event Voted(address indexed voter, uint256 proposalId, uint256 votes);

    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @notice Stake tokens to earn rewards and gain voting power
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        Staker storage staker = stakers[msg.sender];
        
        // Claim any pending rewards before updating stake
        if (staker.amountStaked > 0) {
            _claimRewards(msg.sender);
        }

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update staker info
        staker.amountStaked += amount;
        staker.timeStaked = block.timestamp;
        
        // Check for VIP status
        if (!staker.isVIP && staker.amountStaked >= VIP_STAKE_THRESHOLD) {
            staker.isVIP = true;
            emit VIPStatusChanged(msg.sender, true);
        }

        // Update total staked
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens and claim rewards
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");
        require(
            block.timestamp >= staker.timeStaked + MIN_STAKE_DURATION,
            "Minimum stake duration not reached"
        );

        // Claim rewards first
        _claimRewards(msg.sender);

        // Update staker info
        staker.amountStaked -= amount;
        
        // Check VIP status
        if (staker.isVIP && staker.amountStaked < VIP_STAKE_THRESHOLD) {
            staker.isVIP = false;
            emit VIPStatusChanged(msg.sender, false);
        }

        // Update total staked
        totalStaked -= amount;

        // Transfer tokens back to user
        stakingToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        _claimRewards(msg.sender);
    }

    /**
     * @notice Internal function to calculate and claim rewards
     * @param user The address of the staker
     */
    function _claimRewards(address user) internal {
        Staker storage staker = stakers[user];
        if (staker.amountStaked == 0) return;

        uint256 reward = calculateRewards(user);
        if (reward > 0) {
            staker.unclaimedRewards = 0;
            staker.timeStaked = block.timestamp; // Reset stake time for reward calculation
            
            // Transfer rewards
            stakingToken.safeTransfer(user, reward);
            emit RewardClaimed(user, reward);
        }
    }

    /**
     * @notice Calculate pending rewards for a staker
     * @param user The address of the staker
     * @return The amount of pending rewards
     */
    function calculateRewards(address user) public view returns (uint256) {
        Staker memory staker = stakers[user];
        if (staker.amountStaked == 0) return 0;

        uint256 stakingDuration = block.timestamp - staker.timeStaked;
        uint256 rewardRate = staker.isVIP ? REWARD_RATE_VIP : REWARD_RATE_BASE;
        
        uint256 periods = stakingDuration / REWARD_PERIOD;
        uint256 rewards = (staker.amountStaked * rewardRate * periods) / (100 * 100);
        
        return rewards + staker.unclaimedRewards;
    }

    /**
     * @notice Cast votes on a proposal
     * @param proposalId The ID of the proposal to vote on
     * @param voteAmount The number of votes to cast (based on stake)
     */
    function vote(uint256 proposalId, uint256 voteAmount) external {
        Staker memory staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No stake to vote with");
        require(voteAmount <= staker.amountStaked, "Votes exceed stake");

        // VIPs get 2x voting power
        uint256 votingPower = staker.isVIP ? voteAmount * 2 : voteAmount;
        
        votes[msg.sender] += votingPower;
        proposalVotes[proposalId] += votingPower;
        totalVotes += votingPower;

        emit Voted(msg.sender, proposalId, votingPower);
    }

    /**
     * @notice Emergency withdrawal function for owner to recover tokens
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
