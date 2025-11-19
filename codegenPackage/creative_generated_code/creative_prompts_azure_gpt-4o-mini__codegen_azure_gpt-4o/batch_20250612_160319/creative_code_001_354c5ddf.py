"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsemex.com
Prompt: Generate a Solidity contract that allows staking of $PLSX tokens on the PulseX DEX.
Generated: DETERMINISTIC_354c5ddf1a7626ff
Batch ID: 20250612_160319
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
 * @title PulseX Token Staking Contract
 * @dev Allows users to stake $PLSX tokens and earn rewards.
 */
contract PulseXStaking {
    // Token interface for $PLSX
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // $PLSX token address
    IERC20 public immutable plsxToken;

    // Mapping of user address to their staked balance
    mapping(address => uint256) public stakedBalance;

    // Mapping of user address to their last staking timestamp
    mapping(address => uint256) public stakingTimestamp;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Reward rate (e.g., 1% per day)
    uint256 public constant REWARD_RATE = 100; // Basis points (1% per day)

    // Owner of the contract
    address public owner;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    /**
     * @dev Constructor to set the token address and contract owner.
     * @param _plsxToken Address of the $PLSX token contract.
     */
    constructor(IERC20 _plsxToken) {
        plsxToken = _plsxToken;
        owner = msg.sender;
    }

    /**
     * @dev Stake $PLSX tokens into the contract.
     * @param amount Amount of tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer tokens from user to contract
        bool success = plsxToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update user's staked balance and timestamp
        stakedBalance[msg.sender] += amount;
        stakingTimestamp[msg.sender] = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Calculate reward for a user based on their staking duration.
     * @param user Address of the user.
     * @return Reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        uint256 stakedAmount = stakedBalance[user];
        if (stakedAmount == 0) return 0;

        uint256 stakingDuration = block.timestamp - stakingTimestamp[user];
        uint256 reward = (stakedAmount * REWARD_RATE * stakingDuration) / (10000 * 1 days);

        return reward;
    }

    /**
     * @dev Withdraw staked tokens along with rewards.
     */
    function withdrawTokens() external {
        uint256 stakedAmount = stakedBalance[msg.sender];
        require(stakedAmount > 0, "No staked tokens to withdraw");

        // Calculate reward
        uint256 reward = calculateReward(msg.sender);

        // Reset user's staking data
        stakedBalance[msg.sender] = 0;
        stakingTimestamp[msg.sender] = 0;

        // Update total staked amount
        totalStaked -= stakedAmount;

        // Transfer staked tokens and reward to user
        bool successStake = plsxToken.transfer(msg.sender, stakedAmount);
        require(successStake, "Token transfer failed");

        if (reward > 0) {
            bool successReward = plsxToken.transfer(msg.sender, reward);
            require(successReward, "Reward transfer failed");
        }

        emit Withdrawn(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Emergency withdrawal by the owner to recover stuck tokens.
     * @param amount Amount to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Cannot withdraw zero tokens");

        bool success = plsxToken.transfer(owner, amount);
        require(success, "Token transfer failed");
    }
}
```
