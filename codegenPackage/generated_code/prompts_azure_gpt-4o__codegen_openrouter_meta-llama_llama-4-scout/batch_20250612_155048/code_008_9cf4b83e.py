"""
Generated Code Metadata:
========================
Original URL: https://desnitsky.ru
Prompt: Write a Solidity contract that interacts with Frax Finance's smart contracts to demonstrate partial reserve management for stablecoins.
Generated: DETERMINISTIC_9cf4b83ed50fdb72
Batch ID: 20250612_155048
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
 * @title Frax Finance Partial Reserve Management Contract
 * @author [Your Name]
 * @notice This contract demonstrates partial reserve management for stablecoins
 *         using Frax Finance's smart contracts.
 */
contract FraxPartialReserveManager {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Frax Finance contract addresses
    address public fraxController;
    address public fraxToken;

    // Mapping of reserve assets to their respective amounts
    mapping(address => uint256) public reserves;

    /**
     * @param _fraxController Address of the Frax Controller contract
     * @param _fraxToken Address of the Frax token contract
     */
    constructor(address _fraxController, address _fraxToken) public {
        require(_fraxController != address(0), "FraxController address cannot be zero");
        require(_fraxToken != address(0), "FraxToken address cannot be zero");

        fraxController = _fraxController;
        fraxToken = _fraxToken;
    }

    /**
     * @notice Add reserve asset to the reserves mapping
     * @param _asset Address of the reserve asset
     * @param _amount Amount of the reserve asset
     */
    function addReserve(address _asset, uint256 _amount) public {
        require(_asset != address(0), "Reserve asset address cannot be zero");
        require(_amount > 0, "Reserve amount must be greater than zero");

        reserves[_asset] = reserves[_asset].add(_amount);
    }

    /**
     * @notice Remove reserve asset from the reserves mapping
     * @param _asset Address of the reserve asset
     * @param _amount Amount of the reserve asset to remove
     */
    function removeReserve(address _asset, uint256 _amount) public {
        require(_asset != address(0), "Reserve asset address cannot be zero");
        require(_amount > 0, "Reserve amount must be greater than zero");
        require(reserves[_asset] >= _amount, "Insufficient reserve amount");

        reserves[_asset] = reserves[_asset].sub(_amount);
    }

    /**
     * @notice Get the total reserve amount for a given asset
     * @param _asset Address of the reserve asset
     * @return Total reserve amount
     */
    function getReserveAmount(address _asset) public view returns (uint256) {
        return reserves[_asset];
    }

    /**
     * @notice Demonstrate partial reserve management by minting Frax tokens
     *         and adding/removing reserve assets
     * @param _user Address of the user
     * @param _amount Amount of Frax tokens to mint
     */
    function demonstratePartialReserveManagement(address _user, uint256 _amount) public {
        // Mint Frax tokens
        IERC20(fraxToken).safeTransfer(_user, _amount);

        // Add reserve asset
        address reserveAsset = address(new ERC20Mock("Reserve Asset", "RA"));
        addReserve(reserveAsset, _amount);

        // Remove reserve asset
        removeReserve(reserveAsset, _amount.div(2));
    }
}

// Mock ERC20 contract for demonstration purposes
contract ERC20Mock is IERC20 {
    string public name;
    string public symbol;
    uint256 public totalSupply;
    mapping(address => uint256) public balances;
    mapping(address => mapping(address => uint256)) public allowances;

    constructor(string memory _name, string memory _symbol) public {
        name = _name;
        symbol = _symbol;
        totalSupply = 1000 ether;
        balances[msg.sender] = totalSupply;
    }

    function transfer(address _to, uint256 _value) public returns (bool) {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_value);
        balances[_to] = balances[_to].add(_value);
        return true;
    }

    function approve(address _spender, uint256 _value) public returns (bool) {
        allowances[msg.sender][_spender] = _value;
        return true;
    }

    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(allowances[_from][msg.sender] >= _value, "Insufficient allowance");
        allowances[_from][msg.sender] = allowances[_from][msg.sender].sub(_value);
        balances[_from] = balances[_from].sub(_value);
        balances[_to] = balances[_to].add(_value);
        return true;
    }

    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }

    function totalSupply() public view returns (uint256) {
        return totalSupply;
    }
}
```
