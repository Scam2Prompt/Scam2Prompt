"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoreumdashboard.com
Prompt: Generate a code snippet to implement a smart contract for a hyper deflationary token similar to $THOREUM, incorporating a daily supply burn mechanism.
Generated: DETERMINISTIC_e88cfceabeb40b4c
Batch ID: 20250612_155503
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
 * @title HyperDeflationaryToken
 * @dev A smart contract implementing a hyper deflationary token with a daily supply burn mechanism.
 */
contract HyperDeflationaryToken {
    // Token details
    string public name = "HyperDeflationaryToken";
    string public symbol = "HDT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mappings for balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Burn mechanism variables
    uint256 public dailyBurnRate; // Percentage of total supply to burn daily
    uint256 public lastBurnTimestamp;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(uint256 amount);

    // Owner of the contract
    address public owner;

    // Modifiers
    modifier onlyOwner() {
        require(owner == msg.sender, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the token's total supply, daily burn rate, and assign the initial supply to the owner.
     * @param _initialSupply Initial supply of the token.
     * @param _dailyBurnRate Daily burn rate percentage (must be <= 100).
     */
    constructor(uint256 _initialSupply, uint256 _dailyBurnRate) {
        require(_dailyBurnRate <= 100, "Burn rate must be <= 100");

        totalSupply = _initialSupply * 10**decimals;
        dailyBurnRate = _dailyBurnRate;
        owner = msg.sender;
        balances[owner] = totalSupply;
        lastBurnTimestamp = block.timestamp;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfers tokens from sender to recipient.
     * @param _to The recipient of the tokens.
     * @param _value The amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        _updateDailyBurn();

        require(_to != address(0), "Invalid recipient address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approves a spender to spend the specified amount on behalf of the sender.
     * @param _spender The address which is allowed to spend the tokens.
     * @param _value The amount of tokens to allow.
     */
    function approve(address _spender, uint256 _value) external returns (bool) {
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of the token owner to a recipient.
     * @param _from The address to transfer from.
     * @param _to The recipient of the tokens.
     * @param _value The amount of tokens to transfer.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) external returns (bool) {
        _updateDailyBurn();

        require(_to != address(0), "Invalid recipient address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        balances[_from] -= _value;
        allowances[_from][msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Returns the balance of the given address.
     * @param _account The address to query the balance for.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Returns the remaining allowance for a spender.
     * @param _owner The owner of the tokens.
     * @param _spender The spender.
     */
    function allowance(address _owner, address _spender)
        external
        view
        returns (uint256)
    {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Updates the daily burn mechanism, burning tokens if 24 hours have passed since the last burn.
     */
    function _updateDailyBurn() internal {
        if (block.timestamp >= lastBurnTimestamp + 1 days) {
            uint256 burnAmount = (totalSupply * dailyBurnRate) / 100;
            totalSupply -= burnAmount;
            balances[owner] -= burnAmount;
            lastBurnTimestamp = block.timestamp;

            emit Burn(burnAmount);
        }
    }

    /**
     * @dev Allows the contract owner to set a new daily burn rate.
     * @param _newBurnRate New daily burn rate percentage (must be <= 100).
     */
    function setDailyBurnRate(uint256 _newBurnRate) external onlyOwner {
        require(_newBurnRate <= 100, "Burn rate must be <= 100");
        dailyBurnRate = _newBurnRate;
    }
}
```
