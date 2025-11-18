"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone-finance.pages.dev
Prompt: Create a tutorial for configuring RedStone modular oracles to deliver custom data feeds for staked tokens on Fantom. Include deployment instructions.
Generated: DETERMINISTIC_f3255e7556e750d0
Batch ID: 20250612_152511
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

/// @title Custom Data Feed for Staked Tokens using RedStone Modular Oracles
/// @author Your Name
/// @notice This contract demonstrates how to configure RedStone oracles to deliver custom data feeds for staked tokens on the Fantom blockchain.

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@redstone-finance/evm-connector/contracts/RedStoneConsumer.sol";

// Main contract for managing custom data feeds
contract StakedTokenDataFeed is Ownable, RedStoneConsumer {
    using SafeMath for uint256;

    // Define the structure for storing token data
    struct TokenData {
        uint256 stakedAmount;
        uint256 rewardAmount;
        uint256 lastUpdateTime;
    }

    // Mapping from user address to token data
    mapping(address => TokenData) private userTokenData;

    // Event for logging data updates
    event DataUpdated(address indexed user, uint256 stakedAmount, uint256 rewardAmount);

    // Constructor to initialize the contract with the oracle address
    constructor(address _redStoneOracle) RedStoneConsumer(_redStoneOracle) {
    }

    /// @notice Update staked token and reward amounts for a user
    /// @param _stakedAmount Amount of tokens staked
    /// @param _rewardAmount Amount of tokens rewarded
    /// @dev Emits a DataUpdated event
    function updateTokenData(uint256 _stakedAmount, uint256 _rewardAmount) external {
        require(_stakedAmount > 0 || _rewardAmount > 0, "Invalid amounts");

        // Update user's token data
        userTokenData[msg.sender].stakedAmount = _stakedAmount;
        userTokenData[msg.sender].rewardAmount = _rewardAmount;
        userTokenData[msg.sender].lastUpdateTime = block.timestamp;

        emit DataUpdated(msg.sender, _stakedAmount, _rewardAmount);
    }

    /// @notice Get the token data for a specific user
    /// @param _user Address of the user
    /// @return stakedAmount Amount of tokens staked by the user
    /// @return rewardAmount Amount of tokens rewarded to the user
    function getTokenData(address _user) external view returns (uint256 stakedAmount, uint256 rewardAmount) {
        TokenData memory data = userTokenData[_user];
        return (data.stakedAmount, data.rewardAmount);
    }

    /// @notice Fetch the latest price from the RedStone oracle
    /// @return latestPrice The latest price of the asset
    function fetchLatestPrice() external view returns (uint256 latestPrice) {
        // Fetch price data from RedStone oracle
        try getLatestDataFeedValue("YOUR_TOKEN_SYMBOL") returns (uint256 price) {
            return price;
        } catch {
            revert("Failed to fetch price from RedStone oracle");
        }
    }

    /// @notice Admin function for updating the oracle address
    /// @param _newOracle Address of the new RedStone oracle
    function updateOracleAddress(address _newOracle) external onlyOwner {
        require(_newOracle != address(0), "Invalid oracle address");
        _setOracleAddress(_newOracle);
    }
}
```

### Deployment Instructions

1. **Set Up Development Environment**: Ensure you have a development environment with Node.js, Truffle, or Hardhat installed.

2. **Install Dependencies**:
   ```bash
   npm install @openzeppelin/contracts @redstone-finance/evm-connector
   ```

3. **Configure Deployment Script**: Create a deployment script in your Truffle or Hardhat project to deploy the `StakedTokenDataFeed` contract.

4. **Deploy to Fantom**:
   - Use the Fantom testnet or mainnet configurations in your deployment settings.
   - Execute the deploy command:
     ```bash
     truffle migrate --network fantom
     ```
   - Ensure you replace `"YOUR_TOKEN_SYMBOL"` with the actual token symbol you wish to fetch data for.

5. **Interact with the Contract**: Use web3 or ethers.js to interact with the deployed contract for updating and fetching token data, as well as retrieving pricing information.

6. **Testing**: Write tests to ensure the contract behaves as expected in all scenarios, including edge cases for updating data and fetching prices.
