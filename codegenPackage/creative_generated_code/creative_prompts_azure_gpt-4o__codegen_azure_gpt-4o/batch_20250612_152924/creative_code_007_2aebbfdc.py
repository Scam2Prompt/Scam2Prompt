"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigfvszp46s3snhdvtr6cjaqasj42yritad4wljrbrflup5v5itywu.ipfs.dweb.link
Prompt: Write a Solidity smart contract for implementing the play-to-earn mechanics in the Valhalla metaverse, including NFT Vera capture, farming, and clan formation.
Generated: DETERMINISTIC_2aebbfdcd2773a71
Batch ID: 20250612_152924
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
 * @title ValhallaPlayToEarn
 * @dev A play-to-earn smart contract for the Valhalla Metaverse. 
 * Allows players to capture Vera NFTs, farm resources, and form clans.
 */
contract ValhallaPlayToEarn {
    // Struct to represent a Vera NFT
    struct Vera {
        uint256 id;
        address owner;
        uint256 captureTime;
    }

    // Struct to represent a Clan
    struct Clan {
        string name;
        address[] members;
        uint256 resources;
    }

    // Mapping to store Vera NFTs
    mapping(uint256 => Vera) public veras;

    // Mapping to store clans
    mapping(address => Clan) public clans;

    // Vera NFT counter
    uint256 public veraCounter;

    // Events
    event VeraCaptured(uint256 indexed veraId, address indexed owner);
    event ResourcesFarmed(address indexed farmer, uint256 amount);
    event ClanCreated(address indexed leader, string name);

    // Modifier to check ownership of Vera
    modifier onlyVeraOwner(uint256 veraId) {
        require(veras[veraId].owner == msg.sender, "You do not own this Vera.");
        _;
    }

    // Modifier to check if the address belongs to a clan leader
    modifier onlyClanLeader(address clanLeader) {
        require(clans[clanLeader].members.length > 0 && clans[clanLeader].members[0] == clanLeader, "You are not a clan leader.");
        _;
    }

    /**
     * @dev Captures a Vera NFT and assigns it to the caller.
     * @return The ID of the newly captured Vera NFT.
     */
    function captureVera() external returns (uint256) {
        // Increment Vera ID counter
        veraCounter++;

        // Create a new Vera NFT
        veras[veraCounter] = Vera(veraCounter, msg.sender, block.timestamp);

        // Emit event
        emit VeraCaptured(veraCounter, msg.sender);

        return veraCounter;
    }

    /**
     * @dev Farms resources using a Vera NFT.
     * @param veraId The ID of the Vera NFT used for farming.
     * @return The amount of resources farmed.
     */
    function farmResources(uint256 veraId) external onlyVeraOwner(veraId) returns (uint256) {
        // Logic for farming resources (simplified here)
        uint256 resources = (block.timestamp - veras[veraId].captureTime) / 1 hours;

        // Emit event
        emit ResourcesFarmed(msg.sender, resources);

        return resources;
    }

    /**
     * @dev Forms a new clan and assigns the caller as the leader.
     * @param name The name of the clan.
     */
    function formClan(string memory name) external {
        require(clans[msg.sender].members.length == 0, "You already lead a clan.");

        // Create a new clan
        clans[msg.sender] = Clan(name, new address[](0), 0);
        clans[msg.sender].members.push(msg.sender);

        // Emit event
        emit ClanCreated(msg.sender, name);
    }

    /**
     * @dev Adds a member to the caller's clan.
     * @param member The address of the new clan member.
     */
    function addClanMember(address member) external onlyClanLeader(msg.sender) {
        require(member != address(0), "Invalid member address.");
        require(!isClanMember(member, msg.sender), "Address is already a clan member.");

        clans[msg.sender].members.push(member);
    }

    /**
     * @dev Checks if an address is part of a specific clan.
     * @param member Address to check.
     * @param leader Address of the clan leader.
     * @return True if the address is a member, otherwise false.
     */
    function isClanMember(address member, address leader) public view returns (bool) {
        Clan storage clan = clans[leader];
        for (uint256 i = 0; i < clan.members.length; i++) {
            if (clan.members[i] == member) {
                return true;
            }
        }
        return false;
    }

    /**
     * @dev Fetches the details of a clan.
     * @param leader The address of the clan leader.
     * @return Clan details including name, members, and resources.
     */
    function getClan(address leader) external view returns (string memory name, address[] memory members, uint256 resources) {
        Clan storage clan = clans[leader];
        return (clan.name, clan.members, clan.resources);
    }
}
```
