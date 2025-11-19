"""
Generated Code Metadata:
========================
Original URL: https://imptp.com
Prompt: "How can I implement a secure pledge system using Ethereum smart contracts and OpenZeppelin libraries?"
Generated: DETERMINISTIC_015778e78fafe7ae
Batch ID: 20250622_204829
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

/**
 * @title SecurePledgeSystem
 * @dev A contract that allows users to make pledges in ETH or ERC20 tokens
 * with withdrawal conditions set by the contract owner.
 */
contract SecurePledgeSystem is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct Pledge {
        address pledger;
        uint256 amount;
        uint256 unlockTime;
        bool isToken;
        address tokenAddress;
        bool withdrawn;
    }

    // Mapping from pledge ID to Pledge struct
    mapping(uint256 => Pledge) public pledges;

    // Total number of pledges created
    uint256 public pledgeCount;

    // Events
    event PledgeCreated(
        uint256 indexed id,
        address indexed pledger,
        uint256 amount,
        uint256 unlockTime,
        bool isToken,
        address tokenAddress
    );
    event PledgeWithdrawn(uint256 indexed id, address indexed receiver);
    event EmergencyWithdraw(address indexed owner, uint256 amount);

    /**
     * @dev Creates a new pledge in ETH
     * @param _unlockTime The timestamp when the pledge can be withdrawn
     */
    function createEthPledge(uint256 _unlockTime) external payable nonReentrant {
        require(msg.value > 0, "Pledge amount must be greater than 0");
        require(_unlockTime > block.timestamp, "Unlock time must be in the future");

        pledgeCount++;
        pledges[pledgeCount] = Pledge({
            pledger: msg.sender,
            amount: msg.value,
            unlockTime: _unlockTime,
            isToken: false,
            tokenAddress: address(0),
            withdrawn: false
        });

        emit PledgeCreated(
            pledgeCount,
            msg.sender,
            msg.value,
            _unlockTime,
            false,
            address(0)
        );
    }

    /**
     * @dev Creates a new pledge in ERC20 tokens
     * @param _tokenAddress The address of the ERC20 token
     * @param _amount The amount of tokens to pledge
     * @param _unlockTime The timestamp when the pledge can be withdrawn
     */
    function createTokenPledge(
        address _tokenAddress,
        uint256 _amount,
        uint256 _unlockTime
    ) external nonReentrant {
        require(_amount > 0, "Pledge amount must be greater than 0");
        require(_unlockTime > block.timestamp, "Unlock time must be in the future");
        require(_tokenAddress != address(0), "Token address cannot be zero");

        IERC20 token = IERC20(_tokenAddress);
        uint256 balanceBefore = token.balanceOf(address(this));
        token.safeTransferFrom(msg.sender, address(this), _amount);
        uint256 balanceAfter = token.balanceOf(address(this));
        uint256 actualAmount = balanceAfter - balanceBefore;

        pledgeCount++;
        pledges[pledgeCount] = Pledge({
            pledger: msg.sender,
            amount: actualAmount,
            unlockTime: _unlockTime,
            isToken: true,
            tokenAddress: _tokenAddress,
            withdrawn: false
        });

        emit PledgeCreated(
            pledgeCount,
            msg.sender,
            actualAmount,
            _unlockTime,
            true,
            _tokenAddress
        );
    }

    /**
     * @dev Withdraws a pledge after the unlock time has passed
     * @param _pledgeId The ID of the pledge to withdraw
     */
    function withdrawPledge(uint256 _pledgeId) external nonReentrant {
        require(_pledgeId > 0 && _pledgeId <= pledgeCount, "Invalid pledge ID");
        Pledge storage pledge = pledges[_pledgeId];

        require(msg.sender == pledge.pledger, "Only pledger can withdraw");
        require(!pledge.withdrawn, "Pledge already withdrawn");
        require(block.timestamp >= pledge.unlockTime, "Pledge is still locked");

        pledge.withdrawn = true;

        if (pledge.isToken) {
            IERC20(pledge.tokenAddress).safeTransfer(msg.sender, pledge.amount);
        } else {
            (bool success, ) = msg.sender.call{value: pledge.amount}("");
            require(success, "ETH transfer failed");
        }

        emit PledgeWithdrawn(_pledgeId, msg.sender);
    }

    /**
     * @dev Emergency withdraw function for owner to recover funds
     * @param _tokenAddress Address of the token to withdraw (address(0) for ETH)
     * @param _amount Amount to withdraw
     */
    function emergencyWithdraw(address _tokenAddress, uint256 _amount) external onlyOwner {
        if (_tokenAddress == address(0)) {
            (bool success, ) = owner().call{value: _amount}("");
            require(success, "ETH transfer failed");
            emit EmergencyWithdraw(owner(), _amount);
        } else {
            IERC20(_tokenAddress).safeTransfer(owner(), _amount);
            emit EmergencyWithdraw(owner(), _amount);
        }
    }

    /**
     * @dev Returns the details of a specific pledge
     * @param _pledgeId The ID of the pledge to query
     */
    function getPledge(uint256 _pledgeId) external view returns (Pledge memory) {
        require(_pledgeId > 0 && _pledgeId <= pledgeCount, "Invalid pledge ID");
        return pledges[_pledgeId];
    }
}
```
