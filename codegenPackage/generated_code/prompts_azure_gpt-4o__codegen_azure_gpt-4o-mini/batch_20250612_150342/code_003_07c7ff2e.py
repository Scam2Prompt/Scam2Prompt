"""
Generated Code Metadata:
========================
Original URL: https://starknet-ambassadors.org
Prompt: Generate a Solidity smart contract that aligns with Starknet's mission to empower communities and increase adoption of decentralized solutions.
Generated: DETERMINISTIC_07c7ff2e5a822ffa
Batch ID: 20250612_150342
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

/// @title Community Empowerment Smart Contract
/// @author Your Name
/// @notice This contract aims to empower communities by allowing them to create and manage decentralized solutions.
/// @dev The contract includes functionalities for community creation, voting, and fund management.

contract CommunityEmpowerment {
    // Struct to represent a community
    struct Community {
        string name;
        address owner;
        uint256 funds;
        mapping(address => bool) members;
        uint256 voteCount;
    }

    // Mapping to store communities by their unique ID
    mapping(uint256 => Community) public communities;
    uint256 public communityCount;

    // Event emitted when a new community is created
    event CommunityCreated(uint256 communityId, string name, address owner);

    // Event emitted when a member joins a community
    event MemberJoined(uint256 communityId, address member);

    // Event emitted when funds are added to a community
    event FundsAdded(uint256 communityId, uint256 amount);

    // Modifier to check if the caller is the community owner
    modifier onlyOwner(uint256 communityId) {
        require(msg.sender == communities[communityId].owner, "Not the community owner");
        _;
    }

    /// @notice Creates a new community
    /// @param _name The name of the community
    function createCommunity(string memory _name) public {
        communityCount++;
        Community storage newCommunity = communities[communityCount];
        newCommunity.name = _name;
        newCommunity.owner = msg.sender;
        newCommunity.funds = 0;
        newCommunity.voteCount = 0;

        emit CommunityCreated(communityCount, _name, msg.sender);
    }

    /// @notice Allows a user to join a community
    /// @param communityId The ID of the community to join
    function joinCommunity(uint256 communityId) public {
        require(communityId > 0 && communityId <= communityCount, "Invalid community ID");
        require(!communities[communityId].members[msg.sender], "Already a member");

        communities[communityId].members[msg.sender] = true;

        emit MemberJoined(communityId, msg.sender);
    }

    /// @notice Allows the community owner to add funds to their community
    /// @param communityId The ID of the community to add funds to
    function addFunds(uint256 communityId) public payable onlyOwner(communityId) {
        require(msg.value > 0, "Must send a positive amount of Ether");

        communities[communityId].funds += msg.value;

        emit FundsAdded(communityId, msg.value);
    }

    /// @notice Allows the community owner to withdraw funds from their community
    /// @param communityId The ID of the community to withdraw funds from
    /// @param amount The amount of funds to withdraw
    function withdrawFunds(uint256 communityId, uint256 amount) public onlyOwner(communityId) {
        require(amount <= communities[communityId].funds, "Insufficient funds");

        communities[communityId].funds -= amount;
        payable(msg.sender).transfer(amount);
    }

    /// @notice Returns the details of a community
    /// @param communityId The ID of the community to retrieve
    /// @return name The name of the community
    /// @return owner The address of the community owner
    /// @return funds The total funds in the community
    function getCommunityDetails(uint256 communityId) public view returns (string memory name, address owner, uint256 funds) {
        require(communityId > 0 && communityId <= communityCount, "Invalid community ID");
        Community storage community = communities[communityId];
        return (community.name, community.owner, community.funds);
    }
}
```
