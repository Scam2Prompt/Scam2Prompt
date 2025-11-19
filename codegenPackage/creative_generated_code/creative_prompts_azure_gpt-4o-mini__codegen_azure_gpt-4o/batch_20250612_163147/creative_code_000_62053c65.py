"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hugfytxytugugvytfuyjgykb.pages.dev
Prompt: Generate a smart contract in Solidity for the $ARBINU token that includes features like liquidity lock and transaction fees as described on the Arbinu website.
Generated: DETERMINISTIC_62053c6576d63124
Batch ID: 20250612_163147
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
 * @title ARBINU Token Contract
 * @dev ERC-20 Token with transaction fees and liquidity lock functionality.
 */
contract ARBINUToken {
    // Token properties
    string public name = "$ARBINU";
    string public symbol = "ARBINU";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000 * 10**decimals; // 1 million tokens

    // Address mappings
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Transaction fee rates
    uint256 public buyFeePercent = 2; // 2% fee on buys
    uint256 public sellFeePercent = 2; // 2% fee on sells

    // Fee collector
    address public feeCollector;

    // Liquidity lock parameters
    bool public liquidityLocked = false;
    uint256 public liquidityLockExpiration;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event LiquidityLocked(uint256 expiration);
    event FeeUpdated(uint256 buyFeePercent, uint256 sellFeePercent);

    // Modifiers
    modifier onlyFeeCollector() {
        require(msg.sender == feeCollector, "Caller is not the fee collector");
        _;
    }

    constructor(address _feeCollector) {
        require(_feeCollector != address(0), "Fee collector address cannot be zero");

        feeCollector = _feeCollector;

        // Allocate the total supply to the contract deployer
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfer tokens with fee deduction.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");

        uint256 fee = calculateFee(amount, sellFeePercent);
        uint256 amountAfterFee = amount - fee;

        balances[msg.sender] -= amount;
        balances[recipient] += amountAfterFee;
        balances[feeCollector] += fee;

        emit Transfer(msg.sender, recipient, amountAfterFee);
        emit Transfer(msg.sender, feeCollector, fee);

        return true;
    }

    /**
     * @dev Approve tokens for spending by a third party.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @dev Transfer tokens from an approved account.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        uint256 fee = calculateFee(amount, sellFeePercent);
        uint256 amountAfterFee = amount - fee;

        balances[sender] -= amount;
        balances[recipient] += amountAfterFee;
        balances[feeCollector] += fee;

        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amountAfterFee);
        emit Transfer(sender, feeCollector, fee);

        return true;
    }

    /**
     * @dev Lock liquidity until a specified expiration timestamp.
     */
    function lockLiquidity(uint256 expirationTimestamp) external onlyFeeCollector {
        require(expirationTimestamp > block.timestamp, "Expiration must be in the future");
        liquidityLocked = true;
        liquidityLockExpiration = expirationTimestamp;

        emit LiquidityLocked(expirationTimestamp);
    }

    /**
     * @dev Update transaction fees.
     */
    function updateFees(uint256 newBuyFee, uint256 newSellFee) external onlyFeeCollector {
        require(newBuyFee <= 10 && newSellFee <= 10, "Fees cannot exceed 10%");
        buyFeePercent = newBuyFee;
        sellFeePercent = newSellFee;

        emit FeeUpdated(newBuyFee, newSellFee);
    }

    /**
     * @dev Calculate transaction fee based on given fee percentage.
     */
    function calculateFee(uint256 amount, uint256 feePercent) internal pure returns (uint256) {
        return (amount * feePercent) / 100;
    }

    /**
     * @dev Returns the balance of an account.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Returns the allowance of a spender for a specific owner.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
