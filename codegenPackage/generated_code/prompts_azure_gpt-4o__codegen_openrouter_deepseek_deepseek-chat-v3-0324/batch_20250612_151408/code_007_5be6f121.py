"""
Generated Code Metadata:
========================
Original URL: https://snso.com.cn
Prompt: Write a Solidity smart contract that interacts with TPWallet to enhance security in multi-chain asset management.
Generated: DETERMINISTIC_5be6f121a959ca8a
Batch ID: 20250612_151408
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

interface ITPWallet {
    function verifySignature(bytes32 messageHash, bytes memory signature) external view returns (bool);
    function getOwner() external view returns (address);
}

contract MultiChainAssetManager is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store asset information
    struct Asset {
        address tokenAddress;
        uint256 amount;
        uint256 chainId;
    }

    // Mapping from user address to their assets
    mapping(address => Asset[]) private userAssets;

    // TPWallet contract interface
    ITPWallet public tpWallet;

    // Events
    event AssetDeposited(address indexed user, address token, uint256 amount, uint256 chainId);
    event AssetWithdrawn(address indexed user, address token, uint256 amount, uint256 chainId);
    event TPWalletUpdated(address newTPWallet);

    // Modifier to check if the caller is the TPWallet owner
    modifier onlyTPWalletOwner() {
        require(msg.sender == tpWallet.getOwner(), "Caller is not TPWallet owner");
        _;
    }

    constructor(address _tpWallet) {
        require(_tpWallet != address(0), "Invalid TPWallet address");
        tpWallet = ITPWallet(_tpWallet);
    }

    /**
     * @dev Update TPWallet contract address
     * @param _newTPWallet Address of the new TPWallet contract
     */
    function updateTPWallet(address _newTPWallet) external onlyOwner {
        require(_newTPWallet != address(0), "Invalid TPWallet address");
        tpWallet = ITPWallet(_newTPWallet);
        emit TPWalletUpdated(_newTPWallet);
    }

    /**
     * @dev Deposit assets into the contract
     * @param _tokenAddress Address of the token to deposit
     * @param _amount Amount of tokens to deposit
     * @param _chainId Chain ID where the asset originates
     */
    function deposit(address _tokenAddress, uint256 _amount, uint256 _chainId) external nonReentrant {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_amount > 0, "Amount must be greater than 0");

        IERC20 token = IERC20(_tokenAddress);
        uint256 balanceBefore = token.balanceOf(address(this));
        token.safeTransferFrom(msg.sender, address(this), _amount);
        uint256 balanceAfter = token.balanceOf(address(this));
        require(balanceAfter - balanceBefore == _amount, "Token transfer failed");

        userAssets[msg.sender].push(Asset({
            tokenAddress: _tokenAddress,
            amount: _amount,
            chainId: _chainId
        }));

        emit AssetDeposited(msg.sender, _tokenAddress, _amount, _chainId);
    }

    /**
     * @dev Withdraw assets using TPWallet signature verification
     * @param _tokenAddress Address of the token to withdraw
     * @param _amount Amount of tokens to withdraw
     * @param _chainId Chain ID where the asset should be withdrawn
     * @param _signature Signature from TPWallet to verify the withdrawal
     */
    function withdrawWithSignature(
        address _tokenAddress,
        uint256 _amount,
        uint256 _chainId,
        bytes memory _signature
    ) external nonReentrant {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_amount > 0, "Amount must be greater than 0");

        bytes32 messageHash = keccak256(abi.encodePacked(
            msg.sender,
            _tokenAddress,
            _amount,
            _chainId,
            block.chainid,
            address(this)
        ));

        require(tpWallet.verifySignature(messageHash, _signature), "Invalid signature");

        _withdrawAssets(msg.sender, _tokenAddress, _amount, _chainId);
    }

    /**
     * @dev Emergency withdraw assets (only TPWallet owner)
     * @param _user Address of the user to withdraw for
     * @param _tokenAddress Address of the token to withdraw
     * @param _amount Amount of tokens to withdraw
     * @param _chainId Chain ID where the asset should be withdrawn
     */
    function emergencyWithdraw(
        address _user,
        address _tokenAddress,
        uint256 _amount,
        uint256 _chainId
    ) external onlyTPWalletOwner nonReentrant {
        _withdrawAssets(_user, _tokenAddress, _amount, _chainId);
    }

    /**
     * @dev Internal function to handle asset withdrawal
     */
    function _withdrawAssets(
        address _user,
        address _tokenAddress,
        uint256 _amount,
        uint256 _chainId
    ) internal {
        bool assetFound = false;
        uint256 assetIndex = 0;

        // Find the asset in user's assets
        for (uint256 i = 0; i < userAssets[_user].length; i++) {
            if (userAssets[_user][i].tokenAddress == _tokenAddress && 
                userAssets[_user][i].chainId == _chainId) {
                require(userAssets[_user][i].amount >= _amount, "Insufficient balance");
                assetFound = true;
                assetIndex = i;
                break;
            }
        }

        require(assetFound, "Asset not found");

        // Update the asset amount
        userAssets[_user][assetIndex].amount -= _amount;

        // If amount reaches zero, remove the asset from the array
        if (userAssets[_user][assetIndex].amount == 0) {
            userAssets[_user][assetIndex] = userAssets[_user][userAssets[_user].length - 1];
            userAssets[_user].pop();
        }

        // Transfer the tokens
        IERC20(_tokenAddress).safeTransfer(_user, _amount);

        emit AssetWithdrawn(_user, _tokenAddress, _amount, _chainId);
    }

    /**
     * @dev Get user's assets
     * @param _user Address of the user
     * @return Array of Asset structs
     */
    function getUserAssets(address _user) external view returns (Asset[] memory) {
        return userAssets[_user];
    }

    /**
     * @dev Get user's asset balance for a specific token and chain
     * @param _user Address of the user
     * @param _tokenAddress Address of the token
     * @param _chainId Chain ID
     * @return Balance of the specified asset
     */
    function getUserAssetBalance(
        address _user,
        address _tokenAddress,
        uint256 _chainId
    ) external view returns (uint256) {
        for (uint256 i = 0; i < userAssets[_user].length; i++) {
            if (userAssets[_user][i].tokenAddress == _tokenAddress && 
                userAssets[_user][i].chainId == _chainId) {
                return userAssets[_user][i].amount;
            }
        }
        return 0;
    }
}
```
