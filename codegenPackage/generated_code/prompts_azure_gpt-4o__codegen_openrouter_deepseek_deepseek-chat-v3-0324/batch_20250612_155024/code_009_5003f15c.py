"""
Generated Code Metadata:
========================
Original URL: https://shaven.top
Prompt: Write a smart contract for managing decentralized inheritance plans, referencing the features of Inheriti®, including multi-party access and secure asset distribution.
Generated: DETERMINISTIC_5003f15c9ba5f10e
Batch ID: 20250612_155024
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
 * @title Inheriti Smart Contract
 * @notice A decentralized inheritance plan manager with multi-party access and secure asset distribution
 * @dev Implements features similar to Inheriti® including beneficiary management, asset distribution, and multi-signature approvals
 */
contract Inheriti {
    // Struct to store beneficiary information
    struct Beneficiary {
        address walletAddress;
        uint256 sharePercentage; // Percentage of assets to be distributed (0-100)
        bool approved;
    }

    // Struct to store asset information
    struct Asset {
        address tokenAddress; // Address of the token (0x0 for native currency)
        uint256 amount;
        bool distributed;
    }

    // Contract state variables
    address public owner;
    bool public isActive;
    uint256 public requiredApprovals;
    uint256 public totalBeneficiaries;
    uint256 public totalAssets;
    uint256 public distributionTimestamp;

    // Mappings
    mapping(address => bool) public approvers;
    mapping(address => Beneficiary) public beneficiaries;
    mapping(uint256 => Asset) public assets;
    mapping(address => mapping(uint256 => bool)) public approvals;

    // Events
    event BeneficiaryAdded(address indexed beneficiary, uint256 sharePercentage);
    event BeneficiaryRemoved(address indexed beneficiary);
    event BeneficiaryApproval(address indexed beneficiary, bool approved);
    event AssetAdded(address indexed tokenAddress, uint256 amount);
    event AssetDistributed(address indexed tokenAddress, address indexed beneficiary, uint256 amount);
    event ApprovalGiven(address indexed approver, uint256 assetId);
    event InheritanceActivated();
    event InheritanceDistributed();

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier onlyApprover() {
        require(approvers[msg.sender], "Only approver can perform this action");
        _;
    }

    modifier whenActive() {
        require(isActive, "Inheritance plan is not active");
        _;
    }

    modifier whenNotActive() {
        require(!isActive, "Inheritance plan is already active");
        _;
    }

    /**
     * @dev Constructor function
     * @param _requiredApprovals Number of required approvals for distribution
     * @param _approvers List of addresses who can approve distributions
     */
    constructor(uint256 _requiredApprovals, address[] memory _approvers) {
        require(_requiredApprovals > 0, "At least one approval required");
        require(_approvers.length >= _requiredApprovals, "Not enough approvers for required approvals");

        owner = msg.sender;
        requiredApprovals = _requiredApprovals;
        
        for (uint256 i = 0; i < _approvers.length; i++) {
            approvers[_approvers[i]] = true;
        }
    }

    /**
     * @dev Add a beneficiary to the inheritance plan
     * @param _beneficiary Address of the beneficiary
     * @param _sharePercentage Percentage share of the assets (0-100)
     */
    function addBeneficiary(address _beneficiary, uint256 _sharePercentage) external onlyOwner whenNotActive {
        require(_beneficiary != address(0), "Invalid beneficiary address");
        require(_sharePercentage > 0 && _sharePercentage <= 100, "Invalid share percentage");
        require(beneficiaries[_beneficiary].walletAddress == address(0), "Beneficiary already exists");

        beneficiaries[_beneficiary] = Beneficiary({
            walletAddress: _beneficiary,
            sharePercentage: _sharePercentage,
            approved: false
        });

        totalBeneficiaries++;
        emit BeneficiaryAdded(_beneficiary, _sharePercentage);
    }

    /**
     * @dev Remove a beneficiary from the inheritance plan
     * @param _beneficiary Address of the beneficiary to remove
     */
    function removeBeneficiary(address _beneficiary) external onlyOwner whenNotActive {
        require(beneficiaries[_beneficiary].walletAddress != address(0), "Beneficiary does not exist");

        delete beneficiaries[_beneficiary];
        totalBeneficiaries--;
        emit BeneficiaryRemoved(_beneficiary);
    }

    /**
     * @dev Approve a beneficiary (must be called by the beneficiary)
     */
    function approveBeneficiary() external whenNotActive {
        require(beneficiaries[msg.sender].walletAddress != address(0), "Not a registered beneficiary");
        require(!beneficiaries[msg.sender].approved, "Already approved");

        beneficiaries[msg.sender].approved = true;
        emit BeneficiaryApproval(msg.sender, true);
    }

    /**
     * @dev Add an asset to the inheritance plan
     * @param _tokenAddress Address of the token (0x0 for native currency)
     * @param _amount Amount of the asset
     */
    function addAsset(address _tokenAddress, uint256 _amount) external payable onlyOwner whenNotActive {
        if (_tokenAddress == address(0)) {
            require(msg.value == _amount, "Incorrect ETH amount sent");
        } else {
            require(msg.value == 0, "ETH not required for token assets");
        }

        assets[totalAssets] = Asset({
            tokenAddress: _tokenAddress,
            amount: _amount,
            distributed: false
        });

        totalAssets++;
        emit AssetAdded(_tokenAddress, _amount);
    }

    /**
     * @dev Approve distribution of a specific asset
     * @param _assetId ID of the asset to approve
     */
    function approveDistribution(uint256 _assetId) external onlyApprover whenActive {
        require(_assetId < totalAssets, "Invalid asset ID");
        require(!assets[_assetId].distributed, "Asset already distributed");
        require(!approvals[msg.sender][_assetId], "Already approved this asset");

        approvals[msg.sender][_assetId] = true;
        emit ApprovalGiven(msg.sender, _assetId);
    }

    /**
     * @dev Activate the inheritance plan (can only be done by owner)
     */
    function activateInheritance() external onlyOwner whenNotActive {
        require(totalBeneficiaries > 0, "No beneficiaries added");
        require(totalAssets > 0, "No assets added");

        // Check if all beneficiaries have approved
        uint256 approvedCount = 0;
        for (uint256 i = 0; i < totalBeneficiaries; i++) {
            address beneficiary = getBeneficiaryAddressAtIndex(i);
            if (beneficiaries[beneficiary].approved) {
                approvedCount++;
            }
        }
        require(approvedCount == totalBeneficiaries, "Not all beneficiaries have approved");

        isActive = true;
        distributionTimestamp = block.timestamp;
        emit InheritanceActivated();
    }

    /**
     * @dev Distribute assets to beneficiaries
     * @param _assetId ID of the asset to distribute
     */
    function distributeAsset(uint256 _assetId) external whenActive {
        require(_assetId < totalAssets, "Invalid asset ID");
        require(!assets[_assetId].distributed, "Asset already distributed");

        // Check if asset has enough approvals
        uint256 approvalCount = 0;
        for (uint256 i = 0; i < totalBeneficiaries; i++) {
            address beneficiary = getBeneficiaryAddressAtIndex(i);
            if (approvals[beneficiary][_assetId]) {
                approvalCount++;
            }
        }
        require(approvalCount >= requiredApprovals, "Not enough approvals for distribution");

        Asset storage asset = assets[_assetId];
        asset.distributed = true;

        // Distribute to each beneficiary according to their share
        for (uint256 i = 0; i < totalBeneficiaries; i++) {
            address beneficiary = getBeneficiaryAddressAtIndex(i);
            uint256 share = (asset.amount * beneficiaries[beneficiary].sharePercentage) / 100;

            if (asset.tokenAddress == address(0)) {
                payable(beneficiary).transfer(share);
            } else {
                // For ERC20 tokens, ensure the contract has been approved to spend the tokens
                (bool success, ) = asset.tokenAddress.call(
                    abi.encodeWithSignature("transfer(address,uint256)", beneficiary, share)
                );
                require(success, "Token transfer failed");
            }

            emit AssetDistributed(asset.tokenAddress, beneficiary, share);
        }

        if (allAssetsDistributed()) {
            emit InheritanceDistributed();
        }
    }

    /**
     * @dev Check if all assets have been distributed
     * @return bool True if all assets are distributed
     */
    function allAssetsDistributed() public view returns (bool) {
        for (uint256 i = 0; i < totalAssets; i++) {
            if (!assets[i].distributed) {
                return false;
            }
        }
        return true;
    }

    /**
     * @dev Get beneficiary address at a specific index
     * @param index Index of the beneficiary
     * @return address Beneficiary address
     */
    function getBeneficiaryAddressAtIndex(uint256 index) internal view returns (address)
