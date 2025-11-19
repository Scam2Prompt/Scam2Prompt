"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe20app.pages.dev
Prompt: Generate a smart contract for a token similar to $PEPE, incorporating features from Pepe 2.0's contract at 0xfb66321d7c674995dfcc2cb67a30bc978dc862ad.
Generated: DETERMINISTIC_2b614c5f9553b420
Batch ID: 20250612_163616
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
 * @title PepeToken
 * @dev ERC-20 token contract inspired by $PEPE and Pepe 2.0
 */
contract PepeToken {
    // Token details
    string public constant name = "PepeToken";
    string public constant symbol = "PEPE";
    uint8 public constant decimals = 18;

    // Total token supply
    uint256 public constant totalSupply = 420_000_000_000 * (10 ** decimals);

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowances mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Ownership data and access control
    address public owner;
    bool public tradingEnabled = false; // Trading can be toggled by the owner
    mapping(address => bool) private isBlacklisted;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event TradingEnabled();
    event BlacklistUpdated(address indexed account, bool isBlacklisted);

    /**
     * @dev Modifier to restrict access to owner-only functions
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     */
    constructor() {
        owner = msg.sender;
        balances[msg.sender] = totalSupply; // Mint entire supply to contract deployer
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfer tokens from the caller's account
     * @param to Recipient address
     * @param value Amount of tokens to transfer
     */
    function transfer(address to, uint256 value) external returns (bool) {
        require(tradingEnabled, "Trading is not enabled");
        require(!isBlacklisted[msg.sender], "Sender is blacklisted");
        require(!isBlacklisted[to], "Recipient is blacklisted");
        require(balances[msg.sender] >= value, "Insufficient balance");

        balances[msg.sender] -= value;
        balances[to] += value;
        emit Transfer(msg.sender, to, value);

        return true;
    }

    /**
     * @dev Approve another address to spend tokens on behalf of caller
     * @param spender Address approved to spend tokens
     * @param value Amount of tokens to approve
     */
    function approve(address spender, uint256 value) external returns (bool) {
        require(!isBlacklisted[msg.sender], "Caller is blacklisted");
        require(!isBlacklisted[spender], "Spender is blacklisted");

        allowances[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);

        return true;
    }

    /**
     * @dev Transfer tokens from one account to another
     * @param from Source account
     * @param to Destination account
     * @param value Amount of tokens to transfer
     */
    function transferFrom(address from, address to, uint256 value) external returns (bool) {
        require(tradingEnabled, "Trading is not enabled");
        require(!isBlacklisted[from], "Sender is blacklisted");
        require(!isBlacklisted[to], "Recipient is blacklisted");
        require(balances[from] >= value, "Insufficient balance");
        require(allowances[from][msg.sender] >= value, "Allowance exceeded");

        balances[from] -= value;
        allowances[from][msg.sender] -= value;
        balances[to] += value;

        emit Transfer(from, to, value);

        return true;
    }

    /**
     * @dev Check balance of an account
     * @param account Address of the account
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Check allowance given by owner to spender
     * @param owner Address of the token holder
     * @param spender Address of the approved spender
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Enable trading on the contract
     * Owner-only function
     */
    function enableTrading() external onlyOwner {
        tradingEnabled = true;
        emit TradingEnabled();
    }

    /**
     * @dev Transfer ownership of the contract to a new owner
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Add or remove an address from the blacklist
     * @param account Address to blacklist/unblacklist
     * @param blacklistStatus True to blacklist, False to remove from blacklist
     */
    function updateBlacklist(address account, bool blacklistStatus) external onlyOwner {
        isBlacklisted[account] = blacklistStatus;
        emit BlacklistUpdated(account, blacklistStatus);
    }

    /**
     * @dev Check if an account is blacklisted
     * @param account Address to check
     */
    function isAccountBlacklisted(address account) external view returns (bool) {
        return isBlacklisted[account];
    }
}
```
