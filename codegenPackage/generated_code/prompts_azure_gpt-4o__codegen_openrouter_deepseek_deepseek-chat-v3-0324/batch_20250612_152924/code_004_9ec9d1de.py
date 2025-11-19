"""
Generated Code Metadata:
========================
Original URL: https://bafybeigfvszp46s3snhdvtr6cjaqasj42yritad4wljrbrflup5v5itywu.ipfs.dweb.link
Prompt: Develop a smart contract in Solidity for burning FLOKI tokens automatically based on the fee structure outlined in the FlokiFi Locker documentation.
Generated: DETERMINISTIC_9ec9d1de63003f9b
Batch ID: 20250612_152924
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract FlokiFiAutoBurner is Ownable {
    using SafeMath for uint256;

    IERC20 public flokiToken;
    address public feeCollector;
    uint256 public burnFeePercentage; // Fee percentage to burn (e.g., 1000 = 10%)
    uint256 public constant FEE_DENOMINATOR = 10000;

    event TokensBurned(address indexed from, uint256 amount);
    event FeeCollectorUpdated(address newFeeCollector);
    event BurnFeePercentageUpdated(uint256 newPercentage);

    constructor(
        address _flokiToken,
        address _feeCollector,
        uint256 _burnFeePercentage
    ) {
        require(_flokiToken != address(0), "Invalid token address");
        require(_feeCollector != address(0), "Invalid fee collector address");
        require(_burnFeePercentage <= FEE_DENOMINATOR, "Fee percentage too high");

        flokiToken = IERC20(_flokiToken);
        feeCollector = _feeCollector;
        burnFeePercentage = _burnFeePercentage;
    }

    function setFeeCollector(address _feeCollector) external onlyOwner {
        require(_feeCollector != address(0), "Invalid fee collector address");
        feeCollector = _feeCollector;
        emit FeeCollectorUpdated(_feeCollector);
    }

    function setBurnFeePercentage(uint256 _burnFeePercentage) external onlyOwner {
        require(_burnFeePercentage <= FEE_DENOMINATOR, "Fee percentage too high");
        burnFeePercentage = _burnFeePercentage;
        emit BurnFeePercentageUpdated(_burnFeePercentage);
    }

    function burnTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Calculate burn amount and fee amount
        uint256 burnAmount = amount.mul(burnFeePercentage).div(FEE_DENOMINATOR);
        uint256 feeAmount = amount.sub(burnAmount);

        // Transfer tokens from sender to this contract
        require(
            flokiToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        // Burn tokens by sending to dead address
        require(
            flokiToken.transfer(address(0x000000000000000000000000000000000000dEaD), burnAmount),
            "Burn transfer failed"
        );

        // Send fee to fee collector
        if (feeAmount > 0) {
            require(
                flokiToken.transfer(feeCollector, feeAmount),
                "Fee transfer failed"
            );
        }

        emit TokensBurned(msg.sender, burnAmount);
    }

    // Emergency function to recover other ERC20 tokens sent by mistake
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(flokiToken), "Cannot recover FLOKI tokens");
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
