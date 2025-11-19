"""
Generated Code Metadata:
========================
Original URL: https://bull-dogito-com.pages.dev
Prompt: How can I implement the "B2B Booster" strategy in a smart contract to invest in real-world assets while ensuring token sustainability?
Generated: DETERMINISTIC_759e9b8d5294f898
Batch ID: 20250612_155855
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title B2B Booster Strategy Contract
 * @author [Your Name]
 * @notice This contract implements the B2B Booster strategy for investing in real-world assets
 * while ensuring token sustainability.
 */
contract B2BBoosterStrategy is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping of investors to their investment amounts
    mapping(address => uint256) public investorBalances;

    // Mapping of asset investments to their values
    mapping(address => uint256) public assetValues;

    // Total value of all assets invested
    uint256 public totalAssetValue;

    // Sustainability threshold (e.g., 20% of total asset value)
    uint256 public sustainabilityThreshold;

    // Address of the asset investment contract
    address public assetInvestmentContract;

    /**
     * @dev Constructor for the B2B Booster strategy contract
     * @param _name Name of the token
     * @param _symbol Symbol of the token
     * @param _sustainabilityThreshold Sustainability threshold (e.g., 20% of total asset value)
     * @param _assetInvestmentContract Address of the asset investment contract
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _sustainabilityThreshold,
        address _assetInvestmentContract
    ) ERC20(_name, _symbol) {
        sustainabilityThreshold = _sustainabilityThreshold;
        assetInvestmentContract = _assetInvestmentContract;
    }

    /**
     * @dev Invest in a real-world asset
     * @param _asset Address of the asset to invest in
     * @param _amount Amount to invest
     */
    function investInAsset(address _asset, uint256 _amount) public {
        // Check if the asset investment contract is valid
        require(
            _asset == assetInvestmentContract,
            "Invalid asset investment contract"
        );

        // Transfer funds from the investor to the contract
        require(
            msg.sender.balance >= _amount,
            "Insufficient funds for investment"
        );

        // Update the investor's balance
        investorBalances[msg.sender] = investorBalances[msg.sender].add(
            _amount
        );

        // Update the asset value
        assetValues[_asset] = assetValues[_asset].add(_amount);

        // Update the total asset value
        totalAssetValue = totalAssetValue.add(_amount);

        // Check if the investment is sustainable
        require(
            totalAssetValue >= sustainabilityThreshold,
            "Investment is not sustainable"
        );

        // Emit an event to indicate the investment
        emit InvestedInAsset(msg.sender, _asset, _amount);
    }

    /**
     * @dev Withdraw from a real-world asset
     * @param _asset Address of the asset to withdraw from
     * @param _amount Amount to withdraw
     */
    function withdrawFromAsset(address _asset, uint256 _amount) public {
        // Check if the asset investment contract is valid
        require(
            _asset == assetInvestmentContract,
            "Invalid asset investment contract"
        );

        // Check if the investor has sufficient balance
        require(
            investorBalances[msg.sender] >= _amount,
            "Insufficient balance for withdrawal"
        );

        // Update the investor's balance
        investorBalances[msg.sender] = investorBalances[msg.sender].sub(
            _amount
        );

        // Update the asset value
        assetValues[_asset] = assetValues[_asset].sub(_amount);

        // Update the total asset value
        totalAssetValue = totalAssetValue.sub(_amount);

        // Transfer funds from the contract to the investor
        payable(msg.sender).transfer(_amount);

        // Emit an event to indicate the withdrawal
        emit WithdrewFromAsset(msg.sender, _asset, _amount);
    }

    /**
     * @dev Get the balance of an investor
     * @param _investor Address of the investor
     * @return The balance of the investor
     */
    function getInvestorBalance(address _investor) public view returns (uint256) {
        return investorBalances[_investor];
    }

    /**
     * @dev Get the value of an asset
     * @param _asset Address of the asset
     * @return The value of the asset
     */
    function getAssetValue(address _asset) public view returns (uint256) {
        return assetValues[_asset];
    }

    /**
     * @dev Get the total asset value
     * @return The total asset value
     */
    function getTotalAssetValue() public view returns (uint256) {
        return totalAssetValue;
    }

    event InvestedInAsset(
        address indexed investor,
        address indexed asset,
        uint256 amount
    );

    event WithdrewFromAsset(
        address indexed investor,
        address indexed asset,
        uint256 amount
    );
}
```
