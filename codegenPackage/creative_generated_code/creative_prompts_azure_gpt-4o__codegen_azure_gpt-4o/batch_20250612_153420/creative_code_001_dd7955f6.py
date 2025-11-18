"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-inqubeta.pages.dev
Prompt: Generate Solidity code for a smart contract that implements the QUBE tokenomics, including buy and sell taxes, rewards pool allocation, and token burning mechanisms as described on the InQubeta platform.
Generated: DETERMINISTIC_dd7955f61ddc3f6e
Batch ID: 20250612_153420
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
 * @title QUBE Tokenomics Smart Contract
 * @dev Implements buy/sell tax, rewards pool allocation, and token burning mechanisms.
 */
contract QUBEToken {
    // State variables
    string public name = "QUBE Token";
    string public symbol = "QUBE";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000_000 * 10**uint256(decimals); // 1 billion tokens

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    address public owner;
    address public rewardsPool;

    uint256 public buyTaxPercentage = 5; // 5% buy tax
    uint256 public sellTaxPercentage = 10; // 10% sell tax
    uint256 public burnPercentage = 2; // 2% of tax is burned

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor
    constructor(address _rewardsPool) {
        require(_rewardsPool != address(0), "Rewards pool address cannot be zero");
        owner = msg.sender;
        rewardsPool = _rewardsPool;
        balances[owner] = totalSupply; // Allocate total supply to owner
        emit Transfer(address(0), owner, totalSupply);
    }

    // ERC-20 Functions
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    // Private transfer helper with tax, rewards, and burn logic
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) private {
        require(balances[sender] >= amount, "Transfer amount exceeds balance");
        require(recipient != address(0), "Transfer to the zero address");

        uint256 taxRate = recipient == rewardsPool ? sellTaxPercentage : buyTaxPercentage; // Determine tax rate
        uint256 taxAmount = (amount * taxRate) / 100; // Calculate tax
        uint256 burnAmount = (taxAmount * burnPercentage) / 100; // Calculate burn amount
        uint256 rewardsAmount = taxAmount - burnAmount; // Remaining tax goes to rewards pool
        uint256 transferAmount = amount - taxAmount; // Amount to be transferred to recipient

        balances[sender] -= amount;
        balances[recipient] += transferAmount;
        balances[rewardsPool] += rewardsAmount; // Send rewards to rewards pool
        totalSupply -= burnAmount; // Burn tokens by reducing supply

        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, rewardsPool, rewardsAmount);
        emit Transfer(sender, address(0), burnAmount); // Burn event as transfer to address(0)
    }

    // Owner functions
    function updateBuyTaxPercentage(uint256 newBuyTax) external onlyOwner {
        require(newBuyTax <= 100, "Tax percentage cannot exceed 100");
        buyTaxPercentage = newBuyTax;
    }

    function updateSellTaxPercentage(uint256 newSellTax) external onlyOwner {
        require(newSellTax <= 100, "Tax percentage cannot exceed 100");
        sellTaxPercentage = newSellTax;
    }

    function updateBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 100, "Burn percentage cannot exceed 100");
        burnPercentage = newBurnPercentage;
    }

    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    function updateRewardsPool(address newRewardsPool) external onlyOwner {
        require(newRewardsPool != address(0), "Rewards pool address cannot be zero");
        rewardsPool = newRewardsPool;
    }
}
```
