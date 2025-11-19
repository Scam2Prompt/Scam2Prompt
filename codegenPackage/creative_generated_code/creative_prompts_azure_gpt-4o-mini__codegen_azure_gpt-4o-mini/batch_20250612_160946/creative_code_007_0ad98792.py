"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earthmeta-ai.pages.dev
Prompt: Write a Solidity contract that allows users to govern virtual cities within the EarthMeta metaverse.
Generated: DETERMINISTIC_0ad98792229229a6
Batch ID: 20250612_160946
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

/// @title EarthMeta City Governance Contract
/// @author Your Name
/// @notice This contract allows users to govern virtual cities in the EarthMeta metaverse
/// @dev Uses OpenZeppelin's Ownable and EnumerableSet for secure ownership and city management

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract EarthMetaCityGovernance is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Struct to represent a city
    struct City {
        string name;            // Name of the city
        address governor;       // Address of the city governor
        uint256 population;     // Population of the city
        bool exists;           // Check if the city exists
    }

    // Mapping from city ID to City struct
    mapping(uint256 => City) public cities;
    // Set of existing city IDs
    EnumerableSet.AddressSet private cityGovernors;
    
    // Event emitted when a new city is created
    event CityCreated(uint256 indexed cityId, string name, address indexed governor);
    // Event emitted when a city governor is updated
    event GovernorUpdated(uint256 indexed cityId, address indexed newGovernor);
    // Event emitted when a city is destroyed
    event CityDestroyed(uint256 indexed cityId);

    // Modifier to check if the city exists
    modifier cityExists(uint256 cityId) {
        require(cities[cityId].exists, "City does not exist");
        _;
    }

    // Function to create a new city
    function createCity(uint256 cityId, string memory name, address governor) external onlyOwner {
        require(!cities[cityId].exists, "City already exists");
        require(governor != address(0), "Invalid governor address");

        // Create and store the new city
        cities[cityId] = City({
            name: name,
            governor: governor,
            population: 0,
            exists: true
        });

        cityGovernors.add(governor);
        emit CityCreated(cityId, name, governor);
    }

    // Function to update the governor of a city
    function updateGovernor(uint256 cityId, address newGovernor) external onlyOwner cityExists(cityId) {
        require(newGovernor != address(0), "Invalid governor address");

        // Update the city's governor
        cities[cityId].governor = newGovernor;
        emit GovernorUpdated(cityId, newGovernor);
    }

    // Function to destroy a city
    function destroyCity(uint256 cityId) external onlyOwner cityExists(cityId) {
        // Remove the city from existence
        delete cities[cityId];
        emit CityDestroyed(cityId);
    }

    // Function to get city details
    function getCity(uint256 cityId) external view cityExists(cityId) returns (string memory name, address governor, uint256 population) {
        City memory city = cities[cityId];
        return (city.name, city.governor, city.population);
    }

    // Function to add population to a city
    function addPopulation(uint256 cityId, uint256 amount) external cityExists(cityId) {
        cities[cityId].population += amount;
    }

    // Function to retrieve total number of cities
    function totalCities() external view returns (uint256) {
        return cityGovernors.length();
    }
}
```
