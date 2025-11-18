"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ratotheratcoin.com
Prompt: Generate code to deploy a cryptocurrency token named "Rato the Rat" ($RATO) on the Ethereum blockchain, ensuring it matches the specifications provided (e.g., supply, tax settings, and contract address).
Generated: DETERMINISTIC_58e7b0b048770c70
Batch ID: 20250612_154131
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

// ERC-20 Standard Interface
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

// $RATO Token Contract
contract RatoTheRatToken is IERC20 {
    // Token details
    string public constant name = "Rato the Rat";
    string public constant symbol = "RATO";
    uint8 public constant decimals = 18;

    // Total supply of tokens
    uint256 private _totalSupply;

    // Balances and allowances mappings
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Tax settings
    uint256 public taxRate; // Tax rate in percentage (e.g., 2 means 2%)
    address public taxRecipient; // Address where tax funds will be sent

    // Owner of the contract
    address public owner;

    // Events for ownership management
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 initialSupply, uint256 _taxRate, address _taxRecipient) {
        require(_taxRate <= 100, "Tax rate must be between 0 and 100");
        require(_taxRecipient != address(0), "Tax recipient must be a valid address");
        
        _totalSupply = initialSupply * 10**decimals; // Convert initial supply to smallest units
        _balances[msg.sender] = _totalSupply; // Assign all tokens to the deployer
        
        taxRate = _taxRate; // Set the tax rate
        taxRecipient = _taxRecipient; // Set the tax recipient
        owner = msg.sender; // Set the contract owner

        emit Transfer(address(0), msg.sender, _totalSupply); // Emit transfer event for initial supply
    }

    // ERC-20 functions

    // Returns the total supply of tokens
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    // Returns the balance of a given account
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    // Transfers tokens to another address
    function transfer(address recipient, uint256 amount) external override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    // Returns the allowance of a spender for a specific owner
    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // Approves a spender to transfer tokens on behalf of the owner
    function approve(address spender, uint256 amount) external override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Transfers tokens on behalf of an owner to a recipient
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(_allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");
        _allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    // Internal transfer function with tax deduction
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Sender address cannot be zero");
        require(recipient != address(0), "Recipient address cannot be zero");
        require(_balances[sender] >= amount, "Transfer amount exceeds balance");

        uint256 taxAmount = (amount * taxRate) / 100; // Calculate tax amount
        uint256 netAmount = amount - taxAmount; // Calculate net amount after tax

        _balances[sender] -= amount; // Deduct full amount from sender
        _balances[taxRecipient] += taxAmount; // Send tax to tax recipient
        _balances[recipient] += netAmount; // Send net amount to recipient

        emit Transfer(sender, taxRecipient, taxAmount); // Emit transfer event for tax
        emit Transfer(sender, recipient, netAmount); // Emit transfer event for net amount
    }

    // Updates the tax rate
    function setTaxRate(uint256 newTaxRate) external onlyOwner {
        require(newTaxRate <= 100, "Tax rate must be between 0 and 100");
        taxRate = newTaxRate;
    }

    // Updates the tax recipient address
    function setTaxRecipient(address newTaxRecipient) external onlyOwner {
        require(newTaxRecipient != address(0), "Tax recipient must be a valid address");
        taxRecipient = newTaxRecipient;
    }

    // Transfers ownership of the contract to a new address
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
