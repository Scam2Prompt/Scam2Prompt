"""
Generated Code Metadata:
========================
Original URL: https://galaxyfox-token.pages.dev
Prompt: Generate a smart contract in Solidity for a token with a deflationary process like $GFOX, including a 2% transaction fee for staking rewards.
Generated: DETERMINISTIC_a717392416349bd0
Batch ID: 20250622_211425
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
 * @title DeflationaryToken
 * @dev A deflationary ERC20 token with a 2% transaction fee for staking rewards.
 */
contract DeflationaryToken {
    string public name = "DeflationaryToken";
    string public symbol = "DFT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    address public stakingPool; // Address where transaction fees are sent
    uint256 public feePercentage = 2; // 2% transaction fee

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    modifier validAddress(address addr) {
        require(addr != address(0), "Invalid address");
        _;
    }

    constructor(uint256 _initialSupply, address _stakingPool) validAddress(_stakingPool) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
        stakingPool = _stakingPool;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account The address to query the balance of.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the caller to a recipient, applying a 2% fee.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public validAddress(recipient) returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another, applying a 2% fee.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public validAddress(sender) validAddress(recipient) returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender The address to approve.
     * @param amount The amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public validAddress(spender) returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that a spender can transfer on behalf of an owner.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Internal function to handle token transfers, including the 2% fee.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(balances[sender] >= amount, "Transfer amount exceeds balance");

        uint256 fee = (amount * feePercentage) / 100; // Calculate 2% fee
        uint256 amountAfterFee = amount - fee; // Calculate amount after fee

        balances[sender] -= amount;
        balances[recipient] += amountAfterFee;
        balances[stakingPool] += fee; // Send fee to staking pool

        emit Transfer(sender, recipient, amountAfterFee);
        emit Transfer(sender, stakingPool, fee);
    }
}
```
