"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-extra.fi
Prompt: Write a Solidity contract for yield farming that includes automated reinvestment and rebalancing strategies inspired by Extra Finance's vaults.
Generated: DETERMINISTIC_b5dd8c54402a6d75
Batch ID: 20250612_153923
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IYieldFarm {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function claimRewards() external returns (uint256);
    function balanceOf() external view returns (uint256);
}

contract YieldFarmingVault is Ownable {
    using SafeMath for uint256;

    // Struct to hold information about each asset
    struct Asset {
        IERC20 token;        // The ERC20 token of the asset
        IYieldFarm farm;     // The yield farm contract
        uint256 balance;     // Current balance of the asset in the vault
        uint256 lastClaim;   // Last timestamp when rewards were claimed
    }

    // Mapping of asset addresses to their corresponding Asset struct
    mapping(address => Asset) public assets;
    
    // Event to log deposits
    event Deposited(address indexed token, uint256 amount);
    
    // Event to log withdrawals
    event Withdrawn(address indexed token, uint256 amount);
    
    // Event to log automatic rebalancing
    event Rebalanced(address indexed token, uint256 newBalance);

    // Deposit assets into the vault
    function deposit(address _token, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        Asset storage asset = assets[_token];

        // If asset is not already added, initialize it
        if (asset.token == IERC20(address(0))) {
            asset.token = IERC20(_token);
            asset.farm = IYieldFarm(_token); // Assume the yield farm address is the same as the token address for this example
        }

        // Transfer the tokens to the contract
        asset.token.transferFrom(msg.sender, address(this), _amount);
        asset.balance = asset.balance.add(_amount);

        // Deposit into the yield farm
        asset.token.approve(address(asset.farm), _amount);
        asset.farm.deposit(_amount);

        emit Deposited(_token, _amount);
    }

    // Withdraw assets from the vault
    function withdraw(address _token, uint256 _amount) external onlyOwner {
        Asset storage asset = assets[_token];
        require(asset.balance >= _amount, "Insufficient balance");

        // Withdraw from the yield farm
        asset.farm.withdraw(_amount);
        asset.balance = asset.balance.sub(_amount);
        
        // Transfer tokens back to the owner
        asset.token.transfer(msg.sender, _amount);

        emit Withdrawn(_token, _amount);
    }

    // Claim rewards from the yield farm and automatically reinvest them
    function claimAndReinvest(address _token) external onlyOwner {
        Asset storage asset = assets[_token];

        // Claim rewards
        uint256 rewards = asset.farm.claimRewards();
        
        // Reinvest rewards if any
        if (rewards > 0) {
            asset.token.approve(address(asset.farm), rewards);
            asset.farm.deposit(rewards);
            asset.balance = asset.balance.add(rewards);
        }
        
        asset.lastClaim = block.timestamp;
    }

    // Automated rebalancing strategy (simple example)
    function rebalance() external onlyOwner {
        // For simplicity, this function will just log the rebalancing event
        // A more complex strategy should be implemented as needed
        for (address tokenAddress in allAssetAddresses) {
            Asset storage asset = assets[tokenAddress];
            asset.farm.withdraw(asset.balance); // Withdraw all to rebalance
            asset.farm.deposit(asset.balance);   // Re-deposit back to yield farm

            emit Rebalanced(tokenAddress, asset.balance);
        }
    }

    // Function to view the balance of an asset
    function getAssetBalance(address _token) external view returns (uint256) {
        return assets[_token].balance;
    }
}
```
