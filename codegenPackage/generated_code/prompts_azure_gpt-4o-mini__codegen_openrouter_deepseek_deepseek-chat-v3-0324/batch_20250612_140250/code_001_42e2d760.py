"""
Generated Code Metadata:
========================
Original URL: https://dop-io.web.app
Prompt: How can I integrate ERC20 and ERC721 tokens with the Data Ownership Protocol to allow users to control their data exposure?
Generated: DETERMINISTIC_42e2d760c7ec8ffd
Batch ID: 20250612_140250
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DataOwnershipProtocol is Ownable, ReentrancyGuard {
    // Struct to store data access permissions
    struct DataPermission {
        address requester;
        uint256 tokenId;
        bool isERC20;
        uint256 amount;
        bool approved;
    }

    // Mapping from user address to their data permissions
    mapping(address => DataPermission[]) private userPermissions;

    // Mapping from token address to whether it's whitelisted
    mapping(address => bool) public whitelistedTokens;

    // Events
    event TokenWhitelisted(address indexed tokenAddress, bool isERC20);
    event PermissionRequested(
        address indexed dataOwner,
        address indexed requester,
        uint256 tokenId,
        bool isERC20,
        uint256 amount
    );
    event PermissionApproved(
        address indexed dataOwner,
        address indexed requester,
        uint256 tokenId,
        bool isERC20,
        uint256 amount
    );
    event PermissionRevoked(
        address indexed dataOwner,
        address indexed requester,
        uint256 tokenId,
        bool isERC20
    );

    // Whitelist a token for use in the protocol
    function whitelistToken(address tokenAddress, bool isERC20) external onlyOwner {
        whitelistedTokens[tokenAddress] = true;
        emit TokenWhitelisted(tokenAddress, isERC20);
    }

    // Request permission to access user's data
    function requestDataAccess(
        address dataOwner,
        address tokenAddress,
        uint256 tokenId,
        bool isERC20,
        uint256 amount
    ) external nonReentrant {
        require(whitelistedTokens[tokenAddress], "Token not whitelisted");
        require(dataOwner != msg.sender, "Cannot request access to own data");

        if (isERC20) {
            IERC20 token = IERC20(tokenAddress);
            require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");
            require(token.allowance(msg.sender, address(this)) >= amount, "Insufficient allowance");
        } else {
            IERC721 token = IERC721(tokenAddress);
            require(token.ownerOf(tokenId) == msg.sender, "Not token owner");
        }

        DataPermission memory newPermission = DataPermission({
            requester: msg.sender,
            tokenId: tokenId,
            isERC20: isERC20,
            amount: amount,
            approved: false
        });

        userPermissions[dataOwner].push(newPermission);
        emit PermissionRequested(dataOwner, msg.sender, tokenId, isERC20, amount);
    }

    // Approve a data access request
    function approveDataAccess(
        uint256 permissionIndex,
        address tokenAddress
    ) external nonReentrant {
        require(permissionIndex < userPermissions[msg.sender].length, "Invalid permission index");
        
        DataPermission storage permission = userPermissions[msg.sender][permissionIndex];
        require(!permission.approved, "Permission already approved");

        if (permission.isERC20) {
            IERC20 token = IERC20(tokenAddress);
            require(
                token.transferFrom(permission.requester, msg.sender, permission.amount),
                "ERC20 transfer failed"
            );
        } else {
            IERC721 token = IERC721(tokenAddress);
            token.safeTransferFrom(permission.requester, msg.sender, permission.tokenId);
        }

        permission.approved = true;
        emit PermissionApproved(
            msg.sender,
            permission.requester,
            permission.tokenId,
            permission.isERC20,
            permission.amount
        );
    }

    // Revoke a data access permission
    function revokeDataAccess(
        uint256 permissionIndex,
        address tokenAddress
    ) external nonReentrant {
        require(permissionIndex < userPermissions[msg.sender].length, "Invalid permission index");
        
        DataPermission storage permission = userPermissions[msg.sender][permissionIndex];
        require(permission.approved, "Permission not approved");

        if (permission.isERC20) {
            IERC20 token = IERC20(tokenAddress);
            require(
                token.transfer(permission.requester, permission.amount),
                "ERC20 transfer failed"
            );
        } else {
            IERC721 token = IERC721(tokenAddress);
            token.safeTransferFrom(msg.sender, permission.requester, permission.tokenId);
        }

        // Remove permission from array
        _removePermission(msg.sender, permissionIndex);
        emit PermissionRevoked(
            msg.sender,
            permission.requester,
            permission.tokenId,
            permission.isERC20
        );
    }

    // Get all permissions for a user
    function getUserPermissions(address user) external view returns (DataPermission[] memory) {
        return userPermissions[user];
    }

    // Helper function to remove a permission from array
    function _removePermission(address user, uint256 index) private {
        DataPermission[] storage permissions = userPermissions[user];
        if (index < permissions.length - 1) {
            permissions[index] = permissions[permissions.length - 1];
        }
        permissions.pop();
    }
}
```
