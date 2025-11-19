"""
Generated Code Metadata:
========================
Original URL: https://iqratechpoint.pages.dev
Prompt: Develop a blockchain-based educational game concept that incorporates IQRA Tokens as rewards for achieving milestones, and outline the technical implementation using smart contracts.
Generated: DETERMINISTIC_fff1774451fa5c39
Batch ID: 20250612_151246
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
 * @title IQRA Token Contract
 * @dev ERC20 token with minting capabilities for educational game rewards
 */
contract IQRAToken is ERC20, Ownable, Pausable {
    constructor() ERC20("IQRA Token", "IQRA") {
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Initial supply
    }

    /**
     * @dev Mint new tokens (only callable by owner)
     * @param to Address to receive the minted tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Pause token transfers
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause token transfers
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    function _beforeTokenTransfer(address from, address to, uint256 amount)
        internal
        override
    {
        super._beforeTokenTransfer(from, to, amount);
        require(!paused(), "Token transfer while paused");
    }
}

/**
 * @title EducationalGame Contract
 * @dev Manages game milestones and IQRA token rewards
 */
contract EducationalGame is Ownable, Pausable {
    IQRAToken public iqraToken;
    
    struct Milestone {
        uint256 id;
        string name;
        uint256 rewardAmount;
        bool isActive;
    }

    mapping(uint256 => Milestone) public milestones;
    mapping(address => mapping(uint256 => bool)) public userMilestones;
    uint256 public milestoneCount;

    event MilestoneCompleted(address indexed user, uint256 milestoneId, uint256 rewardAmount);
    event MilestoneAdded(uint256 milestoneId, string name, uint256 rewardAmount);
    event MilestoneUpdated(uint256 milestoneId, string name, uint256 rewardAmount, bool isActive);

    constructor(address _iqraTokenAddress) {
        iqraToken = IQRAToken(_iqraTokenAddress);
    }

    /**
     * @dev Add a new milestone
     * @param name Name of the milestone
     * @param rewardAmount IQRA tokens to reward for completion
     */
    function addMilestone(string memory name, uint256 rewardAmount) external onlyOwner {
        milestoneCount++;
        milestones[milestoneCount] = Milestone({
            id: milestoneCount,
            name: name,
            rewardAmount: rewardAmount,
            isActive: true
        });
        emit MilestoneAdded(milestoneCount, name, rewardAmount);
    }

    /**
     * @dev Update an existing milestone
     * @param milestoneId ID of the milestone to update
     * @param name New name for the milestone
     * @param rewardAmount New reward amount
     * @param isActive Whether the milestone is active
     */
    function updateMilestone(
        uint256 milestoneId,
        string memory name,
        uint256 rewardAmount,
        bool isActive
    ) external onlyOwner {
        require(milestoneId <= milestoneCount && milestoneId > 0, "Invalid milestone ID");
        milestones[milestoneId] = Milestone({
            id: milestoneId,
            name: name,
            rewardAmount: rewardAmount,
            isActive: isActive
        });
        emit MilestoneUpdated(milestoneId, name, rewardAmount, isActive);
    }

    /**
     * @dev Complete a milestone and receive IQRA tokens
     * @param milestoneId ID of the milestone to complete
     */
    function completeMilestone(uint256 milestoneId) external whenNotPaused {
        require(milestoneId <= milestoneCount && milestoneId > 0, "Invalid milestone ID");
        require(milestones[milestoneId].isActive, "Milestone is not active");
        require(!userMilestones[msg.sender][milestoneId], "Milestone already completed");

        userMilestones[msg.sender][milestoneId] = true;
        uint256 rewardAmount = milestones[milestoneId].rewardAmount;
        
        iqraToken.mint(msg.sender, rewardAmount);
        emit MilestoneCompleted(msg.sender, milestoneId, rewardAmount);
    }

    /**
     * @dev Pause the game
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause the game
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Check if user has completed a milestone
     * @param user Address to check
     * @param milestoneId ID of the milestone
     * @return bool Whether the user has completed the milestone
     */
    function hasCompletedMilestone(address user, uint256 milestoneId) external view returns (bool) {
        return userMilestones[user][milestoneId];
    }
}
```
