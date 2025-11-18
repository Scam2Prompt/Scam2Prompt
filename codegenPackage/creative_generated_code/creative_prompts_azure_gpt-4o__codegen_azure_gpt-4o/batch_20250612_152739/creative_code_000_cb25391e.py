"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-de.web.app
Prompt: Write a smart contract in Solidity for an ERC20 token with features similar to $MGLS, including zero buy/sell tax and staking functionality.
Generated: DETERMINISTIC_cb25391eb3c2f56c
Batch ID: 20250612_152739
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
 * @title ERC20 Token with Staking Functionality
 * @dev Implements an ERC20 token with zero buy/sell tax and staking features.
 */
contract MGLSToken {
    // Token metadata
    string public name = "MGLSToken";
    string public symbol = "MGLS";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances mapping
    mapping(address => uint256) public balances;
    // Allowed transfers mapping
    mapping(address => mapping(address => uint256)) public allowances;
    // Staking balances mapping
    mapping(address => uint256) public stakedBalances;

    // Events declaration
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);

    // Constructor for initializing total supply and assigning it to the contract deployer
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** decimals);
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfers tokens from the sender to the recipient.
     * @param _to Address of the recipient.
     * @param _value Amount of tokens to transfer.
     * @return Boolean indicating success.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Invalid address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the sender.
     * @param _spender Address of the spender.
     * @param _value Amount to approve.
     * @return Boolean indicating success.
     */
    function approve(address _spender, uint256 _value) external returns (bool) {
        require(_spender != address(0), "Invalid address");
        
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another.
     * @param _from Address of the sender.
     * @param _to Address of the recipient.
     * @param _value Amount of tokens to transfer.
     * @return Boolean indicating success.
     */
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool) {
        require(_from != address(0) && _to != address(0), "Invalid address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        balances[_from] -= _value;
        balances[_to] += _value;
        allowances[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Stakes a certain amount of tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] -= _amount;
        stakedBalances[msg.sender] += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstakes a certain amount of tokens.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        stakedBalances[msg.sender] -= _amount;
        balances[msg.sender] += _amount;

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Returns the balance of an account.
     * @param _account Address of the account.
     * @return Balance of the account.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Returns the staked balance of an account.
     * @param _account Address of the account.
     * @return Staked balance of the account.
     */
    function stakedBalanceOf(address _account) external view returns (uint256) {
        return stakedBalances[_account];
    }
}
```
