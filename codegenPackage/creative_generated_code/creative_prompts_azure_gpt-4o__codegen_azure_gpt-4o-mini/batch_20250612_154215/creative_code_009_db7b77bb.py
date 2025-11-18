"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahsjdkkk.pages.dev
Prompt: Generate a Solidity smart contract template for a multichain token transfer system, ensuring interoperability across multiple blockchain networks, as supported by the Chain Solution Center.
Generated: DETERMINISTIC_db7b77bb15c57c14
Batch ID: 20250612_154215
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

// Import necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// @title MultiChainTokenTransfer
// @dev A smart contract for transferring ERC20 tokens across multiple blockchain networks
contract MultiChainTokenTransfer is Ownable {
    using Address for address;

    // Event emitted when tokens are transferred
    event TokensTransferred(address indexed token, address indexed to, uint256 amount, uint256 chainId);

    // Mapping to track approvals for token transfers
    mapping(address => mapping(address => bool)) public approvedTokens;

    /**
     * @dev Approve an ERC20 token for transfer across chains
     * @param token The address of the ERC20 token
     * @param isApproved A boolean indicating approval status
     */
    function approveToken(address token, bool isApproved) external onlyOwner {
        require(token.isContract(), "Not a valid contract address");
        approvedTokens[msg.sender][token] = isApproved;
    }

    /**
     * @dev Transfer tokens to a specified address on another chain
     * @param token The address of the ERC20 token to transfer
     * @param to The address to receive the tokens
     * @param amount The amount of tokens to transfer
     * @param chainId The target chain ID for the transfer
     */
    function transferTokens(
        address token,
        address to,
        uint256 amount,
        uint256 chainId
    ) external {
        require(approvedTokens[msg.sender][token], "Token transfer not approved");
        require(IERC20(token).balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Emit event for off-chain processing (for cross-chain transfer logic)
        emit TokensTransferred(token, to, amount, chainId);
        
        // The actual cross-chain transfer logic should be implemented in conjunction with the Chain Solution Center
        // This is a placeholder for the interaction with the cross-chain solution
        // transferToOtherChain(token, to, amount, chainId);
    }

    /**
     * @dev Placeholder for cross-chain transfer implementation
     * This function should handle the logic for transferring tokens to the specified chain.
     */
    // function transferToOtherChain(address token, address to, uint256 amount, uint256 chainId) private {
    //     // Logic to transfer tokens to the other chain
    // }

    /**
     * @dev Withdraw tokens from the contract
     * @param token The address of the ERC20 token to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient contract balance");
        
        // Transfer tokens back to the owner
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
