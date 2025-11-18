"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minkycoin.pages.dev
Prompt: Create a Solidity-based token contract that includes a feature for distributing airdrops, similar to the $MINKY token's 10% allocation.
Generated: DETERMINISTIC_9a071c1067e78d9f
Batch ID: 20250612_145715
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
 * @title AirdropToken
 * @dev ERC-20 Token with an airdrop mechanism. Includes 10% of token supply reserved for airdrops.
 */
contract AirdropToken {
    // State variables
    string public name = "AirdropToken";
    string public symbol = "ADT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    address public owner;
    uint256 public airdropAllocation; // 10% of total supply for airdrops
    uint256 public airdroppedAmount; // Tracks the total amount airdropped

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event AirdropDistributed(address indexed recipient, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");

        owner = msg.sender;
        totalSupply = _initialSupply * 10**uint256(decimals);
        airdropAllocation = (totalSupply * 10) / 100; // 10% for airdrop
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    // Get token balance of an account
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    // Transfer tokens to another account
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    // Approve an allowance for a spender
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Spender cannot be the zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Check the allowance of a spender for a specific owner
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    // Transfer tokens from one account to another using an allowance
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    // Internal function to handle transfers
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Sender cannot be the zero address");
        require(recipient != address(0), "Recipient cannot be the zero address");
        require(balances[sender] >= amount, "Transfer amount exceeds balance");

        balances[sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
    }

    // Distribute tokens as an airdrop to a list of recipients
    function distributeAirdrop(address[] memory recipients, uint256[] memory amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts arrays must have the same length");

        for (uint256 i = 0; i < recipients.length; i++) {
            uint256 amount = amounts[i];
            address recipient = recipients[i];

            require(airdroppedAmount + amount <= airdropAllocation, "Airdrop allocation exceeded");
            require(recipient != address(0), "Cannot airdrop to the zero address");

            airdroppedAmount += amount;
            _transfer(owner, recipient, amount);

            emit AirdropDistributed(recipient, amount);
        }
    }
}
```
