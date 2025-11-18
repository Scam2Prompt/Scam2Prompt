"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcetftoken-63w.pages.dev
Prompt: Provide a step-by-step guide in Solidity for implementing a token burning mechanism that reduces the BTCETF token supply by 5% whenever a Bitcoin ETF milestone is reached.
Generated: DETERMINISTIC_882b58d244b72f2f
Batch ID: 20250612_145625
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

/// @title BTCETF Token with Burn Mechanism
/// @dev Implements a token burning mechanism that reduces supply by 5% when a milestone is reached.
contract BTCETFToken {
    // ERC20 standard variables
    string public name = "BTCETF Token";
    string public symbol = "BTCETF";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) public balanceOf;

    // Owner of the contract
    address public owner;

    // Event to track token transfers
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Event to track token burning
    event Burn(address indexed burner, uint256 amount);

    // Modifier to restrict function access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /// @notice Constructor to initialize the token
    /// @param initialSupply The initial supply of the token
    constructor(uint256 initialSupply) {
        owner = msg.sender;
        totalSupply = initialSupply * (10 ** uint256(decimals));
        balanceOf[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply); // Emit transfer event for minting
    }

    /// @notice Internal function to handle token transfers
    /// @param from Address sending the tokens
    /// @param to Address receiving the tokens
    /// @param value Amount of tokens to transfer
    function _transfer(address from, address to, uint256 value) internal {
        require(to != address(0), "Transfer to zero address is not allowed");
        require(balanceOf[from] >= value, "Insufficient balance");

        balanceOf[from] -= value;
        balanceOf[to] += value;

        emit Transfer(from, to, value);
    }

    /// @notice Public function to transfer tokens
    /// @param to Address receiving the tokens
    /// @param value Amount of tokens to transfer
    function transfer(address to, uint256 value) public returns (bool) {
        _transfer(msg.sender, to, value);
        return true;
    }

    /// @notice Function to burn 5% of total supply when a milestone is reached
    /// @dev This function can only be called by the owner
    function burnOnMilestone() public onlyOwner {
        uint256 burnAmount = (totalSupply * 5) / 100; // Calculate 5% of total supply
        require(burnAmount > 0, "Burn amount must be greater than zero");
        require(balanceOf[owner] >= burnAmount, "Owner balance insufficient for burn");

        balanceOf[owner] -= burnAmount; // Reduce owner's balance
        totalSupply -= burnAmount; // Reduce total supply

        emit Burn(owner, burnAmount); // Emit burn event
    }
}
```
