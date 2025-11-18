"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumbull.pages.dev
Prompt: Generate code to create an ERC-20 token with a fixed supply, ensuring 1.5% of the supply is allocated to a specific wallet address, as mentioned for Vitalik's holdings in $EBULL.
Generated: DETERMINISTIC_6b4857b079a4a178
Batch ID: 20250612_150226
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
 * @title ERC-20 Token Contract
 * @dev This contract implements a fixed supply ERC-20 token with 1.5% of the supply allocated to a specific wallet.
 */
contract EbullToken {
    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // State variables
    string public name = "EBULL Token";
    string public symbol = "EBULL";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    address public owner; // Contract owner
    address public vitalikAddress; // Wallet for Vitalik's holdings

    /**
     * @dev Sets the total supply and allocates 1.5% to Vitalik's wallet.
     * @param _initialSupply The fixed total token supply (in wei).
     * @param _vitalikAddress The wallet address for Vitalik's holdings.
     */
    constructor(uint256 _initialSupply, address _vitalikAddress) {
        require(_vitalikAddress != address(0), "Invalid Vitalik address");

        owner = msg.sender; // Set the contract deployer as the owner
        vitalikAddress = _vitalikAddress;

        totalSupply = _initialSupply;
        uint256 vitalikAllocation = (_initialSupply * 15) / 1000; // 1.5% allocation

        // Distribute tokens
        balances[vitalikAddress] = vitalikAllocation;
        balances[owner] = _initialSupply - vitalikAllocation;

        emit Transfer(address(0), vitalikAddress, vitalikAllocation);
        emit Transfer(address(0), owner, _initialSupply - vitalikAllocation);
    }

    // Public functions

    /**
     * @dev Returns the balance of the specified address.
     * @param account The address to query.
     * @return The balance of the address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the caller to a recipient.
     * @param recipient The address to send tokens to.
     * @param amount The amount of tokens to transfer.
     * @return Success status.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender The address allowed to spend tokens.
     * @param amount The amount of tokens they are allowed to spend.
     * @return Success status.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another on behalf of the caller.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return Success status.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining allowance for a spender.
     * @param owner The address of the token holder.
     * @param spender The address of the spender.
     * @return The remaining allowance.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    // Internal functions

    /**
     * @dev Internal function to transfer tokens.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from zero address");
        require(recipient != address(0), "Transfer to zero address");
        require(balances[sender] >= amount, "Transfer amount exceeds balance");

        balances[sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
    }
}
```
