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

// Importing ERC20 and ERC721 interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DataOwnershipProtocol contract to manage data exposure with ERC20 and ERC721 tokens
contract DataOwnershipProtocol is Ownable {
    // Mapping to track user data exposure settings
    mapping(address => bool) private dataExposure;

    // Events for logging data exposure changes
    event DataExposureChanged(address indexed user, bool isExposed);

    // Function to set data exposure for a user
    function setDataExposure(bool _isExposed) external {
        dataExposure[msg.sender] = _isExposed;
        emit DataExposureChanged(msg.sender, _isExposed);
    }

    // Function to check if a user's data is exposed
    function isDataExposed(address _user) external view returns (bool) {
        return dataExposure[_user];
    }

    // Function to transfer ERC20 tokens with data exposure check
    function transferERC20(IERC20 token, address to, uint256 amount) external {
        require(dataExposure[msg.sender], "Data is not exposed for this user");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        // Transfer tokens
        bool success = token.transferFrom(msg.sender, to, amount);
        require(success, "Token transfer failed");
    }

    // Function to transfer ERC721 tokens with data exposure check
    function transferERC721(IERC721 token, address to, uint256 tokenId) external {
        require(dataExposure[msg.sender], "Data is not exposed for this user");
        require(token.ownerOf(tokenId) == msg.sender, "Caller is not the owner of the token");

        // Transfer token
        token.safeTransferFrom(msg.sender, to, tokenId);
    }
}
```
