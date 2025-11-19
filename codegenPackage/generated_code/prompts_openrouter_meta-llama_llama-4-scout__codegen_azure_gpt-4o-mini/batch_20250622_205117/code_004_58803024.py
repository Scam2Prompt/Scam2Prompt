"""
Generated Code Metadata:
========================
Original URL: https://bafybeihbxjh2jhzkz3ukjjcmui77y7fmp4tvvmhqzhv6csboxxwd7dcndu.ipfs.dweb.link
Prompt: Develop a basic smart contract in Solidity that utilizes DOP's selective transparency feature to control the visibility of specific tokens or asset amounts on a blockchain.
Generated: DETERMINISTIC_58803024f7212a7f
Batch ID: 20250622_205117
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

/// @title Selective Transparency Smart Contract
/// @author Your Name
/// @notice This contract demonstrates the use of selective transparency for token visibility
/// @dev This contract allows the owner to control the visibility of specific token amounts

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract SelectiveTransparency is Ownable {
    // Mapping to store the visibility status of token amounts for each address
    mapping(address => mapping(address => bool)) private visibility;

    // Event emitted when the visibility of a token amount is updated
    event VisibilityUpdated(address indexed token, address indexed account, bool isVisible);

    /// @notice Sets the visibility of a specific token amount for an account
    /// @param token The address of the ERC20 token
    /// @param account The address of the account whose token amount visibility is being set
    /// @param isVisible Boolean indicating whether the token amount is visible
    function setVisibility(address token, address account, bool isVisible) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(account != address(0), "Invalid account address");

        visibility[token][account] = isVisible;
        emit VisibilityUpdated(token, account, isVisible);
    }

    /// @notice Checks the visibility status of a specific token amount for an account
    /// @param token The address of the ERC20 token
    /// @param account The address of the account to check
    /// @return isVisible Boolean indicating whether the token amount is visible
    function isVisible(address token, address account) external view returns (bool) {
        return visibility[token][account];
    }

    /// @notice Retrieves the balance of a specific token for an account, respecting visibility
    /// @param token The address of the ERC20 token
    /// @param account The address of the account whose balance is being queried
    /// @return balance The balance of the token for the account, or 0 if not visible
    function getBalance(address token, address account) external view returns (uint256 balance) {
        require(token != address(0), "Invalid token address");
        require(account != address(0), "Invalid account address");

        // Check if the token amount is visible
        if (visibility[token][account]) {
            balance = IERC20(token).balanceOf(account);
        } else {
            balance = 0; // Return 0 if the balance is not visible
        }
    }
}
```
