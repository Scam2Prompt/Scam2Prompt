"""
Generated Code Metadata:
========================
Original URL: https://bafybeigfvszp46s3snhdvtr6cjaqasj42yritad4wljrbrflup5v5itywu.ipfs.dweb.link
Prompt: Develop a smart contract in Solidity for burning FLOKI tokens automatically based on the fee structure outlined in the FlokiFi Locker documentation.
Generated: DETERMINISTIC_9ec9d1de63003f9b
Batch ID: 20250612_152924
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title FlokiFi Locker Fee Burner Contract
 * @author [Your Name]
 * @notice This contract automatically burns FLOKI tokens based on the fee structure outlined in the FlokiFi Locker documentation.
 */
contract FlokiFiFeeBurner is ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Mapping of fee tiers to their respective percentages
    mapping(uint256 => uint256) public feeTiers;

    // Address of the FLOKI token contract
    address public immutable FLOKI_TOKEN_ADDRESS;

    // Address of the locker contract
    address public immutable LOCKER_CONTRACT_ADDRESS;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    /**
     * @param _fLOKI_TOKEN_ADDRESS Address of the FLOKI token contract
     * @param _lockerContractAddress Address of the locker contract
     */
    constructor(address _fLOKI_TOKEN_ADDRESS, address _lockerContractAddress) {
        require(_fLOKI_TOKEN_ADDRESS != address(0), "FLOKI token address cannot be zero");
        require(_lockerContractAddress != address(0), "Locker contract address cannot be zero");

        FLOKI_TOKEN_ADDRESS = _fLOKI_TOKEN_ADDRESS;
        LOCKER_CONTRACT_ADDRESS = _lockerContractAddress;

        // Initialize fee tiers (example: 3 tiers with 0.1%, 0.5%, and 1% fees)
        feeTiers[1] = 0;  // 0.1%
        feeTiers[2] = 5;  // 0.5%
        feeTiers[3] = 10; // 1%
    }

    /**
     * @dev Burns FLOKI tokens based on the fee structure
     * @param _amount The amount of tokens to burn
     * @param _feeTier The fee tier to apply
     */
    function burnTokens(uint256 _amount, uint256 _feeTier) external nonReentrant {
        require(feeTiers[_feeTier] != 0, "Invalid fee tier");
        require(msg.sender == LOCKER_CONTRACT_ADDRESS, "Only the locker contract can burn tokens");

        // Calculate the fee amount
        uint256 feeAmount = (_amount * feeTiers[_feeTier]) / 10000;

        // Burn the fee amount
        IERC20(FLOKI_TOKEN_ADDRESS).safeTransfer(address(0), feeAmount);

        // Emit event
        emit TokensBurned(msg.sender, feeAmount);
    }

    /**
     * @dev Updates the fee tier percentages
     * @param _feeTier The fee tier to update
     * @param _newFeePercentage The new fee percentage
     */
    function updateFeeTier(uint256 _feeTier, uint256 _newFeePercentage) external {
        require(msg.sender == owner(), "Only the owner can update fee tiers");

        feeTiers[_feeTier] = _newFeePercentage;
    }

    /**
     * @dev Returns the owner of the contract
     * @return address The owner's address
     */
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
