"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-b3.com
Prompt: Generate a smart contract for staking $B3 tokens within the hyper-operable gaming ecosystem described on the B3 platform.
Generated: DETERMINISTIC_595ab32dcc0c6be5
Batch ID: 20250612_150237
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
 * @title B3TokenStaking
 * @dev A smart contract for staking $B3 tokens within the hyper-operable gaming ecosystem.
 */
contract B3TokenStaking {
    // Variables
    IERC20 public b3Token; // ERC20 token interface
    uint256 public totalStaked; // Total amount of tokens staked in the contract
    address public owner; // Contract owner

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Time when the tokens were staked
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No stake found for user");
        _;
    }

    // Constructor
    constructor(address _b3TokenAddress) {
        require(_b3TokenAddress != address(0), "Invalid token address");
        b3Token = IERC20(_b3TokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Stake $B3 tokens into the contract.
     * @param _amount The amount of tokens to stake.
     */
    function stakeTokens(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(
            b3Token.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update stake information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;
        totalStaked += _amount;

        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $B3 tokens from the contract.
     */
    function unstakeTokens() external hasStake(msg.sender) {
        uint256 stakedAmount = stakes[msg.sender].amount;

        // Transfer tokens back to user
        require(
            b3Token.transfer(msg.sender, stakedAmount),
            "Token transfer failed"
        );

        // Update state
        stakes[msg.sender].amount = 0;
        totalStaked -= stakedAmount;

        emit TokensUnstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Calculate staking rewards (example logic: simple time-based reward).
     * @return reward The calculated reward.
     */
    function calculateRewards(address _user) public view hasStake(_user) returns (uint256 reward) {
        Stake memory userStake = stakes[_user];
        uint256 stakingDuration = block.timestamp - userStake.timestamp;

        // Example reward calculation: 0.1% per day
        reward = (userStake.amount * stakingDuration / 1 days) / 1000;
    }

    /**
     * @dev Claim rewards for staking.
     */
    function claimRewards() external hasStake(msg.sender) {
        uint256 reward = calculateRewards(msg.sender);

        // Transfer reward tokens to user (requires contract to hold enough tokens for rewards)
        require(b3Token.transfer(msg.sender, reward), "Reward transfer failed");

        // Reset stake timestamp for next reward calculation
        stakes[msg.sender].timestamp = block.timestamp;

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Emergency function for the owner to withdraw all tokens from the contract.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = b3Token.balanceOf(address(this));
        require(
            b3Token.transfer(owner, contractBalance),
            "Emergency withdraw failed"
        );
    }
}

/**
 * @dev Minimal ERC20 interface.
 * Used for interacting with the $B3 token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
