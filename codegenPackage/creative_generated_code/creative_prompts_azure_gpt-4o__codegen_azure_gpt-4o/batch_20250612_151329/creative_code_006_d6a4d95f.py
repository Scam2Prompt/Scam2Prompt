"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://angelwings.pages.dev
Prompt: Create a Solidity function that implements tokenomics features for a project similar to "Pepe 2.0," such as minting or burning tokens.
Generated: DETERMINISTIC_d6a4d95f712a7dd3
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/// @title Tokenomics Contract for Minting and Burning Tokens
/// @dev This contract implements basic tokenomics features for minting and burning tokens.
contract Tokenomics {
    // State variables
    string public name = "Pepe 2.0 Token";
    string public symbol = "PEPE2";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Mint(address indexed to, uint256 value);
    event Burn(address indexed from, uint256 value);

    // Access control: restrict minting and burning to the contract owner
    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /// @dev Constructor to initialize the token and set the owner
    /// @param _initialSupply The initial supply of the token
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        mint(owner, _initialSupply); // Mint initial supply to owner
    }

    /// @notice Mint new tokens to a specified address
    /// @param _to The address to receive the minted tokens
    /// @param _amount The number of tokens to mint
    function mint(address _to, uint256 _amount) public onlyOwner {
        require(_to != address(0), "Mint to the zero address"); // Prevent minting to the zero address
        require(_amount > 0, "Mint amount must be greater than zero"); // Ensure positive minting amount

        balanceOf[_to] += _amount;
        totalSupply += _amount;

        emit Mint(_to, _amount);
        emit Transfer(address(0), _to, _amount); // ERC20-compliant transfer event from zero address
    }

    /// @notice Burn tokens from a specified address
    /// @param _from The address whose tokens will be burned
    /// @param _amount The number of tokens to burn
    function burn(address _from, uint256 _amount) public onlyOwner {
        require(_from != address(0), "Burn from the zero address"); // Prevent burning from the zero address
        require(_amount > 0, "Burn amount must be greater than zero"); // Ensure positive burn amount
        require(balanceOf[_from] >= _amount, "Insufficient balance to burn"); // Check balance

        balanceOf[_from] -= _amount;
        totalSupply -= _amount;

        emit Burn(_from, _amount);
        emit Transfer(_from, address(0), _amount); // ERC20-compliant transfer event to zero address
    }

    /// @notice Transfer tokens from the caller to a specified address
    /// @param _to The recipient address
    /// @param _amount The number of tokens to transfer
    function transfer(address _to, uint256 _amount) public returns (bool) {
        require(_to != address(0), "Transfer to the zero address"); // Prevent transfers to the zero address
        require(balanceOf[msg.sender] >= _amount, "Insufficient balance"); // Check sender's balance
        
        balanceOf[msg.sender] -= _amount;
        balanceOf[_to] += _amount;

        emit Transfer(msg.sender, _to, _amount);
        return true;
    }
}
```
