"""
Generated Code Metadata:
========================
Original URL: https://cryptexbit.com
Prompt: Develop a smart contract in Solidity for managing CryptexBit's token sale, ensuring transparency and fairness as described in their token structure.
Generated: DETERMINISTIC_a87285072c2edde8
Batch ID: 20250612_150920
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CryptexBitTokenSale
 * @dev A smart contract for managing CryptexBit's token sale with transparency and fairness.
 */
contract CryptexBitTokenSale is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // The token being sold
    IERC20 public token;

    // Address where funds are collected
    address payable public wallet;

    // How many token units a buyer gets per wei
    uint256 public rate;

    // Amount of wei raised
    uint256 public weiRaised;

    // Minimum and maximum contribution amounts
    uint256 public minContribution;
    uint256 public maxContribution;

    // Sale start and end timestamps
    uint256 public startTime;
    uint256 public endTime;

    // Whitelist mapping
    mapping(address => bool) public whitelist;

    // Individual contribution tracking
    mapping(address => uint256) public contributions;

    // Event for token purchase logging
    event TokensPurchased(
        address indexed purchaser,
        address indexed beneficiary,
        uint256 value,
        uint256 amount
    );

    // Event for whitelist update
    event WhitelistUpdated(address indexed account, bool isWhitelisted);

    /**
     * @dev Constructor for CryptexBitTokenSale
     * @param _rate Number of token units a buyer gets per wei
     * @param _wallet Address where collected funds will be forwarded to
     * @param _token Address of the token being sold
     * @param _startTime Sale start time (unix timestamp)
     * @param _endTime Sale end time (unix timestamp)
     * @param _minContribution Minimum contribution amount in wei
     * @param _maxContribution Maximum contribution amount in wei
     */
    constructor(
        uint256 _rate,
        address payable _wallet,
        IERC20 _token,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _minContribution,
        uint256 _maxContribution
    ) {
        require(_rate > 0, "Rate must be greater than 0");
        require(_wallet != address(0), "Wallet cannot be the zero address");
        require(address(_token) != address(0), "Token cannot be the zero address");
        require(_startTime >= block.timestamp, "Start time must be in the future");
        require(_endTime > _startTime, "End time must be after start time");
        require(_minContribution > 0, "Min contribution must be greater than 0");
        require(_maxContribution > _minContribution, "Max contribution must be greater than min");

        rate = _rate;
        wallet = _wallet;
        token = _token;
        startTime = _startTime;
        endTime = _endTime;
        minContribution = _minContribution;
        maxContribution = _maxContribution;
    }

    /**
     * @dev Fallback function for receiving ether
     */
    receive() external payable {
        buyTokens(msg.sender);
    }

    /**
     * @dev Token purchase function
     * @param beneficiary Address receiving the tokens
     */
    function buyTokens(address beneficiary) public payable nonReentrant {
        require(beneficiary != address(0), "Beneficiary cannot be the zero address");
        require(whitelist[msg.sender], "Address is not whitelisted");
        require(block.timestamp >= startTime, "Sale has not started yet");
        require(block.timestamp <= endTime, "Sale has ended");
        require(msg.value >= minContribution, "Contribution is below minimum");
        require(contributions[msg.sender].add(msg.value) <= maxContribution, "Contribution exceeds maximum");

        uint256 weiAmount = msg.value;
        uint256 tokens = weiAmount.mul(rate);

        // Update state
        weiRaised = weiRaised.add(weiAmount);
        contributions[msg.sender] = contributions[msg.sender].add(weiAmount);

        // Transfer tokens
        token.transfer(beneficiary, tokens);

        // Forward funds
        wallet.transfer(weiAmount);

        emit TokensPurchased(msg.sender, beneficiary, weiAmount, tokens);
    }

    /**
     * @dev Add or remove addresses from whitelist
     * @param account Address to update
     * @param isWhitelisted Whether the address is whitelisted
     */
    function updateWhitelist(address account, bool isWhitelisted) public onlyOwner {
        whitelist[account] = isWhitelisted;
        emit WhitelistUpdated(account, isWhitelisted);
    }

    /**
     * @dev Batch update whitelist
     * @param accounts Array of addresses to update
     * @param isWhitelisted Whether the addresses should be whitelisted
     */
    function batchUpdateWhitelist(address[] memory accounts, bool isWhitelisted) public onlyOwner {
        for (uint256 i = 0; i < accounts.length; i++) {
            whitelist[accounts[i]] = isWhitelisted;
            emit WhitelistUpdated(accounts[i], isWhitelisted);
        }
    }

    /**
     * @dev Withdraw remaining tokens after sale ends
     */
    function withdrawRemainingTokens() public onlyOwner {
        require(block.timestamp > endTime, "Sale has not ended yet");
        uint256 balance = token.balanceOf(address(this));
        token.transfer(owner(), balance);
    }

    /**
     * @dev Extend sale duration
     * @param newEndTime New end time (unix timestamp)
     */
    function extendSale(uint256 newEndTime) public onlyOwner {
        require(newEndTime > endTime, "New end time must be after current end time");
        endTime = newEndTime;
    }

    /**
     * @dev Emergency stop function to pause the sale
     */
    function emergencyStop() public onlyOwner {
        endTime = block.timestamp;
    }

    /**
     * @dev Get token amount for given wei amount
     * @param weiAmount Amount in wei
     * @return Number of tokens
     */
    function getTokenAmount(uint256 weiAmount) public view returns (uint256) {
        return weiAmount.mul(rate);
    }

    /**
     * @dev Check if sale is active
     * @return True if sale is active
     */
    function isSaleActive() public view returns (bool) {
        return block.timestamp >= startTime && block.timestamp <= endTime;
    }
}
```
