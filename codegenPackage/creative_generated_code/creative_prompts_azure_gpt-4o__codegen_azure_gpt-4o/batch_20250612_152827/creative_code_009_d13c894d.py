"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-riftswaptokens.pages.dev
Prompt: Create a Solidity contract that supports the ERC404 token standard, as mentioned in Rift Swap's future features, and explain its potential use cases.
Generated: DETERMINISTIC_d13c894d7e910503
Batch ID: 20250612_152827
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
 * @title ERC404 Token Standard
 * @dev An example contract implementing the ERC404 standard mentioned in Rift Swap's future features.
 * Note: Ensure that the ERC404 standard is well-defined in an official EIP before production deployment.
 */
interface IERC404 {
    /**
     * @dev Emitted when data is attached to a token transfer.
     * @param from Address initiating the transfer.
     * @param to Address receiving the transfer.
     * @param tokenId The ID of the token transferred.
     * @param data Attached data in bytes format.
     */
    event TransferWithData(address indexed from, address indexed to, uint256 indexed tokenId, bytes data);

    /**
     * @dev Transfers a token while attaching additional data to the transaction.
     * @param to Recipient address.
     * @param tokenId Token ID to transfer.
     * @param data Arbitrary data attached to the transfer.
     */
    function safeTransferWithData(address to, uint256 tokenId, bytes calldata data) external;

    /**
     * @dev Retrieves the attached data for a specific token ID.
     * @param tokenId Token ID whose data is being queried.
     * @return data Arbitrary data associated with the token.
     */
    function getData(uint256 tokenId) external view returns (bytes memory);
}

/**
 * @title ERC404Token
 * @dev Implementation of the ERC404 Token Standard.
 */
contract ERC404Token is IERC404 {
    // Token owner mapping
    mapping(uint256 => address) private _owners;

    // Mapping to store arbitrary data for each token
    mapping(uint256 => bytes) private _tokenData;

    // Total supply of tokens (optional, depending on use case)
    uint256 private _totalSupply;

    // Modifier to check if the caller is the owner of a token
    modifier onlyOwner(uint256 tokenId) {
        require(_owners[tokenId] == msg.sender, "ERC404Token: caller is not the owner of the token");
        _;
    }

    /**
     * @dev Transfers a token while attaching additional data to the transaction.
     * Emits a TransferWithData event.
     * @param to Recipient address.
     * @param tokenId Token ID to transfer.
     * @param data Arbitrary data attached to the transfer.
     */
    function safeTransferWithData(address to, uint256 tokenId, bytes calldata data) external override onlyOwner(tokenId) {
        require(to != address(0), "ERC404Token: transfer to the zero address");
        require(_owners[tokenId] != address(0), "ERC404Token: token does not exist");

        // Update token ownership
        _owners[tokenId] = to;

        // Attach data to the token
        _tokenData[tokenId] = data;

        // Emit the TransferWithData event
        emit TransferWithData(msg.sender, to, tokenId, data);
    }

    /**
     * @dev Retrieves the attached data for a specific token ID.
     * @param tokenId Token ID whose data is being queried.
     * @return data Arbitrary data associated with the token.
     */
    function getData(uint256 tokenId) external view override returns (bytes memory) {
        require(_owners[tokenId] != address(0), "ERC404Token: token does not exist");
        return _tokenData[tokenId];
    }

    /**
     * @dev Function to mint a new token (example usage).
     * @param to Address to receive the minted token.
     * @param tokenId ID of the token to mint.
     */
    function mint(address to, uint256 tokenId) external {
        require(to != address(0), "ERC404Token: mint to the zero address");
        require(_owners[tokenId] == address(0), "ERC404Token: token already minted");

        // Assign ownership
        _owners[tokenId] = to;

        // Increment total supply
        _totalSupply += 1;
    }

    /**
     * @dev Function to get the owner of a token.
     * @param tokenId ID of the token.
     * @return owner Address of the token owner.
     */
    function ownerOf(uint256 tokenId) external view returns (address) {
        require(_owners[tokenId] != address(0), "ERC404Token: token does not exist");
        return _owners[tokenId];
    }

    /**
     * @dev Function to get the total supply of tokens.
     * @return totalSupply Total supply of tokens.
     */
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }
}
```
