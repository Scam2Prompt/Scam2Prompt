"""
Generated Code Metadata:
========================
Original URL: https://moonbirds.pro
Prompt: Develop a blockchain-based smart contract that symbolizes Moonbird B95's resilience through "winter dumps and summer pumps," incorporating unique identifiers like "code B95."
Generated: DETERMINISTIC_45c8d2ee31166208
Batch ID: 20250612_151020
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

/**
 * @title MoonbirdB95
 * @dev A smart contract that symbolizes Moonbird B95's resilience through market cycles
 * with unique identifier "code B95" and tracks seasonal performance.
 */
contract MoonbirdB95 {
    // Struct to represent seasonal data
    struct Season {
        uint256 winterDump;   // Price decrease in winter
        uint256 summerPump;   // Price increase in summer
        uint256 timestamp;    // When the season was recorded
    }

    // Unique identifier for this contract
    string public constant CODE_B95 = "B95";
    
    // Owner of the contract
    address public owner;
    
    // Mapping of season index to Season data
    mapping(uint256 => Season) public seasons;
    
    // Current season count
    uint256 public seasonCount;
    
    // Events
    event SeasonRecorded(
        uint256 indexed seasonId,
        uint256 winterDump,
        uint256 summerPump,
        uint256 timestamp
    );
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict function access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "MoonbirdB95: caller is not the owner");
        _;
    }

    /**
     * @dev Constructor sets the initial owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Record a new season's performance
     * @param _winterDump The winter dump amount (price decrease)
     * @param _summerPump The summer pump amount (price increase)
     */
    function recordSeason(uint256 _winterDump, uint256 _summerPump) external onlyOwner {
        require(_winterDump > 0 && _summerPump > 0, "MoonbirdB95: values must be positive");
        
        uint256 currentSeason = seasonCount;
        seasons[currentSeason] = Season({
            winterDump: _winterDump,
            summerPump: _summerPump,
            timestamp: block.timestamp
        });
        
        seasonCount++;
        
        emit SeasonRecorded(currentSeason, _winterDump, _summerPump, block.timestamp);
    }

    /**
     * @dev Get season data by index
     * @param _seasonId The season index to query
     * @return winterDump, summerPump, timestamp
     */
    function getSeason(uint256 _seasonId) external view returns (uint256, uint256, uint256) {
        require(_seasonId < seasonCount, "MoonbirdB95: invalid season ID");
        Season memory season = seasons[_seasonId];
        return (season.winterDump, season.summerPump, season.timestamp);
    }

    /**
     * @dev Calculate resilience score (summerPump / winterDump ratio)
     * @param _seasonId The season index to calculate for
     * @return The resilience score
     */
    function calculateResilience(uint256 _seasonId) external view returns (uint256) {
        require(_seasonId < seasonCount, "MoonbirdB95: invalid season ID");
        Season memory season = seasons[_seasonId];
        return season.summerPump / season.winterDump;
    }

    /**
     * @dev Transfer ownership to new address
     * @param newOwner The address to transfer ownership to
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "MoonbirdB95: new owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Get contract identifier
     * @return The CODE_B95 constant
     */
    function getIdentifier() external pure returns (string memory) {
        return CODE_B95;
    }
}
```
