"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreator.pages.dev
Prompt: Write a Solidity smart contract for creating a custom token with liquidity and tax fee, similar to the functionality described on Tokens Creator, ensuring 100% token ownership.
Generated: DETERMINISTIC_0232b139356601b6
Batch ID: 20250612_145916
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
 * @title CustomToken
 * @dev A simple ERC20 token with liquidity and tax fee functionality.
 */
contract CustomToken {
    string public name = "CustomToken";
    string public symbol = "CTKN";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    address public owner;

    uint256 public taxFeePercent; // Tax fee in percentage
    uint256 public liquidityFeePercent; // Liquidity fee in percentage
    address public liquidityWallet;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize token supply and fees.
     * @param _initialSupply Initial supply of the token.
     * @param _taxFeePercent Tax fee percentage (e.g., 2 means 2%).
     * @param _liquidityFeePercent Liquidity fee percentage (e.g., 3 means 3%).
     * @param _liquidityWallet Address where liquidity fees will be sent.
     */
    constructor(
        uint256 _initialSupply,
        uint256 _taxFeePercent,
        uint256 _liquidityFeePercent,
        address _liquidityWallet
    ) {
        require(_taxFeePercent + _liquidityFeePercent <= 100, "Total fees cannot exceed 100%");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be zero address");

        owner = msg.sender;
        taxFeePercent = _taxFeePercent;
        liquidityFeePercent = _liquidityFeePercent;
        liquidityWallet = _liquidityWallet;

        totalSupply = _initialSupply * 10**uint256(decimals);
        _balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Returns the balance of a given account.
     * @param account Address of the account to query.
     */
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Transfers tokens from the caller to a recipient with fees deducted.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Allows a spender to withdraw tokens from the caller's account multiple times, up to the specified amount.
     * @param spender Address authorized to spend tokens.
     * @param amount Maximum amount of tokens spender can withdraw.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of an account with fees deducted.
     * @param sender Address transferring tokens.
     * @param recipient Address receiving tokens.
     * @param amount Amount to transfer.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool) {
        require(_allowances[sender][msg.sender] >= amount, "Transfer exceeds allowance");
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }

    /**
     * @dev Internal function to handle token transfers with fees.
     * @param sender Address transferring tokens.
     * @param recipient Address receiving tokens.
     * @param amount Amount to transfer.
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        require(sender != address(0), "Transfer from zero address");
        require(recipient != address(0), "Transfer to zero address");
        require(_balances[sender] >= amount, "Transfer amount exceeds balance");

        uint256 taxFee = (amount * taxFeePercent) / 100;
        uint256 liquidityFee = (amount * liquidityFeePercent) / 100;
        uint256 transferAmount = amount - taxFee - liquidityFee;

        _balances[sender] -= amount;
        _balances[recipient] += transferAmount;
        _balances[liquidityWallet] += liquidityFee;

        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, liquidityWallet, liquidityFee); // Emit event for liquidity fee
    }

    /**
     * @dev Internal function to approve a spender to withdraw tokens.
     * @param owner Address owning tokens.
     * @param spender Address authorized to spend tokens.
     * @param amount Maximum amount spender can withdraw.
     */
    function _approve(
        address owner,
        address spender,
        uint256 amount
    ) internal {
        require(owner != address(0), "Approve from zero address");
        require(spender != address(0), "Approve to zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    /**
     * @dev Returns the allowance a spender has to spend from an owner's account.
     * @param owner Address owning tokens.
     * @param spender Address authorized to spend tokens.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Allows the owner to update the tax and liquidity fee percentages.
     * @param _taxFeePercent Tax fee percentage.
     * @param _liquidityFeePercent Liquidity fee percentage.
     */
    function updateFees(uint256 _taxFeePercent, uint256 _liquidityFeePercent) public onlyOwner {
        require(_taxFeePercent + _liquidityFeePercent <= 100, "Total fees cannot exceed 100%");
        taxFeePercent = _taxFeePercent;
        liquidityFeePercent = _liquidityFeePercent;
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        owner = newOwner;
    }
}
```
