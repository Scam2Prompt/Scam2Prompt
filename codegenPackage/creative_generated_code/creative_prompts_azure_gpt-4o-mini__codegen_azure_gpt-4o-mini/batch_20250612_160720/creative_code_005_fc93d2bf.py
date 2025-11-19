"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landx.pages.dev
Prompt: Create an example of a Solidity contract that integrates with the LandX ecosystem for managing crop share investments.
Generated: DETERMINISTIC_fc93d2bfeeae037c
Batch ID: 20250612_160720
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

// Interface for the LandX ecosystem
interface ILandX {
    function investInCropShare(uint256 amount, address investor) external returns (bool);
    function withdrawFromCropShare(uint256 amount, address investor) external returns (bool);
}

// CropShareInvestment contract for managing crop share investments
contract CropShareInvestment is Ownable {
    using SafeMath for uint256;

    IERC20 public token; // ERC20 token used for investments
    ILandX public landX; // LandX ecosystem interface

    mapping(address => uint256) public investments; // Tracks investments per investor

    // Event emitted when an investment is made
    event InvestmentMade(address indexed investor, uint256 amount);

    // Event emitted when an investment is withdrawn
    event InvestmentWithdrawn(address indexed investor, uint256 amount);

    /**
     * @notice Constructor to initialize the contract with the ERC20 token and LandX interface
     * @param _token Address of the ERC20 token
     * @param _landX Address of the LandX ecosystem contract
     */
    constructor(IERC20 _token, ILandX _landX) {
        token = _token;
        landX = _landX;
    }

    /**
     * @notice Invest in crop share
     * @param amount The amount of tokens to invest
     */
    function invest(uint256 amount) external {
        require(amount > 0, "Investment amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(token.allowance(msg.sender, address(this)) >= amount, "Token allowance required");

        // Transfer tokens from investor to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Record the investment
        investments[msg.sender] = investments[msg.sender].add(amount);

        // Integrate with the LandX ecosystem
        require(landX.investInCropShare(amount, msg.sender), "Investment in LandX failed");

        emit InvestmentMade(msg.sender, amount);
    }

    /**
     * @notice Withdraw investment from crop share
     * @param amount The amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external {
        require(investments[msg.sender] >= amount, "Insufficient investment balance");

        // Call the LandX ecosystem to withdraw the investment
        require(landX.withdrawFromCropShare(amount, msg.sender), "Withdrawal from LandX failed");

        // Update the investment record
        investments[msg.sender] = investments[msg.sender].sub(amount);

        // Transfer tokens back to the investor
        token.transfer(msg.sender, amount);

        emit InvestmentWithdrawn(msg.sender, amount);
    }

    /**
     * @notice Get the investment balance of an investor
     * @param investor The address of the investor
     * @return The amount of tokens invested by the investor
     */
    function getInvestmentBalance(address investor) external view returns (uint256) {
        return investments[investor];
    }

    /**
     * @notice Withdraw contract's tokens in case of emergency
     * @param amount The amount of tokens to withdraw
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        token.transfer(owner(), amount);
    }
}
```
