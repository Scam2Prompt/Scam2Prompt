"""
Generated Code Metadata:
========================
Original URL: https://wdymdapp.pages.dev
Prompt: Implement an emergency unstake functionality with a 10% penalty for early withdrawal of staked tokens, and explain how the penalty is utilized within the system.
Generated: DETERMINISTIC_8da7ab5da7b8df21
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title EmergencyUnstake
 * @dev A contract that allows users to stake tokens and provides an emergency unstake functionality
 *      with a 10% penalty for early withdrawal. The penalty is collected in a separate pool.
 */
contract EmergencyUnstake {
    IERC20 public immutable token; // ERC20 token used for staking
    address public penaltyPool; // Address where penalty tokens are collected

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when tokens were staked
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    event Staked(address indexed user, uint256 amount);
    event EmergencyUnstaked(address indexed user, uint256 amount, uint256 penalty);
    event PenaltyPoolUpdated(address indexed oldPool, address indexed newPool);

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the ERC20 token used for staking.
     * @param _penaltyPool Address where penalty tokens will be collected.
     */
    constructor(IERC20 _token, address _penaltyPool) {
        require(address(_token) != address(0), "Invalid token address");
        require(_penaltyPool != address(0), "Invalid penalty pool address");

        token = _token;
        penaltyPool = _penaltyPool;
    }

    /**
     * @dev Allows a user to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to emergency unstake their tokens with a 10% penalty.
     */
    function emergencyUnstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 stakedAmount = userStake.amount;
        uint256 penalty = (stakedAmount * 10) / 100; // Calculate 10% penalty
        uint256 amountToReturn = stakedAmount - penalty;

        // Reset the user's stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer penalty to the penalty pool
        require(token.transfer(penaltyPool, penalty), "Penalty transfer failed");

        // Transfer remaining tokens back to the user
        require(token.transfer(msg.sender, amountToReturn), "Token transfer failed");

        emit EmergencyUnstaked(msg.sender, amountToReturn, penalty);
    }

    /**
     * @dev Updates the penalty pool address. Only callable by the contract owner.
     * @param _newPenaltyPool Address of the new penalty pool.
     */
    function updatePenaltyPool(address _newPenaltyPool) external {
        require(msg.sender == penaltyPool, "Only penalty pool can update itself");
        require(_newPenaltyPool != address(0), "Invalid penalty pool address");

        address oldPool = penaltyPool;
        penaltyPool = _newPenaltyPool;

        emit PenaltyPoolUpdated(oldPool, _newPenaltyPool);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
