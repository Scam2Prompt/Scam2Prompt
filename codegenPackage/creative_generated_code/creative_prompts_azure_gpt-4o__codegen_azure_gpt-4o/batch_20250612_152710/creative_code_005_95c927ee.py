"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phi-f1z.pages.dev
Prompt: Develop a smart contract that interacts with Phi Protocol to allow users to mint personalized credentials and store them onchain.
Generated: DETERMINISTIC_95c927ee9a08aa74
Batch ID: 20250612_152710
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
 * @title PhiProtocolCredentialMinter
 * @dev This smart contract interacts with the Phi Protocol to allow users to mint
 * personalized credentials and store them on-chain.
 */
interface IPhiProtocol {
    function mintCredential(address to, string calldata credentialData) external returns (uint256);
}

contract PhiProtocolCredentialMinter {
    // Address of the Phi Protocol contract
    address public phiProtocolAddress;

    // Mapping to track credentials minted by each user
    mapping(address => uint256[]) public userCredentials;

    event CredentialMinted(address indexed user, uint256 credentialId, string credentialData);

    /**
     * @dev Sets the Phi Protocol contract address.
     * @param _phiProtocolAddress Address of the Phi Protocol contract.
     */
    constructor(address _phiProtocolAddress) {
        require(_phiProtocolAddress != address(0), "Invalid Phi Protocol address");
        phiProtocolAddress = _phiProtocolAddress;
    }

    /**
     * @dev Mints a personalized credential for the caller and stores it on-chain.
     * @param credentialData The data of the credential to be minted.
     */
    function mintCredential(string calldata credentialData) external {
        require(bytes(credentialData).length > 0, "Credential data cannot be empty");

        IPhiProtocol phiProtocol = IPhiProtocol(phiProtocolAddress);

        // Attempt to mint the credential
        try phiProtocol.mintCredential(msg.sender, credentialData) returns (uint256 credentialId) {
            // Store the minted credential ID for the user
            userCredentials[msg.sender].push(credentialId);

            emit CredentialMinted(msg.sender, credentialId, credentialData);
        } catch (bytes memory error) {
            revert(string(abi.encodePacked("Failed to mint credential: ", error)));
        }
    }

    /**
     * @dev Fetches the list of credential IDs minted by a specific user.
     * @param user Address of the user whose credentials are being queried.
     * @return An array of credential IDs.
     */
    function getUserCredentials(address user) external view returns (uint256[] memory) {
        return userCredentials[user];
    }
}
```
