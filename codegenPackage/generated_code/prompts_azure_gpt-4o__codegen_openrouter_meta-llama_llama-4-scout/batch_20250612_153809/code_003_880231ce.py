"""
Generated Code Metadata:
========================
Original URL: https://worldlibertyfinancial-labs.com
Prompt: Implement a Solidity contract to manage the gradual transfer of net protocol revenues from WLF Holdco LLC to the DAO, ensuring decentralized control and fair distribution as outlined on the World Liberty Financial Labs site.
Generated: DETERMINISTIC_880231ce8ec7f7e9
Batch ID: 20250612_153809
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title NetProtocolRevenueManager
 * @author World Liberty Financial Labs
 * @notice Manages the gradual transfer of net protocol revenues from WLF Holdco LLC to the DAO.
 */
contract NetProtocolRevenueManager is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of revenue recipients
    mapping(address => uint256) public revenueRecipients;

    // Total revenue allocated
    uint256 public totalRevenue;

    // Revenue transfer rate (in percentage)
    uint256 public revenueTransferRate;

    // Revenue transfer interval (in seconds)
    uint256 public revenueTransferInterval;

    // Last revenue transfer timestamp
    uint256 public lastRevenueTransfer;

    // WLF Holdco LLC's token contract
    IERC20 public wlfToken;

    /**
     * @dev Initializes the contract.
     * @param _wlfToken WLF Holdco LLC's token contract address.
     * @param _revenueTransferRate Revenue transfer rate (in percentage).
     * @param _revenueTransferInterval Revenue transfer interval (in seconds).
     */
    constructor(
        address _wlfToken,
        uint256 _revenueTransferRate,
        uint256 _revenueTransferInterval
    ) public {
        require(_wlfToken != address(0), "Invalid WLF token address");
        require(_revenueTransferRate > 0, "Revenue transfer rate must be greater than 0");
        require(_revenueTransferInterval > 0, "Revenue transfer interval must be greater than 0");

        wlfToken = IERC20(_wlfToken);
        revenueTransferRate = _revenueTransferRate;
        revenueTransferInterval = _revenueTransferInterval;
        lastRevenueTransfer = block.timestamp;
    }

    /**
     * @dev Adds a revenue recipient.
     * @param _recipient Recipient address.
     * @param _allocation Allocation amount.
     */
    function addRevenueRecipient(address _recipient, uint256 _allocation) public onlyOwner {
        require(_recipient != address(0), "Invalid recipient address");
        require(_allocation > 0, "Allocation must be greater than 0");

        revenueRecipients[_recipient] = revenueRecipients[_recipient].add(_allocation);
        totalRevenue = totalRevenue.add(_allocation);
    }

    /**
     * @dev Updates the revenue transfer rate.
     * @param _newRate New revenue transfer rate (in percentage).
     */
    function updateRevenueTransferRate(uint256 _newRate) public onlyOwner {
        require(_newRate > 0, "Revenue transfer rate must be greater than 0");

        revenueTransferRate = _newRate;
    }

    /**
     * @dev Updates the revenue transfer interval.
     * @param _newInterval New revenue transfer interval (in seconds).
     */
    function updateRevenueTransferInterval(uint256 _newInterval) public onlyOwner {
        require(_newInterval > 0, "Revenue transfer interval must be greater than 0");

        revenueTransferInterval = _newInterval;
    }

    /**
     * @dev Transfers revenue to recipients.
     */
    function transferRevenue() public nonReentrant {
        require(block.timestamp.sub(lastRevenueTransfer) >= revenueTransferInterval, "Revenue transfer interval not elapsed");

        uint256 transferAmount = calculateTransferAmount();
        lastRevenueTransfer = block.timestamp;

        for (address recipient in revenueRecipients) {
            uint256 recipientAllocation = revenueRecipients[recipient];
            uint256 recipientTransferAmount = transferAmount.mul(recipientAllocation).div(totalRevenue);

            require(wlfToken.transfer(recipient, recipientTransferAmount), "Revenue transfer failed");
        }
    }

    /**
     * @dev Calculates the revenue transfer amount.
     * @return Revenue transfer amount.
     */
    function calculateTransferAmount() internal view returns (uint256) {
        uint256 wlfBalance = wlfToken.balanceOf(address(this));
        return wlfBalance.mul(revenueTransferRate).div(100);
    }

    /**
     * @dev Withdraws excess tokens.
     * @param _token Token contract address.
     * @param _recipient Recipient address.
     */
    function withdrawExcessTokens(address _token, address _recipient) public onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(_recipient != address(0), "Invalid recipient address");

        IERC20 token = IERC20(_token);
        uint256 balance = token.balanceOf(address(this));
        require(token.transfer(_recipient, balance), "Token withdrawal failed");
    }
}
```
