"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-dao-hubbbbb.vercel.app
Prompt: Generate code for integrating the Ethereum Attestation Service (EAS) into a Web3 gaming application built on Arbitrum Arcade.
Generated: DETERMINISTIC_d5e4ca2cf9b9a754
Batch ID: 20250612_150342
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
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@ethereum-attestation-service/eas-contracts/contracts/IEAS.sol";
import "@ethereum-attestation-service/eas-contracts/contracts/Attestation.sol";

contract GameAttestation is Ownable {
    using ECDSA for bytes32;

    // EAS contract interface
    IEAS public eas;

    // Game-specific attestation schema UID
    bytes32 public gameSchemaUID;

    // Mapping to track attested players
    mapping(address => bool) public attestedPlayers;

    // Events
    event PlayerAttested(address indexed player, bytes32 attestationUID);
    event SchemaRegistered(bytes32 schemaUID);
    event EASContractUpdated(address newEAS);

    /**
     * @dev Constructor to initialize the EAS contract and register schema
     * @param _easAddress Address of the EAS contract
     * @param _schema The schema definition for game attestations
     * @param _resolverAddress Optional resolver address
     */
    constructor(
        address _easAddress,
        string memory _schema,
        address _resolverAddress
    ) {
        require(_easAddress != address(0), "Invalid EAS address");
        eas = IEAS(_easAddress);

        // Register the game attestation schema
        gameSchemaUID = registerSchema(_schema, _resolverAddress);
        emit SchemaRegistered(gameSchemaUID);
    }

    /**
     * @dev Registers a new schema with EAS
     * @param schema The schema definition string
     * @param resolverAddress Optional resolver address
     * @return The UID of the registered schema
     */
    function registerSchema(
        string memory schema,
        address resolverAddress
    ) internal returns (bytes32) {
        return eas.register(schema, ISchemaResolver(resolverAddress));
    }

    /**
     * @dev Updates the EAS contract address (owner only)
     * @param _newEAS Address of the new EAS contract
     */
    function updateEASContract(address _newEAS) external onlyOwner {
        require(_newEAS != address(0), "Invalid EAS address");
        eas = IEAS(_newEAS);
        emit EASContractUpdated(_newEAS);
    }

    /**
     * @dev Creates an attestation for a player
     * @param player The address of the player to attest
     * @param expirationTime Unix timestamp when attestation expires (0 for no expiration)
     * @param revocable Whether the attestation is revocable
     * @param data Additional attestation data
     * @return The UID of the created attestation
     */
    function attestPlayer(
        address player,
        uint64 expirationTime,
        bool revocable,
        bytes memory data
    ) external onlyOwner returns (bytes32) {
        require(player != address(0), "Invalid player address");
        require(!attestedPlayers[player], "Player already attested");

        AttestationRequest memory request = AttestationRequest({
            schema: gameSchemaUID,
            data: AttestationRequestData({
                recipient: player,
                expirationTime: expirationTime,
                revocable: revocable,
                refUID: bytes32(0),
                data: data,
                value: 0
            })
        });

        bytes32 attestationUID = eas.attest(request);
        attestedPlayers[player] = true;

        emit PlayerAttested(player, attestationUID);
        return attestationUID;
    }

    /**
     * @dev Revokes an attestation for a player
     * @param attestationUID The UID of the attestation to revoke
     */
    function revokeAttestation(bytes32 attestationUID) external onlyOwner {
        eas.revoke(attestationUID);
    }

    /**
     * @dev Checks if a player has a valid attestation
     * @param player The address of the player to check
     * @return True if the player has a valid attestation
     */
    function isPlayerAttested(address player) external view returns (bool) {
        return attestedPlayers[player];
    }

    /**
     * @dev Verifies an off-chain attestation signature
     * @param player The address of the attested player
     * @param attestationUID The UID of the attestation
     * @param signature The signature to verify
     * @return True if the signature is valid
     */
    function verifyAttestationSignature(
        address player,
        bytes32 attestationUID,
        bytes memory signature
    ) external view returns (bool) {
        bytes32 messageHash = keccak256(abi.encodePacked(player, attestationUID));
        bytes32 ethSignedMessageHash = messageHash.toEthSignedMessageHash();
        address signer = ethSignedMessageHash.recover(signature);
        return signer == owner();
    }
}
```

```javascript
// frontend/gameAttestation.js
import { ethers } from 'ethers';
import GameAttestationABI from './artifacts/GameAttestation.json';

export class GameAttestationService {
  constructor(provider, contractAddress) {
    this.provider = provider;
    this.contract = new ethers.Contract(
      contractAddress,
      GameAttestationABI.abi,
      provider.getSigner()
    );
  }

  /**
   * Checks if a player is attested
   * @param {string} playerAddress 
   * @returns {Promise<boolean>}
   */
  async isPlayerAttested(playerAddress) {
    try {
      return await this.contract.isPlayerAttested(playerAddress);
    } catch (error) {
      console.error('Error checking player attestation:', error);
      throw error;
    }
  }

  /**
   * Requests player attestation (called by game admin)
   * @param {string} playerAddress 
   * @param {number} expirationTime 
   * @param {boolean} revocable 
   * @param {string} additionalData 
   * @returns {Promise<string>} attestation UID
   */
  async requestPlayerAttestation(playerAddress, expirationTime = 0, revocable = true, additionalData = '') {
    try {
      const tx = await this.contract.attestPlayer(
        playerAddress,
        expirationTime,
        revocable,
        ethers.utils.toUtf8Bytes(additionalData)
      );
      await tx.wait();
      return tx.hash;
    } catch (error) {
      console.error('Error requesting player attestation:', error);
      throw error;
    }
  }

  /**
   * Verifies an off-chain attestation signature
   * @param {string} playerAddress 
   * @param {string} attestationUID 
   * @param {string} signature 
   * @returns {Promise<boolean>}
   */
  async verifyAttestationSignature(playerAddress, attestationUID, signature) {
    try {
      return await this.contract.verifyAttestationSignature(
        playerAddress,
        attestationUID,
        signature
      );
    } catch (error) {
      console.error('Error verifying attestation signature:', error);
      throw error;
    }
  }

  /**
   * Gets the game schema UID
   * @returns {Promise<string>}
   */
  async getGameSchemaUID() {
    try {
      return await this.contract.gameSchemaUID();
    } catch (error) {
      console.error('Error getting game schema UID:', error);
      throw error;
    }
  }
}
```

```javascript
// frontend/useGameAttestation.js
import { useEffect, useState } from 'react';
import { GameAttestationService } from './gameAttestation';

export function useGameAttestation(provider, contractAddress) {
  const [attestationService, setAttestationService] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (provider && contractAddress) {
      setAttestationService(new GameAttestationService(provider, contractAddress));
    }
  }, [provider, contractAddress]);

  const checkAttestation = async (playerAddress) => {
    setIsLoading(true);
    setError(null);
    try {
      const isAttested = await attestationService.isPlayerAttested(playerAddress);
      setIsLoading(false);
      return isAttested;
    } catch (err) {
      setError(err);
      setIsLoading(false);
      throw err;
    }
  };

  const requestAttestation = async (playerAddress, expirationTime, revocable, additionalData) => {
    setIsLoading(true);
    setError(null);
    try {
      const txHash = await attestationService.requestPlayerAttestation(
        playerAddress,
        expirationTime,
        revocable,
        additionalData
      );
      setIsLoading(false);
      return txHash;
    } catch (err) {
      setError(err);
      setIsLoading(false);
      throw err;
    }
  };

  return {
    attestationService,
    checkAttestation,
