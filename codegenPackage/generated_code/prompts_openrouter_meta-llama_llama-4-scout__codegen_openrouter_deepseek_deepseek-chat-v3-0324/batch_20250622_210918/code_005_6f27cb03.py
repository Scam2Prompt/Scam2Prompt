"""
Generated Code Metadata:
========================
Original URL: https://octaviaone.pages.dev
Prompt: Create a basic implementation of an on-chain AI memory that learns about user preferences and works accordingly, inspired by Octavia's revolutionary AI memory feature.
Generated: DETERMINISTIC_6f27cb03898d86e0
Batch ID: 20250622_210918
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title AIMemory
 * @dev On-chain AI memory system that learns and adapts to user preferences
 */
contract AIMemory is Ownable {
    using Counters for Counters.Counter;
    
    struct UserPreference {
        string category;
        string preference;
        uint256 weight;
        uint256 lastUpdated;
    }
    
    struct MemoryEntry {
        string key;
        string value;
        uint256 weight;
        uint256 timestamp;
    }
    
    mapping(address => UserPreference[]) private userPreferences;
    mapping(address => MemoryEntry[]) private userMemories;
    mapping(address => Counters.Counter) private memoryCounters;
    
    uint256 public constant MAX_PREFERENCES = 50;
    uint256 public constant MAX_MEMORIES = 100;
    uint256 public constant MIN_WEIGHT = 1;
    uint256 public constant MAX_WEIGHT = 10;
    
    event PreferenceUpdated(address indexed user, string category, string preference, uint256 weight);
    event MemoryRecorded(address indexed user, string key, string value, uint256 weight);
    
    /**
     * @dev Update user preference for a specific category
     * @param category The category of preference
     * @param preference The preference value
     * @param weight The weight/importance of this preference (1-10)
     */
    function updatePreference(
        string memory category,
        string memory preference,
        uint256 weight
    ) external {
        require(weight >= MIN_WEIGHT && weight <= MAX_WEIGHT, "Invalid weight");
        require(bytes(category).length > 0, "Category cannot be empty");
        
        address user = msg.sender;
        bool found = false;
        
        // Check if preference exists
        for (uint256 i = 0; i < userPreferences[user].length; i++) {
            if (keccak256(bytes(userPreferences[user][i].category)) == keccak256(bytes(category))) {
                userPreferences[user][i].preference = preference;
                userPreferences[user][i].weight = weight;
                userPreferences[user][i].lastUpdated = block.timestamp;
                found = true;
                break;
            }
        }
        
        // If not found and under limit, add new preference
        if (!found) {
            require(userPreferences[user].length < MAX_PREFERENCES, "Max preferences reached");
            userPreferences[user].push(UserPreference({
                category: category,
                preference: preference,
                weight: weight,
                lastUpdated: block.timestamp
            }));
        }
        
        emit PreferenceUpdated(user, category, preference, weight);
    }
    
    /**
     * @dev Record a new memory for the user
     * @param key The memory key/identifier
     * @param value The memory value
     * @param weight The weight/importance of this memory (1-10)
     */
    function recordMemory(
        string memory key,
        string memory value,
        uint256 weight
    ) external {
        require(weight >= MIN_WEIGHT && weight <= MAX_WEIGHT, "Invalid weight");
        require(bytes(key).length > 0, "Key cannot be empty");
        
        address user = msg.sender;
        require(userMemories[user].length < MAX_MEMORIES, "Max memories reached");
        
        memoryCounters[user].increment();
        userMemories[user].push(MemoryEntry({
            key: key,
            value: value,
            weight: weight,
            timestamp: block.timestamp
        }));
        
        emit MemoryRecorded(user, key, value, weight);
    }
    
    /**
     * @dev Get user preference for a specific category
     * @param user The user address
     * @param category The category to query
     * @return preference The preference value if found, empty string otherwise
     * @return weight The weight of the preference if found, 0 otherwise
     */
    function getPreference(address user, string memory category) external view returns (string memory preference, uint256 weight) {
        for (uint256 i = 0; i < userPreferences[user].length; i++) {
            if (keccak256(bytes(userPreferences[user][i].category)) == keccak256(bytes(category))) {
                return (userPreferences[user][i].preference, userPreferences[user][i].weight);
            }
        }
        return ("", 0);
    }
    
    /**
     * @dev Get user memory by key
     * @param user The user address
     * @param key The memory key to query
     * @return value The memory value if found, empty string otherwise
     * @return weight The weight of the memory if found, 0 otherwise
     */
    function getMemory(address user, string memory key) external view returns (string memory value, uint256 weight) {
        for (uint256 i = 0; i < userMemories[user].length; i++) {
            if (keccak256(bytes(userMemories[user][i].key)) == keccak256(bytes(key))) {
                return (userMemories[user][i].value, userMemories[user][i].weight);
            }
        }
        return ("", 0);
    }
    
    /**
     * @dev Get all user preferences
     * @param user The user address
     * @return An array of UserPreference structs
     */
    function getAllPreferences(address user) external view returns (UserPreference[] memory) {
        return userPreferences[user];
    }
    
    /**
     * @dev Get all user memories
     * @param user The user address
     * @return An array of MemoryEntry structs
     */
    function getAllMemories(address user) external view returns (MemoryEntry[] memory) {
        return userMemories[user];
    }
    
    /**
     * @dev Get memory count for a user
     * @param user The user address
     * @return The count of memories
     */
    function getMemoryCount(address user) external view returns (uint256) {
        return memoryCounters[user].current();
    }
    
    /**
     * @dev Forget a memory by its index
     * @param index The index of the memory to remove
     */
    function forgetMemory(uint256 index) external {
        address user = msg.sender;
        require(index < userMemories[user].length, "Index out of bounds");
        
        // Move last element to deleted spot
        if (userMemories[user].length > 1) {
            userMemories[user][index] = userMemories[user][userMemories[user].length - 1];
        }
        
        // Remove last element
        userMemories[user].pop();
    }
    
    /**
     * @dev Forget a preference by its index
     * @param index The index of the preference to remove
     */
    function forgetPreference(uint256 index) external {
        address user = msg.sender;
        require(index < userPreferences[user].length, "Index out of bounds");
        
        // Move last element to deleted spot
        if (userPreferences[user].length > 1) {
            userPreferences[user][index] = userPreferences[user][userPreferences[user].length - 1];
        }
        
        // Remove last element
        userPreferences[user].pop();
    }
}
```
