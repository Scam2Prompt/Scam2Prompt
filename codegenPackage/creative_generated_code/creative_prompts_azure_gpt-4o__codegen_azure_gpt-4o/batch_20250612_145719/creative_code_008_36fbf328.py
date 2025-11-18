"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiresolvechain.firebaseapp.com
Prompt: Write a smart contract for staking tokens and activating APR, incorporating the staking and APR activation features described on MultiResolveChain.
Generated: DETERMINISTIC_36fbf328c9fa7420
Batch ID: 20250612_145719
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
 * @dev A smart contract for staking tokens and earning rewards using an APR mechanism.
 */
contract StakingContract {
    // --- State Variables ---
    address public owner;                      // Owner of the contract
    IERC20 public stakingToken;               // Token used for staking
    uint256 public annualPercentageRate;      // Annual Percentage Rate (APR) in basis points (e.g., 500 = 5%)
    uint256 public constant BASIS_POINTS = 10000; // Denominator for APR basis points

    struct Stake {
        uint256 amount;                       // Amount of tokens staked
        uint256 lastUpdated;                  // Timestamp of the last update (for calculating rewards)
    }
    mapping(address => Stake) public stakes;  // Mapping of user addresses to their stakes

    // --- Events ---
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event APRUpdated(uint256 newAPR);

    // --- Modifiers ---
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier hasStake(address staker) {
        require(stakes[staker].amount > 0, "No active stake found");
        _;
    }

    // --- Constructor ---
    /**
     * @dev Initializes the contract with the token address and the initial APR.
     * @param _stakingToken Address of the ERC20 token used for staking.
     * @param _annualPercentageRate Initial APR in basis points (e.g., 500 = 5%).
     */
    constructor(address _stakingToken, uint256 _annualPercentageRate) {
        require(_stakingToken != address(0), "Invalid token address");
        require(_annualPercentageRate <= BASIS_POINTS, "APR exceeds maximum");

        owner = msg.sender;
        stakingToken = IERC20(_stakingToken);
        annualPercentageRate = _annualPercentageRate;
    }

    // --- Public Functions ---
    /**
     * @dev Stake tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Calculate and update rewards for the user before adding new stake
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update the stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external hasStake(msg.sender) {
        // Calculate rewards and reset the stake
        _updateRewards(msg.sender);
        uint256 stakedAmount = stakes[msg.sender].amount;

        stakes[msg.sender].amount = 0;
        stakes[msg.sender].lastUpdated = 0;

        // Transfer staked tokens back to the user
        require(stakingToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Claim rewards without unstaking.
     */
    function claimRewards() external hasStake(msg.sender) {
        uint256 rewards = _updateRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // --- Owner Functions ---
    /**
     * @dev Update the APR for staking rewards (only callable by owner).
     * @param _newAPR New APR in basis points (e.g., 500 = 5%).
     */
    function updateAPR(uint256 _newAPR) external onlyOwner {
        require(_newAPR <= BASIS_POINTS, "APR exceeds maximum");
        annualPercentageRate = _newAPR;

        emit APRUpdated(_newAPR);
    }

    // --- Internal Functions ---
    /**
     * @dev Calculate and distribute rewards to the user.
     * @param _staker The address of the staker.
     * @return rewards The amount of rewards distributed.
     */
    function _updateRewards(address _staker) internal returns (uint256 rewards) {
        Stake storage stakeInfo = stakes[_staker];

        // Calculate rewards based on time difference and APR
        uint256 timeElapsed = block.timestamp - stakeInfo.lastUpdated;
        rewards = (stakeInfo.amount * annualPercentageRate * timeElapsed) / (BASIS_POINTS * 365 days);

        // Update user's lastUpdated timestamp
        stakeInfo.lastUpdated = block.timestamp;

        // Transfer rewards to the user
        if (rewards > 0) {
            require(stakingToken.transfer(_staker, rewards), "Reward transfer failed");
        }

        return rewards;
    }
}

// --- Interface for ERC20 Token ---
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
