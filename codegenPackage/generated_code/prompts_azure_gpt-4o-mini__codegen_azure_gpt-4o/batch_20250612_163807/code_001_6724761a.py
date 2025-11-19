"""
Generated Code Metadata:
========================
Original URL: https://basedonpepe.pages.dev
Prompt: Write a code snippet for a smart contract that mimics the features of Based $PEPE, including 0% tax and liquidity locking.
Generated: DETERMINISTIC_6724761aa1250a95
Batch ID: 20250612_163807
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
 * @title BasedPEPE Token
 * @dev ERC20 token with 0% tax and liquidity locking functionality.
 */
contract BasedPEPE {
    // Token details
    string public name = "BasedPEPE";
    string public symbol = "BPEPE";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000_000 * (10 ** uint256(decimals)); // 1 billion tokens

    // Mapping to track balances
    mapping(address => uint256) private balances;
    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Liquidity lock variables
    address public liquidityLocker;
    uint256 public liquidityUnlockTime;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Modifier to check liquidity lock
    modifier onlyLiquidityLocker() {
        require(msg.sender == liquidityLocker, "Only liquidity locker can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the token and assign all tokens to the deployer.
     */
    constructor() {
        balances[msg.sender] = totalSupply;
        liquidityLocker = msg.sender; // Assign deployer as liquidity locker
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfer tokens from sender to recipient.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     * @return success True if the transfer is successful.
     */
    function transfer(address recipient, uint256 amount) external returns (bool success) {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        require(recipient != address(0), "Cannot transfer to zero address");

        // Perform transfer
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve a spender to spend tokens on behalf of the owner.
     * @param spender Address of the spender.
     * @param amount Amount of tokens to approve.
     * @return success True if the approval is successful.
     */
    function approve(address spender, uint256 amount) external returns (bool success) {
        require(spender != address(0), "Cannot approve zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param sender Address of the sender.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     * @return success True if the transfer is successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool success) {
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        require(recipient != address(0), "Cannot transfer to zero address");

        // Perform transfer
        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Get the balance of an account.
     * @param account Address of the account.
     * @return balance Balance of the account.
     */
    function balanceOf(address account) external view returns (uint256 balance) {
        return balances[account];
    }

    /**
     * @dev Get the allowance of a spender for a specific owner.
     * @param owner Address of the owner.
     * @param spender Address of the spender.
     * @return remaining Remaining allowance.
     */
    function allowance(address owner, address spender) external view returns (uint256 remaining) {
        return allowances[owner][spender];
    }

    /**
     * @dev Lock liquidity until a specific timestamp.
     * @param unlockTime Timestamp when liquidity can be unlocked.
     */
    function lockLiquidity(uint256 unlockTime) external onlyLiquidityLocker {
        require(unlockTime > block.timestamp, "Unlock time must be in the future");
        liquidityUnlockTime = unlockTime;
    }

    /**
     * @dev Unlock liquidity if the unlock time has passed.
     */
    function unlockLiquidity() external onlyLiquidityLocker {
        require(block.timestamp >= liquidityUnlockTime, "Liquidity is still locked");
        liquidityUnlockTime = 0; // Reset unlock time
    }
}
```
