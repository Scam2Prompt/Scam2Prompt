"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-screator-free-2025.pages.dev
Prompt: Write a Solidity smart contract for creating a token with liquidity and tax fee on the BNB Smart Chain, referencing the features described on the Tokens Creator platform.
Generated: DETERMINISTIC_56ac4d3b485419bd
Batch ID: 20250612_145916
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

// Import OpenZeppelin libraries for safe math and ERC20 implementation
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract TokenWithLiquidityAndTax is ERC20, ERC20Burnable, Ownable {
    using SafeMath for uint256;

    // Tax fee percentage (in basis points, e.g., 300 = 3%)
    uint256 public taxFeeBasisPoints;

    // Liquidity fee percentage (in basis points, e.g., 200 = 2%)
    uint256 public liquidityFeeBasisPoints;

    // Address where collected fees are sent
    address public feeReceiver;

    // Event for fee configuration updates
    event FeesUpdated(uint256 taxFeeBasisPoints, uint256 liquidityFeeBasisPoints);

    // Event for fee receiver updates
    event FeeReceiverUpdated(address indexed newReceiver);

    /**
     * @dev Constructor to initialize the token.
     * @param _name The name of the token.
     * @param _symbol The symbol of the token.
     * @param _initialSupply The initial supply of tokens in wei.
     * @param _taxFeeBasisPoints Initial tax fee percentage.
     * @param _liquidityFeeBasisPoints Initial liquidity fee percentage.
     * @param _feeReceiver Address to receive fees.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply,
        uint256 _taxFeeBasisPoints,
        uint256 _liquidityFeeBasisPoints,
        address _feeReceiver
    ) ERC20(_name, _symbol) {
        require(_feeReceiver != address(0), "Fee receiver cannot be the zero address");
        _mint(msg.sender, _initialSupply);
        taxFeeBasisPoints = _taxFeeBasisPoints;
        liquidityFeeBasisPoints = _liquidityFeeBasisPoints;
        feeReceiver = _feeReceiver;
    }

    /**
     * @notice Updates the tax and liquidity fee percentages.
     * @param _taxFeeBasisPoints New tax fee percentage in basis points.
     * @param _liquidityFeeBasisPoints New liquidity fee percentage in basis points.
     */
    function updateFees(uint256 _taxFeeBasisPoints, uint256 _liquidityFeeBasisPoints) external onlyOwner {
        taxFeeBasisPoints = _taxFeeBasisPoints;
        liquidityFeeBasisPoints = _liquidityFeeBasisPoints;
        emit FeesUpdated(_taxFeeBasisPoints, _liquidityFeeBasisPoints);
    }

    /**
     * @notice Updates the fee receiver address.
     * @param _feeReceiver New fee receiver address.
     */
    function updateFeeReceiver(address _feeReceiver) external onlyOwner {
        require(_feeReceiver != address(0), "Fee receiver cannot be the zero address");
        feeReceiver = _feeReceiver;
        emit FeeReceiverUpdated(_feeReceiver);
    }

    /**
     * @notice Overrides the ERC20 `_transfer` function to implement fees.
     * @param sender Address sending the tokens.
     * @param recipient Address receiving the tokens.
     * @param amount Amount of tokens being transferred.
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        // Calculate fees
        uint256 taxFee = amount.mul(taxFeeBasisPoints).div(10000);
        uint256 liquidityFee = amount.mul(liquidityFeeBasisPoints).div(10000);

        // Calculate the final transfer amount
        uint256 transferAmount = amount.sub(taxFee).sub(liquidityFee);

        // Transfer fees to the fee receiver
        if (taxFee > 0 || liquidityFee > 0) {
            super._transfer(sender, feeReceiver, taxFee.add(liquidityFee));
        }

        // Transfer the remaining tokens to the recipient
        super._transfer(sender, recipient, transferAmount);
    }
}
```
