"""
Generated Code Metadata:
========================
Original URL: https://vantardxyz.web.app
Prompt: Write a smart contract that implements the burning mechanism for Vantard tokens during redemptions, ensuring fees are reinvested into the fund as described.
Generated: DETERMINISTIC_8f3abdba8ab4f285
Batch ID: 20250612_152954
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

contract VantardToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Address of the fund where fees will be reinvested
    address public fundAddress;

    // Fee percentage (e.g., 100 = 1%)
    uint256 public redemptionFeePercentage;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount, uint256 fee);
    event FeeReinvested(uint256 amount);

    /**
     * @dev Constructor that initializes the token
     * @param _initialSupply Initial token supply
     * @param _fundAddress Address where fees will be sent
     * @param _redemptionFeePercentage Fee percentage for redemptions (100 = 1%)
     */
    constructor(
        uint256 _initialSupply,
        address _fundAddress,
        uint256 _redemptionFeePercentage
    ) ERC20("Vantard Token", "VANT") {
        _mint(msg.sender, _initialSupply);
        fundAddress = _fundAddress;
        redemptionFeePercentage = _redemptionFeePercentage;
    }

    /**
     * @dev Burns tokens during redemption and reinvests fees
     * @param amount Amount of tokens to burn
     */
    function redeem(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Calculate fee amount
        uint256 feeAmount = amount.mul(redemptionFeePercentage).div(10000);
        uint256 amountAfterFee = amount.sub(feeAmount);

        // Burn the tokens after fee deduction
        _burn(msg.sender, amountAfterFee);

        // Transfer fee to fund address
        if (feeAmount > 0) {
            _transfer(msg.sender, fundAddress, feeAmount);
            emit FeeReinvested(feeAmount);
        }

        emit TokensBurned(msg.sender, amountAfterFee, feeAmount);
    }

    /**
     * @dev Updates the fund address
     * @param _newFundAddress New fund address
     */
    function updateFundAddress(address _newFundAddress) external onlyOwner {
        require(_newFundAddress != address(0), "Invalid address");
        fundAddress = _newFundAddress;
    }

    /**
     * @dev Updates the redemption fee percentage
     * @param _newFeePercentage New fee percentage (100 = 1%)
     */
    function updateRedemptionFeePercentage(uint256 _newFeePercentage) external onlyOwner {
        require(_newFeePercentage <= 1000, "Fee cannot exceed 10%");
        redemptionFeePercentage = _newFeePercentage;
    }
}
```
