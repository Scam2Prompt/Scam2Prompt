"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://de-agent.com
Prompt: Provide an example of a smart contract that manages a large prize pool for Ethereum-based rewards, ensuring fair distribution among participants.
Generated: DETERMINISTIC_96f8ff199561c11d
Batch ID: 20250612_151605
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
 * @title PrizePool
 * @dev This smart contract manages a prize pool and ensures fair distribution among participants.
 */
contract PrizePool {
    // State variables
    address public owner; // Owner of the contract
    uint256 public totalPool; // Total ETH in the prize pool
    address[] public participants; // List of participants
    mapping(address => uint256) public contributions; // Tracks contributions by participants
    bool public distributionCompleted; // Tracks whether rewards have been distributed

    // Events
    event ContributionReceived(address indexed contributor, uint256 amount);
    event RewardsDistributed(uint256 totalPool, uint256 participantCount);
    event ContractOwnershipTransferred(address indexed oldOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    modifier prizePoolNotDistributed() {
        require(!distributionCompleted, "Prize pool has already been distributed");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows participants to contribute ETH to the prize pool.
     */
    function contribute() external payable {
        require(msg.value > 0, "Contribution must be greater than zero");

        // Update participant's contributions
        if (contributions[msg.sender] == 0) {
            participants.push(msg.sender); // Add to participants if it's their first contribution
        }
        contributions[msg.sender] += msg.value;

        // Update total pool
        totalPool += msg.value;

        emit ContributionReceived(msg.sender, msg.value);
    }

    /**
     * @dev Distributes the prize pool equally among participants.
     * Only callable by the contract owner.
     */
    function distributeRewards() external onlyOwner prizePoolNotDistributed {
        require(participants.length > 0, "No participants to distribute rewards to");
        require(totalPool > 0, "No funds available in the prize pool");

        // Calculate the reward per participant
        uint256 rewardPerParticipant = totalPool / participants.length;

        // Distribute rewards
        for (uint256 i = 0; i < participants.length; i++) {
            address participant = participants[i];
            uint256 reward = rewardPerParticipant;

            // Transfer reward
            (bool success, ) = participant.call{value: reward}("");
            require(success, "Reward transfer failed");
        }

        // Mark distribution as complete
        distributionCompleted = true;

        // Reset total pool to zero
        totalPool = 0;

        emit RewardsDistributed(totalPool, participants.length);
    }

    /**
     * @dev Allows the owner to transfer ownership to a new address.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        emit ContractOwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Fallback function to reject direct ETH transfers.
     */
    receive() external payable {
        revert("Direct deposits not allowed. Use the contribute function.");
    }

    /**
     * @dev Emergency function to withdraw contract funds.
     * Only callable by the contract owner.
     */
    function emergencyWithdraw() external onlyOwner {
        require(address(this).balance > 0, "No funds to withdraw");

        // Transfer all remaining funds to the owner
        (bool success, ) = owner.call{value: address(this).balance}("");
        require(success, "Emergency withdrawal failed");
    }
}
```
