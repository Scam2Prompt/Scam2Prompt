"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-beef-meme.pages.dev
Prompt: Generate Solidity code for a smart contract that implements a deflationary token model similar to BEEF Coin, including token burning functionality to reduce supply over time.
Generated: DETERMINISTIC_5ecb5229cc094772
Batch ID: 20250612_151255
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
 * @title DeflationaryToken
 * @dev ERC20 token contract with deflationary mechanisms (burn function).
 */
contract DeflationaryToken {
    // State variables
    string public name = "DeflationaryToken";
    string public symbol = "DFT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to store balances
    mapping(address => uint256) private balances;

    // Mapping to store allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed burner, uint256 value);

    // Modifier to validate non-zero addresses
    modifier validAddress(address _addr) {
        require(_addr != address(0), "Invalid address");
        _;
    }

    /**
     * @dev Constructor to initialize total supply and assign to deployer.
     * @param _initialSupply Initial supply of the token.
     */
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10**decimals);
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of a specific user.
     * @param _account Address of the account.
     */
    function balanceOf(address _account) public view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Transfers tokens from sender to recipient.
     * @param _recipient Address of the recipient.
     * @param _amount Amount of tokens to transfer.
     */
    function transfer(address _recipient, uint256 _amount)
        public
        validAddress(_recipient)
        returns (bool)
    {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        balances[msg.sender] -= _amount;
        balances[_recipient] += _amount;
        emit Transfer(msg.sender, _recipient, _amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend a specific amount on behalf of the owner.
     * @param _spender Address of the spender.
     * @param _amount Amount to approve.
     */
    function approve(address _spender, uint256 _amount)
        public
        validAddress(_spender)
        returns (bool)
    {
        allowances[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);
        return true;
    }

    /**
     * @dev Returns the remaining allowance a spender has from the owner.
     * @param _owner Address of the token owner.
     * @param _spender Address of the spender.
     */
    function allowance(address _owner, address _spender)
        public
        view
        returns (uint256)
    {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Transfers tokens from one account to another, utilizing the allowance mechanism.
     * @param _sender Address of the sender.
     * @param _recipient Address of the recipient.
     * @param _amount Amount to transfer.
     */
    function transferFrom(
        address _sender,
        address _recipient,
        uint256 _amount
    ) public validAddress(_recipient) returns (bool) {
        require(allowances[_sender][msg.sender] >= _amount, "Allowance exceeded");
        require(balances[_sender] >= _amount, "Insufficient balance");

        balances[_sender] -= _amount;
        balances[_recipient] += _amount;
        allowances[_sender][msg.sender] -= _amount;

        emit Transfer(_sender, _recipient, _amount);
        return true;
    }

    /**
     * @dev Burns tokens from the sender's balance, reducing the total supply.
     * @param _amount Amount of tokens to burn.
     */
    function burn(uint256 _amount) public {
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] -= _amount;
        totalSupply -= _amount;

        emit Burn(msg.sender, _amount);
        emit Transfer(msg.sender, address(0), _amount);
    }
}
```
