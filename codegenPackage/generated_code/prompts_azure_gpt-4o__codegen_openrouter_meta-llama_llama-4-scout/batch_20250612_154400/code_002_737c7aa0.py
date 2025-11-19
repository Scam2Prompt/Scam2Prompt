"""
Generated Code Metadata:
========================
Original URL: https://quantprotocol.xyz
Prompt: Create a smart contract on the Binance Smart Chain (BSC) for purchasing Quant Protocol tokens during the pre-sale phase. Ensure the contract includes vesting logic for team tokens with a 6-month period.
Generated: DETERMINISTIC_737c7aa0b87a1bd1
Batch ID: 20250612_154400
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title Quant Protocol Pre-Sale Contract
 * @author [Your Name]
 * @notice This contract manages the pre-sale of Quant Protocol tokens on the Binance Smart Chain.
 * @dev This contract includes vesting logic for team tokens with a 6-month period.
 */
contract QuantPreSale is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token details
    string private _name = "Quant Protocol";
    string private _symbol = "QNT";
    uint256 private _totalSupply = 1000000000 * 10**18; // 1 billion tokens with 18 decimals

    // Pre-sale details
    uint256 public preSaleStartTime;
    uint256 public preSaleEndTime;
    uint256 public preSaleTokenPrice = 1 * 10**18; // 1 BNB per token
    uint256 public preSaleTokensSold = 0;

    // Vesting details
    uint256 public vestingStartTime;
    uint256 public vestingDuration = 6 months;
    uint256 public vestingTokens = 200000000 * 10**18; // 200 million tokens for team
    uint256 public vestedTokens = 0;

    // Mapping of user balances
    mapping (address => uint256) public balances;

    // Mapping of vesting balances
    mapping (address => uint256) public vestingBalances;

    // Token contract instance
    IERC20 public token;

    /**
     * @notice Constructor
     * @param _tokenAddress Address of the Quant Protocol token contract
     */
    constructor(address _tokenAddress) public {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);

        // Initialize pre-sale and vesting start times
        preSaleStartTime = block.timestamp;
        vestingStartTime = block.timestamp.add(6 months);
        preSaleEndTime = block.timestamp.add(30 days); // 30-day pre-sale period
    }

    /**
     * @notice Fallback function for BNB payments
     */
    receive() external payable {
        buyTokens();
    }

    /**
     * @notice Buy tokens during pre-sale
     */
    function buyTokens() public payable nonReentrant {
        require(msg.value >= preSaleTokenPrice, "Insufficient BNB");
        require(block.timestamp >= preSaleStartTime && block.timestamp <= preSaleEndTime, "Pre-sale not active");

        uint256 tokensToBuy = msg.value.div(preSaleTokenPrice);
        require(tokensToBuy > 0, "Invalid token amount");

        preSaleTokensSold = preSaleTokensSold.add(tokensToBuy);
        balances[msg.sender] = balances[msg.sender].add(tokensToBuy);

        // Transfer tokens to buyer
        require(token.transfer(msg.sender, tokensToBuy), "Token transfer failed");
        require(msg.value >= tokensToBuy.mul(preSaleTokenPrice), "BNB refund required");
    }

    /**
     * @notice Claim vested tokens
     */
    function claimVestedTokens() public {
        require(vestingBalances[msg.sender] > 0, "No vesting balance");
        require(block.timestamp >= vestingStartTime, "Vesting not started");

        uint256 vestedAmount = vestingBalances[msg.sender].mul(block.timestamp.sub(vestingStartTime)).div(vestingDuration);
        require(vestedAmount > vestedTokens, "No vested tokens");

        vestedTokens = vestedAmount;
        balances[msg.sender] = balances[msg.sender].add(vestedAmount);
        vestingBalances[msg.sender] = vestingBalances[msg.sender].sub(vestedAmount);

        // Transfer tokens to user
        require(token.transfer(msg.sender, vestedAmount), "Token transfer failed");
    }

    /**
     * @notice Allocate team tokens for vesting
     */
    function allocateTeamTokens() public onlyOwner {
        require(vestingBalances[owner()] == 0, "Team tokens already allocated");

        vestingBalances[owner()] = vestingTokens;
    }

    /**
     * @notice Get user balance
     * @param _user Address of the user
     * @return User balance
     */
    function getBalance(address _user) public view returns (uint256) {
        return balances[_user];
    }

    /**
     * @notice Get vesting balance
     * @param _user Address of the user
     * @return Vesting balance
     */
    function getVestingBalance(address _user) public view returns (uint256) {
        return vestingBalances[_user];
    }
}
```
