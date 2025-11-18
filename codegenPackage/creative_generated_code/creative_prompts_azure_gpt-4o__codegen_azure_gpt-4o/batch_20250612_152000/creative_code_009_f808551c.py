"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rtt23423.pages.dev
Prompt: Write a smart contract for issuing stablecoins backed by tokenized treasuries, modeled after Ondo Finance's OUSG stablecoin.
Generated: DETERMINISTIC_f808551ca55aa39b
Batch ID: 20250612_152000
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
 * @title Stablecoin backed by tokenized treasuries
 * @notice This contract allows for the issuance of stablecoins backed by tokenized treasury assets.
 * @dev This code is modeled after Ondo Finance's OUSG stablecoin. Follow best practices and review carefully before deploying in production.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
}

contract TokenizedTreasuryStablecoin {
    // Variables
    address public owner; // Owner of the contract
    IERC20 public treasuryToken; // Tokenized treasury asset
    string public name = "Treasury Backed Stablecoin"; // Stablecoin name
    string public symbol = "TBS"; // Stablecoin symbol
    uint8 public decimals = 18; // Stablecoin decimals
    uint256 public totalSupply; // Total supply of stablecoins

    mapping(address => uint256) private balances; // Mapping of account balances
    mapping(address => mapping(address => uint256)) private allowances; // Allowances for transfers

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event StablecoinMinted(address indexed to, uint256 amount);
    event StablecoinBurned(address indexed from, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(IERC20 _treasuryToken) {
        owner = msg.sender;
        treasuryToken = _treasuryToken;
    }

    /**
     * @notice Mint stablecoins by depositing tokenized treasury assets
     * @param amount The amount of stablecoins to mint
     * @dev Users must approve the transfer of the treasuryToken before calling this function
     */
    function mint(uint256 amount) external {
        require(amount > 0, "Mint amount must be greater than zero");

        // Transfer treasuryToken from user to contract as collateral
        bool success = treasuryToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Treasury token transfer failed");

        // Mint corresponding stablecoins to the user
        balances[msg.sender] += amount;
        totalSupply += amount;

        emit StablecoinMinted(msg.sender, amount);
    }

    /**
     * @notice Burn stablecoins to retrieve tokenized treasury assets
     * @param amount The amount of stablecoins to burn
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient stablecoin balance");

        // Burn stablecoins
        balances[msg.sender] -= amount;
        totalSupply -= amount;

        // Return treasuryToken to user
        bool success = treasuryToken.transfer(msg.sender, amount);
        require(success, "Treasury token transfer failed");

        emit StablecoinBurned(msg.sender, amount);
    }

    // ERC20 Functions

    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Cannot transfer to zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Cannot approve zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(sender != address(0), "Sender cannot be zero address");
        require(recipient != address(0), "Recipient cannot be zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    function allowance(address _owner, address spender) external view returns (uint256) {
        return allowances[_owner][spender];
    }

    // Emergency withdrawal feature for owner
    function emergencyWithdrawTreasuryTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot withdraw to zero address");
        bool success = treasuryToken.transfer(to, amount);
        require(success, "Treasury token transfer failed");
    }
}
```
