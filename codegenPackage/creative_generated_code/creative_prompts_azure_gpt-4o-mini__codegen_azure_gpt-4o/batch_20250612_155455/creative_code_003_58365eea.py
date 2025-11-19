"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rainbowxpepe.pages.dev
Prompt: Develop a smart contract function to automate the claiming of $RPEPE tokens based on the roadmap outlined on the Rainbow Pepe site.
Generated: DETERMINISTIC_58365eeafd5e3a3c
Batch ID: 20250612_155455
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
 * @title RainbowPepeTokenClaim
 * @dev Smart contract to automate the claiming of $RPEPE tokens based on the roadmap.
 *      Assumes a roadmap schedule with predefined milestones and amounts.
 */
contract RainbowPepeTokenClaim {
    // Address of the $RPEPE token contract
    IERC20 public rpepeToken;

    // Owner of the contract
    address public owner;

    // Mapping to track milestones and their respective claim amounts
    mapping(uint256 => uint256) public roadmapMilestones;

    // Mapping to track whether a specific milestone has been claimed
    mapping(uint256 => bool) public isMilestoneClaimed;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed claimant, uint256 milestoneIndex, uint256 amount);

    /**
     * @dev Modifier to restrict functions to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _rpepeToken Address of the $RPEPE token contract.
     */
    constructor(address _rpepeToken) {
        require(_rpepeToken != address(0), "Invalid token address");
        rpepeToken = IERC20(_rpepeToken);
        owner = msg.sender;

        // Define the roadmap milestones (example values)
        roadmapMilestones[1] = 1000 ether; // Milestone 1: 1000 $RPEPE
        roadmapMilestones[2] = 2000 ether; // Milestone 2: 2000 $RPEPE
        roadmapMilestones[3] = 3000 ether; // Milestone 3: 3000 $RPEPE
    }

    /**
     * @dev Function to claim tokens for a specific milestone.
     * @param milestoneIndex Index of the milestone to claim tokens for.
     */
    function claimTokens(uint256 milestoneIndex) external {
        require(roadmapMilestones[milestoneIndex] > 0, "Invalid milestone index");
        require(!isMilestoneClaimed[milestoneIndex], "Milestone already claimed");

        uint256 amount = roadmapMilestones[milestoneIndex];

        // Ensure the contract has enough tokens for the claim
        require(rpepeToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Mark the milestone as claimed
        isMilestoneClaimed[milestoneIndex] = true;

        // Transfer tokens to the caller
        require(rpepeToken.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensClaimed(msg.sender, milestoneIndex, amount);
    }

    /**
     * @dev Function to allow the owner to add or update roadmap milestones.
     * @param milestoneIndex Index of the milestone.
     * @param amount Amount of tokens for the milestone.
     */
    function setMilestone(uint256 milestoneIndex, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        roadmapMilestones[milestoneIndex] = amount;
    }

    /**
     * @dev Withdraw any remaining tokens in the contract.
     */
    function withdrawTokens() external onlyOwner {
        uint256 balance = rpepeToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(rpepeToken.transfer(owner, balance), "Token transfer failed");
    }
}

/**
 * @dev Interface for the ERC20 standard token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
