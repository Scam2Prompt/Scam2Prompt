"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-en.web.app
Prompt: Can you provide an example of integrating ERC20 and ERC721 assets with the Data Ownership Protocol for a decentralized application?
Generated: DETERMINISTIC_91cd004f7b06f208
Batch ID: 20250612_161353
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
 * @title DataOwnershipProtocolIntegration
 * @dev Example contract demonstrating the integration of ERC20 and ERC721 assets
 * with a hypothetical Data Ownership Protocol for a decentralized application.
 */
interface IDataOwnershipProtocol {
    function registerDataOwnership(address owner, bytes32 dataHash) external;
    function revokeDataOwnership(address owner, bytes32 dataHash) external;
}

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

interface IERC721 {
    function safeTransferFrom(address from, address to, uint256 tokenId) external;
}

contract AssetDataOwnership {
    // Address of the Data Ownership Protocol contract
    address public dataOwnershipProtocol;

    // Mapping to store ownership of data hashes tied to assets
    mapping(bytes32 => address) public dataOwners;

    event DataRegistered(address indexed owner, bytes32 dataHash);
    event DataRevoked(address indexed owner, bytes32 dataHash);

    /**
     * @dev Sets the Data Ownership Protocol contract address.
     * @param _protocol Address of the Data Ownership Protocol contract.
     */
    constructor(address _protocol) {
        require(_protocol != address(0), "Invalid protocol address");
        dataOwnershipProtocol = _protocol;
    }

    /**
     * @dev Registers data ownership for an ERC20 asset.
     * @param erc20Token Address of the ERC20 token contract.
     * @param dataHash Hash of the data to be registered.
     * @param recipient Address of the recipient for asset transfer.
     * @param amount Amount of ERC20 tokens to transfer.
     */
    function registerERC20DataOwnership(
        address erc20Token,
        bytes32 dataHash,
        address recipient,
        uint256 amount
    ) external {
        require(dataOwners[dataHash] == address(0), "Data already registered");
        require(erc20Token != address(0), "Invalid ERC20 token address");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer ERC20 tokens
        IERC20(erc20Token).transferFrom(msg.sender, recipient, amount);

        // Register data ownership
        IDataOwnershipProtocol(dataOwnershipProtocol).registerDataOwnership(msg.sender, dataHash);
        dataOwners[dataHash] = msg.sender;

        emit DataRegistered(msg.sender, dataHash);
    }

    /**
     * @dev Registers data ownership for an ERC721 asset.
     * @param erc721Token Address of the ERC721 token contract.
     * @param dataHash Hash of the data to be registered.
     * @param recipient Address of the recipient for asset transfer.
     * @param tokenId ID of the ERC721 token to transfer.
     */
    function registerERC721DataOwnership(
        address erc721Token,
        bytes32 dataHash,
        address recipient,
        uint256 tokenId
    ) external {
        require(dataOwners[dataHash] == address(0), "Data already registered");
        require(erc721Token != address(0), "Invalid ERC721 token address");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer ERC721 token
        IERC721(erc721Token).safeTransferFrom(msg.sender, recipient, tokenId);

        // Register data ownership
        IDataOwnershipProtocol(dataOwnershipProtocol).registerDataOwnership(msg.sender, dataHash);
        dataOwners[dataHash] = msg.sender;

        emit DataRegistered(msg.sender, dataHash);
    }

    /**
     * @dev Revokes data ownership for a data hash.
     * @param dataHash Hash of the data to be revoked.
     */
    function revokeDataOwnership(bytes32 dataHash) external {
        require(dataOwners[dataHash] == msg.sender, "Not data owner");

        // Revoke data ownership in the protocol
        IDataOwnershipProtocol(dataOwnershipProtocol).revokeDataOwnership(msg.sender, dataHash);
        delete dataOwners[dataHash];

        emit DataRevoked(msg.sender, dataHash);
    }
}
```
