"""
Generated Code Metadata:
========================
Original URL: https://synspad.firebaseapp.com
Prompt: Develop a code snippet for integrating multi-chain support into a decentralized launchpad, referencing SynsPad's key features.
Generated: DETERMINISTIC_21331fc7efb32a67
Batch ID: 20250612_151026
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MultiChainLaunchpad
 * @dev A decentralized launchpad supporting multiple blockchains with SynsPad-like features
 */
contract MultiChainLaunchpad is Ownable, ReentrancyGuard {
    struct ChainInfo {
        uint256 chainId;
        string name;
        bool isActive;
        address nativeToken;
    }

    struct Project {
        uint256 id;
        address creator;
        string name;
        string description;
        uint256[] supportedChains;
        uint256 softCap;
        uint256 hardCap;
        uint256 startTime;
        uint256 endTime;
        bool isApproved;
        bool isActive;
    }

    mapping(uint256 => ChainInfo) public chains;
    mapping(uint256 => Project) public projects;
    mapping(address => mapping(uint256 => uint256)) public userContributions;
    mapping(uint256 => mapping(uint256 => uint256)) public chainContributions;

    uint256 public projectCount;
    uint256 public feePercentage; // Platform fee in basis points (100 = 1%)
    address public feeWallet;

    event ChainAdded(uint256 chainId, string name, address nativeToken);
    event ChainStatusChanged(uint256 chainId, bool isActive);
    event ProjectCreated(
        uint256 id,
        address creator,
        string name,
        uint256[] supportedChains
    );
    event ProjectApproved(uint256 id);
    event ContributionMade(
        uint256 projectId,
        uint256 chainId,
        address contributor,
        uint256 amount
    );
    event FundsClaimed(uint256 projectId, uint256 chainId, uint256 amount);
    event RefundClaimed(uint256 projectId, address contributor, uint256 amount);

    constructor(uint256 _feePercentage, address _feeWallet) {
        require(_feePercentage <= 1000, "Fee too high"); // Max 10%
        feePercentage = _feePercentage;
        feeWallet = _feeWallet;
    }

    /**
     * @dev Add a new supported chain
     */
    function addChain(
        uint256 _chainId,
        string memory _name,
        address _nativeToken
    ) external onlyOwner {
        require(chains[_chainId].chainId == 0, "Chain already exists");
        chains[_chainId] = ChainInfo(_chainId, _name, true, _nativeToken);
        emit ChainAdded(_chainId, _name, _nativeToken);
    }

    /**
     * @dev Toggle chain activation status
     */
    function toggleChain(uint256 _chainId, bool _isActive) external onlyOwner {
        require(chains[_chainId].chainId != 0, "Chain not found");
        chains[_chainId].isActive = _isActive;
        emit ChainStatusChanged(_chainId, _isActive);
    }

    /**
     * @dev Create a new project
     */
    function createProject(
        string memory _name,
        string memory _description,
        uint256[] memory _supportedChains,
        uint256 _softCap,
        uint256 _hardCap,
        uint256 _startTime,
        uint256 _endTime
    ) external {
        require(_supportedChains.length > 0, "No chains specified");
        require(_softCap < _hardCap, "Invalid caps");
        require(_startTime < _endTime, "Invalid time range");

        for (uint256 i = 0; i < _supportedChains.length; i++) {
            require(
                chains[_supportedChains[i]].isActive,
                "Chain not active"
            );
        }

        projectCount++;
        projects[projectCount] = Project({
            id: projectCount,
            creator: msg.sender,
            name: _name,
            description: _description,
            supportedChains: _supportedChains,
            softCap: _softCap,
            hardCap: _hardCap,
            startTime: _startTime,
            endTime: _endTime,
            isApproved: false,
            isActive: false
        });

        emit ProjectCreated(projectCount, msg.sender, _name, _supportedChains);
    }

    /**
     * @dev Approve a project for launch
     */
    function approveProject(uint256 _projectId) external onlyOwner {
        require(projects[_projectId].id != 0, "Project not found");
        require(!projects[_projectId].isApproved, "Already approved");

        projects[_projectId].isApproved = true;
        projects[_projectId].isActive = true;
        emit ProjectApproved(_projectId);
    }

    /**
     * @dev Contribute to a project on a specific chain
     */
    function contribute(
        uint256 _projectId,
        uint256 _chainId,
        uint256 _amount
    ) external payable nonReentrant {
        Project storage project = projects[_projectId];
        require(project.isActive, "Project not active");
        require(block.timestamp >= project.startTime, "Not started");
        require(block.timestamp <= project.endTime, "Ended");
        require(isChainSupported(_projectId, _chainId), "Chain not supported");

        ChainInfo memory chain = chains[_chainId];
        require(chain.isActive, "Chain not active");

        if (chain.nativeToken == address(0)) {
            require(msg.value == _amount, "Incorrect ETH amount");
        } else {
            IERC20 token = IERC20(chain.nativeToken);
            require(
                token.transferFrom(msg.sender, address(this), _amount),
                "Token transfer failed"
            );
        }

        userContributions[msg.sender][_projectId] += _amount;
        chainContributions[_projectId][_chainId] += _amount;

        emit ContributionMade(_projectId, _chainId, msg.sender, _amount);
    }

    /**
     * @dev Project creator claims raised funds
     */
    function claimFunds(uint256 _projectId, uint256 _chainId)
        external
        nonReentrant
    {
        Project storage project = projects[_projectId];
        require(project.creator == msg.sender, "Not creator");
        require(block.timestamp > project.endTime, "Not ended");
        require(isChainSupported(_projectId, _chainId), "Chain not supported");

        uint256 totalRaised = chainContributions[_projectId][_chainId];
        require(totalRaised >= project.softCap, "Softcap not reached");

        ChainInfo memory chain = chains[_chainId];
        uint256 feeAmount = (totalRaised * feePercentage) / 10000;
        uint256 amountToSend = totalRaised - feeAmount;

        if (chain.nativeToken == address(0)) {
            (bool success, ) = payable(project.creator).call{value: amountToSend}("");
            require(success, "ETH transfer failed");
            if (feeAmount > 0) {
                (success, ) = payable(feeWallet).call{value: feeAmount}("");
                require(success, "Fee transfer failed");
            }
        } else {
            IERC20 token = IERC20(chain.nativeToken);
            require(
                token.transfer(project.creator, amountToSend),
                "Token transfer failed"
            );
            if (feeAmount > 0) {
                require(
                    token.transfer(feeWallet, feeAmount),
                    "Fee transfer failed"
                );
            }
        }

        emit FundsClaimed(_projectId, _chainId, totalRaised);
    }

    /**
     * @dev Contributor claims refund if softcap not reached
     */
    function claimRefund(uint256 _projectId) external nonReentrant {
        Project storage project = projects[_projectId];
        require(block.timestamp > project.endTime, "Not ended");
        require(chainContributions[_projectId][project.supportedChains[0]] < project.softCap, "Softcap reached");

        uint256 userContribution = userContributions[msg.sender][_projectId];
        require(userContribution > 0, "No contribution");

        userContributions[msg.sender][_projectId] = 0;

        ChainInfo memory chain = chains[project.supportedChains[0]];
        if (chain.nativeToken == address(0)) {
            (bool success, ) = payable(msg.sender).call{value: userContribution}("");
            require(success, "ETH transfer failed");
        } else {
            IERC20 token = IERC20(chain.nativeToken);
            require(
                token.transfer(msg.sender, userContribution),
                "Token transfer failed"
            );
        }

        emit RefundClaimed(_projectId, msg.sender, userContribution);
    }

    /**
     * @dev Check if chain is supported by project
     */
    function isChainSupported(uint256 _projectId, uint256 _chainId)
        public
        view
        returns (bool)
    {
        Project storage project = projects[_projectId];
        for
