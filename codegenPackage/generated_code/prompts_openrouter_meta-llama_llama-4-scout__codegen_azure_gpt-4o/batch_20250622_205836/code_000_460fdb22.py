"""
Generated Code Metadata:
========================
Original URL: https://supertruimpcoin.xyz
Prompt: Write a smart contract in Solidity for a tokenomics system with a 0.3% tax, 0.8% allocation to a specific wallet, and a total supply of 2.6 billion tokens.
Generated: DETERMINISTIC_460fdb2247212b48
Batch ID: 20250622_205836
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
 * @title TokenomicsToken
 * @dev ERC20-compliant token with tax and allocation mechanisms.
 */
contract TokenomicsToken {
    // Token details
    string public constant name = "TokenomicsToken";
    string public constant symbol = "TKT";
    uint8 public constant decimals = 18;
    uint256 public constant totalSupply = 2_600_000_000 * (10 ** uint256(decimals));

    // State variables
    address public owner;
    address public allocationWallet;
    uint256 public taxRate = 30; // 0.3% (scaled by 100 for precision)
    uint256 public allocationRate = 80; // 0.8% (scaled by 100 for precision)
    uint256 public constant RATE_DENOMINATOR = 10_000; // Used for percentage calculations

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _allocationWallet Address to receive the allocation percentage.
     */
    constructor(address _allocationWallet) {
        require(_allocationWallet != address(0), "Invalid allocation wallet address");
        owner = msg.sender;
        allocationWallet = _allocationWallet;
        balances[owner] = totalSupply; // Assign total supply to the owner
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account Address to query the balance of.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the caller to a recipient, applying tax and allocation.
     * @param recipient Address to receive the tokens.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender Address to be approved.
     * @param amount Amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another, applying tax and allocation.
     * @param sender Address to send tokens from.
     * @param recipient Address to receive the tokens.
     * @param amount Amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining allowance for a spender.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Internal function to handle token transfers, applying tax and allocation.
     * @param sender Address to send tokens from.
     * @param recipient Address to receive the tokens.
     * @param amount Amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[sender] >= amount, "Transfer amount exceeds balance");

        // Calculate tax and allocation amounts
        uint256 taxAmount = (amount * taxRate) / RATE_DENOMINATOR;
        uint256 allocationAmount = (amount * allocationRate) / RATE_DENOMINATOR;
        uint256 transferAmount = amount - taxAmount - allocationAmount;

        // Update balances
        balances[sender] -= amount;
        balances[recipient] += transferAmount;
        balances[allocationWallet] += allocationAmount;
        balances[owner] += taxAmount; // Tax is sent to the contract owner

        // Emit transfer events
        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, allocationWallet, allocationAmount);
        emit Transfer(sender, owner, taxAmount);
    }

    /**
     * @dev Allows the owner to update the allocation wallet address.
     * @param newAllocationWallet New address for allocation.
     */
    function updateAllocationWallet(address newAllocationWallet) external onlyOwner {
        require(newAllocationWallet != address(0), "Invalid allocation wallet address");
        allocationWallet = newAllocationWallet;
    }

    /**
     * @dev Allows the owner to update the tax rate.
     * @param newTaxRate New tax rate (scaled by 100).
     */
    function updateTaxRate(uint256 newTaxRate) external onlyOwner {
        require(newTaxRate <= RATE_DENOMINATOR, "Tax rate exceeds maximum");
        taxRate = newTaxRate;
    }

    /**
     * @dev Allows the owner to update the allocation rate.
     * @param newAllocationRate New allocation rate (scaled by 100).
     */
    function updateAllocationRate(uint256 newAllocationRate) external onlyOwner {
        require(newAllocationRate <= RATE_DENOMINATOR, "Allocation rate exceeds maximum");
        allocationRate = newAllocationRate;
    }
}
```
