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
 * @title IDORestrictedParticipation
 * @dev Smart contract to restrict participants from certain countries in an IDO.
 */
contract IDORestrictedParticipation {
    address public owner;
    mapping(string => bool) private restrictedCountries;

    event CountryRestricted(string country);
    event CountryUnrestricted(string country);
    event ParticipationRejected(address participant, string country);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add a country to the restricted list.
     * @param country The name of the country (e.g., "Bolivia").
     */
    function restrictCountry(string memory country) external onlyOwner {
        restrictedCountries[country] = true;
        emit CountryRestricted(country);
    }

    /**
     * @dev Remove a country from the restricted list.
     * @param country The name of the country (e.g., "Bolivia").
     */
    function unrestrictCountry(string memory country) external onlyOwner {
        restrictedCountries[country] = false;
        emit CountryUnrestricted(country);
    }

    /**
     * @dev Check if a country is restricted.
     * @param country The name of the country.
     * @return bool True if the country is restricted, false otherwise.
     */
    function isCountryRestricted(string memory country) public view returns (bool) {
        return restrictedCountries[country];
    }

    /**
     * @dev Validate participant eligibility based on country.
     * @param country The name of the participant's country.
     * @return bool True if the participant is eligible, false otherwise.
     */
    function validateParticipation(string memory country) public view returns (bool) {
        return !restrictedCountries[country];
    }

    /**
     * @dev Participate in the IDO if the participant's country is not restricted.
     * @param country The name of the participant's country.
     */
    function participate(string memory country) external {
        // Check if the country is restricted
        if (restrictedCountries[country]) {
            emit ParticipationRejected(msg.sender, country);
            revert("Participants from this country are restricted");
        }
        // Business logic for participation goes here (e.g., accepting funds, issuing tokens)
        // Example: emit a generic participation success event
        // emit ParticipationSuccessful(msg.sender);
    }
}
```
