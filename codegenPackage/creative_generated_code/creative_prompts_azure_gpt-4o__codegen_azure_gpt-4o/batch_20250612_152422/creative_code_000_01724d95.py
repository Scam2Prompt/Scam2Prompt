"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://funkybunnies.pages.dev
Prompt: Write code to generate a custom ERC-20 token named "Funky Bunnies" with unique properties and deploy it to the Ethereum blockchain.
Generated: DETERMINISTIC_01724d95d0281686
Batch ID: 20250612_152422
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
 * @title FunkyBunniesToken
 * @dev Implementation of a standard ERC-20 token with custom token properties.
 * @dev This contract follows the ERC-20 standard and includes basic functionality.
 */
contract FunkyBunniesToken {
    // State variables for token details
    string public name = "Funky Bunnies"; // Name of the token
    string public symbol = "FBT";         // Symbol for the token
    uint8 public decimals = 18;           // Number of decimal places
    uint256 public totalSupply;           // Total supply of the token

    // Mapping to keep track of balances
    mapping(address => uint256) private balances;

    // Mapping to keep track of allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events for logging activities
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the token supply and assign it to the deployer.
     * @param _initialSupply Initial supply of tokens (in smallest unit, e.g., wei).
     */
    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = _initialSupply;
        balances[msg.sender] = _initialSupply; // Assign all tokens to the deployer
        emit Transfer(address(0), msg.sender, _initialSupply); // Emit transfer event from minting
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param account Address to query balance for.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from caller to a specific address.
     * @param recipient Address to transfer tokens to.
     * @param amount Number of tokens to transfer.
     * @return Boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance for transfer");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount); // Emit transfer event
        return true;
    }

    /**
     * @dev Approves a spender to use a specific amount of tokens.
     * @param spender Address allowed to spend tokens.
     * @param amount Number of tokens spender is allowed to use.
     * @return Boolean indicating success.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approval for the zero address is not allowed");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount); // Emit approval event
        return true;
    }

    /**
     * @dev Returns the allowance for a spender on behalf of an owner.
     * @param owner Address of the token owner.
     * @param spender Address of the token spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Transfers tokens on behalf of an owner (requires prior approval).
     * @param sender Address of the token owner.
     * @param recipient Address to transfer tokens to.
     * @param amount Number of tokens to transfer.
     * @return Boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[sender] >= amount, "Insufficient balance for transfer");
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount); // Emit transfer event
        return true;
    }
}
```

To deploy this contract, you can use tools like Remix IDE or hardhat/truffle with a connected Ethereum wallet. Make sure to set the `_initialSupply` parameter in the constructor when deploying.
