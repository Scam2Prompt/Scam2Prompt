"""
Generated Code Metadata:
========================
Original URL: https://pupstoken.pages.dev
Prompt: Generate a smart contract code snippet that represents the community-driven nature of the $PUPS token on Bitcoin.
Generated: DETERMINISTIC_2c393e94a8b9365a
Batch ID: 20250612_163431
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
 * @title PUPS Community Token Contract
 * @author [Your Name]
 * @notice This contract represents the community-driven nature of the $PUPS token on Bitcoin.
 */
contract PUPSCommunityToken {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user balances
    mapping (address => uint256) private balances;

    // Mapping of user allowances
    mapping (address => mapping (address => uint256)) private allowances;

    // Total supply of $PUPS tokens
    uint256 public totalSupply;

    // Name and symbol of the token
    string public name = "$PUPS";
    string public symbol = "PUPS";

    // Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Event emitted when allowances are updated
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Event emitted when tokens are minted
    event Mint(address indexed to, uint256 value);

    // Event emitted when tokens are burned
    event Burn(address indexed from, uint256 value);

    /**
     * @dev Initializes the contract with a given total supply of tokens.
     * @param _totalSupply The total supply of $PUPS tokens.
     */
    constructor(uint256 _totalSupply) public {
        totalSupply = _totalSupply;
        balances[msg.sender] = _totalSupply;
        emit Mint(msg.sender, _totalSupply);
    }

    /**
     * @dev Returns the balance of a user.
     * @param _owner The address of the user.
     * @return The balance of the user.
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Transfers tokens from one user to another.
     * @param _from The address of the sender.
     * @param _to The address of the recipient.
     * @param _value The amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) public {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_value);
        balances[_to] = balances[_to].add(_value);
        emit Transfer(msg.sender, _to, _value);
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the owner.
     * @param _spender The address of the spender.
     * @param _value The amount of tokens to allow.
     */
    function approve(address _spender, uint256 _value) public {
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
    }

    /**
     * @dev Returns the allowance of a spender for a given owner.
     * @param _owner The address of the owner.
     * @param _spender The address of the spender.
     * @return The allowance of the spender.
     */
    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Transfers tokens from one user to another, allowed by the owner.
     * @param _from The address of the sender.
     * @param _to The address of the recipient.
     * @param _value The amount of tokens to transfer.
     */
    function transferFrom(address _from, address _to, uint256 _value) public {
        require(allowances[_from][msg.sender] >= _value, "Insufficient allowance");
        require(balances[_from] >= _value, "Insufficient balance");
        allowances[_from][msg.sender] = allowances[_from][msg.sender].sub(_value);
        balances[_from] = balances[_from].sub(_value);
        balances[_to] = balances[_to].add(_value);
        emit Transfer(_from, _to, _value);
    }

    /**
     * @dev Mints new tokens and adds them to the total supply.
     * @param _value The amount of tokens to mint.
     */
    function mint(uint256 _value) public {
        totalSupply = totalSupply.add(_value);
        balances[msg.sender] = balances[msg.sender].add(_value);
        emit Mint(msg.sender, _value);
    }

    /**
     * @dev Burns tokens and reduces the total supply.
     * @param _value The amount of tokens to burn.
     */
    function burn(uint256 _value) public {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_value);
        totalSupply = totalSupply.sub(_value);
        emit Burn(msg.sender, _value);
    }
}
```
