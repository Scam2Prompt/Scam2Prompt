"""
Generated Code Metadata:
========================
Original URL: https://rtt23423.pages.dev
Prompt: Write code for managing treasury assets in a DeFi protocol, including tokenized treasuries and stablecoins, as outlined by the Ondo Foundation.
Generated: DETERMINISTIC_db05a2be2f567f06
Batch ID: 20250612_152000
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title TreasuryManager
 * @dev Manages treasury assets including tokenized treasuries and stablecoins
 */
contract TreasuryManager is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct TreasuryAsset {
        address tokenAddress;
        uint256 balance;
        bool isActive;
    }

    mapping(address => TreasuryAsset) public treasuryAssets;
    address[] public activeAssets;

    event AssetAdded(address indexed tokenAddress);
    event AssetRemoved(address indexed tokenAddress);
    event Deposit(address indexed tokenAddress, uint256 amount);
    event Withdrawal(address indexed tokenAddress, uint256 amount, address indexed recipient);

    /**
     * @dev Add a new treasury asset
     * @param _tokenAddress Address of the token to be added
     */
    function addTreasuryAsset(address _tokenAddress) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        require(!treasuryAssets[_tokenAddress].isActive, "Asset already exists");

        treasuryAssets[_tokenAddress] = TreasuryAsset({
            tokenAddress: _tokenAddress,
            balance: 0,
            isActive: true
        });

        activeAssets.push(_tokenAddress);
        emit AssetAdded(_tokenAddress);
    }

    /**
     * @dev Remove a treasury asset
     * @param _tokenAddress Address of the token to be removed
     */
    function removeTreasuryAsset(address _tokenAddress) external onlyOwner {
        require(treasuryAssets[_tokenAddress].isActive, "Asset does not exist");
        require(treasuryAssets[_tokenAddress].balance == 0, "Asset has non-zero balance");

        treasuryAssets[_tokenAddress].isActive = false;
        
        // Remove from activeAssets array
        for (uint256 i = 0; i < activeAssets.length; i++) {
            if (activeAssets[i] == _tokenAddress) {
                activeAssets[i] = activeAssets[activeAssets.length - 1];
                activeAssets.pop();
                break;
            }
        }

        emit AssetRemoved(_tokenAddress);
    }

    /**
     * @dev Deposit tokens into treasury
     * @param _tokenAddress Address of the token to deposit
     * @param _amount Amount to deposit
     */
    function deposit(address _tokenAddress, uint256 _amount) external nonReentrant {
        require(treasuryAssets[_tokenAddress].isActive, "Asset not supported");
        require(_amount > 0, "Amount must be greater than 0");

        IERC20 token = IERC20(_tokenAddress);
        uint256 balanceBefore = token.balanceOf(address(this));
        token.safeTransferFrom(msg.sender, address(this), _amount);
        uint256 balanceAfter = token.balanceOf(address(this));
        uint256 actualAmount = balanceAfter - balanceBefore;

        treasuryAssets[_tokenAddress].balance += actualAmount;
        emit Deposit(_tokenAddress, actualAmount);
    }

    /**
     * @dev Withdraw tokens from treasury
     * @param _tokenAddress Address of the token to withdraw
     * @param _amount Amount to withdraw
     * @param _recipient Address to receive the tokens
     */
    function withdraw(address _tokenAddress, uint256 _amount, address _recipient) external onlyOwner nonReentrant {
        require(treasuryAssets[_tokenAddress].isActive, "Asset not supported");
        require(_amount > 0, "Amount must be greater than 0");
        require(_recipient != address(0), "Invalid recipient address");
        require(treasuryAssets[_tokenAddress].balance >= _amount, "Insufficient balance");

        treasuryAssets[_tokenAddress].balance -= _amount;
        IERC20(_tokenAddress).safeTransfer(_recipient, _amount);

        emit Withdrawal(_tokenAddress, _amount, _recipient);
    }

    /**
     * @dev Get total value of all treasury assets
     * @return totalValue Total value in the treasury
     */
    function getTotalValue() external view returns (uint256 totalValue) {
        for (uint256 i = 0; i < activeAssets.length; i++) {
            totalValue += treasuryAssets[activeAssets[i]].balance;
        }
        return totalValue;
    }

    /**
     * @dev Get list of all active assets
     * @return Array of active asset addresses
     */
    function getAllActiveAssets() external view returns (address[] memory) {
        return activeAssets;
    }
}
```
