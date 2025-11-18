"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tgdrop.cc
Prompt: Create a smart contract in Solidity for a TON-based reward system that distributes rewards based on NFT or USDT qualifications.
Generated: DETERMINISTIC_573797429fbaa59a
Batch ID: 20250612_153915
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
 * @title RewardDistributor
 * @dev Smart contract for distributing rewards based on NFT or USDT qualifications in a TON-based system.
 */
contract RewardDistributor {
    address public owner; // Owner of the contract
    address public usdtTokenAddress; // Address of the USDT token contract
    address public nftContractAddress; // Address of the NFT contract
    uint256 public rewardAmountTON; // Amount of TON to distribute as a reward

    // Mapping to track addresses that have already received rewards
    mapping(address => bool) public hasReceivedReward;

    // Events
    event RewardDistributed(address indexed recipient, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to only the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with essential parameters.
     * @param _usdtTokenAddress Address of the USDT token contract.
     * @param _nftContractAddress Address of the NFT contract.
     * @param _rewardAmountTON Amount of TON to distribute as a reward.
     */
    constructor(
        address _usdtTokenAddress,
        address _nftContractAddress,
        uint256 _rewardAmountTON
    ) {
        require(_usdtTokenAddress != address(0), "Invalid USDT token address");
        require(_nftContractAddress != address(0), "Invalid NFT contract address");
        require(_rewardAmountTON > 0, "Reward amount must be greater than zero");

        owner = msg.sender;
        usdtTokenAddress = _usdtTokenAddress;
        nftContractAddress = _nftContractAddress;
        rewardAmountTON = _rewardAmountTON;
    }

    /**
     * @dev Function to distribute rewards to a user based on their qualifications.
     * The user must hold an NFT or have a USDT balance greater than zero.
     * @param recipient Address of the user to receive the reward.
     */
    function distributeReward(address recipient) external {
        require(recipient != address(0), "Invalid recipient address");
        require(!hasReceivedReward[recipient], "Reward already claimed");

        // Check NFT ownership
        bool holdsNFT = checkNFTOwnership(recipient);
        // Check USDT balance
        bool hasUSDTBalance = checkUSDTBalance(recipient);

        require(holdsNFT || hasUSDTBalance, "User does not qualify for rewards");

        hasReceivedReward[recipient] = true;

        // Transfer TON reward
        (bool sent, ) = recipient.call{value: rewardAmountTON}("");
        require(sent, "Failed to send TON reward");

        emit RewardDistributed(recipient, rewardAmountTON);
    }

    /**
     * @dev Function to check if a user holds an NFT.
     * @param user Address of the user.
     * @return bool True if the user holds an NFT, false otherwise.
     */
    function checkNFTOwnership(address user) public view returns (bool) {
        // Interface call to NFT contract to check ownership
        (bool success, bytes memory result) = nftContractAddress.staticcall(
            abi.encodeWithSignature("balanceOf(address)", user)
        );
        require(success, "Failed to query NFT ownership");

        uint256 balance = abi.decode(result, (uint256));
        return balance > 0;
    }

    /**
     * @dev Function to check if a user has a USDT balance greater than zero.
     * @param user Address of the user.
     * @return bool True if the user has a USDT balance, false otherwise.
     */
    function checkUSDTBalance(address user) public view returns (bool) {
        // Interface call to USDT contract to check balance
        (bool success, bytes memory result) = usdtTokenAddress.staticcall(
            abi.encodeWithSignature("balanceOf(address)", user)
        );
        require(success, "Failed to query USDT balance");

        uint256 balance = abi.decode(result, (uint256));
        return balance > 0;
    }

    /**
     * @dev Function to allow the owner to withdraw TON from the contract.
     */
    function withdrawTON() external onlyOwner {
        (bool sent, ) = owner.call{value: address(this).balance}("");
        require(sent, "Failed to withdraw TON");
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Fallback function to receive TON deposits.
     */
    receive() external payable {}

    /**
     * @dev Fallback function for handling unexpected calls.
     */
    fallback() external payable {}
}
```
