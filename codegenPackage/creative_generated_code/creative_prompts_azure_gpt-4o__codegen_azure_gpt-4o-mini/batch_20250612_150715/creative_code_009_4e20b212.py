"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.news
Prompt: Write a smart contract that enables Farcaster members to earn rewards based on their downstream influence on other members, as specified by the Moxie Protocol.
Generated: DETERMINISTIC_4e20b21213c6ce00
Batch ID: 20250612_150715
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

// Importing OpenZeppelin's Ownable contract for access control and security
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// MoxieProtocol contract to reward Farcaster members based on influence
contract MoxieProtocol is Ownable {
    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed member, uint256 amount);
    
    // Struct to hold member data
    struct Member {
        uint256 influenceScore;
        uint256 rewards;
        bool exists;
    }

    // Mapping of member addresses to their data
    mapping(address => Member) private members;

    // ERC20 token used for rewards
    IERC20 public rewardToken;

    // Constructor to initialize the reward token
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
    }

    // Modifier to check if the member exists
    modifier onlyMember() {
        require(members[msg.sender].exists, "Not a registered member");
        _;
    }

    // Function to register a member
    function registerMember() external {
        require(!members[msg.sender].exists, "Member already registered");
        members[msg.sender] = Member(0, 0, true);
    }

    // Function to update influence score (can only be called by the member)
    function updateInfluenceScore(uint256 newScore) external onlyMember {
        members[msg.sender].influenceScore = newScore;
    }

    // Function to distribute rewards based on influence score
    function distributeRewards(address[] calldata memberAddresses) external onlyOwner {
        uint256 totalInfluence = 0;

        // Calculate total influence score of all specified members
        for (uint256 i = 0; i < memberAddresses.length; i++) {
            require(members[memberAddresses[i]].exists, "Member does not exist");
            totalInfluence += members[memberAddresses[i]].influenceScore;
        }

        // Distribute rewards based on influence score
        for (uint256 i = 0; i < memberAddresses.length; i++) {
            uint256 reward = (members[memberAddresses[i]].influenceScore * 1e18) / totalInfluence;
            members[memberAddresses[i]].rewards += reward;

            // Emit event for distributed rewards
            emit RewardsDistributed(memberAddresses[i], reward);
        }
    }

    // Function for members to claim their rewards
    function claimRewards() external onlyMember {
        uint256 rewardAmount = members[msg.sender].rewards;
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the member's rewards to prevent re-entrancy
        members[msg.sender].rewards = 0;

        // Transfer rewards to the member
        bool success = rewardToken.transfer(msg.sender, rewardAmount);
        require(success, "Reward transfer failed");
    }

    // Function to check the member's rewards
    function checkRewards() external view onlyMember returns (uint256) {
        return members[msg.sender].rewards;
    }

    // Function to check a member's influence score
    function checkInfluenceScore(address memberAddress) external view returns (uint256) {
        require(members[memberAddress].exists, "Member does not exist");
        return members[memberAddress].influenceScore;
    }
}
```
