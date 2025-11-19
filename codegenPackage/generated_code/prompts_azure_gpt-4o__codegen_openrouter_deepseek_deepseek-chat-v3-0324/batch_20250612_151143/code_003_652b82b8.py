"""
Generated Code Metadata:
========================
Original URL: https://connecy.pages.dev
Prompt: Write a function to validate a Testnet Voyage NFT recipient's attestation, ensuring the recipient is Tier 1 to 4, as outlined in the Linea PoH requirements.
Generated: DETERMINISTIC_652b82b826a2deed
Batch ID: 20250612_151143
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
 * @title VoyageNFTAttestationValidator
 * @dev Validates Testnet Voyage NFT recipient attestations according to Linea PoH requirements
 */
contract VoyageNFTAttestationValidator {
    // Tier definitions as per Linea PoH requirements
    enum Tier {
        NOT_ELIGIBLE, // 0
        TIER_1,       // 1
        TIER_2,       // 2
        TIER_3,       // 3
        TIER_4        // 4
    }

    // Mapping to store verified attestations
    mapping(address => bool) private _verifiedAttestations;

    // Event emitted when an attestation is validated
    event AttestationValidated(address indexed recipient, Tier tier);

    // Error for invalid tier
    error InvalidTier(uint8 providedTier);

    /**
     * @dev Validates a recipient's attestation
     * @param recipient The address of the NFT recipient
     * @param tier The tier being claimed (must be 1-4)
     */
    function validateAttestation(address recipient, uint8 tier) external {
        // Convert tier to enum and validate
        Tier recipientTier = _validateTier(tier);

        // Mark attestation as verified
        _verifiedAttestations[recipient] = true;

        // Emit validation event
        emit AttestationValidated(recipient, recipientTier);
    }

    /**
     * @dev Internal function to validate the tier
     * @param tier The tier to validate
     * @return The validated Tier enum
     */
    function _validateTier(uint8 tier) internal pure returns (Tier) {
        if (tier < 1 || tier > 4) {
            revert InvalidTier(tier);
        }
        return Tier(tier);
    }

    /**
     * @dev Checks if an address has a verified attestation
     * @param recipient The address to check
     * @return True if the attestation is verified
     */
    function isVerified(address recipient) external view returns (bool) {
        return _verifiedAttestations[recipient];
    }

    /**
     * @dev Gets the maximum allowed tier (4)
     * @return The maximum tier value
     */
    function getMaxTier() external pure returns (uint8) {
        return uint8(Tier.TIER_4);
    }

    /**
     * @dev Gets the minimum allowed tier (1)
     * @return The minimum tier value
     */
    function getMinTier() external pure returns (uint8) {
        return uint8(Tier.TIER_1);
    }
}
```
