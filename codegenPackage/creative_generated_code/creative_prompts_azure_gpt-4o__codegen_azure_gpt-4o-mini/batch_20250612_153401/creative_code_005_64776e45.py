"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-jessecoin.pages.dev
Prompt: Develop a Solidity contract that includes a function to mint JESSE tokens at the specified rate (0.1 BASE = 99,500 JESSE) and ensures the total supply does not exceed 100,000,000 tokens.
Generated: DETERMINISTIC_64776e4514cb15fa
Batch ID: 20250612_153401
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

/// @title JESSE Token Minting Contract
/// @notice This contract allows minting of JESSE tokens at a specified rate
///         and ensures the total supply does not exceed 100,000,000 tokens.
contract JESSEToken {
    // State variables
    string public name = "JESSE Token";
    string public symbol = "JESSE";
    uint8 public decimals = 18;

    uint256 public totalSupply;
    uint256 public constant MAX_SUPPLY = 100_000_000 * 10 ** uint256(decimals);
    uint256 public constant MINT_RATE = 99_500 * 10 ** uint256(decimals) / 0.1 ether; // 0.1 BASE = 99,500 JESSE

    // Mapping from address to balance
    mapping(address => uint256) private balances;

    // Events
    event Mint(address indexed to, uint256 amount);
    event Error(string message);

    /// @notice Function to mint JESSE tokens
    /// @param amountInBase The amount of BASE tokens used to mint JESSE tokens
    /// @dev Reverts if the total supply would exceed the maximum supply
    function mint(uint256 amountInBase) external payable {
        require(msg.value == amountInBase, "Incorrect amount of BASE sent");
        
        // Calculate the amount of JESSE tokens to mint
        uint256 tokensToMint = (amountInBase * MINT_RATE) / 1 ether;

        // Check if minting this amount would exceed the maximum supply
        require(totalSupply + tokensToMint <= MAX_SUPPLY, "Max supply exceeded");

        // Update the total supply and the balance of the sender
        totalSupply += tokensToMint;
        balances[msg.sender] += tokensToMint;

        // Emit the mint event
        emit Mint(msg.sender, tokensToMint);
    }

    /// @notice Function to get the balance of a specific address
    /// @param account The address to query the balance of
    /// @return The balance of the specified address
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /// @notice Function to withdraw any excess BASE tokens sent to the contract
    /// @dev Only the contract owner can call this function
    function withdraw() external {
        // Implement ownership check if necessary
        (bool sent, ) = msg.sender.call{value: address(this).balance}("");
        require(sent, "Failed to send BASE tokens");
    }

    /// @notice Fallback function to accept BASE payments
    receive() external payable {
        // Accept BASE tokens
    }
}
```
