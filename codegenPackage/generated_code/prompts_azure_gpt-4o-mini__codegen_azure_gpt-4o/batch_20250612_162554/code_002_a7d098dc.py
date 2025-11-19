"""
Generated Code Metadata:
========================
Original URL: https://grokxcoinai.com
Prompt: Create a Solidity smart contract for the $GROK Coin that includes triple-layer security features and ensures audited transactions as per CertiK and SlowMist standards.
Generated: DETERMINISTIC_a7d098dce2ee08a0
Batch ID: 20250612_162554
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
 * @title GROK Coin Smart Contract
 * @dev Implements ERC20 token standard with triple-layer security features
 *      and transaction auditing mechanisms.
 */
contract GROKCoin {
    // Token details
    string public name = "$GROK Coin";
    string public symbol = "GROK";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to store balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Security features: Whitelist, Blacklist, and Pausable
    mapping(address => bool) private whitelist;
    mapping(address => bool) private blacklist;
    bool private paused;

    // Owner of the contract
    address public owner;

    // Events for logging
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Paused();
    event Unpaused();
    event Whitelisted(address indexed account);
    event Blacklisted(address indexed account);
    event RemovedFromBlacklist(address indexed account);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Modifier to check if the contract is paused
    modifier whenNotPaused() {
        require(!paused, "Contract is paused");
        _;
    }

    // Modifier to check if the sender is whitelisted
    modifier onlyWhitelisted(address account) {
        require(whitelist[account], "Account is not whitelisted");
        _;
    }

    // Modifier to check if the sender is not blacklisted
    modifier notBlacklisted(address account) {
        require(!blacklist[account], "Account is blacklisted");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with initial supply and owner.
     * @param initialSupply Initial token supply
     */
    constructor(uint256 initialSupply) {
        owner = msg.sender;
        totalSupply = initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply;

        // Automatically whitelist the owner
        whitelist[owner] = true;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfer tokens from sender to recipient.
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount)
        external
        whenNotPaused
        onlyWhitelisted(msg.sender)
        notBlacklisted(msg.sender)
        notBlacklisted(recipient)
        returns (bool)
    {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        require(recipient != address(0), "Invalid recipient address");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve spender to spend tokens on behalf of the sender.
     * @param spender Address of the spender
     * @param amount Amount of tokens to approve
     */
    function approve(address spender, uint256 amount)
        external
        whenNotPaused
        onlyWhitelisted(msg.sender)
        notBlacklisted(msg.sender)
        notBlacklisted(spender)
        returns (bool)
    {
        require(spender != address(0), "Invalid spender address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one account to another.
     * @param sender Address of the sender
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to transfer
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    )
        external
        whenNotPaused
        onlyWhitelisted(sender)
        notBlacklisted(sender)
        notBlacklisted(recipient)
        returns (bool)
    {
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        require(recipient != address(0), "Invalid recipient address");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Get the balance of an account.
     * @param account Address of the account
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Get the allowance of a spender for a specific owner.
     * @param owner Address of the owner
     * @param spender Address of the spender
     */
    function allowance(address owner, address spender)
        external
        view
        returns (uint256)
    {
        return allowances[owner][spender];
    }

    /**
     * @dev Pause the contract (only owner).
     */
    function pause() external onlyOwner {
        paused = true;
        emit Paused();
    }

    /**
     * @dev Unpause the contract (only owner).
     */
    function unpause() external onlyOwner {
        paused = false;
        emit Unpaused();
    }

    /**
     * @dev Add an account to the whitelist (only owner).
     * @param account Address to whitelist
     */
    function addToWhitelist(address account) external onlyOwner {
        whitelist[account] = true;
        emit Whitelisted(account);
    }

    /**
     * @dev Add an account to the blacklist (only owner).
     * @param account Address to blacklist
     */
    function addToBlacklist(address account) external onlyOwner {
        blacklist[account] = true;
        emit Blacklisted(account);
    }

    /**
     * @dev Remove an account from the blacklist (only owner).
     * @param account Address to remove from blacklist
     */
    function removeFromBlacklist(address account) external onlyOwner {
        blacklist[account] = false;
        emit RemovedFromBlacklist(account);
    }
}
```
