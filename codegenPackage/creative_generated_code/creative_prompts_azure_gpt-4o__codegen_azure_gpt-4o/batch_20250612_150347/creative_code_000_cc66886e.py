"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchaineden.pages.dev
Prompt: Write a smart contract for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain, incorporating double staking rewards as described in the tokenomics.
Generated: DETERMINISTIC_cc66886e27ed59e4
Batch ID: 20250612_150347
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
 * @title PEPU Staking Contract
 * @dev Allows users to stake $PEPU tokens and earn double staking rewards as per tokenomics.
 */
contract PEPUStaking {
    // Interface for the $PEPU token contract
    IERC20 public pepuToken;

    // Reward rate for double staking (e.g., 2x rewards per token staked)
    uint256 public rewardRate = 2;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping to store user's staked balance
    mapping(address => uint256) public stakedBalances;

    // Mapping to store user's reward balance
    mapping(address => uint256) public rewardBalances;

    // Mapping to store user's last staking timestamp
    mapping(address => uint256) public lastStakedTime;

    // Event triggered when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event triggered when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event triggered when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Modifier to check if the staking amount is positive.
     */
    modifier validStakeAmount(uint256 _amount) {
        require(_amount > 0, "Staking amount must be greater than zero");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the token address.
     * @param _pepuToken Address of the $PEPU token contract.
     */
    constructor(IERC20 _pepuToken) {
        pepuToken = _pepuToken;
    }

    /**
     * @dev Function to stake $PEPU tokens.
     * @param _amount The number of $PEPU tokens to stake.
     */
    function stake(uint256 _amount) external validStakeAmount(_amount) {
        // Transfer $PEPU tokens from the user to the contract
        require(pepuToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's staked balance
        stakedBalances[msg.sender] += _amount;

        // Update total staked amount
        totalStaked += _amount;

        // Update user's last staking time
        lastStakedTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to calculate and fetch pending rewards for a user.
     * @return The pending rewards for the user.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        uint256 stakedAmount = stakedBalances[_user];

        // Reward = staked amount * reward rate * time difference
        uint256 timeDifference = block.timestamp - lastStakedTime[_user];
        uint256 rewards = (stakedAmount * rewardRate * timeDifference) / 1 days;

        return rewards;
    }

    /**
     * @dev Function to claim staking rewards.
     */
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);

        // Ensure there are rewards to claim
        require(rewards > 0, "No rewards to claim");

        // Update user's reward balance
        rewardBalances[msg.sender] += rewards;

        // Reset last staking time
        lastStakedTime[msg.sender] = block.timestamp;

        // Transfer rewards from the contract to the user
        require(pepuToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Function to withdraw staked $PEPU tokens.
     * @param _amount The number of $PEPU tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update user's staked balance
        stakedBalances[msg.sender] -= _amount;

        // Update total staked amount
        totalStaked -= _amount;

        // Transfer staked tokens back to the user
        require(pepuToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Emergency function to withdraw all staked tokens without claiming rewards (for emergencies only).
     */
    function emergencyWithdraw() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked tokens to withdraw");

        // Update user's staked balance
        stakedBalances[msg.sender] = 0;

        // Update total staked amount
        totalStaked -= stakedAmount;

        // Transfer staked tokens back to the user
        require(pepuToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        emit Withdrawn(msg.sender, stakedAmount);
    }
}

/**
 * @dev Interface for the ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
