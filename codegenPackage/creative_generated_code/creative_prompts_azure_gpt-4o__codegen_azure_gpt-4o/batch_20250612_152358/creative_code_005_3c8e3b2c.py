"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grokcoin.pages.dev
Prompt: Develop a smart contract in Solidity for managing GROK token transactions, including features for burning tokens and tracking total supply.
Generated: DETERMINISTIC_3c8e3b2c5f94b663
Batch ID: 20250612_152358
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
 * @title GROK Token Smart Contract
 * @dev Implements basic ERC20 functionality with ability to burn tokens and track total supply.
 */
contract GROKToken {
    // State variables
    string public name = "GROK Token";
    string public symbol = "GROK";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed burner, uint256 value);

    // Modifier to prevent invalid address usage
    modifier validAddress(address account) {
        require(account != address(0), "Invalid address.");
        _;
    }

    /**
     * @dev Constructor to initialize the token with a supply assigned to the deployer.
     * @param initialSupply The initial token supply.
     */
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of a given account.
     * @param account The account whose balance is to be retrieved.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the caller to a recipient.
     * @param recipient The recipient address.
     * @param amount The amount to transfer.
     */
    function transfer(address recipient, uint256 amount)
        public
        validAddress(recipient)
        returns (bool)
    {
        require(balances[msg.sender] >= amount, "Insufficient balance.");
        balances[msg.sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender The address authorized to spend.
     * @param amount The amount they are authorized to spend.
     */
    function approve(address spender, uint256 amount)
        public
        validAddress(spender)
        returns (bool)
    {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from a sender to a recipient using allowance mechanism.
     * @param sender The address of the sender.
     * @param recipient The address of the recipient.
     * @param amount The amount to transfer.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public validAddress(recipient) returns (bool) {
        require(balances[sender] >= amount, "Insufficient balance.");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded.");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining allowance for a spender.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Burns a specific amount of tokens, reducing total supply.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public returns (bool) {
        require(balances[msg.sender] >= amount, "Insufficient balance.");
        balances[msg.sender] -= amount;
        totalSupply -= amount;
        emit Burn(msg.sender, amount);
        emit Transfer(msg.sender, address(0), amount);
        return true;
    }
}
```
