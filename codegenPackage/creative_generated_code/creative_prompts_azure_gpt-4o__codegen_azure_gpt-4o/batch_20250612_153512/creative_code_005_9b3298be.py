"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uclaimrwdist.pages.dev
Prompt: Write Solidity code for a smart contract that manages $USDC token distribution with FCFS logic and wallet signature verification.
Generated: DETERMINISTIC_9b3298beaa5cd964
Batch ID: 20250612_153512
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

/**
 * @title USDC Distribution Contract with FCFS Logic and Wallet Signature Verification
 * @dev This contract distributes $USDC tokens to eligible users based on an FCFS (First Come First Serve) mechanism.
 *      It also verifies the user's wallet signature for authentication.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract USDCDistribution is Ownable {
    using ECDSA for bytes32;

    // Address of the $USDC token contract
    IERC20 public usdcToken;

    // Maximum amount of $USDC that can be distributed
    uint256 public maxDistributionAmount;

    // Amount of $USDC allocated per user
    uint256 public allocationPerUser;

    // Mapping to track distributed amounts to each user
    mapping(address => bool) public hasClaimed;

    // Address of the signer used for wallet signature verification
    address public signer;

    /**
     * @dev Constructor to initialize contract parameters.
     * @param _usdcToken Address of the $USDC token contract
     * @param _maxDistributionAmount Maximum $USDC allocation for distribution
     * @param _allocationPerUser Amount of $USDC allocated per user
     * @param _signer Address of the signer for signature verification
     */
    constructor(
        address _usdcToken,
        uint256 _maxDistributionAmount,
        uint256 _allocationPerUser,
        address _signer
    ) {
        require(_usdcToken != address(0), "Invalid USDC token address");
        require(_signer != address(0), "Invalid signer address");
        usdcToken = IERC20(_usdcToken);
        maxDistributionAmount = _maxDistributionAmount;
        allocationPerUser = _allocationPerUser;
        signer = _signer;
    }

    /**
     * @dev Allows a user to claim $USDC allocation.
     * @param _signature Signature signed by the signer validating the user's wallet
     */
    function claimUSDC(bytes memory _signature) external {
        // Ensure the user hasn't already claimed
        require(!hasClaimed[msg.sender], "User has already claimed");

        // Ensure sufficient $USDC balance in the contract
        require(usdcToken.balanceOf(address(this)) >= allocationPerUser, "Insufficient $USDC balance in contract");

        // Verify the signature
        bytes32 messageHash = keccak256(abi.encodePacked(msg.sender));
        address recoveredSigner = messageHash.toEthSignedMessageHash().recover(_signature);
        require(recoveredSigner == signer, "Invalid signature");

        // Mark the user as claimed
        hasClaimed[msg.sender] = true;

        // Transfer $USDC to the user
        bool success = usdcToken.transfer(msg.sender, allocationPerUser);
        require(success, "$USDC transfer failed");
    }

    /**
     * @dev Allows the owner to withdraw remaining $USDC tokens from the contract.
     */
    function withdrawRemainingUSDC() external onlyOwner {
        uint256 balance = usdcToken.balanceOf(address(this));
        require(balance > 0, "No $USDC tokens to withdraw");
        bool success = usdcToken.transfer(owner(), balance);
        require(success, "$USDC withdrawal failed");
    }

    /**
     * @dev Allows the owner to update the signer address.
     * @param _newSigner Address of the new signer
     */
    function updateSigner(address _newSigner) external onlyOwner {
        require(_newSigner != address(0), "Invalid signer address");
        signer = _newSigner;
    }

    /**
     * @dev Emergency function to update allocation per user.
     * @param _newAllocation Amount of $USDC to allocate per user
     */
    function updateAllocationPerUser(uint256 _newAllocation) external onlyOwner {
        require(_newAllocation > 0, "Allocation must be greater than zero");
        allocationPerUser = _newAllocation;
    }
}
```
