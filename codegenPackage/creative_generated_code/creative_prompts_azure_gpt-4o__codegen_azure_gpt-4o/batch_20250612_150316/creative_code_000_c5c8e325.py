"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bibbydivs.com
Prompt: Write a smart contract in Solidity that implements a token investment system with a 2% entry fee, a 2% exit fee, and a dividend redistribution mechanism similar to the $BIBBY ecosystem described on BibbyDivs.com.
Generated: DETERMINISTIC_c5c8e32559171f7f
Batch ID: 20250612_150316
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
 * @title TokenInvestment
 * @dev Token investment system with entry and exit fees and dividend redistribution.
 */
contract TokenInvestment {
    // Declaring the state variables
    string public name = "InvestmentToken";
    string public symbol = "INV";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Entry and exit fees
    uint256 public constant ENTRY_FEE_PERCENT = 2;
    uint256 public constant EXIT_FEE_PERCENT = 2;

    // Tracking dividends
    uint256 public totalDividendsDistributed;
    mapping(address => uint256) private dividendBalance;

    // Events for transparency and logging
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event DividendsDistributed(uint256 amount);
    event DividendsClaimed(address indexed user, uint256 amount);

    // Modifier to ensure sufficient balance
    modifier hasEnoughBalance(address _account, uint256 _amount) {
        require(balances[_account] >= _amount, "Insufficient balance");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10**uint256(decimals));
        balances[msg.sender] = totalSupply;
    }

    /**
     * @dev Transfer tokens with entry and exit fees applied.
     * @param _to Recipient address.
     * @param _amount Amount to transfer.
     */
    function transfer(address _to, uint256 _amount)
        external
        hasEnoughBalance(msg.sender, _amount)
        returns (bool)
    {
        uint256 entryFee = (_amount * ENTRY_FEE_PERCENT) / 100;
        uint256 exitFee = (_amount * EXIT_FEE_PERCENT) / 100;
        uint256 amountAfterFees = _amount - entryFee - exitFee;

        // Distribute fees as dividends
        distributeDividends(entryFee + exitFee);

        // Update balances
        balances[msg.sender] -= _amount;
        balances[_to] += amountAfterFees;

        emit Transfer(msg.sender, _to, amountAfterFees);
        return true;
    }

    /**
     * @dev Approve spending by a third party.
     * @param _spender Address approved to spend.
     * @param _amount Amount approved.
     */
    function approve(address _spender, uint256 _amount) external returns (bool) {
        allowances[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);
        return true;
    }

    /**
     * @dev Transfer from a third party.
     * @param _from Address to transfer from.
     * @param _to Address to transfer to.
     * @param _amount Amount to transfer.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _amount
    ) external hasEnoughBalance(_from, _amount) returns (bool) {
        require(allowances[_from][msg.sender] >= _amount, "Allowance exceeded");

        uint256 entryFee = (_amount * ENTRY_FEE_PERCENT) / 100;
        uint256 exitFee = (_amount * EXIT_FEE_PERCENT) / 100;
        uint256 amountAfterFees = _amount - entryFee - exitFee;

        // Distribute fees as dividends
        distributeDividends(entryFee + exitFee);

        // Update balances and allowances
        balances[_from] -= _amount;
        balances[_to] += amountAfterFees;
        allowances[_from][msg.sender] -= _amount;

        emit Transfer(_from, _to, amountAfterFees);
        return true;
    }

    /**
     * @dev Distributes dividends to all token holders.
     * @param _amount Amount of dividends to distribute.
     */
    function distributeDividends(uint256 _amount) internal {
        require(_amount > 0, "No dividends to distribute");
        totalDividendsDistributed += _amount;

        for (uint256 i = 0; i < totalSupply; i++) {
            address holder = address(uint160(i));
            dividendBalance[holder] += (_amount * balances[holder]) / totalSupply;
        }

        emit DividendsDistributed(_amount);
    }

    /**
     * @dev Claim accumulated dividends.
     */
    function claimDividends() external {
        uint256 claimable = dividendBalance[msg.sender];
        require(claimable > 0, "No dividends to claim");

        dividendBalance[msg.sender] = 0;
        payable(msg.sender).transfer(claimable);

        emit DividendsClaimed(msg.sender, claimable);
    }

    /**
     * @dev Get balance of an account.
     * @param _account Address to query.
     * @return Balance of the account.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Allowance of a spender on behalf of an owner.
     * @param _owner Owner of the tokens.
     * @param _spender Approved spender.
     * @return Remaining allowance.
     */
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
