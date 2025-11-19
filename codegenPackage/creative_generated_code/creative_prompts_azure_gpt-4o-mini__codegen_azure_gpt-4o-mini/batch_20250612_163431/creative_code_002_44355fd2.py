"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-memeficlub.pages.dev
Prompt: Create an example of a smart contract for managing clan ownership and rewards distribution in the MemeFi gaming ecosystem.
Generated: DETERMINISTIC_44355fd2fb09d75e
Batch ID: 20250612_163431
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ClanOwnership
 * @dev A smart contract for managing clan ownership and rewards distribution in the MemeFi gaming ecosystem.
 */
contract ClanOwnership is Ownable {
    // Structure to hold clan details
    struct Clan {
        uint256 id;
        string name;
        address owner;
        uint256 totalRewards;
        uint256 rewardPerMember;
        uint256 memberCount;
    }

    // Mapping to store clans by their ID
    mapping(uint256 => Clan) private clans;
    // Mapping to track if an address is a member of the clan
    mapping(uint256 => mapping(address => bool)) private clanMembers;
    // Counter for the number of clans
    uint256 private clanCounter;

    // Events
    event ClanCreated(uint256 indexed clanId, string name, address indexed owner);
    event MemberJoined(uint256 indexed clanId, address indexed member);
    event RewardsDistributed(uint256 indexed clanId, uint256 amount);
    
    // Modifier to check if the caller is the clan owner
    modifier onlyClanOwner(uint256 clanId) {
        require(clans[clanId].owner == msg.sender, "Caller is not the clan owner");
        _;
    }

    /**
     * @dev Create a new clan
     * @param name The name of the clan
     */
    function createClan(string memory name) external {
        require(bytes(name).length > 0, "Clan name cannot be empty");

        clanCounter++;
        clans[clanCounter] = Clan(clanCounter, name, msg.sender, 0, 0, 0);
        
        emit ClanCreated(clanCounter, name, msg.sender);
    }

    /**
     * @dev Join a clan as a member
     * @param clanId The ID of the clan to join
     */
    function joinClan(uint256 clanId) external {
        require(clans[clanId].id != 0, "Clan does not exist");
        require(!clanMembers[clanId][msg.sender], "Already a member");

        clanMembers[clanId][msg.sender] = true;
        clans[clanId].memberCount++;

        emit MemberJoined(clanId, msg.sender);
    }

    /**
     * @dev Distribute rewards to clan members
     * @param clanId The ID of the clan
     * @param amount The total amount of rewards to distribute
     */
    function distributeRewards(uint256 clanId, uint256 amount) external onlyClanOwner(clanId) {
        require(clans[clanId].id != 0, "Clan does not exist");
        require(amount > 0, "Amount must be greater than zero");
        require(clans[clanId].memberCount > 0, "No members in clan to distribute rewards");

        clans[clanId].totalRewards += amount;
        clans[clanId].rewardPerMember = clans[clanId].totalRewards / clans[clanId].memberCount;
        
        emit RewardsDistributed(clanId, amount);
    }

    /**
     * @dev View the details of a clan
     * @param clanId The ID of the clan
     * @return Clan details
     */
    function getClan(uint256 clanId) external view returns (Clan memory) {
        require(clans[clanId].id != 0, "Clan does not exist");
        return clans[clanId];
    }

    /**
     * @dev Check if an address is a member of a clan
     * @param clanId The ID of the clan
     * @param member The address to check
     * @return True if the address is a member, false otherwise
     */
    function isMember(uint256 clanId, address member) external view returns (bool) {
        return clanMembers[clanId][member];
    }
}
```
