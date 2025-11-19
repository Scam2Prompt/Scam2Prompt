"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://6235406996.pages.dev
Prompt: How can I implement staking for the WEPE token in a smart contract?
Generated: DETERMINISTIC_838db0e266c847fc
Batch ID: 20250612_161420
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
 * @title WEPE Token Staking Contract
 * @dev A contract that allows users to stake WEPE tokens and earn rewards.
 */
contract WEPEStaking {
    // Address of the WEPE token contract
    IERC20 public wepeToken;

    // Struct to represent a stake
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 timestamp;     // Time when the stake was made
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Reward rate (e.g., 10% annualized reward rate, expressed as 0.1 * 1e18 = 10%)
    uint256 public rewardRate;

    // Contract owner
    address public owner;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn (unstaked along with rewards)
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _wepeToken, uint256 _rewardRate) {
        wepeToken = _wepeToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Stake WEPE tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer tokens from the user to the contract
        require(
            wepeToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staking details
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked WEPE tokens and rewards.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");

        // Calculate rewards
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 reward = (userStake.amount * rewardRate * stakingDuration) /
            (365 days * 1e18);

        // Transfer staked tokens and rewards to the user
        uint256 totalAmount = userStake.amount + reward;
        require(wepeToken.balanceOf(address(this)) >= totalAmount, "Insufficient contract balance");

        // Reset user's stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer tokens
        require(wepeToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        emit Withdrawn(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Allows the contract owner to set a new reward rate.
     * @param _rewardRate New reward rate.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Emergency function for the owner to withdraw tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(
            wepeToken.transfer(owner, _amount),
            "Token transfer failed"
        );
    }
}

// Minimal interface for the ERC20 token
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
