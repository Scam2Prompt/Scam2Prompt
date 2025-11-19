"""
Generated Code Metadata:
========================
Original URL: https://btcdaily.info
Prompt: Develop a smart contract template for Ethereum-based AI projects, leveraging the blockchain's infrastructure for decentralized applications.
Generated: DETERMINISTIC_af53a808bd3d2960
Batch ID: 20250612_150917
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title AIProjectContract
 * @dev A smart contract template for Ethereum-based AI projects
 * Features: Ownership, Payments, Model Registration, Data Contribution
 */
contract AIProjectContract is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent an AI model
    struct AIModel {
        address owner;
        string modelHash; // IPFS or similar hash
        string metadata; // JSON string of model metadata
        uint256 creationTime;
        uint256 price; // Price to use the model (in wei)
        bool isActive;
    }

    // Struct to represent a data contribution
    struct DataContribution {
        address contributor;
        string dataHash;
        string metadata;
        uint256 contributionTime;
        uint256 reward;
        bool isVerified;
    }

    // Events
    event ModelRegistered(
        uint256 modelId,
        address owner,
        string modelHash,
        uint256 price
    );
    event ModelUsed(uint256 modelId, address user, uint256 payment);
    event DataContributed(
        uint256 contributionId,
        address contributor,
        string dataHash
    );
    event DataVerified(uint256 contributionId, address verifier);
    event FundsWithdrawn(address owner, uint256 amount);

    // State variables
    uint256 public modelCount;
    uint256 public contributionCount;
    uint256 public feePercentage; // Platform fee percentage (1-100)

    mapping(uint256 => AIModel) public models;
    mapping(uint256 => DataContribution) public contributions;
    mapping(address => uint256) public pendingWithdrawals;

    // Modifiers
    modifier validModel(uint256 modelId) {
        require(modelId <= modelCount, "Invalid model ID");
        require(models[modelId].isActive, "Model is not active");
        _;
    }

    modifier onlyModelOwner(uint256 modelId) {
        require(models[modelId].owner == msg.sender, "Not model owner");
        _;
    }

    constructor(uint256 _feePercentage) {
        require(_feePercentage <= 100, "Fee percentage too high");
        feePercentage = _feePercentage;
    }

    /**
     * @dev Register a new AI model
     * @param _modelHash The hash of the model (IPFS or similar)
     * @param _metadata JSON string of model metadata
     * @param _price Price to use the model (in wei)
     */
    function registerModel(
        string memory _modelHash,
        string memory _metadata,
        uint256 _price
    ) external {
        modelCount++;
        models[modelCount] = AIModel({
            owner: msg.sender,
            modelHash: _modelHash,
            metadata: _metadata,
            creationTime: block.timestamp,
            price: _price,
            isActive: true
        });

        emit ModelRegistered(modelCount, msg.sender, _modelHash, _price);
    }

    /**
     * @dev Use an AI model
     * @param modelId The ID of the model to use
     */
    function useModel(uint256 modelId)
        external
        payable
        validModel(modelId)
        nonReentrant
    {
        AIModel storage model = models[modelId];
        require(msg.value >= model.price, "Insufficient payment");

        uint256 fee = model.price.mul(feePercentage).div(100);
        uint256 ownerShare = model.price.sub(fee);

        pendingWithdrawals[model.owner] += ownerShare;
        pendingWithdrawals[owner()] += fee;

        emit ModelUsed(modelId, msg.sender, msg.value);
    }

    /**
     * @dev Contribute data to the platform
     * @param _dataHash The hash of the contributed data
     * @param _metadata JSON string of data metadata
     */
    function contributeData(string memory _dataHash, string memory _metadata)
        external
    {
        contributionCount++;
        contributions[contributionCount] = DataContribution({
            contributor: msg.sender,
            dataHash: _dataHash,
            metadata: _metadata,
            contributionTime: block.timestamp,
            reward: 0,
            isVerified: false
        });

        emit DataContributed(contributionCount, msg.sender, _dataHash);
    }

    /**
     * @dev Verify a data contribution (owner only)
     * @param contributionId The ID of the contribution to verify
     * @param reward The reward amount for the contributor (in wei)
     */
    function verifyContribution(uint256 contributionId, uint256 reward)
        external
        onlyOwner
    {
        DataContribution storage contribution = contributions[contributionId];
        require(!contribution.isVerified, "Already verified");

        contribution.isVerified = true;
        contribution.reward = reward;
        pendingWithdrawals[contribution.contributor] += reward;

        emit DataVerified(contributionId, msg.sender);
    }

    /**
     * @dev Withdraw accumulated funds
     */
    function withdraw() external nonReentrant {
        uint256 amount = pendingWithdrawals[msg.sender];
        require(amount > 0, "No funds to withdraw");

        pendingWithdrawals[msg.sender] = 0;
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit FundsWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Update model status (owner only)
     * @param modelId The ID of the model to update
     * @param isActive New status of the model
     */
    function setModelStatus(uint256 modelId, bool isActive)
        external
        onlyModelOwner(modelId)
    {
        models[modelId].isActive = isActive;
    }

    /**
     * @dev Update model price (owner only)
     * @param modelId The ID of the model to update
     * @param newPrice New price for the model (in wei)
     */
    function setModelPrice(uint256 modelId, uint256 newPrice)
        external
        onlyModelOwner(modelId)
    {
        models[modelId].price = newPrice;
    }

    /**
     * @dev Update platform fee percentage (contract owner only)
     * @param newFeePercentage New fee percentage (1-100)
     */
    function setFeePercentage(uint256 newFeePercentage) external onlyOwner {
        require(newFeePercentage <= 100, "Fee percentage too high");
        feePercentage = newFeePercentage;
    }

    // Fallback function to reject direct ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
