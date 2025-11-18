"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-ai.pages.dev
Prompt: Generate code to implement a rewards program in a blockchain-based platform like Pushd, where users earn tokens for completing specific tasks or milestones. Include token distribution logic.
Generated: DETERMINISTIC_638ab3efe5827c67
Batch ID: 20250612_152249
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
 * @title RewardsProgram
 * @dev Implements token-based rewards for completing specific tasks or milestones in a blockchain-based platform.
 */
contract RewardsProgram {
    // Define the owner of the contract
    address public owner;

    // Define the token used for rewards
    IERC20 public rewardToken;

    // Event emitted when tokens are distributed
    event RewardDistributed(address indexed user, uint256 amount);

    // Mapping to store user task completion status
    mapping(address => mapping(string => bool)) public taskCompletion;

    // Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the owner and reward token.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        owner = msg.sender;
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Mark a task as completed and distribute rewards.
     * @param _user Address of the user completing the task.
     * @param _taskId Identifier of the task.
     * @param _rewardAmount Amount of tokens to reward for the task.
     */
    function completeTask(
        address _user,
        string memory _taskId,
        uint256 _rewardAmount
    ) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_rewardAmount > 0, "Reward amount must be greater than 0");
        require(!taskCompletion[_user][_taskId], "Task already completed");

        // Mark task as completed
        taskCompletion[_user][_taskId] = true;

        // Distribute rewards
        require(
            rewardToken.transfer(_user, _rewardAmount),
            "Token transfer failed"
        );

        // Emit event
        emit RewardDistributed(_user, _rewardAmount);
    }

    /**
     * @dev Withdraw tokens from the contract (emergency or maintenance).
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(
            rewardToken.transfer(owner, _amount),
            "Token withdrawal failed"
        );
    }

    /**
     * @dev Change the ownership of the contract.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        owner = _newOwner;
    }
}

// Minimal ERC20 interface for interacting with the reward token
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
