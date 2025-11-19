"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinotg.pages.dev
Prompt: Create a Solidity contract that implements a basic staking mechanism for the $TGC token, allowing users to earn passive income.
Generated: DETERMINISTIC_ac9fbc9efb753c90
Batch ID: 20250612_155140
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
 * @title TGCStaking
 * @dev A basic staking contract for the $TGC token, allowing users to stake tokens and earn rewards.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract TGCStaking {
    // Address of the $TGC token contract
    IERC20 public immutable tgcToken;

    // Owner of the staking contract
    address public owner;

    // Annual reward rate (e.g., 10% rewards = 1000 basis points)
    uint256 public constant REWARD_RATE = 1000; // Basis points (BP)

    // Reward interval (1 year in seconds)
    uint256 public constant REWARD_INTERVAL = 365 days;

    // Tracks staked balances of users
    mapping(address => uint256) public stakedBalance;

    // Tracks timestamp of user's last claim or stake
    mapping(address => uint256) public lastStakeTimestamp;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to set the token address and contract owner.
     * @param _tgcToken Address of the $TGC token contract.
     */
    constructor(IERC20 _tgcToken) {
        tgcToken = _tgcToken;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake $TGC tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Update rewards before changing stake
        _claimRewards(msg.sender);

        // Transfer $TGC tokens from user to contract
        require(
            tgcToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update user's staked balance
        stakedBalance[msg.sender] += _amount;
        lastStakeTimestamp[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their tokens and withdraw them.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(
            stakedBalance[msg.sender] >= _amount,
            "Unstake amount exceeds staked balance"
        );

        // Claim rewards before unstaking
        _claimRewards(msg.sender);

        // Reduce user's staked balance
        stakedBalance[msg.sender] -= _amount;

        // Transfer $TGC tokens back to the user
        require(
            tgcToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their staking rewards.
     */
    function claimRewards() external {
        _claimRewards(msg.sender);
    }

    /**
     * @dev Internal function to calculate and distribute rewards.
     * @param _user Address of the user to claim rewards for.
     */
    function _claimRewards(address _user) internal {
        uint256 stakedAmount = stakedBalance[_user];
        require(stakedAmount > 0, "No staked balance");

        uint256 timeElapsed = block.timestamp - lastStakeTimestamp[_user];
        uint256 reward = (stakedAmount * REWARD_RATE * timeElapsed) /
            (10000 * REWARD_INTERVAL);

        if (reward > 0) {
            require(
                tgcToken.transfer(_user, reward),
                "Reward transfer failed"
            );
            emit RewardsClaimed(_user, reward);
        }

        // Update last stake timestamp to current time
        lastStakeTimestamp[_user] = block.timestamp;
    }

    /**
     * @dev Allows the owner to withdraw excess tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function ownerWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(
            tgcToken.balanceOf(address(this)) >= _amount,
            "Insufficient contract balance"
        );

        require(
            tgcToken.transfer(owner, _amount),
            "Token transfer failed"
        );
    }
}
```
