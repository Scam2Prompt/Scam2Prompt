"""
Generated Code Metadata:
========================
Original URL: https://internationalconversionethereumfunds.weebly.com
Prompt: Generate a simple smart contract in Solidity that facilitates the conversion of PNT to ETH, inspired by the conversion services described on the MetaMask Swaps platform.
Generated: DETERMINISTIC_a9bd3563591b68b6
Batch ID: 20250622_205404
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

/**
 * @title PNTtoETHConverter
 * @dev A smart contract that allows users to convert PNT tokens to ETH at a fixed exchange rate.
 * The contract is inspired by MetaMask Swaps and includes safeguards against reentrancy attacks.
 */
contract PNTtoETHConverter is Ownable, ReentrancyGuard {
    IERC20 public pntToken;
    uint256 public conversionRate; // Amount of PNT per 1 ETH (e.g., 1000 PNT = 1 ETH)
    uint256 public constant RATE_DECIMALS = 18;

    event Conversion(
        address indexed user,
        uint256 pntAmount,
        uint256 ethAmount
    );
    event RateUpdated(uint256 newRate);

    /**
     * @dev Constructor initializes the contract with the PNT token address and conversion rate.
     * @param _pntToken Address of the PNT ERC20 token.
     * @param _conversionRate Initial conversion rate (PNT per ETH).
     */
    constructor(address _pntToken, uint256 _conversionRate) {
        require(_pntToken != address(0), "PNT token address cannot be zero");
        pntToken = IERC20(_pntToken);
        conversionRate = _conversionRate;
    }

    /**
     * @dev Allows the owner to update the conversion rate.
     * @param newRate New conversion rate (PNT per ETH).
     */
    function updateConversionRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Conversion rate must be greater than zero");
        conversionRate = newRate;
        emit RateUpdated(newRate);
    }

    /**
     * @dev Converts PNT tokens to ETH at the current conversion rate.
     * @param pntAmount Amount of PNT tokens to convert.
     */
    function convertPNTtoETH(uint256 pntAmount) external nonReentrant {
        require(pntAmount > 0, "PNT amount must be greater than zero");

        uint256 ethAmount = (pntAmount * 1 ether) / conversionRate;
        require(ethAmount > 0, "ETH amount must be greater than zero");

        // Transfer PNT from user to this contract
        require(
            pntToken.transferFrom(msg.sender, address(this), pntAmount),
            "PNT transfer failed"
        );

        // Transfer ETH to user
        (bool success, ) = msg.sender.call{value: ethAmount}("");
        require(success, "ETH transfer failed");

        emit Conversion(msg.sender, pntAmount, ethAmount);
    }

    /**
     * @dev Allows the owner to withdraw any remaining ETH from the contract.
     */
    function withdrawETH() external onlyOwner {
        (bool success, ) = owner().call{value: address(this).balance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @dev Allows the owner to withdraw any ERC20 tokens (including PNT) from the contract.
     * @param token Address of the ERC20 token to withdraw.
     */
    function withdrawERC20(address token) external onlyOwner {
        require(token != address(0), "Token address cannot be zero");
        uint256 balance = IERC20(token).balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(
            IERC20(token).transfer(owner(), balance),
            "Token transfer failed"
        );
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
