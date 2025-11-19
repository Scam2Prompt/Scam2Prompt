"""
Generated Code Metadata:
========================
Original URL: https://bafybeiha7aew6cnrfx323nbkbwheqhy7qp4rdsogs3bqahgzfex7vgmlya.ipfs.dweb.link
Prompt: Generate a smart contract in Solidity for a token sale that includes a presale cap of 1000 ETH and a conversion rate of 1 ETH to 99,500 BCKR.
Generated: DETERMINISTIC_f38f440d9d85d7fb
Batch ID: 20250612_160940
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
 * @title BCKR Token Sale Contract
 */
contract BCKRTokenSale {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token details
    string public name = "BCKR Token Sale";
    string public symbol = "BCKR";

    // Conversion rate: 1 ETH = 99,500 BCKR
    uint256 public conversionRate = 99500;

    // Presale cap: 1000 ETH
    uint256 public presaleCap = 1000 ether;

    // Token being sold
    IERC20 public token;

    // Address of the token owner
    address public owner;

    // Mapping of ETH contributions to BCKR allocations
    mapping (address => uint256) public contributions;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed purchaser, uint256 ethAmount, uint256 tokenAmount);

    /**
     * @dev Constructor
     * @param _token Address of the BCKR token contract
     */
    constructor(IERC20 _token) public {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
        owner = msg.sender;
    }

    /**
     * @dev Fallback function for simple purchases
     */
    fallback() external payable {
        buyTokens();
    }

    /**
     * @dev Purchase tokens with ETH
     */
    function buyTokens() public payable {
        require(msg.value > 0, "Invalid ETH amount");
        require(token.balanceOf(address(this)) >= msg.value.mul(conversionRate), "Insufficient token balance");

        // Check presale cap
        uint256 totalContributions = contributions[msg.sender].add(msg.value);
        require(totalContributions <= presaleCap, "Presale cap exceeded");

        // Update contributions
        contributions[msg.sender] = totalContributions;

        // Calculate token amount
        uint256 tokenAmount = msg.value.mul(conversionRate);

        // Transfer tokens to buyer
        token.safeTransfer(msg.sender, tokenAmount);

        // Emit event
        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }

    /**
     * @dev Withdraw remaining tokens
     */
    function withdrawTokens() public {
        require(msg.sender == owner, "Only owner can withdraw tokens");
        uint256 remainingTokens = token.balanceOf(address(this));
        token.safeTransfer(owner, remainingTokens);
    }

    /**
     * @dev Withdraw ETH
     */
    function withdrawETH() public {
        require(msg.sender == owner, "Only owner can withdraw ETH");
        uint256 balance = address(this).balance;
        payable(owner).transfer(balance);
    }
}
```
