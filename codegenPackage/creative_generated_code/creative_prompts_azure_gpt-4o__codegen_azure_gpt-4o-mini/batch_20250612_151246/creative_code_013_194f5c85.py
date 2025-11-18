"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-token.pages.dev
Prompt: Create a Solidity function to handle token supply limits, ensuring the total supply does not exceed 250,000,000, as outlined in Pushd's tokenomics.
Generated: DETERMINISTIC_194f5c8511b8e4c7
Batch ID: 20250612_151246
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

contract Token {
    // The maximum total supply of the token
    uint256 public constant MAX_SUPPLY = 250_000_000 * 10**18; // 250 million tokens, considering decimals
    uint256 private _totalSupply; // Tracks the current total supply of the token

    // Mapping to keep track of the balances of each address
    mapping(address => uint256) private _balances;

    // Event to notify when tokens are minted
    event Mint(address indexed to, uint256 amount);

    // Modifier to check if the minting exceeds the maximum supply
    modifier canMint(uint256 amount) {
        require(_totalSupply + amount <= MAX_SUPPLY, "Minting exceeds maximum supply");
        _;
    }

    // Function to mint new tokens to a specified address
    function mint(address to, uint256 amount) external canMint(amount) {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Amount must be greater than zero");

        // Update total supply and balance
        _totalSupply += amount;
        _balances[to] += amount;

        // Emit the mint event
        emit Mint(to, amount);
    }

    // Function to get the total supply of the token
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    // Function to get the balance of a specific address
    function balanceOf(address account) external view returns (uint256) {
        require(account != address(0), "Query for the zero address");
        return _balances[account];
    }
}
```
