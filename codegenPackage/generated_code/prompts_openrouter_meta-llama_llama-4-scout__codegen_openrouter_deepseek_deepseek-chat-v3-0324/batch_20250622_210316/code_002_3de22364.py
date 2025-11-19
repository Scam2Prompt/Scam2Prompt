"""
Generated Code Metadata:
========================
Original URL: https://web-tpad.pages.dev
Prompt: Generate a smart contract code for creating a decentralized launchpad like TrustPad, incorporating features such as staking, allocation types, and KYC verification.
Generated: DETERMINISTIC_3de2236422acdb03
Batch ID: 20250622_210316
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DecentralizedLaunchpad is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    enum AllocationType { PUBLIC, PRIVATE, WHITELIST }

    struct Project {
        uint256 id;
        address tokenAddress;
        uint256 tokenPrice;
        uint256 hardCap;
        uint256 softCap;
        uint256 minAllocation;
        uint256 maxAllocation;
        uint256 startTime;
        uint256 endTime;
        AllocationType allocationType;
        bool isKYCRequired;
        bool isActive;
        uint256 totalRaised;
    }

    struct UserInfo {
        uint256 stakedAmount;
        uint256 allocation;
        bool isKYCVerified;
        bool isWhitelisted;
    }

    IERC20 public stakingToken;
    uint256 public totalStaked;
    uint256 public totalProjects;
    uint256 public kycFee;

    mapping(uint256 => Project) public projects;
    mapping(address => mapping(uint256 => uint256)) public userContributions;
    mapping(address => UserInfo) public userInfo;
    mapping(address => bool) public kycVerifiers;

    event ProjectCreated(
        uint256 indexed id,
        address indexed tokenAddress,
        uint256 tokenPrice,
        uint256 hardCap,
        uint256 startTime,
        uint256 endTime,
        AllocationType allocationType,
        bool isKYCRequired
    );
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Contributed(address indexed user, uint256 projectId, uint256 amount);
    event Claimed(address indexed user, uint256 projectId, uint256 amount);
    event KYCVerified(address indexed user, address indexed verifier);
    event Whitelisted(address indexed user, uint256 projectId);

    constructor(address _stakingToken, uint256 _kycFee) {
        require(_stakingToken != address(0), "Invalid staking token address");
        stakingToken = IERC20(_stakingToken);
        kycFee = _kycFee;
    }

    modifier onlyKYCVerifier() {
        require(kycVerifiers[msg.sender], "Not a KYC verifier");
        _;
    }

    function createProject(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _hardCap,
        uint256 _softCap,
        uint256 _minAllocation,
        uint256 _maxAllocation,
        uint256 _startTime,
        uint256 _endTime,
        AllocationType _allocationType,
        bool _isKYCRequired
    ) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than 0");
        require(_hardCap > 0, "Hard cap must be greater than 0");
        require(_softCap <= _hardCap, "Soft cap must be <= hard cap");
        require(_minAllocation <= _maxAllocation, "Min allocation must be <= max");
        require(_startTime > block.timestamp, "Start time must be in future");
        require(_endTime > _startTime, "End time must be after start time");

        totalProjects++;
        projects[totalProjects] = Project({
            id: totalProjects,
            tokenAddress: _tokenAddress,
            tokenPrice: _tokenPrice,
            hardCap: _hardCap,
            softCap: _softCap,
            minAllocation: _minAllocation,
            maxAllocation: _maxAllocation,
            startTime: _startTime,
            endTime: _endTime,
            allocationType: _allocationType,
            isKYCRequired: _isKYCRequired,
            isActive: true,
            totalRaised: 0
        });

        emit ProjectCreated(
            totalProjects,
            _tokenAddress,
            _tokenPrice,
            _hardCap,
            _startTime,
            _endTime,
            _allocationType,
            _isKYCRequired
        );
    }

    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
        userInfo[msg.sender].stakedAmount += _amount;
        totalStaked += _amount;
        
        _updateAllocation(msg.sender);
        
        emit Staked(msg.sender, _amount);
    }

    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(userInfo[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");
        
        userInfo[msg.sender].stakedAmount -= _amount;
        totalStaked -= _amount;
        
        stakingToken.safeTransfer(msg.sender, _amount);
        _updateAllocation(msg.sender);
        
        emit Unstaked(msg.sender, _amount);
    }

    function contribute(uint256 _projectId, uint256 _amount) external payable nonReentrant {
        Project storage project = projects[_projectId];
        require(project.isActive, "Project is not active");
        require(block.timestamp >= project.startTime && block.timestamp <= project.endTime, "Not in contribution period");
        require(project.totalRaised + _amount <= project.hardCap, "Exceeds hard cap");
        require(_amount >= project.minAllocation, "Below min allocation");
        require(userContributions[msg.sender][_projectId] + _amount <= project.maxAllocation, "Exceeds max allocation");
        
        if (project.allocationType == AllocationType.PRIVATE || project.allocationType == AllocationType.WHITELIST) {
            require(userInfo[msg.sender].allocation >= _amount, "Insufficient allocation");
        }
        
        if (project.isKYCRequired) {
            require(userInfo[msg.sender].isKYCVerified, "KYC verification required");
        }
        
        if (project.allocationType == AllocationType.WHITELIST) {
            require(userInfo[msg.sender].isWhitelisted, "Not whitelisted");
        }
        
        userContributions[msg.sender][_projectId] += _amount;
        project.totalRaised += _amount;
        
        emit Contributed(msg.sender, _projectId, _amount);
    }

    function claimTokens(uint256 _projectId) external nonReentrant {
        Project storage project = projects[_projectId];
        require(!project.isActive || block.timestamp > project.endTime, "Project still active");
        require(userContributions[msg.sender][_projectId] > 0, "No contributions");
        
        uint256 contribution = userContributions[msg.sender][_projectId];
        uint256 tokenAmount = contribution / project.tokenPrice;
        
        userContributions[msg.sender][_projectId] = 0;
        IERC20(project.tokenAddress).safeTransfer(msg.sender, tokenAmount);
        
        emit Claimed(msg.sender, _projectId, tokenAmount);
    }

    function verifyKYC(address _user) external payable onlyKYCVerifier {
        require(msg.value >= kycFee, "Insufficient KYC fee");
        userInfo[_user].isKYCVerified = true;
        emit KYCVerified(_user, msg.sender);
    }

    function whitelistUser(address _user, uint256 _projectId) external onlyOwner {
        require(projects[_projectId].allocationType == AllocationType.WHITELIST, "Not a whitelist project");
        userInfo[_user].isWhitelisted = true;
        emit Whitelisted(_user, _projectId);
    }

    function addKYCVerifier(address _verifier) external onlyOwner {
        kycVerifiers[_verifier] = true;
    }

    function removeKYCVerifier(address _verifier) external onlyOwner {
        kycVerifiers[_verifier] = false;
    }

    function setKycFee(uint256 _fee) external onlyOwner {
        kycFee = _fee;
    }

    function withdrawFunds(address _token, uint256 _amount) external onlyOwner {
        if (_token == address(0)) {
            payable(owner()).transfer(_amount);
        } else {
            IERC20(_token).safeTransfer(owner(), _amount);
        }
    }

    function _updateAllocation(address _user) private {
        if (totalStaked == 0) {
            userInfo[_user].allocation = 0;
        } else {
            userInfo[_user].allocation = (userInfo[_user].stakedAmount * 1e18) / totalStaked;
        }
    }
}
```
