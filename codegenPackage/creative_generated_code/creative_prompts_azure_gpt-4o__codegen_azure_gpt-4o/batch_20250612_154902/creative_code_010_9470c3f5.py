"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudo-protocol.xyz
Prompt: Develop a smart contract in Solidity for Crudo Protocol's tokenomics, ensuring proper allocation of tokens for presale, rewards, marketing, and ecosystem operations as described in the roadmap.
Generated: DETERMINISTIC_9470c3f5f5cf9f3a
Batch ID: 20250612_154902
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
 * @title CrudoToken
 * @dev ERC20-compliant token with tokenomics for presale, rewards, marketing, and ecosystem operations.
 */
contract CrudoToken {
    // Token details
    string public constant name = "CrudoToken";
    string public constant symbol = "CRUDO";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Allocation percentages
    uint256 public constant PRESALE_PERCENT = 25; // 25%
    uint256 public constant REWARDS_PERCENT = 35; // 35%
    uint256 public constant MARKETING_PERCENT = 20; // 20%
    uint256 public constant ECOSYSTEM_PERCENT = 20; // 20%

    // Allocation balances
    uint256 public presaleAllocation;
    uint256 public rewardsAllocation;
    uint256 public marketingAllocation;
    uint256 public ecosystemAllocation;

    // Token balances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Owner of the contract
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only contract owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the token and allocate balances.
     * @param _totalSupply Total supply of the token.
     */
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero");

        owner = msg.sender;
        totalSupply = _totalSupply;

        // Calculate allocations based on percentages
        presaleAllocation = (_totalSupply * PRESALE_PERCENT) / 100;
        rewardsAllocation = (_totalSupply * REWARDS_PERCENT) / 100;
        marketingAllocation = (_totalSupply * MARKETING_PERCENT) / 100;
        ecosystemAllocation = (_totalSupply * ECOSYSTEM_PERCENT) / 100;

        // Allocate tokens to owner for distribution
        balances[owner] = _totalSupply;

        emit Transfer(address(0), owner, _totalSupply);
    }

    /**
     * @dev Get the balance of a specific address.
     * @param account Address to query the balance of.
     * @return uint256 Representing the balance of the given address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfer tokens from sender to recipient.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return bool Success status of the transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Cannot transfer to zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);

        return true;
    }

    /**
     * @dev Approve an address to spend tokens on behalf of the sender.
     * @param spender Address allowed to spend tokens.
     * @param amount Amount of tokens to approve for spending.
     * @return bool Success status of the approval.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Cannot approve zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance mechanism.
     * @param sender Address from which tokens are transferred.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return bool Success status of the transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Cannot transfer from zero address");
        require(recipient != address(0), "Cannot transfer to zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);

        return true;
    }

    /**
     * @dev Check the allowance of a spender for a specific owner.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     * @return uint256 Remaining allowance for the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Allocate presale tokens to an address.
     * @param recipient Address to receive the presale tokens.
     * @param amount Amount of tokens to allocate.
     */
    function allocatePresaleTokens(address recipient, uint256 amount) public onlyOwner {
        require(recipient != address(0), "Cannot allocate to zero address");
        require(amount <= presaleAllocation, "Amount exceeds presale allocation");

        balances[owner] -= amount;
        balances[recipient] += amount;
        presaleAllocation -= amount;

        emit Transfer(owner, recipient, amount);
    }

    /**
     * @dev Allocate rewards tokens to an address.
     * @param recipient Address to receive the rewards tokens.
     * @param amount Amount of tokens to allocate.
     */
    function allocateRewardsTokens(address recipient, uint256 amount) public onlyOwner {
        require(recipient != address(0), "Cannot allocate to zero address");
        require(amount <= rewardsAllocation, "Amount exceeds rewards allocation");

        balances[owner] -= amount;
        balances[recipient] += amount;
        rewardsAllocation -= amount;

        emit Transfer(owner, recipient, amount);
    }

    /**
     * @dev Allocate marketing tokens to an address.
     * @param recipient Address to receive the marketing tokens.
     * @param amount Amount of tokens to allocate.
     */
    function allocateMarketingTokens(address recipient, uint256 amount) public onlyOwner {
        require(recipient != address(0), "Cannot allocate to zero address");
        require(amount <= marketingAllocation, "Amount exceeds marketing allocation");

        balances[owner] -= amount;
        balances[recipient] += amount;
        marketingAllocation -= amount;

        emit Transfer(owner, recipient, amount);
    }

    /**
     * @dev Allocate ecosystem tokens to an address.
     * @param recipient Address to receive the ecosystem tokens.
     * @param amount Amount of tokens to allocate.
     */
    function allocateEcosystemTokens(address recipient, uint256 amount) public onlyOwner {
        require(recipient != address(0), "Cannot allocate to zero address");
        require(amount <= ecosystemAllocation, "Amount exceeds ecosystem allocation");

        balances[owner] -= amount;
        balances[recipient] += amount;
        ecosystemAllocation -= amount;

        emit Transfer(owner, recipient, amount);
    }
}
```
