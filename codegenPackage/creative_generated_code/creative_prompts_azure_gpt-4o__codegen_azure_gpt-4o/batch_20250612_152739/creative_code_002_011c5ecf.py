"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://backup-ar.pages.dev
Prompt: Generate a smart contract template for an ERC-20 token using DTORO Studio, including functionality for airdrops and discounted rates for diamond status holders.
Generated: DETERMINISTIC_011c5ecff278def1
Batch ID: 20250612_152739
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
 * @title ERC-20 Token with Airdrop and Diamond Status Discount
 * @dev Implements standard ERC-20 functionality with additional features for airdrops and discounted rates.
 */
contract CustomERC20Token {
    // Token details
    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;

    // Mapping for balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Diamond status mapping
    mapping(address => bool) public isDiamondStatus;

    // Event declarations
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Airdrop(address indexed recipient, uint256 value);
    event DiamondStatusDiscountApplied(address indexed recipient, uint256 discount);

    // Constructor to initialize the token
    constructor(
        string memory _name,
        string memory _symbol,
        uint8 _decimals,
        uint256 _initialSupply
    ) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _initialSupply * (10**uint256(_decimals));
        balances[msg.sender] = totalSupply;

        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // Returns the balance of a given account
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    // Transfers tokens from the sender to another account
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(balances[msg.sender] >= amount, "ERC20: insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    // Approves another account to spend tokens on behalf of the sender
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "ERC20: approve to the zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Transfers tokens from one account to another
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool) {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(balances[sender] >= amount, "ERC20: insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "ERC20: allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    // Returns the allowance of a spender for a given owner
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    // Airdrop functionality to distribute tokens to multiple recipients
    function airdrop(address[] calldata recipients, uint256 value) public returns (bool) {
        require(value > 0, "Airdrop: value must be greater than zero");
        uint256 totalAirdrop = value * recipients.length;
        require(balances[msg.sender] >= totalAirdrop, "Airdrop: insufficient balance");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            require(recipient != address(0), "Airdrop: recipient is zero address");

            balances[msg.sender] -= value;
            balances[recipient] += value;

            emit Airdrop(recipient, value);
        }
        return true;
    }

    // Set Diamond status for an address
    function setDiamondStatus(address account, bool status) public {
        require(account != address(0), "Diamond Status: invalid address");
        isDiamondStatus[account] = status;
    }

    // Apply a discount for Diamond status holders during transfers
    function transferWithDiscount(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "ERC20: transfer to the zero address");
        uint256 discount = isDiamondStatus[msg.sender] ? amount / 10 : 0; // 10% discount for Diamond status holders
        uint256 finalAmount = amount - discount;
        require(balances[msg.sender] >= finalAmount, "ERC20: insufficient balance");

        balances[msg.sender] -= finalAmount;
        balances[recipient] += finalAmount;

        if (discount > 0) {
            emit DiamondStatusDiscountApplied(msg.sender, discount);
        }

        emit Transfer(msg.sender, recipient, finalAmount);
        return true;
    }
}
```
