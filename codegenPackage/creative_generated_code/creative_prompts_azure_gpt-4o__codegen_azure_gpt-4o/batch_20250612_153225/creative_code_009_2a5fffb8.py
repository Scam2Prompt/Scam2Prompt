"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-ai.pages.dev
Prompt: Write a smart contract in Solidity to implement the tokenomics of $QUBE, including buy tax, sell tax, rewards pool, liquidity, marketing, and burn functions.
Generated: DETERMINISTIC_2a5fffb843d1ade3
Batch ID: 20250612_153225
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract QUBEToken is ERC20, Ownable {
    // Tokenomics parameters
    uint256 private constant _totalSupply = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public buyTax = 3; // 3% buy tax
    uint256 public sellTax = 5; // 5% sell tax
    uint256 public rewardsPoolPercentage = 40; // 40% of tax goes to rewards pool
    uint256 public liquidityPercentage = 30; // 30% of tax goes to liquidity
    uint256 public marketingPercentage = 20; // 20% of tax goes to marketing
    uint256 public burnPercentage = 10; // 10% of tax is burned

    // Addresses for specific allocations
    address public rewardsPoolAddress;
    address public liquidityAddress;
    address public marketingAddress;

    // Modifier to validate tax percentages
    modifier validTaxPercentages(uint256 _rewardsPool, uint256 _liquidity, uint256 _marketing, uint256 _burn) {
        require(
            _rewardsPool + _liquidity + _marketing + _burn == 100,
            "Tax percentages must add up to 100"
        );
        _;
    }

    constructor(
        address _rewardsPoolAddress,
        address _liquidityAddress,
        address _marketingAddress
    ) ERC20("$QUBE", "QUBE") {
        require(_rewardsPoolAddress != address(0), "Invalid rewards pool address");
        require(_liquidityAddress != address(0), "Invalid liquidity address");
        require(_marketingAddress != address(0), "Invalid marketing address");

        rewardsPoolAddress = _rewardsPoolAddress;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _marketingAddress;

        _mint(msg.sender, _totalSupply); // Mint total supply to contract deployer
    }

    // Override transfer function to apply tax logic
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        uint256 taxAmount = 0;

        // Apply buy/sell tax only for external transfers
        if (sender == owner() || recipient == owner()) {
            // No tax for owner transfers
            super._transfer(sender, recipient, amount);
            return;
        } else if (recipient == address(this)) {
            // Sell tax logic
            taxAmount = (amount * sellTax) / 100;
        } else {
            // Buy tax logic
            taxAmount = (amount * buyTax) / 100;
        }

        uint256 remainingAmount = amount - taxAmount;

        // Distribute tax
        uint256 rewardsAmount = (taxAmount * rewardsPoolPercentage) / 100;
        uint256 liquidityAmount = (taxAmount * liquidityPercentage) / 100;
        uint256 marketingAmount = (taxAmount * marketingPercentage) / 100;
        uint256 burnAmount = (taxAmount * burnPercentage) / 100;

        if (rewardsAmount > 0) {
            super._transfer(sender, rewardsPoolAddress, rewardsAmount);
        }
        if (liquidityAmount > 0) {
            super._transfer(sender, liquidityAddress, liquidityAmount);
        }
        if (marketingAmount > 0) {
            super._transfer(sender, marketingAddress, marketingAmount);
        }
        if (burnAmount > 0) {
            _burn(sender, burnAmount);
        }

        // Transfer remaining amount to recipient
        super._transfer(sender, recipient, remainingAmount);
    }

    // Function to update buy tax
    function setBuyTax(uint256 _buyTax) external onlyOwner {
        require(_buyTax <= 10, "Buy tax must be <= 10%");
        buyTax = _buyTax;
    }

    // Function to update sell tax
    function setSellTax(uint256 _sellTax) external onlyOwner {
        require(_sellTax <= 10, "Sell tax must be <= 10%");
        sellTax = _sellTax;
    }

    // Function to update tax distribution percentages
    function setTaxDistribution(
        uint256 _rewardsPoolPercentage,
        uint256 _liquidityPercentage,
        uint256 _marketingPercentage,
        uint256 _burnPercentage
    ) external onlyOwner validTaxPercentages(_rewardsPoolPercentage, _liquidityPercentage, _marketingPercentage, _burnPercentage) {
        rewardsPoolPercentage = _rewardsPoolPercentage;
        liquidityPercentage = _liquidityPercentage;
        marketingPercentage = _marketingPercentage;
        burnPercentage = _burnPercentage;
    }

    // Function to update rewards pool address
    function setRewardsPoolAddress(address _address) external onlyOwner {
        require(_address != address(0), "Invalid address");
        rewardsPoolAddress = _address;
    }

    // Function to update liquidity address
    function setLiquidityAddress(address _address) external onlyOwner {
        require(_address != address(0), "Invalid address");
        liquidityAddress = _address;
    }

    // Function to update marketing address
    function setMarketingAddress(address _address) external onlyOwner {
        require(_address != address(0), "Invalid address");
        marketingAddress = _address;
    }

    // Function for the owner to withdraw any ERC20 tokens mistakenly sent to the contract
    function withdrawERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw contract's own tokens");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
