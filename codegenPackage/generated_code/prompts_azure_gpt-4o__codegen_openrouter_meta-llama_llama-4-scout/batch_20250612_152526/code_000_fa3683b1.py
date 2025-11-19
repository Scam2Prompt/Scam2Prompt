"""
Generated Code Metadata:
========================
Original URL: https://metisdap.pages.dev
Prompt: Write a smart contract using Solidity to deploy a dApp on the Metis Layer 2 network, ensuring low gas fees and fast transaction processing. Reference the Metis documentation for integration details.
Generated: DETERMINISTIC_fa3683b15e7d1c20
Batch ID: 20250612_152526
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
 * @title Metis DApp Smart Contract
 * @author [Your Name]
 * @notice A simple dApp smart contract deployed on the Metis Layer 2 network.
 */
contract MetisDApp {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user balances
    mapping(address => uint256) public balances;

    // Token address
    address public tokenAddress;

    /**
     * @notice Constructor
     * @param _tokenAddress Address of the ERC20 token
     */
    constructor(address _tokenAddress) public {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        tokenAddress = _tokenAddress;
    }

    /**
     * @notice Deposit function
     * @param _amount Amount to deposit
     */
    function deposit(uint256 _amount) public {
        require(_amount > 0, "Deposit amount must be greater than zero");
        IERC20(tokenAddress).safeTransferFrom(msg.sender, address(this), _amount);
        balances[msg.sender] = balances[msg.sender].add(_amount);
    }

    /**
     * @notice Withdraw function
     * @param _amount Amount to withdraw
     */
    function withdraw(uint256 _amount) public {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_amount);
        IERC20(tokenAddress).safeTransfer(msg.sender, _amount);
    }

    /**
     * @notice Get user balance
     * @return User balance
     */
    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }

    /**
     * @dev Fallback function
     */
    receive() external payable {}

    /**
     * @dev Fallback function
     */
    fallback() external {}
}
```
