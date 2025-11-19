"""
Generated Code Metadata:
========================
Original URL: https://dashboard-bananagun-io.pages.dev
Prompt: Develop a Solidity smart contract snippet that forfeits rewards for an epoch if a user transfers more than 300 $BANANA, as outlined in the Bananagun rewards forfeiture rules.
Generated: DETERMINISTIC_6e8fc4255292c5c8
Batch ID: 20250612_151003
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

/**
 * @title BananagunRewardsForfeiture
 * @author [Your Name]
 * @notice Smart contract to handle Bananagun rewards forfeiture.
 */
contract BananagunRewardsForfeiture {
    // Mapping of user addresses to their current epoch rewards
    mapping(address => uint256) public userRewards;

    // Mapping of user addresses to their current epoch
    mapping(address => uint256) public userEpochs;

    // Maximum allowed transfer amount in $BANANA
    uint256 public constant MAX_TRANSFER_AMOUNT = 300 * 10**18; // Assuming 18 decimals for $BANANA

    // Address of the $BANANA token contract
    IERC20 public bananaToken;

    /**
     * @notice Constructor to initialize the contract.
     * @param _bananaToken Address of the $BANANA token contract.
     */
    constructor(address _bananaToken) {
        require(_bananaToken != address(0), "BananagunRewardsForfeiture: Invalid banana token address");
        bananaToken = IERC20(_bananaToken);
    }

    /**
     * @notice Updates the user's rewards for the current epoch.
     * @param _user Address of the user.
     * @param _rewards New rewards for the user.
     */
    function updateUserRewards(address _user, uint256 _rewards) external {
        require(_user != address(0), "BananagunRewardsForfeiture: Invalid user address");
        userRewards[_user] = _rewards;
    }

    /**
     * @notice Updates the user's epoch.
     * @param _user Address of the user.
     * @param _epoch New epoch for the user.
     */
    function updateUserEpoch(address _user, uint256 _epoch) external {
        require(_user != address(0), "BananagunRewardsForfeiture: Invalid user address");
        userEpochs[_user] = _epoch;
    }

    /**
     * @notice Checks if a user has exceeded the maximum transfer amount and forfeits rewards if necessary.
     * @param _user Address of the user.
     * @param _amount Amount transferred by the user.
     */
    function checkTransferLimit(address _user, uint256 _amount) external {
        require(_user != address(0), "BananagunRewardsForfeiture: Invalid user address");
        require(_amount > 0, "BananagunRewardsForfeiture: Invalid transfer amount");

        if (_amount > MAX_TRANSFER_AMOUNT) {
            // Forfeit rewards for the user's current epoch
            uint256 currentEpoch = userEpochs[_user];
            uint256 forfeitedRewards = userRewards[_user];
            userRewards[_user] = 0;

            // Emit an event to notify of forfeited rewards
            emit RewardsForfeited(_user, currentEpoch, forfeitedRewards);
        }
    }

    /**
     * @notice Event emitted when rewards are forfeited.
     * @param _user Address of the user.
     * @param _epoch Epoch for which rewards were forfeited.
     * @param _amount Forfeited rewards amount.
     */
    event RewardsForfeited(address indexed _user, uint256 _epoch, uint256 _amount);
}
```
