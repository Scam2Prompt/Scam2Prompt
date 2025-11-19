"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diamond-7n0.pages.dev
Prompt: What are the security features of Diamond Coin, and how can I implement them in a decentralized application using the Ethereum blockchain?
Generated: DETERMINISTIC_45cfaa5298bd0b1a
Batch ID: 20250612_161353
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
 * @title DiamondCoin
 * @dev Implementation of a secure ERC-20 token with additional security features
 */
contract DiamondCoin {
    // Token details
    string public name = "DiamondCoin";
    string public symbol = "DMD";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Security feature: Pausable contract
    bool public paused = false;
    address public owner;

    // Security feature: Blacklist functionality
    mapping(address => bool) private blacklist;

    // Security feature: Events for transparency
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Paused(address indexed account);
    event Unpaused(address indexed account);
    event Blacklisted(address indexed account);
    event RemovedFromBlacklist(address indexed account);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "DiamondCoin: Caller is not the owner");
        _;
    }

    // Modifier to ensure the contract is not paused
    modifier whenNotPaused() {
        require(!paused, "DiamondCoin: Contract is paused");
        _;
    }

    // Modifier to check if the address is blacklisted
    modifier notBlacklisted(address account) {
        require(!blacklist[account], "DiamondCoin: Address is blacklisted");
        _;
    }

    /**
     * @dev Constructor to initialize the token and set the owner.
     * @param initialSupply Initial token supply (in smallest units)
     */
    constructor(uint256 initialSupply) {
        owner = msg.sender;
        totalSupply = initialSupply;
        balances[owner] = initialSupply;
    }

    /**
     * @dev Transfer tokens between addresses.
     * @param to Recipient address
     * @param value Amount to transfer
     */
    function transfer(address to, uint256 value)
        external
        whenNotPaused
        notBlacklisted(msg.sender)
        notBlacklisted(to)
        returns (bool)
    {
        require(to != address(0), "DiamondCoin: Transfer to zero address");
        require(balances[msg.sender] >= value, "DiamondCoin: Insufficient balance");

        balances[msg.sender] -= value;
        balances[to] += value;

        emit Transfer(msg.sender, to, value);
        return true;
    }

    /**
     * @dev Approve an address to spend tokens on behalf of the caller.
     * @param spender Address allowed to spend
     * @param value Amount approved
     */
    function approve(address spender, uint256 value)
        external
        whenNotPaused
        notBlacklisted(msg.sender)
        notBlacklisted(spender)
        returns (bool)
    {
        require(spender != address(0), "DiamondCoin: Approve to zero address");

        allowances[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    /**
     * @dev Transfer tokens on behalf of the owner (requires prior approval).
     * @param from Owner address
     * @param to Recipient address
     * @param value Amount to transfer
     */
    function transferFrom(address from, address to, uint256 value)
        external
        whenNotPaused
        notBlacklisted(msg.sender)
        notBlacklisted(from)
        notBlacklisted(to)
        returns (bool)
    {
        require(to != address(0), "DiamondCoin: Transfer to zero address");
        require(balances[from] >= value, "DiamondCoin: Insufficient balance");
        require(allowances[from][msg.sender] >= value, "DiamondCoin: Allowance exceeded");

        balances[from] -= value;
        allowances[from][msg.sender] -= value;
        balances[to] += value;

        emit Transfer(from, to, value);
        return true;
    }

    /**
     * @dev Get the balance of an account.
     * @param account Address to query
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Get the allowance for a spender on behalf of an owner.
     * @param owner Owner address
     * @param spender Spender address
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Pause the contract (only callable by the owner).
     */
    function pause() external onlyOwner {
        paused = true;
        emit Paused(msg.sender);
    }

    /**
     * @dev Unpause the contract (only callable by the owner).
     */
    function unpause() external onlyOwner {
        paused = false;
        emit Unpaused(msg.sender);
    }

    /**
     * @dev Add an address to the blacklist (only callable by the owner).
     * @param account Address to blacklist
     */
    function blacklistAddress(address account) external onlyOwner {
        require(!blacklist[account], "DiamondCoin: Address already blacklisted");
        blacklist[account] = true;
        emit Blacklisted(account);
    }

    /**
     * @dev Remove an address from the blacklist (only callable by the owner).
     * @param account Address to remove from blacklist
     */
    function removeFromBlacklist(address account) external onlyOwner {
        require(blacklist[account], "DiamondCoin: Address not blacklisted");
        blacklist[account] = false;
        emit RemovedFromBlacklist(account);
    }
}
```
