"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbinu.app
Prompt: Develop a smart contract in Solidity that implements the community-led initiatives mentioned on the Arbinu site, ensuring decentralized management of token holders.
Generated: DETERMINISTIC_6e13ce4f8bf1cea0
Batch ID: 20250612_162849
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
 * @title CommunityInitiatives
 * @dev A smart contract to manage community-led initiatives in a decentralized way.
 * Token holders can create, vote, and fund initiatives.
 */
contract CommunityInitiatives {
    // Struct to represent an initiative
    struct Initiative {
        string description; // Description of the initiative
        address creator; // Address of the creator
        uint256 fundingGoal; // Funding goal in wei
        uint256 fundsRaised; // Total funds raised so far
        uint256 voteCount; // Number of votes in favor
        bool completed; // Whether the initiative is completed
        mapping(address => bool) votes; // Track who has voted
    }

    // Mapping to store initiatives
    mapping(uint256 => Initiative) public initiatives;
    uint256 public initiativeCount; // Counter for initiatives

    // ERC20 token address for verifying token holders
    address public tokenAddress;

    // Events for transparency
    event InitiativeCreated(uint256 indexed initiativeId, string description, uint256 fundingGoal);
    event InitiativeFunded(uint256 indexed initiativeId, address indexed funder, uint256 amount);
    event InitiativeVoted(uint256 indexed initiativeId, address indexed voter);

    /**
     * @dev Constructor to initialize the contract with the ERC20 token address.
     * @param _tokenAddress Address of the ERC20 token contract.
     */
    constructor(address _tokenAddress) {
        tokenAddress = _tokenAddress;
    }

    /**
     * @dev Modifier to restrict actions to token holders only.
     */
    modifier onlyTokenHolder() {
        require(balanceOf(msg.sender) > 0, "Only token holders can perform this action");
        _;
    }

    /**
     * @dev Function to get the balance of an account from the ERC20 token contract.
     * @param account Address of the account to check balance.
     * @return uint256 Balance of the account in tokens.
     */
    function balanceOf(address account) internal view returns (uint256) {
        (bool success, bytes memory data) = tokenAddress.staticcall(
            abi.encodeWithSignature("balanceOf(address)", account)
        );
        require(success, "Failed to fetch token balance");
        return abi.decode(data, (uint256));
    }

    /**
     * @dev Function to create a new initiative.
     * @param description Description of the initiative.
     * @param fundingGoal Funding goal in wei.
     */
    function createInitiative(string memory description, uint256 fundingGoal) external onlyTokenHolder {
        require(fundingGoal > 0, "Funding goal must be greater than zero");
        
        Initiative storage newInitiative = initiatives[initiativeCount];
        newInitiative.description = description;
        newInitiative.creator = msg.sender;
        newInitiative.fundingGoal = fundingGoal;
        newInitiative.completed = false;

        emit InitiativeCreated(initiativeCount, description, fundingGoal);
        initiativeCount++;
    }

    /**
     * @dev Function to fund an initiative.
     * @param initiativeId ID of the initiative to fund.
     */
    function fundInitiative(uint256 initiativeId) external payable onlyTokenHolder {
        require(initiativeId < initiativeCount, "Invalid initiative ID");
        Initiative storage initiative = initiatives[initiativeId];
        require(!initiative.completed, "Initiative is already completed");
        require(msg.value > 0, "Funding amount must be greater than zero");

        initiative.fundsRaised += msg.value;

        emit InitiativeFunded(initiativeId, msg.sender, msg.value);

        // Mark as completed if funding goal is reached
        if (initiative.fundsRaised >= initiative.fundingGoal) {
            initiative.completed = true;
        }
    }

    /**
     * @dev Function to vote for an initiative.
     * @param initiativeId ID of the initiative to vote for.
     */
    function voteForInitiative(uint256 initiativeId) external onlyTokenHolder {
        require(initiativeId < initiativeCount, "Invalid initiative ID");
        Initiative storage initiative = initiatives[initiativeId];
        require(!initiative.completed, "Initiative is already completed");
        require(!initiative.votes[msg.sender], "You have already voted");

        initiative.votes[msg.sender] = true;
        initiative.voteCount++;

        emit InitiativeVoted(initiativeId, msg.sender);
    }

    /**
     * @dev Function to fetch initiative details.
     * @param initiativeId ID of the initiative.
     * @return description Initiative description.
     * @return creator Initiative creator address.
     * @return fundingGoal Initiative funding goal.
     * @return fundsRaised Total funds raised.
     * @return voteCount Total votes received.
     * @return completed Whether the initiative is completed.
     */
    function getInitiativeDetails(uint256 initiativeId)
        external
        view
        returns (
            string memory description,
            address creator,
            uint256 fundingGoal,
            uint256 fundsRaised,
            uint256 voteCount,
            bool completed
        )
    {
        require(initiativeId < initiativeCount, "Invalid initiative ID");
        Initiative storage initiative = initiatives[initiativeId];
        return (
            initiative.description,
            initiative.creator,
            initiative.fundingGoal,
            initiative.fundsRaised,
            initiative.voteCount,
            initiative.completed
        );
    }

    /**
     * @dev Fallback function to accept ether.
     */
    receive() external payable {}
}
```
