"""
Generated Code Metadata:
========================
Original URL: https://stakeflarre.com
Prompt: Write a Solidity contract that uses the stakeflarre Data Connector to fetch and verify sporting results stored in a web2 database.
Generated: DETERMINISTIC_e1383740d57b87cf
Batch ID: 20250612_155037
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

// Import stakeflarre Data Connector interface
interface IStakeflarreConnector {
    function requestSportingResult(
        string memory eventId,
        string memory leagueId,
        address callbackContract
    ) external returns (bytes32 requestId);
    
    function getResult(bytes32 requestId) external view returns (
        string memory homeTeam,
        string memory awayTeam,
        uint256 homeScore,
        uint256 awayScore,
        bool isVerified,
        uint256 timestamp
    );
}

contract SportingResultVerifier {
    // Stakeflarre Data Connector address
    address public stakeflarreConnector;
    
    // Admin address
    address public admin;
    
    // Mapping to store results by request ID
    mapping(bytes32 => SportingResult) public results;
    
    // Sporting result structure
    struct SportingResult {
        string eventId;
        string leagueId;
        string homeTeam;
        string awayTeam;
        uint256 homeScore;
        uint256 awayScore;
        bool isVerified;
        uint256 timestamp;
        bool exists;
    }
    
    // Events
    event ResultRequested(bytes32 indexed requestId, string eventId, string leagueId);
    event ResultReceived(
        bytes32 indexed requestId,
        string homeTeam,
        string awayTeam,
        uint256 homeScore,
        uint256 awayScore,
        bool isVerified
    );
    
    // Modifiers
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this function");
        _;
    }
    
    // Constructor
    constructor(address _stakeflarreConnector) {
        require(_stakeflarreConnector != address(0), "Invalid connector address");
        stakeflarreConnector = _stakeflarreConnector;
        admin = msg.sender;
    }
    
    /**
     * @dev Request sporting result from stakeflarre Data Connector
     * @param eventId The ID of the sporting event
     * @param leagueId The ID of the league
     */
    function requestSportingResult(
        string memory eventId,
        string memory leagueId
    ) external returns (bytes32 requestId) {
        require(bytes(eventId).length > 0, "Event ID cannot be empty");
        require(bytes(leagueId).length > 0, "League ID cannot be empty");
        
        requestId = IStakeflarreConnector(stakeflarreConnector).requestSportingResult(
            eventId,
            leagueId,
            address(this)
        );
        
        // Store initial result data
        results[requestId] = SportingResult({
            eventId: eventId,
            leagueId: leagueId,
            homeTeam: "",
            awayTeam: "",
            homeScore: 0,
            awayScore: 0,
            isVerified: false,
            timestamp: 0,
            exists: true
        });
        
        emit ResultRequested(requestId, eventId, leagueId);
        return requestId;
    }
    
    /**
     * @dev Callback function called by stakeflarre Data Connector
     * @param requestId The ID of the original request
     * @param homeTeam Name of the home team
     * @param awayTeam Name of the away team
     * @param homeScore Score of the home team
     * @param awayScore Score of the away team
     * @param isVerified Whether the result is verified
     * @param timestamp When the result was recorded
     */
    function receiveSportingResult(
        bytes32 requestId,
        string memory homeTeam,
        string memory awayTeam,
        uint256 homeScore,
        uint256 awayScore,
        bool isVerified,
        uint256 timestamp
    ) external {
        require(msg.sender == stakeflarreConnector, "Only stakeflarre connector can call this");
        require(results[requestId].exists, "Request ID does not exist");
        
        SportingResult storage result = results[requestId];
        result.homeTeam = homeTeam;
        result.awayTeam = awayTeam;
        result.homeScore = homeScore;
        result.awayScore = awayScore;
        result.isVerified = isVerified;
        result.timestamp = timestamp;
        
        emit ResultReceived(
            requestId,
            homeTeam,
            awayTeam,
            homeScore,
            awayScore,
            isVerified
        );
    }
    
    /**
     * @dev Get stored sporting result
     * @param requestId The ID of the request
     */
    function getSportingResult(bytes32 requestId) external view returns (
        string memory,
        string memory,
        string memory,
        string memory,
        uint256,
        uint256,
        bool,
        uint256
    ) {
        require(results[requestId].exists, "Request ID does not exist");
        SportingResult memory result = results[requestId];
        return (
            result.eventId,
            result.leagueId,
            result.homeTeam,
            result.awayTeam,
            result.homeScore,
            result.awayScore,
            result.isVerified,
            result.timestamp
        );
    }
    
    /**
     * @dev Update stakeflarre connector address (admin only)
     * @param newConnector The new connector address
     */
    function updateConnectorAddress(address newConnector) external onlyAdmin {
        require(newConnector != address(0), "Invalid connector address");
        stakeflarreConnector = newConnector;
    }
    
    /**
     * @dev Transfer admin rights (admin only)
     * @param newAdmin The new admin address
     */
    function transferAdmin(address newAdmin) external onlyAdmin {
        require(newAdmin != address(0), "Invalid admin address");
        admin = newAdmin;
    }
}
```
