"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-dogecoin20.pages.dev
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens on Ethereum that distributes rewards proportionally to stakers over a two-year period, as described in the DOGE20 roadmap.
Generated: DETERMINISTIC_0b524440a48d9a87
Batch ID: 20250612_153400
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
 * @title StakingContract
 * @dev A staking contract for DOGE20 tokens that distributes rewards proportionally to stakers
 *      over a two-year period as described in the DOGE20 roadmap.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract StakingContract is ReentrancyGuard {
    // Address of the DOGE20 token
    IERC20 public immutable doge20Token;

    // Duration of the rewards distribution in seconds (2 years)
    uint256 public constant REWARD_PERIOD = 730 days;

    // Timestamp when rewards start
    uint256 public immutable rewardStartTime;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping of staker address to their staked amount
    mapping(address => uint256) public stakedBalances;

    // Mapping of staker address to their last claimed timestamp
    mapping(address => uint256) public lastClaimedTime;

    // Total rewards pool (in DOGE20 tokens) allocated for distribution
    uint256 public rewardPool;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _doge20Token Address of the DOGE20 token contract
     * @param _rewardPool Total rewards pool allocated for distribution
     */
    constructor(IERC20 _doge20Token, uint256 _rewardPool) {
        require(_rewardPool > 0, "Reward pool must be greater than zero");

        doge20Token = _doge20Token;
        rewardPool = _rewardPool;
        rewardStartTime = block.timestamp; // Start reward time from contract deployment
    }

    /**
     * @dev Function to stake DOGE20 tokens.
     * @param _amount Amount of DOGE20 tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer DOGE20 tokens from the sender to the contract
        doge20Token.transferFrom(msg.sender, address(this), _amount);

        // Update staked balances and total staked amount
        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        // Update last claimed time for the staker
        if (lastClaimedTime[msg.sender] == 0) {
            lastClaimedTime[msg.sender] = block.timestamp;
        }

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw staked DOGE20 tokens.
     * @param _amount Amount of DOGE20 tokens to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Claim any pending rewards before withdrawing
        claimRewards();

        // Update staked balances and total staked amount
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer the tokens back to the user
        doge20Token.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Function to claim rewards.
     */
    function claimRewards() public nonReentrant {
        // Ensure rewards are within the distribution period
        require(block.timestamp <= rewardStartTime + REWARD_PERIOD, "Reward period has ended");

        uint256 stakerBalance = stakedBalances[msg.sender];
        require(stakerBalance > 0, "No staked balance");

        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update the last claimed timestamp
        lastClaimedTime[msg.sender] = block.timestamp;

        // Transfer calculated rewards from the reward pool to the staker
        rewardPool -= rewards;
        doge20Token.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to calculate rewards for a staker.
     * @param _staker Address of the staker
     * @return rewards Amount of rewards to be claimed
     */
    function calculateRewards(address _staker) internal view returns (uint256) {
        uint256 stakerBalance = stakedBalances[_staker];
        uint256 lastClaimed = lastClaimedTime[_staker];
        uint256 timeElapsed = block.timestamp - lastClaimed;

        // Calculate proportional rewards based on staker's balance and time elapsed
        uint256 rewards = (rewardPool * stakerBalance * timeElapsed) / (totalStaked * REWARD_PERIOD);

        return rewards;
    }

    /**
     * @dev Function to get the current rewards available for a staker.
     * @param _staker Address of the staker
     * @return rewards Amount of rewards available for claiming
     */
    function getPendingRewards(address _staker) external view returns (uint256) {
        if (stakedBalances[_staker] == 0 || block.timestamp > rewardStartTime + REWARD_PERIOD) {
            return 0;
        }
        return calculateRewards(_staker);
    }
}
```
