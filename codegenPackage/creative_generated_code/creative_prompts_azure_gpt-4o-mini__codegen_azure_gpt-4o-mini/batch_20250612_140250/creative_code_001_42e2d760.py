"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-io.web.app
Prompt: How can I integrate ERC20 and ERC721 tokens with the Data Ownership Protocol to allow users to control their data exposure?
Generated: DETERMINISTIC_42e2d760c7ec8ffd
Batch ID: 20250612_140250
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

// Import ERC20 and ERC721 interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DataOwnershipProtocol contract to manage data exposure with ERC20 and ERC721 tokens
contract DataOwnershipProtocol is Ownable {
    // Mapping to track user data exposure permissions
    mapping(address => mapping(uint256 => bool)) private dataExposurePermissions;

    // Event to emit when data exposure permission is set
    event DataExposurePermissionSet(address indexed user, uint256 indexed dataId, bool permission);

    // ERC20 token address
    IERC20 public erc20Token;
    
    // ERC721 token address
    IERC721 public erc721Token;

    // Constructor to initialize the contract with ERC20 and ERC721 token addresses
    constructor(address _erc20Token, address _erc721Token) {
        require(_erc20Token != address(0), "Invalid ERC20 token address");
        require(_erc721Token != address(0), "Invalid ERC721 token address");
        
        erc20Token = IERC20(_erc20Token);
        erc721Token = IERC721(_erc721Token);
    }

    // Function to set data exposure permission for a specific user and data ID
    function setDataExposurePermission(uint256 dataId, bool permission) external {
        dataExposurePermissions[msg.sender][dataId] = permission;
        emit DataExposurePermissionSet(msg.sender, dataId, permission);
    }

    // Function to check if a user has permission to expose their data
    function hasDataExposurePermission(address user, uint256 dataId) external view returns (bool) {
        return dataExposurePermissions[user][dataId];
    }

    // Function to allow users to stake ERC20 tokens to enable data sharing
    function stakeERC20(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        bool success = erc20Token.transferFrom(msg.sender, address(this), amount);
        require(success, "Transfer failed");
    }

    // Function to allow users to share their ERC721 token
    function shareERC721(uint256 tokenId) external {
        require(erc721Token.ownerOf(tokenId) == msg.sender, "You are not the owner of this token");
        erc721Token.safeTransferFrom(msg.sender, address(this), tokenId);
    }

    // Function to withdraw staked ERC20 tokens
    function withdrawERC20(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(erc20Token.balanceOf(address(this)) >= amount, "Insufficient balance in contract");
        
        bool success = erc20Token.transfer(msg.sender, amount);
        require(success, "Transfer failed");
    }

    // Function to withdraw shared ERC721 token
    function withdrawERC721(uint256 tokenId) external onlyOwner {
        require(erc721Token.ownerOf(tokenId) == address(this), "Token not held in contract");
        
        erc721Token.safeTransferFrom(address(this), msg.sender, tokenId);
    }

    // Fallback function to prevent sending ether directly to the contract
    receive() external payable {
        revert("Direct ether transfer not allowed");
    }
}
```
