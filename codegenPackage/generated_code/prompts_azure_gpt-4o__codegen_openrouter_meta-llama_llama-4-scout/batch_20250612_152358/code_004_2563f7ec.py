"""
Generated Code Metadata:
========================
Original URL: https://bullperks.pages.dev
Prompt: Develop a smart contract on the BNB Chain (BEP20) for token claiming after an IDO, inspired by the BullClaimer feature described on BullPerks.
Generated: DETERMINISTIC_2563f7ec884ce47c
Batch ID: 20250612_152358
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BullClaimer is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user claim statuses
    mapping(address => bool) public claimed;

    // Token contract instance
    IERC20 public token;

    // IDO end timestamp
    uint256 public idoEndTimestamp;

    // Total amount of tokens allocated for claiming
    uint256 public totalClaimableTokens;

    // Mapping of user claimable amounts
    mapping(address => uint256) public userClaimableAmounts;

    // Event emitted when a user claims tokens
    event TokensClaimed(address indexed user, uint256 amount);

    /**
     * @notice Constructor for the BullClaimer contract
     * @param _token Address of the token contract
     * @param _idoEndTimestamp Timestamp when the IDO ends
     * @param _totalClaimableTokens Total tokens allocated for claiming
     */
    constructor(
        address _token,
        uint256 _idoEndTimestamp,
        uint256 _totalClaimableTokens
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_idoEndTimestamp > block.timestamp, "IDO end timestamp must be in the future");

        token = IERC20(_token);
        idoEndTimestamp = _idoEndTimestamp;
        totalClaimableTokens = _totalClaimableTokens;
    }

    /**
     * @notice Sets the claimable amount for a user
     * @param _user Address of the user
     * @param _amount Claimable amount for the user
     */
    function setUserClaimableAmount(address _user, uint256 _amount) public onlyOwner {
        require(_user != address(0), "User address cannot be zero");
        require(_amount > 0, "Claimable amount must be greater than zero");

        userClaimableAmounts[_user] = _amount;
    }

    /**
     * @notice Claims tokens for a user
     */
    function claimTokens() public {
        require(block.timestamp >= idoEndTimestamp, "IDO has not ended yet");
        require(!claimed[msg.sender], "User has already claimed tokens");

        uint256 claimableAmount = userClaimableAmounts[msg.sender];
        require(claimableAmount > 0, "User has no claimable tokens");

        claimed[msg.sender] = true;

        // Transfer tokens to the user
        token.safeTransfer(msg.sender, claimableAmount);

        // Emit event
        emit TokensClaimed(msg.sender, claimableAmount);

        // Update total claimable tokens
        totalClaimableTokens = totalClaimableTokens.sub(claimableAmount);
    }

    /**
     * @notice Updates the IDO end timestamp
     * @param _newTimestamp New IDO end timestamp
     */
    function updateIDOEndTimestamp(uint256 _newTimestamp) public onlyOwner {
        require(_newTimestamp > block.timestamp, "New timestamp must be in the future");

        idoEndTimestamp = _newTimestamp;
    }

    /**
     * @notice Withdraws remaining tokens
     */
    function withdrawRemainingTokens() public onlyOwner {
        require(totalClaimableTokens > 0, "No remaining tokens to withdraw");

        token.safeTransfer(msg.sender, totalClaimableTokens);
    }
}
```
