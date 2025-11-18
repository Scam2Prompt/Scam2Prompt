"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-v-0-0.pages.dev
Prompt: Develop a function in Solidity to enable OUSD holders to stake OGV tokens and earn rewards while participating in decentralized governance.
Generated: DETERMINISTIC_9d2a104d0101720a
Batch ID: 20250612_153526
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
 * @title Staking Contract for OUSD Holders to Stake OGV Tokens
 * @notice This contract allows OUSD holders to stake OGV tokens, earn rewards, and participate in governance.
 */
contract OGVStaking {
    
    // Structure to represent a staker
    struct Staker {
        uint256 stakedAmount; // Amount of OGV tokens staked
        uint256 rewardDebt;   // Reward debt for the staker
    }

    // ERC20 interface to interact with OGV token
    IERC20 public immutable ogvToken;
    IERC20 public immutable ousdToken;

    // Governance Token reward pool
    uint256 public rewardPool;
    uint256 public rewardPerToken; // Reward per staked token (accumulated)
    uint256 public lastUpdateTime; // Last time rewards were updated

    // Mapping of staker address to their staking details
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Modifier to ensure the caller holds OUSD tokens.
     */
    modifier onlyOUSDHolder() {
        require(ousdToken.balanceOf(msg.sender) > 0, "Caller does not hold OUSD tokens");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with OGV and OUSD token addresses.
     * @param _ogvToken Address of the OGV token
     * @param _ousdToken Address of the OUSD token
     */
    constructor(IERC20 _ogvToken, IERC20 _ousdToken) {
        ogvToken = _ogvToken;
        ousdToken = _ousdToken;
        lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Function to stake OGV tokens.
     * @param amount Amount of OGV tokens to stake
     */
    function stake(uint256 amount) external onlyOUSDHolder {
        require(amount > 0, "Amount must be greater than zero");

        // Update rewards before staking
        updateRewards();

        // Transfer OGV tokens from the caller to the contract
        require(ogvToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staker details
        Staker storage staker = stakers[msg.sender];
        staker.rewardDebt += (amount * rewardPerToken);
        staker.stakedAmount += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw staked OGV tokens.
     * @param amount Amount of OGV tokens to withdraw
     */
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= amount, "Insufficient staked amount");

        // Update rewards before withdrawing
        updateRewards();

        // Update staker details
        staker.stakedAmount -= amount;

        // Transfer OGV tokens back to the caller
        require(ogvToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to claim staking rewards.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];

        // Update rewards before claiming
        updateRewards();

        // Calculate pending rewards
        uint256 pendingReward = (staker.stakedAmount * rewardPerToken) - staker.rewardDebt;
        require(pendingReward > 0, "No rewards to claim");

        // Update reward debt and transfer rewards
        staker.rewardDebt = (staker.stakedAmount * rewardPerToken);
        require(ogvToken.transfer(msg.sender, pendingReward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, pendingReward);
    }

    /**
     * @dev Internal function to update staking rewards.
     */
    function updateRewards() internal {
        // Calculate time difference since last update
        uint256 timeElapsed = block.timestamp - lastUpdateTime;

        // Update reward pool and per token reward
        if (timeElapsed > 0 && rewardPool > 0) {
            rewardPerToken += (rewardPool / totalStaked());
            lastUpdateTime = block.timestamp;
        }
    }

    /**
     * @dev Function to calculate total staked OGV tokens.
     * @return Total staked amount
     */
    function totalStaked() public view returns (uint256) {
        uint256 total = 0;
        for (address stakerAddress in stakers) {
            Staker storage staker = stakers[stakerAddress];
            total += staker.stakedAmount;
        }
        return total;
    }

    /**
     * @dev Function to add rewards to the reward pool (admin only).
     * @param amount Amount of tokens to add to the reward pool
     */
    function addRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens to the reward pool
        require(ogvToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        rewardPool += amount;
    }
}

/**
 * @dev Minimal ERC20 interface for token interactions.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
