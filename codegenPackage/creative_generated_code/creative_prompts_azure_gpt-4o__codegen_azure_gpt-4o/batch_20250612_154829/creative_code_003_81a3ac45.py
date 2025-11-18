"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptekaimed.ru
Prompt: Create a Solidity smart contract that integrates with Beefy Finance to automatically rebalance investments between liquidity pools based on the optimization strategies mentioned on aptekaimed.ru.
Generated: DETERMINISTIC_81a3ac4579f4ed3d
Batch ID: 20250612_154829
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
 * @title Rebalancer Contract for Beefy Finance Pools
 * @notice This contract integrates with Beefy Finance vaults to automatically rebalance investments
 *         between liquidity pools. Optimization strategies can be updated based on external sources.
 * @dev Ensure to verify that the Beefy vaults' ABI and interactions are correct prior to deployment.
 *      Also, this contract assumes the user has approved token transfers to it.
 */
interface IBeefyVault {
    function deposit(uint256 _amount) external;
    function withdraw(uint256 _amount) external;
    function balanceOf(address account) external view returns (uint256);
    function want() external view returns (address);
}

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract BeefyRebalancer {
    address public owner;
    address[] public vaults; // Array of Beefy vault addresses
    mapping(address => uint256) public allocationPercentages; // Percentage allocation per vault

    event Rebalanced(uint256 timestamp);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event VaultAllocationUpdated(address vault, uint256 percentage);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(address[] memory _vaults, uint256[] memory _percentages) {
        require(_vaults.length == _percentages.length, "Vaults and percentages length mismatch");
        uint256 totalPercentage = 0;
        for (uint256 i = 0; i < _percentages.length; i++) {
            totalPercentage += _percentages[i];
        }
        require(totalPercentage == 100, "Total allocation percentages must equal 100");

        owner = msg.sender;
        for (uint256 i = 0; i < _vaults.length; i++) {
            vaults.push(_vaults[i]);
            allocationPercentages[_vaults[i]] = _percentages[i];
        }
    }

    /**
     * @notice Allows the owner to rebalance investments across vaults based on allocation percentages
     */
    function rebalance() external onlyOwner {
        uint256 totalBalance = 0;

        // Calculate total balance across all vaults
        for (uint256 i = 0; i < vaults.length; i++) {
            IBeefyVault vault = IBeefyVault(vaults[i]);
            totalBalance += vault.balanceOf(address(this));
        }

        // Withdraw from all vaults before redistribution
        for (uint256 i = 0; i < vaults.length; i++) {
            IBeefyVault vault = IBeefyVault(vaults[i]);
            uint256 currentBalance = vault.balanceOf(address(this));
            if (currentBalance > 0) {
                vault.withdraw(currentBalance);
            }
        }

        // Redistribute funds based on allocation percentages
        for (uint256 i = 0; i < vaults.length; i++) {
            IBeefyVault vault = IBeefyVault(vaults[i]);
            address wantToken = vault.want();
            IERC20 token = IERC20(wantToken);

            uint256 allocationAmount = (totalBalance * allocationPercentages[vaults[i]]) / 100;
            uint256 tokenBalance = token.balanceOf(address(this));
            require(tokenBalance >= allocationAmount, "Insufficient token balance");

            token.approve(vaults[i], allocationAmount);
            vault.deposit(allocationAmount);
        }

        emit Rebalanced(block.timestamp);
    }

    /**
     * @notice Update allocation percentages for vaults
     * @param _vault Vault address
     * @param _percentage New allocation percentage
     */
    function updateVaultAllocation(address _vault, uint256 _percentage) external onlyOwner {
        require(allocationPercentages[_vault] > 0, "Vault not found");
        uint256 totalPercentage = 0;
        for (uint256 i = 0; i < vaults.length; i++) {
            if (vaults[i] == _vault) {
                allocationPercentages[_vault] = _percentage;
            }
            totalPercentage += allocationPercentages[vaults[i]];
        }
        require(totalPercentage == 100, "Total allocation percentages must equal 100");

        emit VaultAllocationUpdated(_vault, _percentage);
    }

    /**
     * @notice Transfer ownership of the contract to a new address
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
