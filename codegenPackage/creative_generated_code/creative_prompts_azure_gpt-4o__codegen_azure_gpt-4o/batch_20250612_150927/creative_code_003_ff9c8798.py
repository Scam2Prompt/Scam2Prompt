"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9aa9e9cd.dapp-a9y.pages.dev
Prompt: Provide an example of how to use HatsFinance's tools to set up a smart contract audit competition in a blockchain environment.
Generated: DETERMINISTIC_ff9c8798f8b059ea
Batch ID: 20250612_150927
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
 * @title HatsFinanceAuditCompetition
 * @dev This contract demonstrates how to set up a smart contract audit competition
 * using HatsFinance's tools in a blockchain environment.
 */
contract HatsFinanceAuditCompetition {
    // Address of the HatsFinance registry
    address public immutable hatsRegistry;

    // Struct to represent an audit competition
    struct AuditCompetition {
        uint256 competitionId; // Unique ID for the competition
        string description; // Description of the competition (e.g., purpose, scope)
        uint256 startTime; // Start timestamp
        uint256 endTime; // End timestamp
        uint256 prizePool; // Total prize pool in wei
        address creator; // Address that created the competition
    }

    // Mapping of competition IDs to their details
    mapping(uint256 => AuditCompetition) public competitions;

    // Counter for competition IDs
    uint256 public nextCompetitionId;

    // Event emitted when a new competition is created
    event CompetitionCreated(
        uint256 indexed competitionId,
        string description,
        uint256 startTime,
        uint256 endTime,
        uint256 prizePool,
        address creator
    );

    // Modifier to ensure only HatsFinance registry can call certain functions
    modifier onlyRegistry() {
        require(msg.sender == hatsRegistry, "Caller is not the HatsFinance registry");
        _;
    }

    /**
     * @dev Constructor to initialize the HatsFinance registry address.
     * @param _hatsRegistry Address of the HatsFinance registry.
     */
    constructor(address _hatsRegistry) {
        require(_hatsRegistry != address(0), "HatsFinance registry address cannot be zero");
        hatsRegistry = _hatsRegistry;
    }

    /**
     * @dev Function to create a new audit competition.
     * @param _description Description of the audit competition.
     * @param _startTime Start timestamp for the competition.
     * @param _endTime End timestamp for the competition.
     * @param _prizePool Total prize pool in wei.
     */
    function createCompetition(
        string memory _description,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _prizePool
    ) external onlyRegistry {
        require(_startTime < _endTime, "Start time must be before end time");
        require(_prizePool > 0, "Prize pool must be greater than zero");

        // Increment competition ID counter
        uint256 competitionId = nextCompetitionId++;
        
        // Create and store the competition details
        competitions[competitionId] = AuditCompetition({
            competitionId: competitionId,
            description: _description,
            startTime: _startTime,
            endTime: _endTime,
            prizePool: _prizePool,
            creator: msg.sender
        });

        // Emit event for the creation of the competition
        emit CompetitionCreated(
            competitionId,
            _description,
            _startTime,
            _endTime,
            _prizePool,
            msg.sender
        );
    }

    /**
     * @dev Function to retrieve details of a specific competition.
     * @param _competitionId ID of the competition to retrieve.
     * @return An AuditCompetition struct containing competition details.
     */
    function getCompetition(uint256 _competitionId)
        external
        view
        returns (AuditCompetition memory)
    {
        require(_competitionId < nextCompetitionId, "Competition does not exist");
        return competitions[_competitionId];
    }

    /**
     * @dev Function to update prize pool for an existing competition.
     * @param _competitionId ID of the competition to update.
     * @param _newPrizePool New prize pool in wei.
     */
    function updatePrizePool(uint256 _competitionId, uint256 _newPrizePool) external onlyRegistry {
        require(_competitionId < nextCompetitionId, "Competition does not exist");
        require(_newPrizePool > 0, "Prize pool must be greater than zero");

        // Update prize pool
        competitions[_competitionId].prizePool = _newPrizePool;
    }
}
```
