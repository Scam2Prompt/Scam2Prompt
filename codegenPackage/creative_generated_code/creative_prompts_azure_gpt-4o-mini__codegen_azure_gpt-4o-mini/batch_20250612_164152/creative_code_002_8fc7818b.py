"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc-wl.web.app
Prompt: What are the steps to create a whitelist minting process for a cryptocurrency token, based on the USDC Whitelist Mint example?
Generated: DETERMINISTIC_8fc7818bdebc57f8
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title WhitelistMinting
 * @dev This contract allows users to mint tokens if they are on a whitelist and have provided USDC as payment.
 */
contract WhitelistMinting is Ownable {
    using SafeMath for uint256;

    // Token to be minted
    IERC20 public mintableToken;

    // USDC token address for payment
    IERC20 public usdcToken;

    // Mapping of addresses on the whitelist
    mapping(address => bool) public whitelist;

    // Minting price in USDC
    uint256 public mintPrice;

    // Event emitted when a user mints tokens
    event TokensMinted(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the token addresses and mint price.
     * @param _mintableToken Address of the token that can be minted.
     * @param _usdcToken Address of the USDC token.
     * @param _mintPrice Price in USDC for minting one token.
     */
    constructor(IERC20 _mintableToken, IERC20 _usdcToken, uint256 _mintPrice) {
        mintableToken = _mintableToken;
        usdcToken = _usdcToken;
        mintPrice = _mintPrice;
    }

    /**
     * @dev Add multiple addresses to the whitelist.
     * @param _addresses Array of addresses to whitelist.
     */
    function addToWhitelist(address[] calldata _addresses) external onlyOwner {
        for (uint256 i = 0; i < _addresses.length; i++) {
            whitelist[_addresses[i]] = true;
        }
    }

    /**
     * @dev Remove multiple addresses from the whitelist.
     * @param _addresses Array of addresses to remove from whitelist.
     */
    function removeFromWhitelist(address[] calldata _addresses) external onlyOwner {
        for (uint256 i = 0; i < _addresses.length; i++) {
            whitelist[_addresses[i]] = false;
        }
    }

    /**
     * @dev Mint tokens if the user is on the whitelist and pays the mint price in USDC.
     * @param amount Number of tokens to mint.
     */
    function mintTokens(uint256 amount) external {
        require(whitelist[msg.sender], "You are not whitelisted");
        require(amount > 0, "Amount must be greater than zero");
        
        uint256 totalCost = mintPrice.mul(amount);
        
        // Transfer USDC from user to this contract
        require(usdcToken.transferFrom(msg.sender, address(this), totalCost), "USDC transfer failed");
        
        // Mint the specified amount of tokens to the user
        mintableToken.transfer(msg.sender, amount);
        
        emit TokensMinted(msg.sender, amount);
    }

    /**
     * @dev Allow the owner to withdraw USDC from the contract.
     * @param amount Amount of USDC to withdraw.
     */
    function withdrawUSDC(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(usdcToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        
        // Transfer USDC from this contract to the owner
        require(usdcToken.transfer(msg.sender, amount), "USDC withdrawal failed");
    }
}
```
