"""
Generated Code Metadata:
========================
Original URL: https://a292d5c1.docs-62t.pages.dev
Prompt: Generate a smart contract client library in TypeScript using Código's platform for a decentralized application that enables transparent asset tracking. Include web-based documentation generation.
Generated: DETERMINISTIC_ef15b00f76241e28
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title AssetTracker
 * @dev A smart contract for transparent asset tracking on the blockchain
 */
contract AssetTracker {
    struct Asset {
        string id;
        string name;
        string description;
        address owner;
        uint256 timestamp;
        string location;
        string metadata;
    }

    mapping(string => Asset) private assets;
    string[] private assetIds;

    event AssetRegistered(
        string indexed id,
        string name,
        address owner,
        uint256 timestamp
    );
    event AssetTransferred(
        string indexed id,
        address indexed from,
        address indexed to,
        uint256 timestamp
    );
    event AssetUpdated(
        string indexed id,
        string location,
        string metadata,
        uint256 timestamp
    );

    /**
     * @dev Register a new asset
     * @param _id Unique identifier for the asset
     * @param _name Name of the asset
     * @param _description Description of the asset
     * @param _location Current location of the asset
     * @param _metadata Additional metadata about the asset
     */
    function registerAsset(
        string memory _id,
        string memory _name,
        string memory _description,
        string memory _location,
        string memory _metadata
    ) public {
        require(bytes(_id).length > 0, "Asset ID cannot be empty");
        require(bytes(assets[_id].id).length == 0, "Asset already exists");

        Asset memory newAsset = Asset({
            id: _id,
            name: _name,
            description: _description,
            owner: msg.sender,
            timestamp: block.timestamp,
            location: _location,
            metadata: _metadata
        });

        assets[_id] = newAsset;
        assetIds.push(_id);

        emit AssetRegistered(_id, _name, msg.sender, block.timestamp);
    }

    /**
     * @dev Transfer ownership of an asset
     * @param _id Asset ID to transfer
     * @param _newOwner Address of the new owner
     */
    function transferAsset(string memory _id, address _newOwner) public {
        require(bytes(_id).length > 0, "Asset ID cannot be empty");
        require(assets[_id].owner == msg.sender, "Only owner can transfer asset");
        require(_newOwner != address(0), "Invalid new owner address");

        assets[_id].owner = _newOwner;
        assets[_id].timestamp = block.timestamp;

        emit AssetTransferred(_id, msg.sender, _newOwner, block.timestamp);
    }

    /**
     * @dev Update asset information
     * @param _id Asset ID to update
     * @param _location New location of the asset
     * @param _metadata Updated metadata about the asset
     */
    function updateAsset(
        string memory _id,
        string memory _location,
        string memory _metadata
    ) public {
        require(bytes(_id).length > 0, "Asset ID cannot be empty");
        require(assets[_id].owner == msg.sender, "Only owner can update asset");

        assets[_id].location = _location;
        assets[_id].metadata = _metadata;
        assets[_id].timestamp = block.timestamp;

        emit AssetUpdated(_id, _location, _metadata, block.timestamp);
    }

    /**
     * @dev Get asset details by ID
     * @param _id Asset ID to query
     * @return Asset details
     */
    function getAsset(string memory _id) public view returns (Asset memory) {
        require(bytes(_id).length > 0, "Asset ID cannot be empty");
        return assets[_id];
    }

    /**
     * @dev Get all asset IDs
     * @return Array of all asset IDs
     */
    function getAllAssetIds() public view returns (string[] memory) {
        return assetIds;
    }

    /**
     * @dev Get asset count
     * @return Total number of assets registered
     */
    function getAssetCount() public view returns (uint256) {
        return assetIds.length;
    }
}
```

```typescript
// asset-tracker-client.ts
import { ethers } from 'ethers';
import { TypedDataDomain, TypedDataField } from '@ethersproject/abstract-signer';

/**
 * Asset Tracker Client Library
 * A TypeScript client for interacting with the AssetTracker smart contract
 */
export class AssetTrackerClient {
    private contract: ethers.Contract;
    private provider: ethers.providers.Provider;
    private signer?: ethers.Signer;

    /**
     * Initialize the AssetTrackerClient
     * @param contractAddress Address of the deployed AssetTracker contract
     * @param provider Ethereum provider (e.g., JsonRpcProvider, Web3Provider)
     * @param signer Optional signer for write operations
     */
    constructor(
        contractAddress: string,
        provider: ethers.providers.Provider,
        signer?: ethers.Signer
    ) {
        const abi = [
            // ABI definitions would be generated from the contract
            // Using simplified version for this example
            "function registerAsset(string,string,string,string,string)",
            "function transferAsset(string,address)",
            "function updateAsset(string,string,string)",
            "function getAsset(string) view returns (tuple(string id, string name, string description, address owner, uint256 timestamp, string location, string metadata))",
            "function getAllAssetIds() view returns (string[])",
            "function getAssetCount() view returns (uint256)",
            "event AssetRegistered(string indexed id, string name, address owner, uint256 timestamp)",
            "event AssetTransferred(string indexed id, address indexed from, address indexed to, uint256 timestamp)",
            "event AssetUpdated(string indexed id, string location, string metadata, uint256 timestamp)"
        ];

        this.provider = provider;
        this.signer = signer;
        this.contract = new ethers.Contract(
            contractAddress,
            abi,
            signer || provider
        );
    }

    /**
     * Register a new asset
     * @param id Unique identifier for the asset
     * @param name Name of the asset
     * @param description Description of the asset
     * @param location Current location of the asset
     * @param metadata Additional metadata about the asset
     * @returns Transaction receipt
     */
    async registerAsset(
        id: string,
        name: string,
        description: string,
        location: string,
        metadata: string
    ): Promise<ethers.ContractReceipt> {
        if (!this.signer) {
            throw new Error('Signer is required for write operations');
        }

        const tx = await this.contract.registerAsset(
            id,
            name,
            description,
            location,
            metadata
        );
        return await tx.wait();
    }

    /**
     * Transfer ownership of an asset
     * @param id Asset ID to transfer
     * @param newOwner Address of the new owner
     * @returns Transaction receipt
     */
    async transferAsset(
        id: string,
        newOwner: string
    ): Promise<ethers.ContractReceipt> {
        if (!this.signer) {
            throw new Error('Signer is required for write operations');
        }

        const tx = await this.contract.transferAsset(id, newOwner);
        return await tx.wait();
    }

    /**
     * Update asset information
     * @param id Asset ID to update
     * @param location New location of the asset
     * @param metadata Updated metadata about the asset
     * @returns Transaction receipt
     */
    async updateAsset(
        id: string,
        location: string,
        metadata: string
    ): Promise<ethers.ContractReceipt> {
        if (!this.signer) {
            throw new Error('Signer is required for write operations');
        }

        const tx = await this.contract.updateAsset(id, location, metadata);
        return await tx.wait();
    }

    /**
     * Get asset details by ID
     * @param id Asset ID to query
     * @returns Asset details
     */
    async getAsset(id: string): Promise<Asset> {
        return await this.contract.getAsset(id);
    }

    /**
     * Get all asset IDs
     * @returns Array of all asset IDs
     */
    async getAllAssetIds(): Promise<string[]> {
        return await this.contract.getAllAssetIds();
    }

    /**
     * Get asset count
     * @returns Total number of assets registered
     */
    async getAssetCount(): Promise<number> {
        const count = await this.contract.getAssetCount();
        return count.toNumber();
    }

    /**
     * Listen for AssetRegistered events
     * @param callback Function to call when event is emitted
     * @returns Function to unsubscribe
     */
    onAssetRegistered(
        callback: (id: string, name: string, owner: string, timestamp: number) => void
    ): () => void {
        const filter = this.contract.filters.AssetRegistered();
        this.contract.on(filter, (id, name, owner, timestamp, event) => {
            callback(id, name, owner, timestamp.toNumber());
        });

        return
