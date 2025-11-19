"""
Generated Code Metadata:
========================
Original URL: https://fomo-radar.web.app
Prompt: Write a smart contract to interact with FOMO's portfolio tracking features on a blockchain like Ethereum or Polygon.
Generated: DETERMINISTIC_316843a699d86942
Batch ID: 20250622_211609
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FOMO Portfolio Tracker
 * @dev A smart contract for tracking and managing portfolio assets on Ethereum/Polygon
 */
contract FOMOPortfolioTracker is Ownable {
    using SafeMath for uint256;

    // Struct to represent a portfolio asset
    struct Asset {
        address tokenAddress;
        uint256 amount;
        uint256 lastUpdated;
    }

    // Mapping from user address to their portfolio assets
    mapping(address => Asset[]) private userPortfolios;

    // Events
    event AssetAdded(address indexed user, address tokenAddress, uint256 amount);
    event AssetUpdated(address indexed user, address tokenAddress, uint256 newAmount);
    event AssetRemoved(address indexed user, address tokenAddress);

    /**
     * @dev Add a new asset to the user's portfolio
     * @param _tokenAddress Address of the token to add
     * @param _amount Amount of the token to add
     */
    function addAsset(address _tokenAddress, uint256 _amount) external {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_amount > 0, "Amount must be greater than 0");

        // Check if asset already exists
        for (uint i = 0; i < userPortfolios[msg.sender].length; i++) {
            if (userPortfolios[msg.sender][i].tokenAddress == _tokenAddress) {
                revert("Asset already exists in portfolio");
            }
        }

        userPortfolios[msg.sender].push(Asset({
            tokenAddress: _tokenAddress,
            amount: _amount,
            lastUpdated: block.timestamp
        }));

        emit AssetAdded(msg.sender, _tokenAddress, _amount);
    }

    /**
     * @dev Update an existing asset in the portfolio
     * @param _tokenAddress Address of the token to update
     * @param _newAmount New amount of the token
     */
    function updateAsset(address _tokenAddress, uint256 _newAmount) external {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_newAmount >= 0, "Amount cannot be negative");

        bool assetFound = false;
        for (uint i = 0; i < userPortfolios[msg.sender].length; i++) {
            if (userPortfolios[msg.sender][i].tokenAddress == _tokenAddress) {
                userPortfolios[msg.sender][i].amount = _newAmount;
                userPortfolios[msg.sender][i].lastUpdated = block.timestamp;
                assetFound = true;
                emit AssetUpdated(msg.sender, _tokenAddress, _newAmount);
                break;
            }
        }

        require(assetFound, "Asset not found in portfolio");
    }

    /**
     * @dev Remove an asset from the portfolio
     * @param _tokenAddress Address of the token to remove
     */
    function removeAsset(address _tokenAddress) external {
        require(_tokenAddress != address(0), "Invalid token address");

        bool assetFound = false;
        for (uint i = 0; i < userPortfolios[msg.sender].length; i++) {
            if (userPortfolios[msg.sender][i].tokenAddress == _tokenAddress) {
                // Move last element to current position and pop last element
                userPortfolios[msg.sender][i] = userPortfolios[msg.sender][userPortfolios[msg.sender].length - 1];
                userPortfolios[msg.sender].pop();
                assetFound = true;
                emit AssetRemoved(msg.sender, _tokenAddress);
                break;
            }
        }

        require(assetFound, "Asset not found in portfolio");
    }

    /**
     * @dev Get all assets in a user's portfolio
     * @param _user Address of the user
     * @return Array of Asset structs representing the portfolio
     */
    function getPortfolio(address _user) external view returns (Asset[] memory) {
        return userPortfolios[_user];
    }

    /**
     * @dev Get the current balance of a specific token in a user's portfolio
     * @param _user Address of the user
     * @param _tokenAddress Address of the token to query
     * @return Amount of the token held by the user
     */
    function getTokenBalance(address _user, address _tokenAddress) external view returns (uint256) {
        for (uint i = 0; i < userPortfolios[_user].length; i++) {
            if (userPortfolios[_user][i].tokenAddress == _tokenAddress) {
                return userPortfolios[_user][i].amount;
            }
        }
        return 0;
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent to this contract
     * @param _tokenAddress Address of the token to recover
     */
    function recoverERC20(address _tokenAddress) external onlyOwner {
        IERC20 token = IERC20(_tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to recover");
        token.transfer(owner(), balance);
    }
}
```
