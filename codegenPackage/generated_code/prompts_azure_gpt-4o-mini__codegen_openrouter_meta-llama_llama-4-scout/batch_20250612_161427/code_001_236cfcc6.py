"""
Generated Code Metadata:
========================
Original URL: https://ghozalii.pages.dev
Prompt: How can I create a smart contract that manages the claiming process for Ghozali token holders based on a total supply of 100,000,000?
Generated: DETERMINISTIC_236cfcc6a89329a1
Batch ID: 20250612_161427
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
 * @title Ghozali Token Claiming Contract
 * @author [Your Name]
 * @notice This contract manages the claiming process for Ghozali token holders.
 */
contract GhozaliTokenClaiming {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Total supply of Ghozali tokens
    uint256 public constant TOTAL_SUPPLY = 100_000_000 ether;

    // IERC20 instance for Ghozali token
    IERC20 public ghozaliToken;

    // Mapping of claimants and their claimed amounts
    mapping(address => uint256) public claimedAmounts;

    // Event emitted when a claim is made
    event Claim(address indexed claimant, uint256 amount);

    /**
     * @notice Constructor
     * @param _ghozaliTokenAddress Address of the Ghozali token contract
     */
    constructor(address _ghozaliTokenAddress) public {
        require(_ghozaliTokenAddress != address(0), "Invalid token address");
        ghozaliToken = IERC20(_ghozaliTokenAddress);
    }

    /**
     * @notice Claim Ghozali tokens
     * @param _amount Amount of tokens to claim
     */
    function claim(uint256 _amount) public {
        require(_amount > 0, "Claim amount must be greater than 0");
        require(ghozaliToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(claimedAmounts[msg.sender].add(_amount) <= ghozaliToken.balanceOf(msg.sender), "Exceeds available claimable amount");

        claimedAmounts[msg.sender] = claimedAmounts[msg.sender].add(_amount);
        ghozaliToken.safeTransfer(msg.sender, _amount);

        emit Claim(msg.sender, _amount);
    }

    /**
     * @notice Get the available claimable amount for a claimant
     * @param _claimant Address of the claimant
     * @return Available claimable amount
     */
    function getAvailableClaimableAmount(address _claimant) public view returns (uint256) {
        return ghozaliToken.balanceOf(_claimant).sub(claimedAmounts[_claimant]);
    }
}

interface IERC20 {
    function balanceOf(address owner) external view returns (uint256);
    function transfer(address to, uint256 value) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 value) external returns (bool);
    function transferFrom(address from, address to, uint256 value) external returns (bool);
}
```
