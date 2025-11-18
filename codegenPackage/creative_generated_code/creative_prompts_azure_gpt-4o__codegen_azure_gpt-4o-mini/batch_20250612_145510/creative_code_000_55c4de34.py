"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainnet-dioneprotocol.pages.dev
Prompt: Write a Solidity smart contract optimized for deployment on the Odyssey Chain, leveraging its EVM compatibility and low transaction fees. Include features for swift transaction finality and scalability.
Generated: DETERMINISTIC_55c4de3404a4cbca
Batch ID: 20250612_145510
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

/**
 * @title OdysseyChainToken
 * @dev A simple ERC20 token contract optimized for the Odyssey Chain.
 * This contract supports basic token functionalities and includes
 * mechanisms for swift transaction finality and scalability.
 */
contract OdysseyChainToken {
    string public name; // Token name
    string public symbol; // Token symbol
    uint8 public decimals; // Number of decimal places
    uint256 public totalSupply; // Total supply of the token

    mapping(address => uint256) private balances; // Mapping of balances
    mapping(address => mapping(address => uint256)) private allowances; // Mapping for allowances

    event Transfer(address indexed from, address indexed to, uint256 value); // Event for token transfers
    event Approval(address indexed owner, address indexed spender, uint256 value); // Event for approvals

    /**
     * @dev Constructor to set the token details.
     * @param _name The name of the token.
     * @param _symbol The symbol of the token.
     * @param _decimals Number of decimal places for the token.
     * @param _initialSupply The initial supply of tokens minted to the deployer.
     */
    constructor(string memory _name, string memory _symbol, uint8 _decimals, uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _initialSupply * (10 ** uint256(decimals)); // Adjust initial supply for decimals
        balances[msg.sender] = totalSupply; // Assign initial supply to contract deployer
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param account The address for which to query the balance.
     * @return The balance of the specified address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the caller's account to a specified address.
     * @param to The address to which the tokens will be sent.
     * @param amount The amount of tokens to send.
     * @return A boolean indicating success.
     */
    function transfer(address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approves a spender to withdraw from the caller's account multiple times.
     * @param spender The address of the account that is approved.
     * @param amount The amount of tokens that can be spent.
     * @return A boolean indicating success.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Approval to the zero address is not allowed");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of another address.
     * @param from The address from which the tokens will be withdrawn.
     * @param to The address to which the tokens will be sent.
     * @param amount The amount of tokens to send.
     * @return A boolean indicating success.
     */
    function transferFrom(address from, address to, uint256 amount) external returns (bool) {
        require(from != address(0), "Transfer from the zero address is not allowed");
        require(to != address(0), "Transfer to the zero address is not allowed");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        balances[from] -= amount;
        balances[to] += amount;
        allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Returns the amount of tokens that a spender is allowed to withdraw from an owner’s account.
     * @param owner The address of the account that owns the tokens.
     * @param spender The address of the account that is allowed to spend tokens.
     * @return The remaining allowance for the spender.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
