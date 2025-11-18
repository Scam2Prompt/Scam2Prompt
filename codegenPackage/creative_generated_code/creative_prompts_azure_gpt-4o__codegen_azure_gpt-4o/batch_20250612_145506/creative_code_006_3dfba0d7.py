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

/**
 * @title PURPE Token Smart Contract
 * @dev Implements ERC20 standard with additional features for community event participation
 *      and rewards distribution.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PURPE is ERC20, Ownable {
    // Mapping to track users' participation in community events
    mapping(address => bool) public hasParticipated;

    // Event to log participation
    event EventParticipation(address indexed participant, uint256 reward);

    // Event to log rewards distribution
    event RewardsDistributed(address indexed recipient, uint256 reward);

    // Reward amount for participating in community events
    uint256 public participationReward;

    /**
     * @dev Constructor to initialize the token name, symbol, and initial supply.
     * @param initialSupply Initial supply of $PURPE tokens
     */
    constructor(uint256 initialSupply, uint256 _participationReward) ERC20("PURPE Token", "PURPE") {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, initialSupply * 10**decimals());
        
        // Set the participation reward
        participationReward = _participationReward;
    }

    /**
     * @dev Allows users to participate in community events and receive rewards.
     * Prevents duplicate participation.
     */
    function participateInEvent() external {
        require(!hasParticipated[msg.sender], "You have already participated in this event.");
        require(balanceOf(address(this)) >= participationReward, "Insufficient reward tokens in contract.");

        // Mark user as participated
        hasParticipated[msg.sender] = true;

        // Transfer reward tokens to user
        _transfer(address(this), msg.sender, participationReward);
        
        // Emit participation event
        emit EventParticipation(msg.sender, participationReward);
    }

    /**
     * @dev Allows the owner to set a new participation reward.
     * @param newReward New reward amount for participation
     */
    function setParticipationReward(uint256 newReward) external onlyOwner {
        participationReward = newReward;
    }

    /**
     * @dev Distributes rewards to a list of recipients.
     * @param recipients Array of recipient addresses
     * @param rewards Array of rewards corresponding to each recipient
     */
    function distributeRewards(address[] calldata recipients, uint256[] calldata rewards) external onlyOwner {
        require(recipients.length == rewards.length, "Recipients and rewards arrays must have the same length.");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(balanceOf(address(this)) >= rewards[i], "Insufficient reward tokens in contract.");
            
            // Transfer reward to recipient
            _transfer(address(this), recipients[i], rewards[i]);
            
            // Emit rewards distribution event
            emit RewardsDistributed(recipients[i], rewards[i]);
        }
    }

    /**
     * @dev Allows the owner to deposit tokens into the contract for rewards distribution.
     * @param amount Amount of tokens to deposit
     */
    function depositTokens(uint256 amount) external onlyOwner {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to deposit.");
        
        // Transfer tokens from owner to contract
        _transfer(msg.sender, address(this), amount);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(balanceOf(address(this)) >= amount, "Insufficient tokens in contract.");
        
        // Transfer tokens from contract to owner
        _transfer(address(this), msg.sender, amount);
    }
}
```
