"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axieinfi-nity.github.io
Prompt: Create a smart contract on Ethereum that mimics the Axie Infinity "play-to-earn" model, allowing players to earn tokens based on in-game activities.
Generated: DETERMINISTIC_671bda10948de0e9
Batch ID: 20250612_151525
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
 * @title PlayToEarnToken
 * @dev A smart contract that mimics the Axie Infinity "play-to-earn" model,
 * allowing players to earn tokens based on in-game activities.
 */
contract PlayToEarnToken {
    // The token symbol and name
    string public constant name = "PlayToEarnToken";
    string public constant symbol = "PET";

    // Total supply of the tokens
    uint256 public totalSupply;

    // Number of decimals for the token
    uint8 public constant decimals = 18;

    // Mapping to track balances of player addresses
    mapping(address => uint256) public balances;

    // Mapping to allow token transfers via approval mechanism
    mapping(address => mapping(address => uint256)) public allowances;

    // Owner of the contract (game administrator)
    address public owner;

    // Event to notify when tokens are minted
    event TokensEarned(address indexed player, uint256 amount);

    // Event to notify when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 amount);

    // Event to notify when approval is granted
    event Approval(address indexed owner, address indexed spender, uint256 amount);

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * Sets the owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function for the game administrator to mint tokens for players.
     * @param player Address of the player earning the tokens.
     * @param amount Amount of tokens to mint.
     */
    function earnTokens(address player, uint256 amount) external onlyOwner {
        require(player != address(0), "Invalid player address");
        require(amount > 0, "Amount must be greater than zero");

        // Mint tokens and update balances
        totalSupply += amount;
        balances[player] += amount;

        emit TokensEarned(player, amount);
    }

    /**
     * @dev Function to transfer tokens between addresses.
     * @param to Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update balances
        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Function to approve another address to spend tokens on behalf of the caller.
     * @param spender Address to approve tokens for.
     * @param amount Amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Invalid spender address");

        // Set allowance
        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Function to transfer tokens using the allowance mechanism.
     * @param from Address to transfer tokens from.
     * @param to Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) external returns (bool) {
        require(from != address(0), "Invalid sender address");
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        // Update balances and allowance
        balances[from] -= amount;
        balances[to] += amount;
        allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Function to check the balance of a given address.
     * @param account Address to check the balance for.
     * @return Balance of the given address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Function to check the allowance of a spender for a given account.
     * @param account Address of the token owner.
     * @param spender Address of the spender.
     * @return Remaining allowance for the spender.
     */
    function allowance(address account, address spender) external view returns (uint256) {
        return allowances[account][spender];
    }
}
```
