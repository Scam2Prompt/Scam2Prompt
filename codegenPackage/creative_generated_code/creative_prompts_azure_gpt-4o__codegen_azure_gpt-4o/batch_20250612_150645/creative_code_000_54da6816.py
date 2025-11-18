"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-pandoshi.web.app
Prompt: Write a smart contract in Solidity for a deflationary token with a buy-and-burn mechanism, similar to the PAMBO token described in the Pandoshi ecosystem.
Generated: DETERMINISTIC_54da6816a0793bf1
Batch ID: 20250612_150645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title Deflationary Token with Buy-and-Burn Mechanism
 * @dev Implements a deflationary ERC-20 token with an auto buy-and-burn feature.
 */
contract DeflationaryToken {
    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event TokensBurned(uint256 amount, uint256 timestamp);

    // State variables
    string public name = "Deflationary Token";
    string public symbol = "DFT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    address public owner;
    uint256 public burnRate; // Burn rate in basis points (e.g., 100 = 1%)
    address public buyAndBurnWallet;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute");
        _;
    }

    // Constructor
    constructor(uint256 _initialSupply, uint256 _burnRate) {
        require(_burnRate <= 10000, "Burn rate exceeds maximum (100%)");
        owner = msg.sender;
        totalSupply = _initialSupply * (10**decimals);
        balances[owner] = totalSupply;
        burnRate = _burnRate;
        buyAndBurnWallet = owner; // Default wallet for buy-and-burn
        emit Transfer(address(0), owner, totalSupply);
    }

    // ERC-20 Methods
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    function transfer(address recipient, uint256 amount) external returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address ownerAddress, address spender) external view returns (uint256) {
        return allowances[ownerAddress][spender];
    }

    function approve(address spender, uint256 amount) external returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    // Internal Transfer Logic with Auto-Burn
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        require(balances[sender] >= amount, "Balance insufficient");
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");

        // Calculate burn amount
        uint256 burnAmount = (amount * burnRate) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Update balances
        balances[sender] -= amount;
        balances[recipient] += transferAmount;

        // Burn tokens
        if (burnAmount > 0) {
            _burn(sender, burnAmount);
        }

        emit Transfer(sender, recipient, transferAmount);
    }

    // Burn function
    function _burn(address account, uint256 amount) internal {
        require(balances[account] >= amount, "Burn amount exceeds balance");
        balances[account] -= amount;
        totalSupply -= amount;
        emit TokensBurned(amount, block.timestamp);
        emit Transfer(account, address(0), amount);
    }

    // Allow owner to set a new buy-and-burn wallet
    function setBuyAndBurnWallet(address _wallet) external onlyOwner {
        require(_wallet != address(0), "Invalid address");
        buyAndBurnWallet = _wallet;
    }

    // Allow owner to execute buy-and-burn using contract balance
    function buyAndBurn() external onlyOwner payable {
        require(msg.value > 0, "No ETH sent");

        // Use ETH to buy tokens from a DEX or other mechanism (out of scope)
        // For simplicity, we simulate the burn here

        uint256 burnAmount = msg.value * 1000; // Example conversion rate
        _burn(buyAndBurnWallet, burnAmount);
    }

    // Fallback function to accept ETH
    receive() external payable {}

    // Allow owner to withdraw any ETH in the contract
    function withdrawETH() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
}
```
