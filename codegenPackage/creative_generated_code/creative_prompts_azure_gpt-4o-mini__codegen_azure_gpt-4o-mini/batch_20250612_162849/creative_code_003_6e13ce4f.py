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

// Interface for interacting with ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

// Contract for managing community-led initiatives
contract CommunityInitiative {

    // State variables
    address public owner; // Owner of the contract
    IERC20 public token; // ERC20 token used for voting and initiatives
    uint256 public initiativeCount; // Count of initiatives
    mapping(uint256 => Initiative) public initiatives; // Mapping to track initiatives by ID

    // Structure to define an Initiative
    struct Initiative {
        uint256 id; // Initiative ID
        string description; // Description of the initiative
        address creator; // Address of the initiative creator
        uint256 votesFor; // Votes in favor
        uint256 votesAgainst; // Votes against
        bool executed; // Track if the initiative has been executed
    }

    // Events for logging
    event InitiativeCreated(uint256 id, string description, address creator);
    event Voted(uint256 initiativeId, address voter, bool support);
    event InitiativeExecuted(uint256 id);

    // Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor(address tokenAddress) {
        owner = msg.sender;
        token = IERC20(tokenAddress);
    }

    // Create a new initiative
    function createInitiative(string memory description) external {
        initiativeCount++;
        initiatives[initiativeCount] = Initiative(initiativeCount, description, msg.sender, 0, 0, false);
        emit InitiativeCreated(initiativeCount, description, msg.sender);
    }

    // Vote on an initiative
    function vote(uint256 initiativeId, bool support) external {
        Initiative storage initiative = initiatives[initiativeId];

        require(initiative.id != 0, "Initiative does not exist");
        require(!initiative.executed, "Initiative already executed");

        // Ensure that only token holders can vote
        require(token.balanceOf(msg.sender) > 0, "Must hold tokens to vote");

        if (support) {
            initiative.votesFor++;
        } else {
            initiative.votesAgainst++;
        }

        emit Voted(initiativeId, msg.sender, support);
    }

    // Execute an initiative if the votes are sufficient
    function executeInitiative(uint256 initiativeId) external {
        Initiative storage initiative = initiatives[initiativeId];

        require(initiative.id != 0, "Initiative does not exist");
        require(!initiative.executed, "Initiative already executed");

        // Ensure that the initiative has more votes for than against
        require(initiative.votesFor > initiative.votesAgainst, "Not enough votes for execution");

        initiative.executed = true;

        // Logic for executing the initiative can be added here
        // ...

        emit InitiativeExecuted(initiativeId);
    }

    // Function to withdraw ERC20 tokens (if required)
    function withdrawTokens(address recipient, uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        token.transfer(recipient, amount);
    }
}
```
