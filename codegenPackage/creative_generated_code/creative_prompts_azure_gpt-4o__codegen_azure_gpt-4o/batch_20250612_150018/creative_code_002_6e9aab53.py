"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orangepepe.pages.dev
Prompt: Generate code in Solidity to create a memecoin similar to $ORPE, including features like zero buy/sell tax and ownership revocation.
Generated: DETERMINISTIC_6e9aab537c3d537d
Batch ID: 20250612_150018
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
 * @title Memecoin Contract
 * @dev This contract implements a simple ERC20 token with zero buy/sell tax and ownership revocation.
 */
contract Memecoin {
    // Token metadata
    string public name = "Memecoin";
    string public symbol = "MEME";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping of balances
    mapping(address => uint256) private balances;
    // Mapping for allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Owner of the contract
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event OwnershipRevoked();

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the token supply and assign it to the deployer.
     * @param _initialSupply The total supply of the token.
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * 10 ** decimals;
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param account The address to query the balance of.
     * @return The balance of the address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specific address.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approves another address to spend tokens on behalf of the sender.
     * @param spender The address authorized to spend.
     * @param amount The amount authorized to spend.
     * @return True if the approval is successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Cannot approve the zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that `spender` is allowed to spend on behalf of `owner`.
     * @param tokenOwner The address of the token owner.
     * @param spender The address of the spender.
     * @return The amount remaining to be spent.
     */
    function allowance(address tokenOwner, address spender) public view returns (uint256) {
        return allowances[tokenOwner][spender];
    }

    /**
     * @dev Transfers tokens from one address to another using allowance.
     * @param from The address to transfer tokens from.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Transfer amount exceeds allowance");

        balances[from] -= amount;
        balances[to] += amount;
        allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Revokes ownership of the contract. This action is irreversible.
     */
    function revokeOwnership() public onlyOwner {
        owner = address(0);
        emit OwnershipRevoked();
    }
}
```
