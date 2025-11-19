"""
Generated Code Metadata:
========================
Original URL: https://desnitsky.ru
Prompt: Create a smart contract example that demonstrates the algorithmic stabilization mechanism used by Frax Finance for maintaining FRAX token price stability.
Generated: DETERMINISTIC_67e926fdf33b0ab1
Batch ID: 20250612_155048
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

contract FraxStablecoin is ERC20, Ownable {
    using SafeMath for uint256;

    // Constants
    uint256 public constant PRICE_PRECISION = 1e6;
    uint256 public constant COLLATERAL_RATIO_PRECISION = 1e6;
    uint256 public constant COLLATERAL_RATIO_MAX = 1e6;

    // System parameters
    uint256 public collateral_ratio; // Ratio of collateral to FRAX (1e6 precision)
    uint256 public target_price; // Target price in USD (1e6 precision)
    uint256 public refresh_cooldown; // Seconds between refresh
    uint256 public last_refresh_time; // Last time the collateral ratio was refreshed

    // Addresses
    address public collateral_token;
    address public oracle_address;
    address public treasury_address;

    // Events
    event CollateralRatioRefreshed(uint256 new_ratio);
    event Minted(address indexed user, uint256 frax_amount, uint256 collateral_amount);
    event Redeemed(address indexed user, uint256 frax_amount, uint256 collateral_amount);

    constructor(
        string memory _name,
        string memory _symbol,
        address _collateral_token,
        address _oracle_address,
        address _treasury_address,
        uint256 _initial_ratio,
        uint256 _target_price,
        uint256 _refresh_cooldown
    ) ERC20(_name, _symbol) {
        collateral_token = _collateral_token;
        oracle_address = _oracle_address;
        treasury_address = _treasury_address;
        collateral_ratio = _initial_ratio;
        target_price = _target_price;
        refresh_cooldown = _refresh_cooldown;
        last_refresh_time = block.timestamp;
    }

    // Refresh the collateral ratio based on market conditions
    function refreshCollateralRatio() public {
        require(block.timestamp - last_refresh_time >= refresh_cooldown, "Cooldown not elapsed");
        
        // Get current FRAX price from oracle (simplified)
        uint256 current_price = getFraxPrice();
        
        // Algorithmic stabilization logic
        if (current_price > target_price) {
            // Price is above target - decrease collateral ratio
            if (collateral_ratio > 0) {
                collateral_ratio = collateral_ratio.sub(1e4); // Decrease by 1% (1e4)
                if (collateral_ratio < 0) collateral_ratio = 0;
            }
        } else if (current_price < target_price) {
            // Price is below target - increase collateral ratio
            if (collateral_ratio < COLLATERAL_RATIO_MAX) {
                collateral_ratio = collateral_ratio.add(1e4); // Increase by 1% (1e4)
                if (collateral_ratio > COLLATERAL_RATIO_MAX) collateral_ratio = COLLATERAL_RATIO_MAX;
            }
        }

        last_refresh_time = block.timestamp;
        emit CollateralRatioRefreshed(collateral_ratio);
    }

    // Simplified oracle price feed (in production would use Chainlink or similar)
    function getFraxPrice() public view returns (uint256) {
        // In a real implementation, this would query an oracle
        return target_price; // Simplified for example
    }

    // Mint new FRAX tokens with collateral
    function mint(uint256 collateral_amount, uint256 frax_out_min) external {
        require(collateral_amount > 0, "Must provide collateral");
        
        // Calculate FRAX to mint based on collateral ratio
        uint256 frax_amount = collateral_amount.mul(PRICE_PRECISION).div(getCollateralPrice());
        frax_amount = frax_amount.mul(collateral_ratio).div(COLLATERAL_RATIO_PRECISION);
        
        require(frax_amount >= frax_out_min, "Slippage limit exceeded");
        
        // Transfer collateral from user to treasury
        IERC20(collateral_token).transferFrom(msg.sender, treasury_address, collateral_amount);
        
        // Mint FRAX to user
        _mint(msg.sender, frax_amount);
        
        emit Minted(msg.sender, frax_amount, collateral_amount);
    }

    // Redeem FRAX for collateral
    function redeem(uint256 frax_amount, uint256 collateral_out_min) external {
        require(frax_amount > 0, "Must redeem positive amount");
        
        // Calculate collateral to return based on collateral ratio
        uint256 collateral_amount = frax_amount.mul(getCollateralPrice()).div(PRICE_PRECISION);
        collateral_amount = collateral_amount.mul(collateral_ratio).div(COLLATERAL_RATIO_PRECISION);
        
        require(collateral_amount >= collateral_out_min, "Slippage limit exceeded");
        
        // Burn FRAX from user
        _burn(msg.sender, frax_amount);
        
        // Transfer collateral from treasury to user
        IERC20(collateral_token).transferFrom(treasury_address, msg.sender, collateral_amount);
        
        emit Redeemed(msg.sender, frax_amount, collateral_amount);
    }

    // Simplified collateral price feed (in production would use oracle)
    function getCollateralPrice() public view returns (uint256) {
        // In a real implementation, this would query an oracle
        return PRICE_PRECISION; // 1:1 peg for example
    }

    // Admin functions
    function setOracle(address _oracle_address) external onlyOwner {
        oracle_address = _oracle_address;
    }

    function setTreasury(address _treasury_address) external onlyOwner {
        treasury_address = _treasury_address;
    }

    function setRefreshCooldown(uint256 _refresh_cooldown) external onlyOwner {
        refresh_cooldown = _refresh_cooldown;
    }

    function setTargetPrice(uint256 _target_price) external onlyOwner {
        target_price = _target_price;
    }
}

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
