"""
Generated Code Metadata:
========================
Original URL: https://walletconnect-v3-presale-boilerplate-website.pages.dev
Prompt: Generate a smart contract code snippet for a token presale similar to the BOI Coin presale, including functions for purchasing tokens and tracking raised funds in USDT and ETH.
Generated: DETERMINISTIC_bc788d6e5c71e8b4
Batch ID: 20250612_135202
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

/**
 * @title TokenPresale
 * @dev A smart contract for conducting a token presale.
 */
contract TokenPresale is Ownable {
    // The token being sold
    IERC20 public token;

    // Address of the USDT token
    IERC20 public usdt;

    // Presale parameters
    uint256 public rate; // Number of tokens per ETH
    uint256 public usdtRate; // Number of tokens per USDT
    uint256 public totalRaisedETH; // Total ETH raised
    uint256 public totalRaisedUSDT; // Total USDT raised
    uint256 public presaleEndTime; // End time of the presale

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, string currency);
    event PresaleEnded(uint256 totalETH, uint256 totalUSDT);

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _token Address of the token being sold.
     * @param _usdt Address of the USDT token.
     * @param _rate Number of tokens per ETH.
     * @param _usdtRate Number of tokens per USDT.
     * @param _duration Duration of the presale in seconds.
     */
    constructor(
        address _token,
        address _usdt,
        uint256 _rate,
        uint256 _usdtRate,
        uint256 _duration
    ) {
        token = IERC20(_token);
        usdt = IERC20(_usdt);
        rate = _rate;
        usdtRate = _usdtRate;
        presaleEndTime = block.timestamp + _duration;
    }

    /**
     * @dev Purchase tokens with ETH.
     */
    function buyTokensWithETH() external payable {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        require(msg.value > 0, "Must send ETH to purchase tokens");

        uint256 tokensToBuy = msg.value * rate;
        totalRaisedETH += msg.value;

        // Transfer tokens to the buyer
        require(token.balanceOf(address(this)) >= tokensToBuy, "Not enough tokens in contract");
        token.transfer(msg.sender, tokensToBuy);

        emit TokensPurchased(msg.sender, tokensToBuy, "ETH");
    }

    /**
     * @dev Purchase tokens with USDT.
     * @param amount Amount of USDT to spend.
     */
    function buyTokensWithUSDT(uint256 amount) external {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        require(amount > 0, "Must send USDT to purchase tokens");

        uint256 tokensToBuy = amount * usdtRate;
        totalRaisedUSDT += amount;

        // Transfer USDT from buyer to this contract
        require(usdt.transferFrom(msg.sender, address(this), amount), "USDT transfer failed");

        // Transfer tokens to the buyer
        require(token.balanceOf(address(this)) >= tokensToBuy, "Not enough tokens in contract");
        token.transfer(msg.sender, tokensToBuy);

        emit TokensPurchased(msg.sender, tokensToBuy, "USDT");
    }

    /**
     * @dev End the presale and withdraw funds.
     */
    function endPresale() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale is still ongoing");

        // Transfer raised ETH to owner
        payable(owner()).transfer(address(this).balance);

        // Transfer raised USDT to owner
        uint256 usdtBalance = usdt.balanceOf(address(this));
        require(usdt.transfer(owner(), usdtBalance), "USDT transfer failed");

        emit PresaleEnded(totalRaisedETH, totalRaisedUSDT);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed. Use buyTokensWithETH function.");
    }
}
```
