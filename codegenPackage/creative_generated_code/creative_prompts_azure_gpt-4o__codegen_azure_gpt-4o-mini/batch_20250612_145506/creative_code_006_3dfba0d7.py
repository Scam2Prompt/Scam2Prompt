"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purplepepesolana.pages.dev
Prompt: Develop a smart contract for $PURPE token transactions that includes features for community event participation and rewards distribution.
Generated: DETERMINISTIC_3dfba0d7a9b05a44
Batch ID: 20250612_145506
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PURPE Token Contract
 * @dev This contract implements the ERC20 token standard with additional features 
 * for community event participation and rewards distribution.
 */
contract PURPEToken is ERC20, Ownable {
    // Mapping to track user participation in events
    mapping(address => bool) public hasParticipated;
    
    // Event emitted when an event participation is recorded
    event EventParticipation(address indexed participant);
    
    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed recipient, uint256 amount);

    // Reward amount for participation
    uint256 public rewardAmount;

    /**
     * @dev Constructor to initialize the token with a name, symbol, and initial supply.
     * @param initialSupply The initial supply of the token.
     * @param _rewardAmount The reward amount for event participation.
     */
    constructor(uint256 initialSupply, uint256 _rewardAmount) 
        ERC20("PURPE Token", "PURPE") 
    {
        _mint(msg.sender, initialSupply);
        rewardAmount = _rewardAmount;
    }
    
    /**
     * @dev Allows users to participate in community events.
     * Requires that the user has not already participated.
     */
    function participateInEvent() external {
        require(!hasParticipated[msg.sender], "Already participated in the event.");
        
        // Record participation
        hasParticipated[msg.sender] = true;
        
        // Emit the participation event
        emit EventParticipation(msg.sender);
        
        // Distribute rewards to the participant
        _distributeRewards(msg.sender);
    }
    
    /**
     * @dev Internal function to handle reward distribution.
     * @param recipient The address of the recipient of the rewards.
     */
    function _distributeRewards(address recipient) internal {
        require(balanceOf(address(this)) >= rewardAmount, "Insufficient balance for rewards.");
        
        // Transfer reward tokens to the recipient
        _transfer(address(this), recipient, rewardAmount);
        
        // Emit the rewards distribution event
        emit RewardsDistributed(recipient, rewardAmount);
    }
    
    /**
     * @dev Allows the owner to deposit tokens into the contract for rewards distribution.
     * @param amount The amount of tokens to deposit.
     */
    function depositForRewards(uint256 amount) external onlyOwner {
        _transfer(msg.sender, address(this), amount);
    }
    
    /**
     * @dev Allows the owner to update the reward amount for participation.
     * @param newRewardAmount The new reward amount to set.
     */
    function updateRewardAmount(uint256 newRewardAmount) external onlyOwner {
        rewardAmount = newRewardAmount;
    }

    /**
     * @dev Function to enable token transfers (not required for basic ERC20).
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transferTokens(address recipient, uint256 amount) external {
        transfer(recipient, amount);
    }
}
```
