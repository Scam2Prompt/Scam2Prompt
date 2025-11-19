"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradecurvemarket-en.pages.dev
Prompt: Describe how to set up a staking mechanism for TCRV tokens in a smart contract on the Ethereum blockchain, including code examples.
Generated: DETERMINISTIC_b65141fd2d263c4e
Batch ID: 20250612_161700
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
 * @title TCRV Staking Contract
 * @notice This contract allows users to stake TCRV tokens and earn rewards.
 */
contract TCRVStaking {
    // ERC20 interface
    IERC20 public tcrvToken;

    // Mapping of user addresses to their staked balances
    mapping(address => uint256) public stakedBalances;

    // Mapping of user addresses to their reward balances
    mapping(address => uint256) public rewardBalances;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate (tokens per second)
    uint256 public rewardRate;

    // Last time rewards were calculated for each user
    mapping(address => uint256) public lastRewardTime;

    // Contract owner
    address public owner;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the TCRV token address and reward rate.
     * @param _tcrvToken Address of the TCRV token contract.
     * @param _rewardRate Reward rate in tokens per second.
     */
    constructor(IERC20 _tcrvToken, uint256 _rewardRate) {
        tcrvToken = _tcrvToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Stake TCRV tokens in the contract.
     * @param amount Number of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Update rewards for the user before staking
        _updateRewards(msg.sender);

        // Transfer tokens to the contract
        require(tcrvToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staked balance
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake TCRV tokens and claim rewards.
     * @param amount Number of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake zero tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update rewards for the user before unstaking
        _updateRewards(msg.sender);

        // Transfer tokens back to the user
        require(tcrvToken.transfer(msg.sender, amount), "Token transfer failed");

        // Update staked balance
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        // Update rewards for the user
        _updateRewards(msg.sender);

        uint256 reward = rewardBalances[msg.sender];
        require(reward > 0, "No rewards available");

        // Transfer rewards to the user
        rewardBalances[msg.sender] = 0;
        require(tcrvToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user.
     */
    function _updateRewards(address user) internal {
        uint256 timeElapsed = block.timestamp - lastRewardTime[user];
        if (timeElapsed > 0) {
            rewardBalances[user] += stakedBalances[user] * rewardRate * timeElapsed / 1e18;
            lastRewardTime[user] = block.timestamp;
        }
    }

    /**
     * @dev Change the reward rate. Only callable by the contract owner.
     * @param _rewardRate New reward rate.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
