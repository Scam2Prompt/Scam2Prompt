"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://desnitsky.ru
Prompt: Write a Solidity contract that interacts with Frax Finance's smart contracts to demonstrate partial reserve management for stablecoins.
Generated: DETERMINISTIC_9cf4b83ed50fdb72
Batch ID: 20250612_155048
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

/**
 * @title FraxReserveManager
 * @dev This contract demonstrates interaction with Frax Finance smart contracts
 *      for partial reserve management of stablecoins.
 *
 *      Note: Ensure Frax Finance's contract addresses are correctly configured
 *      before deploying this contract. This is a demonstration contract and
 *      should be thoroughly tested before use in production.
 */

interface IFraxPool {
    function mintFrax(uint256 collateralAmount, uint256 fraxAmount) external;
    function redeemFrax(uint256 fraxAmount, uint256 collateralAmount) external;
    function collateralReserveBalance() external view returns (uint256);
    function fraxPrice() external view returns (uint256);
}

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract FraxReserveManager {
    address public owner;
    address public fraxPoolAddress;
    address public collateralTokenAddress;

    IFraxPool public fraxPool;
    IERC20 public collateralToken;

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not owner");
        _;
    }

    event MintedFrax(uint256 collateralAmount, uint256 fraxAmount);
    event RedeemedFrax(uint256 fraxAmount, uint256 collateralAmount);

    /**
     * @dev Initializes the contract with Frax Pool address and collateral token address.
     * @param _fraxPoolAddress Address of the Frax Pool contract
     * @param _collateralTokenAddress Address of the collateral token contract
     */
    constructor(address _fraxPoolAddress, address _collateralTokenAddress) {
        require(_fraxPoolAddress != address(0), "Invalid Frax Pool address");
        require(_collateralTokenAddress != address(0), "Invalid collateral token address");

        owner = msg.sender;
        fraxPoolAddress = _fraxPoolAddress;
        collateralTokenAddress = _collateralTokenAddress;

        fraxPool = IFraxPool(_fraxPoolAddress);
        collateralToken = IERC20(_collateralTokenAddress);
    }

    /**
     * @dev Mints Frax using collateral tokens.
     * @param collateralAmount Amount of collateral tokens to use for minting
     * @param fraxAmount Desired amount of Frax to mint
     */
    function mintFrax(uint256 collateralAmount, uint256 fraxAmount) external onlyOwner {
        require(collateralAmount > 0, "Collateral amount must be greater than zero");
        require(fraxAmount > 0, "Frax amount must be greater than zero");

        // Transfer collateral tokens from owner to the contract
        require(collateralToken.transferFrom(owner, address(this), collateralAmount), "Collateral transfer failed");

        // Approve the Frax Pool to spend the collateral tokens
        require(collateralToken.approve(fraxPoolAddress, collateralAmount), "Approval failed");

        // Call the Frax Pool to mint Frax
        fraxPool.mintFrax(collateralAmount, fraxAmount);

        emit MintedFrax(collateralAmount, fraxAmount);
    }

    /**
     * @dev Redeems Frax for collateral tokens.
     * @param fraxAmount Amount of Frax to redeem
     * @param collateralAmount Desired amount of collateral tokens to receive
     */
    function redeemFrax(uint256 fraxAmount, uint256 collateralAmount) external onlyOwner {
        require(fraxAmount > 0, "Frax amount must be greater than zero");
        require(collateralAmount > 0, "Collateral amount must be greater than zero");

        // Call the Frax Pool to redeem Frax
        fraxPool.redeemFrax(fraxAmount, collateralAmount);

        emit RedeemedFrax(fraxAmount, collateralAmount);
    }

    /**
     * @dev Gets the current collateral reserve balance in the Frax Pool.
     * @return Collateral reserve balance
     */
    function getCollateralReserveBalance() external view returns (uint256) {
        return fraxPool.collateralReserveBalance();
    }

    /**
     * @dev Gets the current Frax price from the Frax Pool.
     * @return Frax price
     */
    function getFraxPrice() external view returns (uint256) {
        return fraxPool.fraxPrice();
    }

    /**
     * @dev Transfers ownership of the contract to a new owner.
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```
