"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drainertemp.pages.dev
Prompt: Generate code to exclude participants from restricted countries (e.g., Bolivia, Cambodia, etc.) in an IDO smart contract, as outlined in the Nanoledger documentation.
Generated: DETERMINISTIC_7e6145135b73a71a
Batch ID: 20250612_154151
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
 * @title IDO Smart Contract
 * @dev This contract manages the participation in the Initial DEX Offering (IDO)
 * and excludes participants from restricted countries.
 */
contract IDO {
    // List of restricted countries
    string[] private restrictedCountries = ["Bolivia", "Cambodia", "North Korea"];
    
    // Mapping from participant address to their country
    mapping(address => string) public participantCountries;

    // Event to log successful participation
    event Participation(address indexed participant, string country);

    /**
     * @dev Modifier to check if the participant is from a restricted country
     * @param _country The country of the participant
     */
    modifier notRestricted(string memory _country) {
        require(!isRestrictedCountry(_country), "Participant from restricted country");
        _;
    }

    /**
     * @dev Allows a participant to register for the IDO
     * @param _country The country of the participant
     */
    function registerForIDO(string memory _country) external notRestricted(_country) {
        // Store the participant's country
        participantCountries[msg.sender] = _country;

        // Emit participation event
        emit Participation(msg.sender, _country);
    }

    /**
     * @dev Check if a country is restricted
     * @param _country The country to check
     * @return bool True if the country is restricted, false otherwise
     */
    function isRestrictedCountry(string memory _country) internal view returns (bool) {
        for (uint256 i = 0; i < restrictedCountries.length; i++) {
            if (keccak256(abi.encodePacked(restrictedCountries[i])) == keccak256(abi.encodePacked(_country))) {
                return true;
            }
        }
        return false;
    }

    /**
     * @dev Get the list of restricted countries
     * @return string[] The array of restricted countries
     */
    function getRestrictedCountries() external view returns (string[] memory) {
        return restrictedCountries;
    }
}
```
