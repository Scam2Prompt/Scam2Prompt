"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainnetnodewebresolver.vercel.app
Prompt: Generate code to implement staking functionality for tokens, ensuring secure and efficient staking operations, as described on the Web3 Dapp Resolver platform.
Generated: DETERMINISTIC_f543bd2fa826633d
Batch ID: 20250612_142615
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
 * @title TokenStaking
 * @dev A secure and efficient staking contract for tokens on Web3 Dapp Resolver platforms.
 */
contract TokenStaking {
    // State variables
    address public owner; // Contract owner
    IERC20 public stakingToken; // Token used for staking
    uint256 public totalStaked; // Total staked tokens in the contract

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Time when tokens were staked
        bool isWithdrawn; // Tracking if stake has been withdrawn
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stake info

    // Events
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Constructor
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        owner = msg.sender;
        stakingToken = IERC20(_stakingToken);
    }

    // Modifier to check contract ownership
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to check valid staking amount
    modifier validStakeAmount(uint256 _amount) {
        require(_amount > 0, "Amount must be greater than zero");
        _;
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Allows users to stake a specified amount of tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external validStakeAmount(_amount) {
        require(stakingToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(stakingToken.allowance(msg.sender, address(this)) >= _amount, "Token allowance too low");

        // Transfer tokens from user to contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update staking information
        stakes[msg.sender] = Stake({
            amount: _amount,
            timestamp: block.timestamp,
            isWithdrawn: false
        });

        totalStaked += _amount;

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Allows users to unstake their tokens, including any rewards accrued.
     * Rewards are calculated based on a simple mechanism for demonstration purposes.
     */
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        
        require(userStake.amount > 0, "No tokens staked");
        require(!userStake.isWithdrawn, "Stake has already been withdrawn");

        // Reward calculation (example: 10% annual interest prorated by time staked)
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 reward = (userStake.amount * stakingDuration * 10) / (365 days * 100);

        uint256 totalAmount = userStake.amount + reward;

        // Transfer staked tokens + reward back to user
        bool success = stakingToken.transfer(msg.sender, totalAmount);
        require(success, "Token transfer failed");

        // Update staking information
        stakes[msg.sender].isWithdrawn = true;
        totalStaked -= userStake.amount;

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Emergency function for the owner to withdraw all tokens from the contract.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = stakingToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");

        bool success = stakingToken.transfer(owner, contractBalance);
        require(success, "Token transfer failed");

        totalStaked = 0; // Reset total staked to zero
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function allowance(address owner, address spender) external view returns (uint256);
}
```
