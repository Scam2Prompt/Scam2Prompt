"""
Generated Code Metadata:
========================
Original URL: https://99bitcoin-presale.pages.dev
Prompt: "Generate a BRC-20 token standard compatible smart contract for a Learn-to-Earn platform like 99Bitcoins."
Generated: DETERMINISTIC_feeee9ad74bb5db7
Batch ID: 20250622_205124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title BRC-20 Token Standard Compatible Smart Contract
 * @dev This contract implements a Learn-to-Earn platform token.
 *      Users can earn tokens by completing educational tasks.
 */
contract LearnToEarnToken {
    // Token details
    string public name = "LearnToEarnToken";
    string public symbol = "LET";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to store balances
    mapping(address => uint256) private balances;

    // Mapping to store allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account The address to query the balance of.
     * @return The balance of the given address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the operation succeeded.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender The address authorized to spend tokens.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating whether the operation succeeded.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the operation succeeded.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that a spender is allowed to spend on behalf of an owner.
     * @param owner The address of the token owner.
     * @param spender The address authorized to spend tokens.
     * @return The remaining allowance.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Mints new tokens to a specified address. Restricted to the contract owner.
     * @param recipient The address to receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address recipient, uint256 amount) public onlyOwner {
        require(recipient != address(0), "Mint to the zero address");

        uint256 mintAmount = amount * (10 ** uint256(decimals));
        totalSupply += mintAmount;
        balances[recipient] += mintAmount;

        emit Transfer(address(0), recipient, mintAmount);
    }

    /**
     * @dev Burns tokens from a specified address. Restricted to the contract owner.
     * @param account The address whose tokens will be burned.
     * @param amount The amount of tokens to burn.
     */
    function burn(address account, uint256 amount) public onlyOwner {
        require(account != address(0), "Burn from the zero address");
        require(balances[account] >= amount, "Insufficient balance to burn");

        uint256 burnAmount = amount * (10 ** uint256(decimals));
        totalSupply -= burnAmount;
        balances[account] -= burnAmount;

        emit Transfer(account, address(0), burnAmount);
    }
}
```
