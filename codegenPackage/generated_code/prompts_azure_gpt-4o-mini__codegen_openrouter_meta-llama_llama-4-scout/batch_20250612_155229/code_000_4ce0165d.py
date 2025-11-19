"""
Generated Code Metadata:
========================
Original URL: https://owy-wtf.pages.dev
Prompt: Generate a smart contract in Solidity for a functional memecoin similar to Owy, detailing its unique features and functionalities.
Generated: DETERMINISTIC_4ce0165d1b753cc0
Batch ID: 20250612_155229
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title Memecoin Contract
 * @author [Your Name]
 * @notice A functional memecoin contract with unique features and functionalities.
 */
contract Memecoin {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user balances
    mapping (address => uint256) private balances;

    // Mapping of user allowances
    mapping (address => mapping (address => uint256)) private allowances;

    // Total supply of memecoin
    uint256 public totalSupply;

    // Name and symbol of memecoin
    string public name;
    string public symbol;

    // Decimals of memecoin
    uint8 public decimals;

    // Address of the memecoin owner
    address public owner;

    // Event emitted when transfer occurs
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Event emitted when approval occurs
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Event emitted when memecoin is minted
    event Mint(address indexed to, uint256 value);

    // Event emitted when memecoin is burned
    event Burn(address indexed from, uint256 value);

    /**
     * @dev Constructor function
     * @param _name Name of memecoin
     * @param _symbol Symbol of memecoin
     * @param _decimals Decimals of memecoin
     * @param _totalSupply Total supply of memecoin
     */
    constructor(string memory _name, string memory _symbol, uint8 _decimals, uint256 _totalSupply) public {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _totalSupply;
        balances[msg.sender] = _totalSupply;
        owner = msg.sender;
    }

    /**
     * @dev Returns the balance of the specified address
     * @param _owner Address to query
     * @return Balance of _owner
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Transfers tokens from one address to another
     * @param _from Address to transfer from
     * @param _to Address to transfer to
     * @param _value Amount to transfer
     * @return Success
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_value);
        balances[_to] = balances[_to].add(_value);
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approves another address to spend tokens on behalf of the owner
     * @param _spender Address to approve
     * @param _value Amount to approve
     * @return Success
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Returns the allowance of the specified spender for the specified owner
     * @param _owner Owner address
     * @param _spender Spender address
     * @return Allowance
     */
    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Transfers tokens from one address to another, allowed by the owner
     * @param _from Address to transfer from
     * @param _to Address to transfer to
     * @param _value Amount to transfer
     * @param _fee Fee to deduct
     * @return Success
     */
    function transferFrom(address _from, address _to, uint256 _value, uint256 _fee) public returns (bool) {
        require(allowances[_from][msg.sender] >= _value, "Insufficient allowance");
        require(balances[_from] >= _value, "Insufficient balance");
        allowances[_from][msg.sender] = allowances[_from][msg.sender].sub(_value);
        balances[_from] = balances[_from].sub(_value);
        balances[_to] = balances[_to].add(_value.sub(_fee));
        balances[owner] = balances[owner].add(_fee);
        emit Transfer(_from, _to, _value.sub(_fee));
        emit Transfer(_from, owner, _fee);
        return true;
    }

    /**
     * @dev Mints additional tokens
     * @param _to Address to mint to
     * @param _value Amount to mint
     * @return Success
     */
    function mint(address _to, uint256 _value) public returns (bool) {
        require(msg.sender == owner, "Only owner can mint");
        totalSupply = totalSupply.add(_value);
        balances[_to] = balances[_to].add(_value);
        emit Mint(_to, _value);
        emit Transfer(address(0), _to, _value);
        return true;
    }

    /**
     * @dev Burns tokens
     * @param _value Amount to burn
     * @return Success
     */
    function burn(uint256 _value) public returns (bool) {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_value);
        totalSupply = totalSupply.sub(_value);
        emit Burn(msg.sender, _value);
        emit Transfer(msg.sender, address(0), _value);
        return true;
    }
}
```
