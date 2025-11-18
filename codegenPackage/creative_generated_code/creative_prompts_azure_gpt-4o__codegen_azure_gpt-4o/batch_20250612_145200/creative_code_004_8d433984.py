"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmetaen.web.app
Prompt: Develop a function in Solidity to enable NFT city trading within the EarthMeta Marketplace, including governance features for virtual cities.
Generated: DETERMINISTIC_8d433984ba4c679f
Batch ID: 20250612_145200
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
 * @title EarthMeta Marketplace Contract
 * @dev Enables NFT city trading within the EarthMeta Marketplace ecosystem, including governance features for virtual cities.
 */
contract EarthMetaMarketplace {
    // Events
    event CityListed(uint256 indexed cityId, address indexed owner, uint256 price);
    event CityPurchased(uint256 indexed cityId, address indexed buyer, uint256 price);
    event CityDelisted(uint256 indexed cityId, address indexed owner);
    event GovernanceProposalCreated(uint256 indexed proposalId, address indexed proposer, string description, uint256 voteEndTime);

    // Structs
    struct City {
        uint256 id;
        address owner;
        uint256 price;
        bool isListed;
    }

    struct GovernanceProposal {
        uint256 id;
        address proposer;
        string description;
        uint256 voteEndTime;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
    }

    // Mappings
    mapping(uint256 => City) public cities; // Mapping of cityId to City details
    mapping(uint256 => GovernanceProposal) public proposals; // Mapping of proposalId to GovernanceProposal details
    mapping(address => mapping(uint256 => bool)) public hasVoted; // Track voting per address per proposal

    // State variables
    uint256 public nextCityId; // For auto-incrementing city IDs
    uint256 public nextProposalId; // For auto-incrementing proposal IDs

    // Modifier to check city ownership
    modifier onlyCityOwner(uint256 cityId) {
        require(cities[cityId].owner == msg.sender, "Not the owner of the city.");
        _;
    }

    /**
     * @dev List a city for sale in the marketplace.
     * @param price The sale price of the city.
     */
    function listCityForSale(uint256 price) external {
        require(price > 0, "Price must be greater than zero.");

        uint256 cityId = nextCityId++;
        cities[cityId] = City({
            id: cityId,
            owner: msg.sender,
            price: price,
            isListed: true
        });

        emit CityListed(cityId, msg.sender, price);
    }

    /**
     * @dev Purchase a listed city.
     * @param cityId The ID of the city to purchase.
     */
    function purchaseCity(uint256 cityId) external payable {
        City storage city = cities[cityId];
        require(city.isListed, "City is not listed for sale.");
        require(msg.value >= city.price, "Insufficient payment.");

        address previousOwner = city.owner;

        // Transfer ownership
        city.owner = msg.sender;
        city.isListed = false;

        // Transfer funds to the previous owner
        payable(previousOwner).transfer(city.price);

        emit CityPurchased(cityId, msg.sender, city.price);
    }

    /**
     * @dev Delist a city from the marketplace.
     * @param cityId The ID of the city to delist.
     */
    function delistCity(uint256 cityId) external onlyCityOwner(cityId) {
        City storage city = cities[cityId];
        require(city.isListed, "City is not listed.");

        city.isListed = false;

        emit CityDelisted(cityId, msg.sender);
    }

    /**
     * @dev Create a governance proposal for virtual city governance.
     * @param description The description of the governance proposal.
     * @param votingDuration The duration (in seconds) for voting.
     */
    function createGovernanceProposal(string calldata description, uint256 votingDuration) external {
        require(votingDuration > 0, "Voting duration must be greater than zero.");

        uint256 proposalId = nextProposalId++;
        proposals[proposalId] = GovernanceProposal({
            id: proposalId,
            proposer: msg.sender,
            description: description,
            voteEndTime: block.timestamp + votingDuration,
            votesFor: 0,
            votesAgainst: 0,
            executed: false
        });

        emit GovernanceProposalCreated(proposalId, msg.sender, description, block.timestamp + votingDuration);
    }

    /**
     * @dev Vote on a governance proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param support True to vote in favor, false to vote against.
     */
    function voteOnProposal(uint256 proposalId, bool support) external {
        GovernanceProposal storage proposal = proposals[proposalId];
        require(block.timestamp < proposal.voteEndTime, "Voting period has ended.");
        require(!hasVoted[msg.sender][proposalId], "Already voted on this proposal.");

        // Track the vote
        hasVoted[msg.sender][proposalId] = true;

        if (support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }
    }

    /**
     * @dev Execute a governance proposal if voting is complete.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external {
        GovernanceProposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.voteEndTime, "Voting period is not over.");
        require(!proposal.executed, "Proposal already executed.");

        proposal.executed = true;

        // Logic for executing proposal can be added here (e.g., city governance updates).
    }

    /**
     * @dev Retrieve city details.
     * @param cityId The ID of the city to retrieve.
     * @return City details.
     */
    function getCityDetails(uint256 cityId) external view returns (City memory) {
        return cities[cityId];
    }

    /**
     * @dev Retrieve proposal details.
     * @param proposalId The ID of the proposal to retrieve.
     * @return Proposal details.
     */
    function getProposalDetails(uint256 proposalId) external view returns (GovernanceProposal memory) {
        return proposals[proposalId];
    }
}
```
