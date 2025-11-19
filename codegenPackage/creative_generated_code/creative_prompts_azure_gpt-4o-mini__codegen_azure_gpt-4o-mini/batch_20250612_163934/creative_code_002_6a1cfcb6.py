"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappdroppage.pages.dev
Prompt: Write a simple smart contract in Solidity that could be used for a dApp drop scenario, incorporating unique features that might have been discussed on a dApp drop page.
Generated: DETERMINISTIC_6a1cfcb6129a81d0
Batch ID: 20250612_163934
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

/// @title A Simple Token Drop Smart Contract
/// @notice This contract allows for airdrops of ERC20 tokens to multiple recipients
/// @dev This implementation includes event logging and basic access control

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenDrop is Ownable {
    // Event to log the airdrop action
    event Airdrop(address indexed token, address indexed recipient, uint256 amount);

    /// @notice Airdrops tokens to a list of addresses
    /// @param token The address of the ERC20 token to be airdropped
    /// @param recipients An array of addresses to receive the tokens
    /// @param amounts An array of amounts corresponding to each recipient
    /// @dev The length of recipients and amounts must match
    function airdropTokens(
        address token,
        address[] calldata recipients,
        uint256[] calldata amounts
    ) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");
        
        IERC20 erc20Token = IERC20(token);

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 amount = amounts[i];

            require(recipient != address(0), "Invalid recipient address");
            require(amount > 0, "Amount must be greater than zero");
            require(erc20Token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

            // Transfer tokens to the recipient
            erc20Token.transfer(recipient, amount);
            
            // Emit the Airdrop event
            emit Airdrop(token, recipient, amount);
        }
    }

    /// @notice Withdraw tokens from the contract
    /// @param token The address of the ERC20 token to withdraw
    /// @param amount The amount of tokens to withdraw
    /// @dev Only the contract owner can withdraw tokens
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20 erc20Token = IERC20(token);
        require(erc20Token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        erc20Token.transfer(owner(), amount);
    }

    /// @notice Get the contract balance of a specific token
    /// @param token The address of the ERC20 token
    /// @return The balance of the specified token in this contract
    function getTokenBalance(address token) external view returns (uint256) {
        IERC20 erc20Token = IERC20(token);
        return erc20Token.balanceOf(address(this));
    }
}
```
