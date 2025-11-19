"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindogsclub-en.pages.dev
Prompt: Develop a smart contract for the $0DOG token that includes features for claiming tokens after the presale ends.
Generated: DETERMINISTIC_94795b2de18db24b
Batch ID: 20250612_161617
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
 * @title $0DOG Token Smart Contract
 * @dev This contract implements an ERC20 token with presale claim functionality.
 */
contract ZeroDogToken {
    // Token details
    string public constant name = "$0DOG";
    string public constant symbol = "0DOG";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Address mappings
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // OnlyOwner functionality
    address public owner;

    // Presale details
    bool public presaleActive = true; // Presale status
    mapping(address => uint256) public presaleAllocations; // Tokens allocated to users during presale

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Claimed(address indexed claimer, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to owner only.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Modifier to check if presale is inactive.
     */
    modifier presaleEnded() {
        require(!presaleActive, "Presale is still active");
        _;
    }

    /**
     * @dev Constructor to initialize the token contract.
     * @param _initialSupply Initial token supply to mint.
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply;
        balances[owner] = _initialSupply;
        emit Transfer(address(0), owner, _initialSupply);
    }

    /**
     * @dev Transfer tokens to a specified address.
     * @param recipient The address to transfer to.
     * @param amount The amount to be transferred.
     * @return success Boolean indicating success of the operation.
     */
    function transfer(address recipient, uint256 amount) external returns (bool success) {
        require(recipient != address(0), "Transfer to zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve a spender to withdraw tokens from owner's account.
     * @param spender The address of the spender.
     * @param amount The amount to be approved.
     * @return success Boolean indicating success of the operation.
     */
    function approve(address spender, uint256 amount) external returns (bool success) {
        require(spender != address(0), "Approve to zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param sender The address of the token sender.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     * @return success Boolean indicating success of the operation.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool success) {
        require(sender != address(0), "Transfer from zero address");
        require(recipient != address(0), "Transfer to zero address");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        require(balances[sender] >= amount, "Insufficient balance");

        balances[sender] -= amount;
        allowances[sender][msg.sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Check the balance of a given account.
     * @param account The address of the account to check.
     * @return balance The balance of the account.
     */
    function balanceOf(address account) external view returns (uint256 balance) {
        return balances[account];
    }

    /**
     * @dev Check the allowance of a spender for a given owner.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     * @return remaining The remaining allowance for the spender.
     */
    function allowance(address owner, address spender) external view returns (uint256 remaining) {
        return allowances[owner][spender];
    }

    /**
     * @dev Set presale allocations for tokens.
     * @param recipient The address to allocate tokens to.
     * @param amount The amount of tokens to allocate.
     */
    function setPresaleAllocation(address recipient, uint256 amount) external onlyOwner {
        require(presaleActive, "Presale has ended");
        presaleAllocations[recipient] = amount;
    }

    /**
     * @dev Claim presale tokens after presale has ended.
     */
    function claimTokens() external presaleEnded {
        uint256 amount = presaleAllocations[msg.sender];
        require(amount > 0, "No tokens allocated for claim");

        presaleAllocations[msg.sender] = 0;
        balances[owner] -= amount;
        balances[msg.sender] += amount;

        emit Claimed(msg.sender, amount);
        emit Transfer(owner, msg.sender, amount);
    }

    /**
     * @dev End the presale.
     */
    function endPresale() external onlyOwner {
        presaleActive = false;
    }

    /**
     * @dev Transfer ownership of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is zero address");

        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
