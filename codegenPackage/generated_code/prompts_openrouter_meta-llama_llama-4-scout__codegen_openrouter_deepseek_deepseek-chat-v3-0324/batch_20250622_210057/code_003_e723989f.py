"""
Generated Code Metadata:
========================
Original URL: https://arbius-en.pages.dev
Prompt: "Generate a smart contract code for Arbius token that enforces economic rules, including a max supply of 1 million tokens and a task reward system."
Generated: DETERMINISTIC_e723989f7bf69579
Batch ID: 20250622_210057
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title Arbius Token Contract
 * @dev ERC20 token with max supply of 1,000,000 tokens and task reward system
 */
contract ArbiusToken is ERC20, Ownable, Pausable {
    uint256 public constant MAX_SUPPLY = 1_000_000 * 10**18; // 1 million tokens with 18 decimals
    uint256 public constant TASK_REWARD = 10 * 10**18; // 10 tokens per task completion
    uint256 public totalMinted = 0;

    // Mapping to track task completions to prevent double-spending
    mapping(bytes32 => bool) public completedTasks;

    event TaskCompleted(address indexed user, bytes32 taskId, uint256 reward);
    event Mint(address indexed to, uint256 amount);

    /**
     * @dev Constructor that mints initial supply to the owner
     * @param initialSupply Initial amount of tokens to mint (must be <= MAX_SUPPLY)
     */
    constructor(uint256 initialSupply) ERC20("Arbius", "AIUS") {
        require(initialSupply <= MAX_SUPPLY, "Initial supply exceeds max supply");
        _mint(msg.sender, initialSupply);
        totalMinted = initialSupply;
    }

    /**
     * @dev Mint new tokens as task rewards
     * @param to Address to receive the reward
     * @param taskId Unique identifier for the completed task
     */
    function rewardTaskCompletion(address to, bytes32 taskId) external onlyOwner whenNotPaused {
        require(!completedTasks[taskId], "Task already completed");
        require(totalMinted + TASK_REWARD <= MAX_SUPPLY, "Max supply reached");

        completedTasks[taskId] = true;
        totalMinted += TASK_REWARD;
        _mint(to, TASK_REWARD);

        emit TaskCompleted(to, taskId, TASK_REWARD);
    }

    /**
     * @dev Pause token transfers and rewards
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause token transfers and rewards
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Hook that is called before any transfer of tokens
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Prevent renouncing ownership to maintain control over token economics
     */
    function renounceOwnership() public override onlyOwner {
        revert("Ownership cannot be renounced");
    }
}
```
