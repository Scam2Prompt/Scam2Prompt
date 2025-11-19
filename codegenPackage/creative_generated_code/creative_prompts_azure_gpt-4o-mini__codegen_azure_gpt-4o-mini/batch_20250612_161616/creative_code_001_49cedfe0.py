"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://outlaws.wtf
Prompt: Write a smart contract that manages bounty hunts and rewards for participants in the Outlaws.WTF digital storytelling experience.
Generated: DETERMINISTIC_49cedfe0aefb0ccf
Batch ID: 20250612_161616
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract BountyHunt {
    // Struct to store information about a bounty
    struct Bounty {
        uint256 id;
        string description;
        address payable creator;
        uint256 rewardAmount;
        bool isActive;
    }

    // Mapping to store bounties using a unique ID
    mapping(uint256 => Bounty) public bounties;
    uint256 public bountyCount;

    // Event emitted when a new bounty is created
    event BountyCreated(uint256 indexed id, string description, address indexed creator, uint256 rewardAmount);
    
    // Event emitted when a bounty is completed
    event BountyCompleted(uint256 indexed id, address indexed hunter);

    // ERC20 Token used for rewards
    IERC20 public rewardToken;

    // Constructor to initialize the contract with an ERC20 token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        rewardToken = IERC20(_tokenAddress);
    }

    // Function to create a new bounty
    function createBounty(string calldata _description, uint256 _rewardAmount) external {
        require(_rewardAmount > 0, "Reward must be greater than zero");

        // Transfer the reward amount from the creator to the contract
        require(rewardToken.transferFrom(msg.sender, address(this), _rewardAmount), "Transfer failed");

        bountyCount++;
        bounties[bountyCount] = Bounty(bountyCount, _description, payable(msg.sender), _rewardAmount, true);
        
        emit BountyCreated(bountyCount, _description, msg.sender, _rewardAmount);
    }

    // Function to complete a bounty
    function completeBounty(uint256 _bountyId) external {
        Bounty storage bounty = bounties[_bountyId];
        
        require(bounty.isActive, "Bounty is not active");
        require(bounty.creator != msg.sender, "Creator cannot complete their own bounty");

        // Mark the bounty as completed
        bounty.isActive = false;

        // Transfer the reward to the hunter
        require(rewardToken.transfer(msg.sender, bounty.rewardAmount), "Transfer failed");

        emit BountyCompleted(_bountyId, msg.sender);
    }

    // Function to retrieve bounty details
    function getBounty(uint256 _bountyId) external view returns (Bounty memory) {
        return bounties[_bountyId];
    }

    // Function to retrieve the total number of bounties
    function totalBounties() external view returns (uint256) {
        return bountyCount;
    }
}
```
