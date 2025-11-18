"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bingomeme.pages.dev
Prompt: Provide an example of a smart contract for a community-led meme cryptocurrency like $BINGO, including features for low transaction taxes and total supply management.
Generated: DETERMINISTIC_3692e5c9d53d1e10
Batch ID: 20250612_153517
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
 * @title MemeCoin - Community-led cryptocurrency smart contract
 * @dev This smart contract implements a basic ERC20 token with additional features like
 * low transaction taxes and total supply management. Built for community-driven meme coins.
 */
contract MemeCoin {
    // Token details
    string public constant name = "Bingo Coin";
    string public constant symbol = "BINGO";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // State variables
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Transaction tax (e.g., 1% tax)
    uint256 public constant transactionTaxPercent = 1;
    
    // Tax beneficiary (e.g., community fund wallet)
    address public taxBeneficiary;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize the token
    constructor(uint256 _initialSupply, address _taxBeneficiary) {
        require(_initialSupply > 0, "Initial supply must be greater than zero.");
        require(_taxBeneficiary != address(0), "Invalid tax beneficiary address.");

        totalSupply = _initialSupply * 10**decimals; // Scale supply to token decimals
        balances[msg.sender] = totalSupply; // Assign all tokens to contract deployer
        taxBeneficiary = _taxBeneficiary; // Set tax beneficiary

        emit Transfer(address(0), msg.sender, totalSupply); // Emit initial supply event
    }

    // Public function to check balance of an address
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    // Public function to transfer tokens
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    // Public function to approve an allowance
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Cannot approve to zero address.");
        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Public function to check allowance
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    // Public function for transferFrom (used for spending allowances)
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded.");
        _transfer(sender, recipient, amount);
        allowances[sender][msg.sender] -= amount;
        return true;
    }

    // Internal function to handle transfers with tax
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        require(sender != address(0), "Transfer from zero address.");
        require(recipient != address(0), "Transfer to zero address.");
        require(balances[sender] >= amount, "Insufficient balance.");

        uint256 taxAmount = (amount * transactionTaxPercent) / 100;
        uint256 netAmount = amount - taxAmount;

        // Update balances
        balances[sender] -= amount;
        balances[recipient] += netAmount;
        balances[taxBeneficiary] += taxAmount;

        emit Transfer(sender, recipient, netAmount);
        emit Transfer(sender, taxBeneficiary, taxAmount);
    }

    // Public function to increase total supply (community-driven, controlled by owner/admin)
    function mint(uint256 amount) public {
        require(msg.sender == taxBeneficiary, "Only tax beneficiary can mint.");
        require(amount > 0, "Mint amount must be greater than zero.");

        uint256 scaledAmount = amount * 10**decimals; // Scale to token decimals
        totalSupply += scaledAmount;
        balances[msg.sender] += scaledAmount;

        emit Transfer(address(0), msg.sender, scaledAmount);
    }

    // Public function to burn tokens (reduce supply)
    function burn(uint256 amount) public {
        require(amount > 0, "Burn amount must be greater than zero.");
        require(balances[msg.sender] >= amount, "Insufficient balance to burn.");

        uint256 scaledAmount = amount * 10**decimals; // Scale to token decimals
        totalSupply -= scaledAmount;
        balances[msg.sender] -= scaledAmount;

        emit Transfer(msg.sender, address(0), scaledAmount);
    }
}
```
