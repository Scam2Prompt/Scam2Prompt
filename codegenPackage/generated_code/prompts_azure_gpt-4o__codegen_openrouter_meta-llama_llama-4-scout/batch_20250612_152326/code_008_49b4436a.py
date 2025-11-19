"""
Generated Code Metadata:
========================
Original URL: https://clean-4dq.pages.dev
Prompt: Write a smart contract that demonstrates the issuance of assets on SatoshiVM, utilizing its compatibility with the Ethereum ecosystem and native BTC gas.
Generated: DETERMINISTIC_49b4436a30851ed2
Batch ID: 20250612_152326
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
 * @title SatoshiVM Asset Issuance Contract
 * @author [Your Name]
 * @notice This contract demonstrates the issuance of assets on SatoshiVM,
 *          utilizing its compatibility with the Ethereum ecosystem and native BTC gas.
 */
contract SatoshiVMAssetIssuance {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of asset owners and their respective balances
    mapping (address => uint256) public assetBalances;

    // Mapping of asset allowances
    mapping (address => mapping (address => uint256)) public assetAllowances;

    // Total supply of the asset
    uint256 public totalSupply;

    // Name and symbol of the asset
    string public name;
    string public symbol;

    // Event emitted when an asset is issued
    event IssueAsset(address indexed to, uint256 amount);

    // Event emitted when an asset is transferred
    event Transfer(address indexed from, address indexed to, uint256 amount);

    // Event emitted when an asset allowance is approved
    event Approval(address indexed owner, address indexed spender, uint256 amount);

    /**
     * @dev Constructor function
     * @param _name Name of the asset
     * @param _symbol Symbol of the asset
     * @param _initialSupply Initial supply of the asset
     */
    constructor(string memory _name, string memory _symbol, uint256 _initialSupply) public {
        name = _name;
        symbol = _symbol;
        totalSupply = _initialSupply;
        assetBalances[msg.sender] = _initialSupply;
        emit IssueAsset(msg.sender, _initialSupply);
    }

    /**
     * @dev Returns the balance of the asset for a given owner
     * @param owner Owner of the asset
     * @return Balance of the asset
     */
    function balanceOf(address owner) public view returns (uint256) {
        return assetBalances[owner];
    }

    /**
     * @dev Transfers an asset from the sender to a recipient
     * @param to Recipient of the asset
     * @param amount Amount of the asset to transfer
     * @return Whether the transfer was successful
     */
    function transfer(address to, uint256 amount) public returns (bool) {
        require(assetBalances[msg.sender] >= amount, "Insufficient balance");
        assetBalances[msg.sender] = assetBalances[msg.sender].sub(amount);
        assetBalances[to] = assetBalances[to].add(amount);
        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer an asset on behalf of the owner
     * @param spender Spender of the asset
     * @param amount Amount of the asset to approve
     * @return Whether the approval was successful
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        assetAllowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers an asset from an owner to a recipient, using an approved spender
     * @param from Owner of the asset
     * @param to Recipient of the asset
     * @param amount Amount of the asset to transfer
     * @return Whether the transfer was successful
     */
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(assetAllowances[from][msg.sender] >= amount, "Insufficient allowance");
        require(assetBalances[from] >= amount, "Insufficient balance");
        assetAllowances[from][msg.sender] = assetAllowances[from][msg.sender].sub(amount);
        assetBalances[from] = assetBalances[from].sub(amount);
        assetBalances[to] = assetBalances[to].add(amount);
        emit Transfer(from, to, amount);
        return true;
    }
}
```
