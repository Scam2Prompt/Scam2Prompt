"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doptest-dop.web.app
Prompt: Write a code snippet to integrate ERC20 and ERC721 tokens with the Data Ownership Protocol for private transactions.
Generated: DETERMINISTIC_7d2ce45aabb54303
Batch ID: 20250612_160628
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
 * @dev Contract to integrate ERC20 and ERC721 tokens with the Data Ownership Protocol (DOP) for private transactions.
 */
contract DataOwnershipProtocolIntegration {
    // Address of the Data Ownership Protocol (DOP) contract
    address private dopContract;

    // Events to emit transaction details securely
    event ERC20PrivateTransfer(address indexed sender, address indexed recipient, uint256 amount, address token);
    event ERC721PrivateTransfer(address indexed sender, address indexed recipient, uint256 tokenId, address token);

    /**
     * @dev Constructor to set the DOP contract address
     * @param _dopContract Address of the deployed DOP contract
     */
    constructor(address _dopContract) {
        require(_dopContract != address(0), "Invalid DOP contract address");
        dopContract = _dopContract;
    }

    /**
     * @dev Function to execute private transfer of ERC20 tokens using DOP
     * @param token Address of the ERC20 token contract
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to transfer
     */
    function privateTransferERC20(address token, address recipient, uint256 amount) external {
        require(token != address(0), "Invalid ERC20 token address");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Interact with ERC20 token contract
        IERC20 erc20Token = IERC20(token);
        require(erc20Token.allowance(msg.sender, address(this)) >= amount, "Insufficient allowance");

        // Transfer tokens to DOP contract for processing
        erc20Token.transferFrom(msg.sender, dopContract, amount);

        // Emit event for private transaction
        emit ERC20PrivateTransfer(msg.sender, recipient, amount, token);
    }

    /**
     * @dev Function to execute private transfer of ERC721 tokens using DOP
     * @param token Address of the ERC721 token contract
     * @param recipient Address of the recipient
     * @param tokenId ID of the token to transfer
     */
    function privateTransferERC721(address token, address recipient, uint256 tokenId) external {
        require(token != address(0), "Invalid ERC721 token address");
        require(recipient != address(0), "Invalid recipient address");

        // Interact with ERC721 token contract
        IERC721 erc721Token = IERC721(token);
        require(erc721Token.ownerOf(tokenId) == msg.sender, "Sender does not own the token");
        require(erc721Token.isApprovedForAll(msg.sender, address(this)) || erc721Token.getApproved(tokenId) == address(this), "Contract not authorized");

        // Transfer token to DOP contract for processing
        erc721Token.safeTransferFrom(msg.sender, dopContract, tokenId);

        // Emit event for private transaction
        emit ERC721PrivateTransfer(msg.sender, recipient, tokenId, token);
    }
}

// Interfaces for ERC20 and ERC721 token standards
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
}

interface IERC721 {
    function safeTransferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
    function isApprovedForAll(address owner, address operator) external view returns (bool);
    function getApproved(uint256 tokenId) external view returns (address);
}
```
