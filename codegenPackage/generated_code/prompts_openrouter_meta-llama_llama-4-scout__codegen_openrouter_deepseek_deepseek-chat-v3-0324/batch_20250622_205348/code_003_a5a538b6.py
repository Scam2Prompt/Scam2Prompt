"""
Generated Code Metadata:
========================
Original URL: https://chaintether.web.app
Prompt: "Design a DeFi application for a ChainTether-like platform focusing on secure, decentralized, and multi-chain IDO launches."
Generated: DETERMINISTIC_a5a538b6ff4220b9
Batch ID: 20250622_205348
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MultiChainIDOPlatform
 * @dev A decentralized IDO launch platform supporting multiple chains
 */
contract MultiChainIDOPlatform is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    struct IDOProject {
        address projectOwner;
        address tokenAddress;
        uint256 tokenPrice;
        uint256 hardCap;
        uint256 softCap;
        uint256 minContribution;
        uint256 maxContribution;
        uint256 startTime;
        uint256 endTime;
        uint256 totalRaised;
        uint256 totalTokensSold;
        bool isWhitelistEnabled;
        bool isActive;
        bool isCompleted;
    }

    struct ChainInfo {
        uint256 chainId;
        string rpcUrl;
        bool isSupported;
    }

    mapping(uint256 => IDOProject) public idoProjects;
    mapping(uint256 => ChainInfo) public supportedChains;
    mapping(address => mapping(uint256 => uint256)) public userContributions;
    mapping(uint256 => mapping(address => bool)) public whitelist;
    mapping(address => bool) public verifiedProjectOwners;

    uint256 public projectCounter;
    uint256 public platformFeePercentage; // Basis points (e.g., 200 = 2%)
    address public feeWallet;
    address public stablecoin; // USDT/USDC address

    event ProjectCreated(uint256 projectId, address projectOwner, address tokenAddress);
    event ContributionMade(uint256 projectId, address contributor, uint256 amount);
    event ProjectCompleted(uint256 projectId, bool success);
    event WhitelistUpdated(uint256 projectId, address[] addresses, bool status);
    event ChainAdded(uint256 chainId, string rpcUrl);
    event ChainRemoved(uint256 chainId);

    modifier onlyProjectOwner(uint256 projectId) {
        require(idoProjects[projectId].projectOwner == msg.sender, "Not project owner");
        _;
    }

    modifier onlyActiveProject(uint256 projectId) {
        require(idoProjects[projectId].isActive, "Project not active");
        _;
    }

    constructor(address _stablecoin, address _feeWallet, uint256 _platformFee) {
        require(_stablecoin != address(0), "Invalid stablecoin address");
        require(_feeWallet != address(0), "Invalid fee wallet address");
        stablecoin = _stablecoin;
        feeWallet = _feeWallet;
        platformFeePercentage = _platformFee;
    }

    /**
     * @dev Create a new IDO project
     */
    function createProject(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _hardCap,
        uint256 _softCap,
        uint256 _minContribution,
        uint256 _maxContribution,
        uint256 _startTime,
        uint256 _endTime,
        bool _isWhitelistEnabled
    ) external {
        require(verifiedProjectOwners[msg.sender], "Not verified project owner");
        require(_tokenAddress != address(0), "Invalid token address");
        require(_endTime > _startTime, "Invalid time range");
        require(_hardCap > _softCap, "Hard cap must be greater than soft cap");
        require(_maxContribution > _minContribution, "Invalid contribution range");

        projectCounter++;
        idoProjects[projectCounter] = IDOProject({
            projectOwner: msg.sender,
            tokenAddress: _tokenAddress,
            tokenPrice: _tokenPrice,
            hardCap: _hardCap,
            softCap: _softCap,
            minContribution: _minContribution,
            maxContribution: _maxContribution,
            startTime: _startTime,
            endTime: _endTime,
            totalRaised: 0,
            totalTokensSold: 0,
            isWhitelistEnabled: _isWhitelistEnabled,
            isActive: true,
            isCompleted: false
        });

        emit ProjectCreated(projectCounter, msg.sender, _tokenAddress);
    }

    /**
     * @dev Contribute to an IDO project
     */
    function contribute(uint256 projectId, uint256 amount) external nonReentrant onlyActiveProject(projectId) {
        IDOProject storage project = idoProjects[projectId];
        require(block.timestamp >= project.startTime && block.timestamp <= project.endTime, "IDO not active");
        require(project.totalRaised.add(amount) <= project.hardCap, "Exceeds hard cap");
        
        if (project.isWhitelistEnabled) {
            require(whitelist[projectId][msg.sender], "Not whitelisted");
        }

        uint256 userTotal = userContributions[msg.sender][projectId].add(amount);
        require(userTotal >= project.minContribution, "Below min contribution");
        require(userTotal <= project.maxContribution, "Exceeds max contribution");

        IERC20(stablecoin).transferFrom(msg.sender, address(this), amount);
        
        uint256 fee = amount.mul(platformFeePercentage).div(10000);
        uint256 netAmount = amount.sub(fee);
        
        IERC20(stablecoin).transfer(feeWallet, fee);
        
        project.totalRaised = project.totalRaised.add(netAmount);
        userContributions[msg.sender][projectId] = userTotal;
        
        uint256 tokensToSend = netAmount.div(project.tokenPrice);
        project.totalTokensSold = project.totalTokensSold.add(tokensToSend);
        
        IERC20(project.tokenAddress).transfer(msg.sender, tokensToSend);
        
        emit ContributionMade(projectId, msg.sender, amount);
    }

    /**
     * @dev Finalize an IDO project
     */
    function finalizeProject(uint256 projectId) external onlyProjectOwner(projectId) {
        IDOProject storage project = idoProjects[projectId];
        require(block.timestamp > project.endTime, "IDO not ended");
        require(!project.isCompleted, "Already completed");

        project.isActive = false;
        project.isCompleted = true;
        
        bool success = project.totalRaised >= project.softCap;
        
        if (success) {
            IERC20(stablecoin).transfer(project.projectOwner, project.totalRaised);
        } else {
            // Refund contributors if soft cap not met
            // Implementation would require tracking all contributors
            // This is simplified for demonstration
        }
        
        emit ProjectCompleted(projectId, success);
    }

    /**
     * @dev Update whitelist for a project
     */
    function updateWhitelist(uint256 projectId, address[] calldata addresses, bool status) external onlyProjectOwner(projectId) {
        require(idoProjects[projectId].isWhitelistEnabled, "Whitelist not enabled");
        
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelist[projectId][addresses[i]] = status;
        }
        
        emit WhitelistUpdated(projectId, addresses, status);
    }

    /**
     * @dev Add a supported chain
     */
    function addSupportedChain(uint256 chainId, string memory rpcUrl) external onlyOwner {
        supportedChains[chainId] = ChainInfo({
            chainId: chainId,
            rpcUrl: rpcUrl,
            isSupported: true
        });
        emit ChainAdded(chainId, rpcUrl);
    }

    /**
     * @dev Remove a supported chain
     */
    function removeSupportedChain(uint256 chainId) external onlyOwner {
        require(supportedChains[chainId].isSupported, "Chain not supported");
        delete supportedChains[chainId];
        emit ChainRemoved(chainId);
    }

    /**
     * @dev Verify a project owner
     */
    function verifyProjectOwner(address owner, bool status) external onlyOwner {
        verifiedProjectOwners[owner] = status;
    }

    /**
     * @dev Update platform fee
     */
    function updatePlatformFee(uint256 newFee) external onlyOwner {
        require(newFee <= 1000, "Fee too high"); // Max 10%
        platformFeePercentage = newFee;
    }

    /**
     * @dev Update fee wallet
     */
    function updateFeeWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Invalid address");
        feeWallet = newWallet;
    }
}
```
