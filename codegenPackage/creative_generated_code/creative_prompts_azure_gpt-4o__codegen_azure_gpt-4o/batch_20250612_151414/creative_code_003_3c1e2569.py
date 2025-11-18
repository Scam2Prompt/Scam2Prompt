"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peetdecentralized.finance
Prompt: Write a smart contract in Solidity to stake PTE tokens on multiple blockchains using Peet's ROI-optimized staking mechanism.
Generated: DETERMINISTIC_3c1e25693b9e9b2c
Batch ID: 20250612_151414
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
 * @title MultiChainStaking
 * @dev A smart contract for staking PTE tokens across multiple blockchains
 * using Peet's ROI-optimized staking mechanism.
 */
contract MultiChainStaking {
    // Define the PTE token interface
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // State variables
    address public owner;
    IERC20 public pteToken;

    struct Stake {
        uint256 amount;
        uint256 timestamp;
        uint256 duration;
    }

    mapping(address => Stake) public stakes;

    // Event declarations
    event Staked(address indexed user, uint256 amount, uint256 duration);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier hasStake(address user) {
        require(stakes[user].amount > 0, "No active stake");
        _;
    }

    constructor(address _pteTokenAddress) {
        owner = msg.sender;
        pteToken = IERC20(_pteTokenAddress);
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Allows users to stake PTE tokens.
     * @param amount The amount of PTE tokens to stake.
     * @param duration The duration of the stake in seconds.
     */
    function stake(uint256 amount, uint256 duration) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(duration > 0, "Stake duration must be greater than zero");

        // Transfer tokens from user to contract
        bool success = pteToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Record the stake
        stakes[msg.sender] = Stake({
            amount: amount,
            timestamp: block.timestamp,
            duration: duration
        });

        emit Staked(msg.sender, amount, duration);
    }

    /**
     * @dev Allows users to unstake PTE tokens and claim rewards.
     */
    function unstake() external hasStake(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        require(block.timestamp >= userStake.timestamp + userStake.duration, "Stake duration not yet completed");

        uint256 amount = userStake.amount;

        // Calculate rewards using Peet's ROI-optimized mechanism
        uint256 reward = calculateReward(userStake.amount, userStake.duration);

        // Remove the stake record
        delete stakes[msg.sender];

        // Transfer tokens and reward back to the user
        bool success = pteToken.transfer(msg.sender, amount + reward);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, amount, reward);
    }

    /**
     * @dev Calculates the reward based on Peet's ROI-optimized mechanism.
     * @param amount The staked amount.
     * @param duration The staking duration in seconds.
     * @return The reward amount.
     */
    function calculateReward(uint256 amount, uint256 duration) internal pure returns (uint256) {
        // Example ROI logic: 5% reward for every 30 days (2592000 seconds)
        uint256 roiRate = 5; // 5%
        uint256 reward = (amount * roiRate * duration) / (100 * 2592000);
        return reward;
    }

    /**
     * @dev Allows the owner to withdraw any PTE tokens accidentally sent to the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(pteToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        bool success = pteToken.transfer(owner, amount);
        require(success, "Token transfer failed");
    }
}
```
