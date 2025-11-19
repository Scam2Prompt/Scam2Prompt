"""
Generated Code Metadata:
========================
Original URL: https://poodlana-token.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates the presale and token distribution for the Poodlana cryptocurrency, ensuring all tokens are unlocked from day one.
Generated: DETERMINISTIC_f1c7b3f5105b0904
Batch ID: 20250612_163807
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
 * @title Poodlana Presale and Token Distribution Contract
 * @author [Your Name]
 * @notice This contract facilitates the presale and token distribution for the Poodlana cryptocurrency.
 */
contract PoodlanaPresale is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user balances during presale
    mapping (address => uint256) public presaleBalances;

    // Total tokens available for presale
    uint256 public totalPresaleTokens;

    // Presale start and end timestamps
    uint256 public presaleStart;
    uint256 public presaleEnd;

    // Flag to check if presale is active
    bool public isPresaleActive;

    /**
     * @notice Constructor for PoodlanaPresale contract
     * @param _name Name of the token
     * @param _symbol Symbol of the token
     * @param _totalSupply Total supply of tokens
     */
    constructor(string memory _name, string memory _symbol, uint256 _totalSupply) ERC20(_name, _symbol) {
        // Mint total supply to contract for token distribution
        _mint(msg.sender, _totalSupply);
        totalPresaleTokens = _totalSupply;
    }

    /**
     * @notice Start the presale
     * @param _presaleDuration Duration of the presale in seconds
     */
    function startPresale(uint256 _presaleDuration) external onlyOwner {
        require(!isPresaleActive, "Presale is already active");
        presaleStart = block.timestamp;
        presaleEnd = presaleStart.add(_presaleDuration);
        isPresaleActive = true;
    }

    /**
     * @notice Buy tokens during presale
     * @param _amount Amount of tokens to buy
     */
    function buyTokens(uint256 _amount) external nonReentrant {
        require(isPresaleActive, "Presale is not active");
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale has not started or has ended");
        require(_amount > 0, "Buy amount must be greater than 0");
        require(totalPresaleTokens >= _amount, "Insufficient tokens available");

        // Update user's presale balance
        presaleBalances[msg.sender] = presaleBalances[msg.sender].add(_amount);
        totalPresaleTokens = totalPresaleTokens.sub(_amount);

        // Transfer tokens to user
        _transfer(msg.sender, _amount);
    }

    /**
     * @notice Claim tokens after presale
     */
    function claimTokens() external nonReentrant {
        require(!isPresaleActive, "Presale is still active");
        require(presaleBalances[msg.sender] > 0, "No tokens to claim");

        // Update user's presale balance
        uint256 claimAmount = presaleBalances[msg.sender];
        presaleBalances[msg.sender] = 0;

        // Transfer tokens to user
        _transfer(msg.sender, claimAmount);
    }

    /**
     * @notice End the presale
     */
    function endPresale() external onlyOwner nonReentrant {
        require(isPresaleActive, "Presale is not active");
        isPresaleActive = false;
    }

    /**
     * @dev Hook to check if token transfer is allowed
     */
    override function _beforeTokenTransfer(address from, address to, uint256[] memory ids) internal virtual override {
        super._beforeTokenTransfer(from, to, ids);
    }

    /**
     * @dev Hook to check if token transfer is allowed
     */
    override function _afterTokenTransfer(address from, address to, uint256[] memory ids) internal virtual override {
        super._afterTokenTransfer(from, to, ids);
    }
}
```
