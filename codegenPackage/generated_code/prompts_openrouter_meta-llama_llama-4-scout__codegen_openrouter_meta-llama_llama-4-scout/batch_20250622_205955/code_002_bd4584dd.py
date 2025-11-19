"""
Generated Code Metadata:
========================
Original URL: https://memeskombat.pages.dev
Prompt: Generate a smart contract code in Solidity for a token presale system, similar to the one used in Meme Kombat, with a 50% token supply allocated for presale.
Generated: DETERMINISTIC_bd4584ddb9f2ea90
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MemeKombatPresale
 * @author [Your Name]
 * @notice Token presale contract for Meme Kombat
 */
contract MemeKombatPresale is ReentrancyGuard {
    using SafeMath for uint256;

    // Token contract instance
    ERC20 public token;

    // Presale start and end timestamps
    uint256 public presaleStart;
    uint256 public presaleEnd;

    // Token price in wei
    uint256 public tokenPrice;

    // Total token supply
    uint256 public totalSupply;

    // Token supply allocated for presale (50%)
    uint256 public presaleSupply;

    // Tokens sold during presale
    uint256 public tokensSold;

    // Mapping of user balances during presale
    mapping (address => uint256) public userBalances;

    /**
     * @notice Constructor
     * @param _token Token contract instance
     * @param _presaleStart Presale start timestamp
     * @param _presaleEnd Presale end timestamp
     * @param _tokenPrice Token price in wei
     * @param _totalSupply Total token supply
     */
    constructor(
        ERC20 _token,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _tokenPrice,
        uint256 _totalSupply
    ) {
        require(_presaleStart < _presaleEnd, "Invalid presale dates");
        require(_tokenPrice > 0, "Token price must be greater than 0");

        token = _token;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        tokenPrice = _tokenPrice;
        totalSupply = _totalSupply;
        presaleSupply = totalSupply.mul(50).div(100); // 50% of total supply

        // Mint tokens for presale
        _token.mint(address(this), presaleSupply);
    }

    /**
     * @notice Start presale
     */
    function startPresale() external {
        require(block.timestamp >= presaleStart, "Presale has not started yet");
        require(tokensSold == 0, "Presale has already started");
    }

    /**
     * @notice Buy tokens during presale
     * @param _amount Amount of tokens to buy
     */
    function buyTokens(uint256 _amount) external nonReentrant {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        require(_amount > 0, "Amount must be greater than 0");

        uint256 cost = _amount.mul(tokenPrice);
        require(msg.value >= cost, "Insufficient payment");

        // Update tokens sold and user balance
        tokensSold = tokensSold.add(_amount);
        userBalances[msg.sender] = userBalances[msg.sender].add(_amount);

        // Transfer tokens to user
        token.transfer(msg.sender, _amount);

        // Refund excess payment
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value.sub(cost));
        }
    }

    /**
     * @notice End presale
     */
    function endPresale() external {
        require(block.timestamp > presaleEnd, "Presale has not ended yet");
        require(tokensSold > 0, "No tokens sold during presale");

        // Burn unsold tokens
        uint256 unsoldTokens = presaleSupply.sub(tokensSold);
        token.burn(unsoldTokens);
    }

    /**
     * @notice Withdraw funds
     */
    function withdrawFunds() external {
        require(block.timestamp > presaleEnd, "Presale has not ended yet");
        require(tokensSold > 0, "No tokens sold during presale");

        // Transfer funds to owner
        payable(msg.sender).transfer(address(this).balance);
    }

    /**
     * @notice Get user balance
     * @param _user User address
     * @return User balance
     */
    function getUserBalance(address _user) external view returns (uint256) {
        return userBalances[_user];
    }
}
```
