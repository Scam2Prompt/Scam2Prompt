"""
Generated Code Metadata:
========================
Original URL: https://bafybeidlrlbotyuulbnias66uqhqkoy7f4px26fibleghikvgo24hd7tje.ipfs.dweb.link
Prompt: Generate code for a cross-chain asset transfer system that utilizes Moonwell's WELL activation and system upgrade features.
Generated: DETERMINISTIC_53ef8c7daf977b61
Batch ID: 20250612_152358
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IMoonwell {
    function activateWELL() external;
    function upgradeSystem() external;
    function isWELLActive() external view returns (bool);
    function isUpgradeAvailable() external view returns (bool);
}

contract CrossChainAssetTransfer is Ownable, Pausable {
    using SafeMath for uint256;

    IMoonwell public moonwell;
    IERC20 public wellToken;
    IERC20 public assetToken;

    struct TransferRequest {
        address sender;
        address recipient;
        uint256 amount;
        uint256 targetChainId;
        bool isCompleted;
    }

    mapping(uint256 => TransferRequest) public transferRequests;
    uint256 public requestCounter;
    mapping(uint256 => bool) public supportedChains;

    event TransferInitiated(
        uint256 indexed requestId,
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        uint256 targetChainId
    );
    event TransferCompleted(uint256 indexed requestId);
    event WELLActivated();
    event SystemUpgraded();
    event ChainSupportUpdated(uint256 chainId, bool isSupported);

    constructor(
        address _moonwell,
        address _wellToken,
        address _assetToken
    ) {
        require(_moonwell != address(0), "Invalid Moonwell address");
        require(_wellToken != address(0), "Invalid WELL token address");
        require(_assetToken != address(0), "Invalid asset token address");

        moonwell = IMoonwell(_moonwell);
        wellToken = IERC20(_wellToken);
        assetToken = IERC20(_assetToken);
    }

    modifier onlyActiveWELL() {
        require(moonwell.isWELLActive(), "WELL is not active");
        _;
    }

    function initiateTransfer(
        address _recipient,
        uint256 _amount,
        uint256 _targetChainId
    ) external whenNotPaused onlyActiveWELL {
        require(_recipient != address(0), "Invalid recipient address");
        require(_amount > 0, "Amount must be greater than 0");
        require(supportedChains[_targetChainId], "Chain not supported");

        uint256 allowance = assetToken.allowance(msg.sender, address(this));
        require(allowance >= _amount, "Insufficient allowance");

        bool transferSuccess = assetToken.transferFrom(
            msg.sender,
            address(this),
            _amount
        );
        require(transferSuccess, "Token transfer failed");

        requestCounter++;
        transferRequests[requestCounter] = TransferRequest({
            sender: msg.sender,
            recipient: _recipient,
            amount: _amount,
            targetChainId: _targetChainId,
            isCompleted: false
        });

        emit TransferInitiated(
            requestCounter,
            msg.sender,
            _recipient,
            _amount,
            _targetChainId
        );
    }

    function completeTransfer(uint256 _requestId) external onlyOwner {
        require(_requestId <= requestCounter, "Invalid request ID");
        TransferRequest storage request = transferRequests[_requestId];
        require(!request.isCompleted, "Transfer already completed");

        bool transferSuccess = assetToken.transfer(
            request.recipient,
            request.amount
        );
        require(transferSuccess, "Token transfer failed");

        request.isCompleted = true;
        emit TransferCompleted(_requestId);
    }

    function activateWELL() external onlyOwner {
        require(!moonwell.isWELLActive(), "WELL already active");
        moonwell.activateWELL();
        emit WELLActivated();
    }

    function upgradeSystem() external onlyOwner {
        require(moonwell.isUpgradeAvailable(), "No upgrade available");
        moonwell.upgradeSystem();
        emit SystemUpgraded();
    }

    function updateChainSupport(uint256 _chainId, bool _isSupported)
        external
        onlyOwner
    {
        supportedChains[_chainId] = _isSupported;
        emit ChainSupportUpdated(_chainId, _isSupported);
    }

    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    function emergencyWithdraw(address _token, uint256 _amount)
        external
        onlyOwner
    {
        IERC20 token = IERC20(_token);
        token.transfer(owner(), _amount);
    }
}
```
