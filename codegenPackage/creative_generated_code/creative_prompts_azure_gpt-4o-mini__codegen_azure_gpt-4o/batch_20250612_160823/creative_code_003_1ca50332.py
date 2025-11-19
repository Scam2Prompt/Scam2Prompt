"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdccash.xyz
Prompt: Generate a Solidity code snippet for a token that distributes USDC reflections to holders like the $UPRINT token.
Generated: DETERMINISTIC_1ca5033273f16c93
Batch ID: 20250612_160823
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
 * @title Reflective USDC Token
 * @dev A token contract that distributes USDC reflections to holders.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract ReflectiveUSDC {
    string public name = "Reflective USDC Token";
    string public symbol = "RUSDC";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // USDC token address (ERC20-compatible)
    IERC20 public usdcToken;

    // Reflection tracking variables
    mapping(address => uint256) public reflectionsOwed;
    uint256 public totalReflections;
    uint256 public reflectionRate;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event ReflectionsDistributed(uint256 amount);

    /**
     * @dev Constructor to set initial supply and USDC token address.
     */
    constructor(uint256 _initialSupply, address _usdcTokenAddress) {
        require(_usdcTokenAddress != address(0), "USDC token address cannot be zero");

        usdcToken = IERC20(_usdcTokenAddress);
        totalSupply = _initialSupply;
        _balances[msg.sender] = _initialSupply;

        emit Transfer(address(0), msg.sender, _initialSupply);
    }

    /**
     * @dev Transfer tokens and update reflections owed.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve another address to spend tokens.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(_allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }

    /**
     * @dev Distribute USDC reflections to token holders.
     */
    function distributeReflections(uint256 usdcAmount) external {
        require(usdcToken.transferFrom(msg.sender, address(this), usdcAmount), "Failed to transfer USDC");
        totalReflections += usdcAmount;
        reflectionRate = totalReflections / totalSupply;

        emit ReflectionsDistributed(usdcAmount);
    }

    /**
     * @dev Claim reflections owed to a token holder.
     */
    function claimReflections() external {
        uint256 owed = _balances[msg.sender] * reflectionRate / (10**decimals) - reflectionsOwed[msg.sender];
        require(owed > 0, "No reflections owed");
        reflectionsOwed[msg.sender] += owed;

        require(usdcToken.transfer(msg.sender, owed), "USDC transfer failed");
    }

    /**
     * @dev Internal function to handle token transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Transfer amount exceeds balance");

        _balances[sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Internal function to approve spending allowance.
     */
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "Approve from the zero address");
        require(spender != address(0), "Approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    /**
     * @dev Returns the balance of the specified address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Returns the allowance of a spender for a specific owner.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return _allowances[owner][spender];
    }
}
```
