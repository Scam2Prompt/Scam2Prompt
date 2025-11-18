"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-screator-ethereum666.pages.dev
Prompt: Provide a Solidity template for creating a token with customizable liquidity and tax fee parameters, compatible with a platform offering full token ownership.
Generated: DETERMINISTIC_dedf4691574b3c35
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
 * @title CustomizableToken
 * @dev ERC20 token with configurable liquidity and tax fee mechanisms.
 *      This contract allows full ownership and control to the token owner.
 */
contract CustomizableToken {
    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // State variables
    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;

    address public owner;

    uint256 public liquidityFee; // Fee percentage for liquidity (e.g., 2%)
    uint256 public taxFee;       // Fee percentage for tax (e.g., 1%)

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor
    constructor(
        string memory _name,
        string memory _symbol,
        uint8 _decimals,
        uint256 _initialSupply,
        uint256 _liquidityFee,
        uint256 _taxFee
    ) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _initialSupply * 10**uint256(_decimals);

        owner = msg.sender;
        balances[owner] = totalSupply;

        liquidityFee = _liquidityFee;
        taxFee = _taxFee;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfers tokens from caller to a recipient, deducting fees.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves another address to spend tokens on behalf of the caller.
     * @param spender Address allowed to spend tokens.
     * @param amount Amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another, deducting fees.
     * @param sender Address to send tokens from.
     * @param recipient Address to send tokens to.
     * @param amount Amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Internal function to handle token transfers with fees.
     * @param sender Address to send tokens from.
     * @param recipient Address to send tokens to.
     * @param amount Amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[sender] >= amount, "Insufficient balance");

        uint256 liquidityAmount = (amount * liquidityFee) / 100;
        uint256 taxAmount = (amount * taxFee) / 100;
        uint256 transferAmount = amount - liquidityAmount - taxAmount;

        balances[sender] -= amount;
        balances[recipient] += transferAmount;
        balances[owner] += liquidityAmount + taxAmount; // Owner collects fees

        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, owner, liquidityAmount + taxAmount); // Fee transfer
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account Address to query.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Returns the remaining allowance for a spender.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Allows owner to update the liquidity fee.
     * @param _liquidityFee New liquidity fee percentage.
     */
    function updateLiquidityFee(uint256 _liquidityFee) external onlyOwner {
        liquidityFee = _liquidityFee;
    }

    /**
     * @dev Allows owner to update the tax fee.
     * @param _taxFee New tax fee percentage.
     */
    function updateTaxFee(uint256 _taxFee) external onlyOwner {
        taxFee = _taxFee;
    }

    /**
     * @dev Allows owner to withdraw collected fees.
     */
    function withdrawFees() external onlyOwner {
        uint256 ownerBalance = balances[owner];
        require(ownerBalance > 0, "No fees to withdraw");
        balances[owner] = 0;
        payable(owner).transfer(ownerBalance);
    }

    /**
     * @dev Allows owner to renounce ownership (irreversible).
     */
    function renounceOwnership() external onlyOwner {
        owner = address(0);
    }

    /**
     * @dev Fallback function to handle ETH transfers.
     */
    receive() external payable {}
}
```
