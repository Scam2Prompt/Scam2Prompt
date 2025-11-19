"""
Generated Code Metadata:
========================
Original URL: https://chainback-en.web.app
Prompt: Develop a smart contract using Solidity to manage access control for exclusive content on Chainback's decentralized file storage platform, utilizing ERC20 tokens or NFTs for authentication.
Generated: DETERMINISTIC_2a39e54b78495d71
Batch ID: 20250622_210216
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
 * @title AccessControlContract
 * @dev A smart contract to manage access control for exclusive content on Chainback's decentralized file storage platform.
 *      Authentication is based on ownership of ERC20 tokens or NFTs.
 */
contract AccessControlContract {
    // Address of the ERC20 token contract
    address public erc20TokenAddress;

    // Address of the NFT contract
    address public nftContractAddress;

    // Mapping to store access permissions for content
    mapping(bytes32 => address) public contentOwners;

    // Event emitted when access is granted
    event AccessGranted(address indexed user, bytes32 indexed contentId);

    // Event emitted when content is registered
    event ContentRegistered(address indexed owner, bytes32 indexed contentId);

    /**
     * @dev Constructor to initialize the contract with ERC20 and NFT contract addresses.
     * @param _erc20TokenAddress Address of the ERC20 token contract.
     * @param _nftContractAddress Address of the NFT contract.
     */
    constructor(address _erc20TokenAddress, address _nftContractAddress) {
        require(_erc20TokenAddress != address(0), "Invalid ERC20 token address");
        require(_nftContractAddress != address(0), "Invalid NFT contract address");

        erc20TokenAddress = _erc20TokenAddress;
        nftContractAddress = _nftContractAddress;
    }

    /**
     * @dev Modifier to check if the caller owns the required ERC20 tokens or NFTs.
     */
    modifier hasAccess(bytes32 contentId) {
        require(
            IERC20(erc20TokenAddress).balanceOf(msg.sender) > 0 ||
            IERC721(nftContractAddress).balanceOf(msg.sender) > 0,
            "Access denied: insufficient tokens or NFTs"
        );
        _;
    }

    /**
     * @dev Function to register exclusive content.
     * @param contentId Unique identifier for the content.
     */
    function registerContent(bytes32 contentId) external {
        require(contentOwners[contentId] == address(0), "Content already registered");
        contentOwners[contentId] = msg.sender;

        emit ContentRegistered(msg.sender, contentId);
    }

    /**
     * @dev Function to grant access to exclusive content.
     * @param contentId Unique identifier for the content.
     */
    function grantAccess(bytes32 contentId) external hasAccess(contentId) {
        require(contentOwners[contentId] != address(0), "Content not registered");
        require(contentOwners[contentId] == msg.sender, "Caller is not the owner of the content");

        emit AccessGranted(msg.sender, contentId);
    }
}

/**
 * @dev Interface for ERC20 token contract.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}

/**
 * @dev Interface for ERC721 (NFT) contract.
 */
interface IERC721 {
    function balanceOf(address owner) external view returns (uint256);
}
```
