"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Write a Solidity contract for a stablecoin that maintains its value pegged to the US dollar, using the principles described on Ethereum.org.
Generated: DETERMINISTIC_f9c611e48cc863ee
Batch ID: 20250612_151948
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
 * @title StableCoin
 * @dev A basic implementation of a USD-pegged stablecoin.
 */
contract StableCoin {
    // Total supply of the stablecoin
    uint256 private _totalSupply;

    // Mapping from address to balance
    mapping(address => uint256) private _balances;

    // Mapping from owner to spender allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Name and symbol of the stablecoin
    string public constant name = "Stable USD";
    string public constant symbol = "SUSD";
    uint8 public constant decimals = 18;

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Emitted when tokens are transferred.
     */
    event Transfer(address indexed from, address indexed to, uint256 value);

    /**
     * @dev Emitted when an approval is made.
     */
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to set the contract deployer as the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Returns the total supply of the stablecoin.
     */
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param account The address to query the balance of.
     */
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param recipient The address to transfer to.
     * @param amount The amount to transfer.
     * @return True if the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend on behalf of the caller.
     * @param spender The address to approve.
     * @param amount The amount to approve.
     * @return True if the approval was successful.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        _allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the remaining amount a spender is allowed to spend on behalf of the owner.
     * @param owner Address of the owner.
     * @param spender Address of the spender.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Transfers tokens on behalf of the owner.
     * @param sender The address to transfer from.
     * @param recipient The address to transfer to.
     * @param amount The amount to transfer.
     * @return True if the transfer was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Mints new stablecoins, increasing the total supply.
     * @param account The address to mint to.
     * @param amount The amount to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Mint to the zero address");

        _totalSupply += amount;
        _balances[account] += amount;

        emit Transfer(address(0), account, amount);
    }

    /**
     * @dev Burns stablecoins, reducing the total supply.
     * @param account The address to burn from.
     * @param amount The amount to burn.
     */
    function burn(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Burn from the zero address");
        require(_balances[account] >= amount, "Insufficient balance");

        _totalSupply -= amount;
        _balances[account] -= amount;

        emit Transfer(account, address(0), amount);
    }
}
```
