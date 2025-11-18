"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dancingtriangle.website
Prompt: Write a function in Solidity to automatically burn a percentage of $triangle tokens after every transaction, following the token's "ponzinomics" model.
Generated: DETERMINISTIC_a5d7527fc5583614
Batch ID: 20250612_154302
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
 * @title TriangleToken
 * @dev A token contract implementing "ponzinomics" with automatic burning of a percentage after every transaction.
 */
contract TriangleToken {
    // Token details
    string public name = "TriangleToken";
    string public symbol = "TRI";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping for balances
    mapping(address => uint256) private balances;
    // Mapping for allowances (used for ERC-20 compatibility)
    mapping(address => mapping(address => uint256)) private allowances;

    // Percentage of tokens to burn per transaction (e.g., 2%)
    uint256 public burnRate = 2;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * 10**decimals;
        balances[msg.sender] = totalSupply; // Assign all tokens to the contract deployer
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Get the balance of a given account.
     * @param account The address of the account to query.
     * @return The balance of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfer tokens with automatic burning.
     * @param recipient The recipient address.
     * @param amount The amount to transfer.
     * @return True if the transfer is successful.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve tokens for spending by another account.
     * @param spender The address authorized to spend.
     * @param amount The amount to approve.
     * @return True if the approval is successful.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another with automatic burning.
     * @param sender The address sending the tokens.
     * @param recipient The recipient address.
     * @param amount The amount to transfer.
     * @return True if the transfer is successful.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "ERC20: transfer amount exceeds allowance");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Internal function to handle token transfers and burning.
     * @param sender The address sending the tokens.
     * @param recipient The recipient address.
     * @param amount The amount to transfer.
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(balances[sender] >= amount, "ERC20: transfer amount exceeds balance");

        // Calculate the burn amount
        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 transferAmount = amount - burnAmount;

        // Update balances
        balances[sender] -= amount;
        balances[recipient] += transferAmount;
        totalSupply -= burnAmount; // Reduce total supply for burned tokens

        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, address(0), burnAmount); // Emit a transfer to the zero address for burns
    }

    /**
     * @dev Get the remaining allowance for a spender.
     * @param owner The owner of the tokens.
     * @param spender The spender authorized to spend.
     * @return The remaining allowance.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
