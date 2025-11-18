"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erc20-eth.vip
Prompt: Write a Solidity function for an ERC-20 token contract that calculates transaction fees, suitable for DeFi applications.
Generated: DETERMINISTIC_cac5d7aa5d0bb805
Batch ID: 20250612_154002
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
 * @title ERC-20 Token with Transaction Fee
 * @author Your Name
 * @notice This contract includes functionality to calculate transaction fees suitable for DeFi applications.
 */
contract ERC20WithFees {
    string public name = "ExampleToken";
    string public symbol = "EXT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Fee rate expressed in basis points (e.g., 100 = 1%, 250 = 2.5%)
    uint256 public feeRateBasisPoints = 100; // Default fee is 1%.

    // Address to collect transaction fees
    address public feeRecipient;

    /**
     * @notice Event emitted whenever a transfer occurs.
     */
    event Transfer(address indexed from, address indexed to, uint256 value);

    /**
     * @notice Event emitted whenever transaction fees are updated.
     */
    event FeeRateUpdated(uint256 oldFeeRate, uint256 newFeeRate);

    /**
     * @notice Constructor initializes the token supply and fee recipient.
     */
    constructor(uint256 _initialSupply, address _feeRecipient) {
        require(_feeRecipient != address(0), "Fee recipient cannot be the zero address");
        totalSupply = _initialSupply * 10**decimals;
        balances[msg.sender] = totalSupply;
        feeRecipient = _feeRecipient;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @notice Get the token balance of a specific address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @notice Transfer tokens to a specified address while charging a fee.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return success Returns true if the transfer is successful.
     */
    function transfer(address recipient, uint256 amount) external returns (bool success) {
        require(recipient != address(0), "Recipient cannot be the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Calculate the fee and net amount
        uint256 fee = (amount * feeRateBasisPoints) / 10000;
        uint256 netAmount = amount - fee;

        require(feeRecipient != address(0), "Fee recipient is not set");

        // Update balances
        balances[msg.sender] -= amount;
        balances[recipient] += netAmount;
        balances[feeRecipient] += fee;

        // Emit Transfer events
        emit Transfer(msg.sender, recipient, netAmount);
        emit Transfer(msg.sender, feeRecipient, fee);

        return true;
    }

    /**
     * @notice Update the transaction fee rate.
     * @param newFeeRateBasisPoints The new fee rate in basis points.
     */
    function updateFeeRate(uint256 newFeeRateBasisPoints) external {
        require(newFeeRateBasisPoints <= 1000, "Fee rate cannot exceed 10% (1000 basis points)");
        require(msg.sender == feeRecipient, "Only the fee recipient can update the fee rate");

        uint256 oldFeeRate = feeRateBasisPoints;
        feeRateBasisPoints = newFeeRateBasisPoints;

        emit FeeRateUpdated(oldFeeRate, newFeeRateBasisPoints);
    }

    /**
     * @notice Approve another address to spend tokens on your behalf.
     * @param spender The address authorized to spend tokens.
     * @param amount The maximum amount they are allowed to spend.
     * @return success Returns true if the approval is successful.
     */
    function approve(address spender, uint256 amount) external returns (bool success) {
        require(spender != address(0), "Spender cannot be the zero address");
        allowances[msg.sender][spender] = amount;
        return true;
    }

    /**
     * @notice Transfer tokens on behalf of another address (requires prior approval).
     * @param sender The address from which tokens are transferred.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return success Returns true if the transfer is successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool success) {
        require(sender != address(0), "Sender cannot be the zero address");
        require(recipient != address(0), "Recipient cannot be the zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        // Calculate the fee and net amount
        uint256 fee = (amount * feeRateBasisPoints) / 10000;
        uint256 netAmount = amount - fee;

        require(feeRecipient != address(0), "Fee recipient is not set");

        // Update balances and allowances
        balances[sender] -= amount;
        balances[recipient] += netAmount;
        balances[feeRecipient] += fee;
        allowances[sender][msg.sender] -= amount;

        // Emit Transfer events
        emit Transfer(sender, recipient, netAmount);
        emit Transfer(sender, feeRecipient, fee);

        return true;
    }

    /**
     * @notice Get the remaining allowance a spender has for an owner.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
