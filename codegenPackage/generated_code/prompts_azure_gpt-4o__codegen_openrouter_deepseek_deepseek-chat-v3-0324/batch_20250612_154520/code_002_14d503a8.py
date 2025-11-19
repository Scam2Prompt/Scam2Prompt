"""
Generated Code Metadata:
========================
Original URL: https://website-9v1.pages.dev
Prompt: Generate code to implement a token burn policy for $PLRT tokens, ensuring organic price growth over time as described in the PLR Tokenomics.
Generated: DETERMINISTIC_14d503a88291394b
Batch ID: 20250612_154520
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract PLRTToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Burn rate in basis points (1% = 100 basis points)
    uint256 public burnRate = 100; 
    // Minimum tokens required in contract to enable burning
    uint256 public minBurnThreshold = 1000 * 10**18;
    // Address where burned tokens are sent (dead address)
    address public constant BURN_ADDRESS = 0x000000000000000000000000000000000000dEaD;

    event TokensBurned(uint256 amount);
    event BurnRateChanged(uint256 newRate);
    event MinBurnThresholdChanged(uint256 newThreshold);

    constructor(uint256 initialSupply) ERC20("PLRT Token", "PLRT") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Sets the burn rate in basis points (1% = 100 basis points)
     * @param _burnRate New burn rate (0-10000)
     */
    function setBurnRate(uint256 _burnRate) external onlyOwner {
        require(_burnRate <= 10000, "Burn rate cannot exceed 100%");
        burnRate = _burnRate;
        emit BurnRateChanged(_burnRate);
    }

    /**
     * @dev Sets the minimum token threshold for burning
     * @param _threshold New minimum threshold in token units
     */
    function setMinBurnThreshold(uint256 _threshold) external onlyOwner {
        minBurnThreshold = _threshold;
        emit MinBurnThresholdChanged(_threshold);
    }

    /**
     * @dev Overrides ERC20 transfer to implement burn on transfer
     * @param recipient Address receiving the tokens
     * @param amount Amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 burnAmount = calculateBurnAmount(amount);
        uint256 transferAmount = amount.sub(burnAmount);

        if (burnAmount > 0) {
            _burn(msg.sender, burnAmount);
            emit TokensBurned(burnAmount);
        }

        super.transfer(recipient, transferAmount);
        return true;
    }

    /**
     * @dev Overrides ERC20 transferFrom to implement burn on transfer
     * @param sender Address sending the tokens
     * @param recipient Address receiving the tokens
     * @param amount Amount of tokens to transfer
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        uint256 burnAmount = calculateBurnAmount(amount);
        uint256 transferAmount = amount.sub(burnAmount);

        if (burnAmount > 0) {
            _burn(sender, burnAmount);
            emit TokensBurned(burnAmount);
        }

        super.transferFrom(sender, recipient, transferAmount);
        return true;
    }

    /**
     * @dev Calculates the burn amount based on current burn rate
     * @param amount Original transfer amount
     * @return Amount to be burned
     */
    function calculateBurnAmount(uint256 amount) internal view returns (uint256) {
        if (balanceOf(address(this)) < minBurnThreshold) {
            return 0;
        }
        return amount.mul(burnRate).div(10000);
    }

    /**
     * @dev Burns tokens from the contract balance
     * @param amount Amount of tokens to burn
     */
    function manualBurn(uint256 amount) external onlyOwner {
        require(balanceOf(address(this)) >= amount, "Insufficient balance");
        _burn(address(this), amount);
        emit TokensBurned(amount);
    }
}
```
