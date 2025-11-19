"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubetas-ai.pages.dev
Prompt: Generate a code snippet to implement a staking mechanism for $QUBE tokens that allows users to earn rewards from a 5% sell tax.
Generated: DETERMINISTIC_429d90aba902fdec
Batch ID: 20250612_162207
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
 * @title QUBE Token Staking Contract
 * @dev This contract allows users to stake $QUBE tokens and earn rewards accumulated from a 5% sell tax.
 */
contract QubeStaking {
    // Token interface for ERC20
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // $QUBE token contract address
    IERC20 public qubeToken;

    // Reward pool balance
    uint256 public rewardPool;

    // Total staked amount
    uint256 public totalStaked;

    // User staking data
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
    }

    // Mapping of user addresses to their staking data
    mapping(address => Stake) public stakes;

    // Events for logging staking and rewards
    event StakeTokens(address indexed user, uint256 amount);
    event UnstakeTokens(address indexed user, uint256 amount);
    event ClaimRewards(address indexed user, uint256 amount);
    event AddToRewardPool(uint256 amount);

    // Modifier to ensure non-zero staking
    modifier nonZero(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    /**
     * @dev Constructor to initialize the QUBE token contract address.
     * @param _qubeToken Address of the QUBE token contract.
     */
    constructor(address _qubeToken) {
        require(_qubeToken != address(0), "Invalid token address");
        qubeToken = IERC20(_qubeToken);
    }

    /**
     * @dev Allows users to stake $QUBE tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external nonZero(_amount) {
        // Transfer $QUBE tokens from the user to this contract
        require(qubeToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking data
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.rewardDebt = (rewardPool * userStake.amount) / totalStaked;

        // Update total staked amount
        totalStaked += _amount;

        emit StakeTokens(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their tokens partially or fully.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external nonZero(_amount) {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Calculate and update rewards before unstaking
        claimRewards();

        // Update staking data
        userStake.amount -= _amount;

        // Transfer tokens back to the user
        require(qubeToken.transfer(msg.sender, _amount), "Token transfer failed");

        // Update total staked amount
        totalStaked -= _amount;

        emit UnstakeTokens(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their accumulated rewards.
     */
    function claimRewards() public {
        Stake storage userStake = stakes[msg.sender];
        uint256 pendingRewards = ((rewardPool * userStake.amount) / totalStaked) - userStake.rewardDebt;

        require(pendingRewards > 0, "No rewards available");

        // Update reward debt
        userStake.rewardDebt = (rewardPool * userStake.amount) / totalStaked;

        // Transfer rewards to the user
        require(qubeToken.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        rewardPool -= pendingRewards;

        emit ClaimRewards(msg.sender, pendingRewards);
    }

    /**
     * @dev Allows an external source (e.g., tax distribution mechanism) to add rewards to the reward pool.
     * @param _amount Amount of tokens added to the reward pool.
     */
    function addToRewardPool(uint256 _amount) external nonZero(_amount) {
        // Transfer $QUBE tokens from the sender to the contract
        require(qubeToken.transferFrom(msg.sender, address(this), _amount), "Token transfer to reward pool failed");

        // Update reward pool balance
        rewardPool += _amount;

        emit AddToRewardPool(_amount);
    }

    /**
     * @dev View function to calculate a user's pending rewards.
     * @param _user Address of the user.
     * @return Amount of pending rewards.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 pending = ((rewardPool * userStake.amount) / totalStaked) - userStake.rewardDebt;
        return pending;
    }
}
```
