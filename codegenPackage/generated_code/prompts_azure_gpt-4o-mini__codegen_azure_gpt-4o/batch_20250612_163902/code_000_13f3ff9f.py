"""
Generated Code Metadata:
========================
Original URL: https://fudthepug.pages.dev
Prompt: Generate a smart contract in Solidity for the Simon’s Cat Token ($CAT) that includes tokenomics features such as presale investors and liquidity allocation.
Generated: DETERMINISTIC_13f3ff9fffd8be8b
Batch ID: 20250612_163902
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
 * @title Simon's Cat Token ($CAT)
 * @dev ERC20 token with tokenomics features such as presale investors and liquidity allocation.
 */
contract SimonsCatToken {
    // ERC20 standard variables
    string public name = "Simon's Cat Token";
    string public symbol = "CAT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Address mappings
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Tokenomics variables
    uint256 public presaleAllocation;
    uint256 public liquidityAllocation;
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the token and allocate presale and liquidity tokens.
     * @param _totalSupply Total supply of the token.
     * @param _presaleAllocation Amount allocated for presale investors.
     * @param _liquidityAllocation Amount allocated for liquidity.
     */
    constructor(
        uint256 _totalSupply,
        uint256 _presaleAllocation,
        uint256 _liquidityAllocation
    ) {
        require(
            _presaleAllocation + _liquidityAllocation <= _totalSupply,
            "Allocations exceed total supply"
        );

        owner = msg.sender;
        totalSupply = _totalSupply;
        presaleAllocation = _presaleAllocation;
        liquidityAllocation = _liquidityAllocation;

        // Allocate presale and liquidity tokens to the owner
        balances[owner] = _totalSupply;
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account Address to query the balance of.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
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
     * @param spender Address to approve.
     * @param amount Amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using allowance.
     * @param sender Address to transfer tokens from.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool) {
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
     * @dev Returns the remaining allowance for a spender.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     */
    function allowance(address owner, address spender)
        public
        view
        returns (uint256)
    {
        return allowances[owner][spender];
    }

    /**
     * @dev Allocates presale tokens to a specific address.
     * @param investor Address of the presale investor.
     * @param amount Amount of tokens to allocate.
     */
    function allocatePresaleTokens(address investor, uint256 amount)
        public
        onlyOwner
    {
        require(investor != address(0), "Allocate to the zero address");
        require(amount <= presaleAllocation, "Exceeds presale allocation");

        presaleAllocation -= amount;
        balances[owner] -= amount;
        balances[investor] += amount;

        emit Transfer(owner, investor, amount);
    }

    /**
     * @dev Allocates liquidity tokens to a specific address.
     * @param liquidityProvider Address of the liquidity provider.
     * @param amount Amount of tokens to allocate.
     */
    function allocateLiquidityTokens(address liquidityProvider, uint256 amount)
        public
        onlyOwner
    {
        require(liquidityProvider != address(0), "Allocate to the zero address");
        require(amount <= liquidityAllocation, "Exceeds liquidity allocation");

        liquidityAllocation -= amount;
        balances[owner] -= amount;
        balances[liquidityProvider] += amount;

        emit Transfer(owner, liquidityProvider, amount);
    }
}
```
