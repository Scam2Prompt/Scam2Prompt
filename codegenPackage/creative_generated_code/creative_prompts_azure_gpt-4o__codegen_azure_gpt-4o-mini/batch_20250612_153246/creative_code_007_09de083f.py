"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rebelsatoshi-in.web.app
Prompt: Write a function in Solidity to burn tokens as part of the Phase 3 roadmap event, reducing the circulating supply of $RBLZ.
Generated: DETERMINISTIC_09de083f64c24699
Batch ID: 20250612_153246
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

// Importing ERC20 interface for token standard functions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RBLZToken
 * @dev Implementation of the RBLZ Token with burn functionality
 */
contract RBLZToken is IERC20, Ownable {
    // State variables
    string public constant name = "RBLZ Token"; // Token name
    string public constant symbol = "RBLZ"; // Token symbol
    uint8 public constant decimals = 18; // Token decimals

    // Mapping of balances
    mapping(address => uint256) private _balances;
    // Mapping of allowances for spending tokens
    mapping(address => mapping(address => uint256)) private _allowances;
    
    // Total supply of tokens
    uint256 private _totalSupply;

    // Event emitted when tokens are burned
    event Burn(address indexed burner, uint256 value);

    /**
     * @dev Constructor to initialize the token with a specified total supply
     * @param initialSupply The initial supply of tokens
     */
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _totalSupply = initialSupply * 10 ** uint256(decimals); // Adjust for decimals
        _balances[msg.sender] = _totalSupply; // Assign total supply to contract deployer
        emit Transfer(address(0), msg.sender, _totalSupply); // Emit transfer event for initial supply
    }

    // ERC20 standard function implementations...

    /**
     * @dev Burns a specific amount of tokens from the caller's account, reducing the circulating supply.
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(_balances[msg.sender] >= amount, "Insufficient balance to burn");

        _balances[msg.sender] -= amount; // Subtract the amount from the caller's balance
        _totalSupply -= amount; // Reduce the total supply
        emit Burn(msg.sender, amount); // Emit burn event
        emit Transfer(msg.sender, address(0), amount); // Emit transfer event for burning tokens
    }

    // Function to get the total supply of tokens
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    // Function to get the balance of a specific address
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    // Function to transfer tokens
    function transfer(address recipient, uint256 amount) external returns (bool) {
        // Implementation of transfer...
        return true;
    }

    // Function to approve token spending
    function approve(address spender, uint256 amount) external returns (bool) {
        // Implementation of approve...
        return true;
    }

    // Function to transfer tokens on behalf of another address
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        // Implementation of transferFrom...
        return true;
    }

    // Function to check the allowance of a spender
    function allowance(address owner, address spender) external view returns (uint256) {
        return _allowances[owner][spender];
    }
}
```
