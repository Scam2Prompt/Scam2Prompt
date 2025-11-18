"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-is.web.app
Prompt: Write a smart contract in Solidity for an ERC20 token with a burn mechanism similar to $MPEPE, where tokens are automatically burned after every transaction.
Generated: DETERMINISTIC_a91335827e3d7714
Batch ID: 20250612_145300
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
 * @title ERC20TokenWithBurn
 * @dev ERC20 implementation with a burn mechanism that deducts a percentage of tokens after each transaction.
 */
contract ERC20TokenWithBurn {
    // Token details
    string public name = "MyBurnableToken";
    string public symbol = "MBT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Track balances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Burn rate (e.g., 1% burn rate: burnRate = 100 means 1%)
    uint256 public burnRate = 100; // 1%

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor(uint256 _initialSupply) {
        // Allocate the initial supply to the deployer
        totalSupply = _initialSupply * (10 ** decimals);
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param account The address to query the balance of.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the caller to a recipient, applying the burn rate.
     * @param recipient The address to transfer to.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves an address to spend a specific amount of tokens on behalf of the caller.
     * @param spender The address allowed to spend the funds.
     * @param amount The amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another, applying the burn rate.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "ERC20: transfer amount exceeds allowance");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining allowance for a spender from a specific owner.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Internal function to handle transfers and apply the burn mechanism.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(balances[sender] >= amount, "ERC20: transfer amount exceeds balance");

        // Calculate the burn amount
        uint256 burnAmount = (amount * burnRate) / 10000; // Burn rate is in basis points (10000 = 100%)
        uint256 transferAmount = amount - burnAmount; // Amount actually transferred

        // Update balances
        balances[sender] -= amount;
        balances[recipient] += transferAmount;
        totalSupply -= burnAmount; // Reduce total supply by the burn amount

        // Emit transfer events
        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, address(0), burnAmount); // Burn event (tokens sent to zero address)
    }
}
```
