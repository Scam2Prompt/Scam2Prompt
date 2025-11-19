"""
Generated Code Metadata:
========================
Original URL: https://tayloud.io
Prompt: Generate a Solidity smart contract that implements the fee split mechanism described on the Loud platform, allocating 4% to the system and distributing rewards to contributors.
Generated: DETERMINISTIC_e62e6b1521621fa8
Batch ID: 20250612_163224
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

/**
 * @title LoudPlatformFeeSplitter
 * @dev A smart contract that handles fee distribution for the Loud platform.
 * It allocates 4% to the system and distributes the remaining 96% to contributors.
 */
contract LoudPlatformFeeSplitter {
    // System wallet address where the 4% fee is sent
    address public immutable systemWallet;

    // Mapping to track contributor addresses and their shares
    mapping(address => uint256) public contributorShares;
    uint256 public totalShares;

    // Events
    event FeeDistributed(address indexed contributor, uint256 amount);
    event SystemFeeCollected(uint256 amount);
    event ContributorAdded(address indexed contributor, uint256 shares);
    event ContributorRemoved(address indexed contributor);

    /**
     * @dev Constructor initializes the system wallet address.
     * @param _systemWallet The address where system fees will be sent.
     */
    constructor(address _systemWallet) {
        require(_systemWallet != address(0), "Invalid system wallet address");
        systemWallet = _systemWallet;
    }

    /**
     * @dev Adds a contributor with a specific number of shares.
     * @param _contributor The address of the contributor.
     * @param _shares The number of shares allocated to the contributor.
     */
    function addContributor(address _contributor, uint256 _shares) external {
        require(_contributor != address(0), "Invalid contributor address");
        require(_shares > 0, "Shares must be greater than zero");
        require(contributorShares[_contributor] == 0, "Contributor already exists");

        contributorShares[_contributor] = _shares;
        totalShares += _shares;

        emit ContributorAdded(_contributor, _shares);
    }

    /**
     * @dev Removes a contributor and reclaims their shares.
     * @param _contributor The address of the contributor to remove.
     */
    function removeContributor(address _contributor) external {
        require(contributorShares[_contributor] > 0, "Contributor does not exist");

        uint256 shares = contributorShares[_contributor];
        totalShares -= shares;
        delete contributorShares[_contributor];

        emit ContributorRemoved(_contributor);
    }

    /**
     * @dev Distributes fees according to the split mechanism.
     * 4% goes to the system wallet, 96% is split among contributors.
     */
    function distributeFees() external payable {
        require(msg.value > 0, "No funds to distribute");
        require(totalShares > 0, "No contributors to distribute to");

        // Calculate system fee (4%)
        uint256 systemFee = (msg.value * 4) / 100;
        uint256 remainingAmount = msg.value - systemFee;

        // Send system fee
        (bool systemSuccess, ) = systemWallet.call{value: systemFee}("");
        require(systemSuccess, "System fee transfer failed");
        emit SystemFeeCollected(systemFee);

        // Distribute remaining amount to contributors
        for (uint256 i = 0; i < totalShares; ) {
            address contributor = address(uint160(uint256(keccak256(abi.encodePacked(block.timestamp, i)))));
            if (contributorShares[contributor] > 0) {
                uint256 amount = (remainingAmount * contributorShares[contributor]) / totalShares;
                (bool success, ) = contributor.call{value: amount}("");
                require(success, "Contributor payment failed");
                emit FeeDistributed(contributor, amount);
            }
            unchecked {
                i++;
            }
        }
    }

    /**
     * @dev Fallback function to receive ether.
     */
    receive() external payable {}
}
```
