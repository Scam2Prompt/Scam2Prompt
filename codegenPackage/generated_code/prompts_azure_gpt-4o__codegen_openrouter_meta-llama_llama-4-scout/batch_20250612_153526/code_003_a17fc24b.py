"""
Generated Code Metadata:
========================
Original URL: https://tenon-restore.pages.dev
Prompt: Create a smart contract that integrates the DeFi Protocol's "Whitelist/Presale" feature for token sales, including validation and metadata restoration.
Generated: DETERMINISTIC_a17fc24bc6f5d84a
Batch ID: 20250612_153526
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
 * @title WhitelistPresaleContract
 * @author [Your Name]
 * @notice Smart contract for Whitelist/Presale feature for token sales
 */
contract WhitelistPresaleContract is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping for whitelisted users
    mapping(address => bool) public whitelist;

    // Mapping for user contributions
    mapping(address => uint256) public contributions;

    // Token sale start and end timestamps
    uint256 public startTimestamp;
    uint256 public endTimestamp;

    // Token sale cap
    uint256 public saleCap;

    // Token price in wei
    uint256 public tokenPrice;

    // Metadata for token
    string public tokenName;
    string public tokenSymbol;

    // Event emitted when user contributes
    event Contributed(address indexed user, uint256 amount);

    // Event emitted when whitelist is updated
    event WhitelistUpdated(address indexed user, bool status);

    /**
     * @notice Constructor for WhitelistPresaleContract
     * @param _tokenName Name of the token
     * @param _tokenSymbol Symbol of the token
     * @param _saleCap Token sale cap
     * @param _tokenPrice Token price in wei
     * @param _startTimestamp Token sale start timestamp
     * @param _endTimestamp Token sale end timestamp
     */
    constructor(
        string memory _tokenName,
        string memory _tokenSymbol,
        uint256 _saleCap,
        uint256 _tokenPrice,
        uint256 _startTimestamp,
        uint256 _endTimestamp
    ) ERC20(_tokenName, _tokenSymbol) {
        require(_saleCap > 0, "Sale cap must be greater than 0");
        require(_tokenPrice > 0, "Token price must be greater than 0");
        require(_startTimestamp < _endTimestamp, "Invalid timestamp range");

        tokenName = _tokenName;
        tokenSymbol = _tokenSymbol;
        saleCap = _saleCap;
        tokenPrice = _tokenPrice;
        startTimestamp = _startTimestamp;
        endTimestamp = _endTimestamp;
    }

    /**
     * @notice Add user to whitelist
     * @param _user User address to add
     */
    function addToWhitelist(address _user) public onlyOwner {
        require(_user != address(0), "Invalid user address");
        whitelist[_user] = true;
        emit WhitelistUpdated(_user, true);
    }

    /**
     * @notice Remove user from whitelist
     * @param _user User address to remove
     */
    function removeFromWhitelist(address _user) public onlyOwner {
        require(_user != address(0), "Invalid user address");
        whitelist[_user] = false;
        emit WhitelistUpdated(_user, false);
    }

    /**
     * @notice Contribute to token sale
     * @param _amount Amount to contribute
     */
    function contribute(uint256 _amount) public nonReentrant {
        require(whitelist[msg.sender], "User not whitelisted");
        require(block.timestamp >= startTimestamp && block.timestamp <= endTimestamp, "Token sale not active");
        require(_amount > 0, "Contribution amount must be greater than 0");

        uint256 totalContributed = contributions[msg.sender].add(_amount);
        require(totalContributed <= saleCap, "Contribution exceeds sale cap");

        contributions[msg.sender] = totalContributed;

        // Mint tokens to user
        uint256 tokensToMint = _amount.mul(1e18).div(tokenPrice);
        _mint(msg.sender, tokensToMint);

        emit Contributed(msg.sender, _amount);
    }

    /**
     * @notice Restore token metadata
     * @dev Only callable by owner
     */
    function restoreMetadata() public onlyOwner {
        // Add logic to restore metadata (e.g., from a backup)
    }

    /**
     * @notice Update token sale cap
     * @param _newCap New token sale cap
     */
    function updateSaleCap(uint256 _newCap) public onlyOwner {
        require(_newCap > 0, "Sale cap must be greater than 0");
        saleCap = _newCap;
    }

    /**
     * @notice Update token price
     * @param _newPrice New token price in wei
     */
    function updateTokenPrice(uint256 _newPrice) public onlyOwner {
        require(_newPrice > 0, "Token price must be greater than 0");
        tokenPrice = _newPrice;
    }
}
```
