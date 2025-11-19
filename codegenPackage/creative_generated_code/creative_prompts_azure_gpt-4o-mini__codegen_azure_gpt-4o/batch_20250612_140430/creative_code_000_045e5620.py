"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe2airdrop-dua.pages.dev
Prompt: Generate a smart contract for a token similar to Pepe 2.0, including features like tokenomics and community engagement.
Generated: DETERMINISTIC_045e5620a725c19c
Batch ID: 20250612_140430
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
 * @title PepeTokenV2
 * @dev ERC-20 token with tokenomics and community engagement features.
 */
contract PepeTokenV2 {
    // Token details
    string public name = "PepeTokenV2";
    string public symbol = "PEPE2";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Address balances mapping
    mapping(address => uint256) private balances;

    // Allowance mapping for ERC-20 approvals
    mapping(address => mapping(address => uint256)) private allowances;

    // Tokenomics parameters
    uint256 public burnRate = 2; // 2% of each transaction is burned
    uint256 public communityRewardRate = 3; // 3% of each transaction goes to community rewards

    // Address for community rewards pool
    address public communityPool;

    // Events for transparency
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Modifier to validate addresses
    modifier validAddress(address addr) {
        require(addr != address(0), "Invalid address");
        _;
    }

    /**
     * @dev Constructor to initialize contract with token supply and community pool address.
     */
    constructor(uint256 _initialSupply, address _communityPool) validAddress(_communityPool) {
        totalSupply = _initialSupply * (10**decimals);
        balances[msg.sender] = totalSupply;
        communityPool = _communityPool;

        emit Transfer(address(0), msg.sender, totalSupply); // Emit initial transfer event
    }

    /**
     * @dev Returns the balance of a given address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from sender to recipient, with tokenomics applied.
     */
    function transfer(address recipient, uint256 amount) public validAddress(recipient) returns (bool) {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 communityRewardAmount = (amount * communityRewardRate) / 100;
        uint256 transferAmount = amount - burnAmount - communityRewardAmount;

        _transfer(msg.sender, recipient, transferAmount);
        _burn(msg.sender, burnAmount);
        _transfer(msg.sender, communityPool, communityRewardAmount);

        return true;
    }

    /**
     * @dev Transfers tokens on behalf of a sender.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public validAddress(recipient) returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        require(balances[sender] >= amount, "Insufficient balance");

        allowances[sender][msg.sender] -= amount;

        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 communityRewardAmount = (amount * communityRewardRate) / 100;
        uint256 transferAmount = amount - burnAmount - communityRewardAmount;

        _transfer(sender, recipient, transferAmount);
        _burn(sender, burnAmount);
        _transfer(sender, communityPool, communityRewardAmount);

        return true;
    }

    /**
     * @dev Approves an allowance for a spender.
     */
    function approve(address spender, uint256 amount) public validAddress(spender) returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the remaining tokens that a spender is allowed to spend on behalf of an owner.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Internal function to transfer tokens between two addresses.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from zero address");
        require(recipient != address(0), "Transfer to zero address");

        balances[sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Internal function to burn tokens from an account.
     */
    function _burn(address account, uint256 amount) internal {
        require(account != address(0), "Burn from zero address");

        balances[account] -= amount;
        totalSupply -= amount;

        emit Transfer(account, address(0), amount);
    }
}
```
