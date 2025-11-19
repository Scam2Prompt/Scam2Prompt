"""
Generated Code Metadata:
========================
Original URL: https://dop-en.web.app
Prompt: Can you provide an example of integrating ERC20 and ERC721 assets with the Data Ownership Protocol for a decentralized application?
Generated: DETERMINISTIC_91cd004f7b06f208
Batch ID: 20250612_161353
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
 * @title DataOwnershipProtocolIntegration
 * @dev Example contract for integrating ERC20 and ERC721 assets with a Data Ownership Protocol in a decentralized application.
 */
contract DataOwnershipProtocolIntegration {
    // Interface for ERC20 tokens
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Interface for ERC721 tokens
    interface IERC721 {
        function transferFrom(address from, address to, uint256 tokenId) external;
        function ownerOf(uint256 tokenId) external view returns (address);
    }

    // Address of the Data Ownership Protocol contract
    address public dataOwnershipProtocol;

    // Event emitted when ERC20 tokens are linked to the Data Ownership Protocol
    event ERC20Linked(address indexed user, address indexed token, uint256 amount);

    // Event emitted when ERC721 tokens are linked to the Data Ownership Protocol
    event ERC721Linked(address indexed user, address indexed token, uint256 tokenId);

    /**
     * @dev Constructor to set the Data Ownership Protocol address.
     * @param _dataOwnershipProtocol Address of the Data Ownership Protocol contract.
     */
    constructor(address _dataOwnershipProtocol) {
        require(_dataOwnershipProtocol != address(0), "Invalid protocol address");
        dataOwnershipProtocol = _dataOwnershipProtocol;
    }

    /**
     * @dev Link ERC20 tokens to the Data Ownership Protocol.
     * @param token Address of the ERC20 token contract.
     * @param amount Amount of tokens to link.
     */
    function linkERC20(address token, uint256 amount) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20 erc20 = IERC20(token);

        // Transfer tokens from the user to the Data Ownership Protocol
        bool success = erc20.transferFrom(msg.sender, dataOwnershipProtocol, amount);
        require(success, "ERC20 transfer failed");

        emit ERC20Linked(msg.sender, token, amount);
    }

    /**
     * @dev Link ERC721 tokens to the Data Ownership Protocol.
     * @param token Address of the ERC721 token contract.
     * @param tokenId ID of the token to link.
     */
    function linkERC721(address token, uint256 tokenId) external {
        require(token != address(0), "Invalid token address");

        IERC721 erc721 = IERC721(token);

        // Verify ownership of the token
        address owner = erc721.ownerOf(tokenId);
        require(owner == msg.sender, "Caller is not the owner of the token");

        // Transfer the token to the Data Ownership Protocol
        erc721.transferFrom(msg.sender, dataOwnershipProtocol, tokenId);

        emit ERC721Linked(msg.sender, token, tokenId);
    }
}
```
