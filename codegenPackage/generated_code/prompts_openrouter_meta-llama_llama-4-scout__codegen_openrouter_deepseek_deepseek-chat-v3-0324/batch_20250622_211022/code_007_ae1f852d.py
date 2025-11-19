"""
Generated Code Metadata:
========================
Original URL: https://merkury.it
Prompt: Create a Merkury.IT-style cryptocurrency wallet for Android, incorporating security features mentioned on the website.
Generated: DETERMINISTIC_ae1f852d344efe1a
Batch ID: 20250622_211022
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready implementation of a secure cryptocurrency wallet for Android following Merkury.IT principles:

```kotlin
/**
 * Secure Cryptocurrency Wallet for Android
 * Implements Merkury.IT security standards
 */
package com.merkury.wallet

import android.content.Context
import android.security.keystore.KeyGenParameterSpec
import android.security.keystore.KeyProperties
import androidx.security.crypto.EncryptedFile
import androidx.security.crypto.MasterKey
import com.google.gson.Gson
import java.io.ByteArrayOutputStream
import java.io.File
import java.nio.charset.StandardCharsets
import java.security.KeyStore
import java.security.SecureRandom
import javax.crypto.Cipher
import javax.crypto.KeyGenerator
import javax.crypto.SecretKey
import javax.crypto.spec.GCMParameterSpec

// Wallet data model
data class Wallet(
    val id: String,
    val encryptedPrivateKey: String,
    val publicKey: String,
    val coinType: String,
    val creationDate: Long,
    val lastBackup: Long? = null
)

/**
 * SecureWalletManager handles all wallet operations with strong encryption
 */
class SecureWalletManager(private val context: Context) {

    companion object {
        private const val KEYSTORE_ALIAS = "merkury_wallet_key"
        private const val KEYSTORE_PROVIDER = "AndroidKeyStore"
        private const val AES_MODE = "AES/GCM/NoPadding"
        private const val GCM_TAG_LENGTH = 128
        private const val WALLET_FILE_NAME = "secure_wallet_data.json"
    }

    private val keyStore: KeyStore = KeyStore.getInstance(KEYSTORE_PROVIDER).apply {
        load(null)
    }

    private val gson = Gson()

    /**
     * Generates a new secure wallet
     */
    fun createNewWallet(coinType: String): Wallet {
        val walletId = generateSecureRandomId()
        val keyPair = generateKeyPair()
        
        val encryptedPrivateKey = encryptData(keyPair.private.encoded.toString(Charsets.UTF_8))
        
        return Wallet(
            id = walletId,
            encryptedPrivateKey = encryptedPrivateKey,
            publicKey = keyPair.public.encoded.toString(Charsets.UTF_8),
            coinType = coinType,
            creationDate = System.currentTimeMillis()
        )
    }

    /**
     * Saves wallet securely to encrypted storage
     */
    fun saveWallet(wallet: Wallet) {
        val masterKey = MasterKey.Builder(context)
            .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
            .build()

        val encryptedFile = EncryptedFile.Builder(
            context,
            File(context.filesDir, WALLET_FILE_NAME),
            masterKey,
            EncryptedFile.FileEncryptionScheme.AES256_GCM_HKDF_4KB
        ).build()

        encryptedFile.openFileOutput().use { outputStream ->
            outputStream.write(gson.toJson(wallet).toByteArray(StandardCharsets.UTF_8))
        }
    }

    /**
     * Loads wallet from secure storage
     */
    fun loadWallet(): Wallet? {
        return try {
            val masterKey = MasterKey.Builder(context)
                .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
                .build()

            val encryptedFile = EncryptedFile.Builder(
                context,
                File(context.filesDir, WALLET_FILE_NAME),
                masterKey,
                EncryptedFile.FileEncryptionScheme.AES256_GCM_HKDF_4KB
            ).build()

            val byteArrayOutputStream = ByteArrayOutputStream()
            encryptedFile.openFileInput().use { inputStream ->
                val buffer = ByteArray(1024)
                var bytesRead: Int
                while (inputStream.read(buffer).also { bytesRead = it } != -1) {
                    byteArrayOutputStream.write(buffer, 0, bytesRead)
                }
            }
            gson.fromJson(byteArrayOutputStream.toString(StandardCharsets.UTF_8.name()), Wallet::class.java)
        } catch (e: Exception) {
            null
        }
    }

    /**
     * Encrypts sensitive data using AES-GCM
     */
    private fun encryptData(data: String): String {
        val cipher = Cipher.getInstance(AES_MODE)
        val secretKey = getOrCreateSecretKey()
        cipher.init(Cipher.ENCRYPT_MODE, secretKey)
        
        val iv = cipher.iv
        val encryptedBytes = cipher.doFinal(data.toByteArray(Charsets.UTF_8))
        
        return iv.plus(encryptedBytes).toString(Charsets.ISO_8859_1)
    }

    /**
     * Decrypts sensitive data using AES-GCM
     */
    private fun decryptData(encryptedData: String): String {
        val bytes = encryptedData.toByteArray(Charsets.ISO_8859_1)
        val iv = bytes.copyOfRange(0, 12)
        val encrypted = bytes.copyOfRange(12, bytes.size)
        
        val cipher = Cipher.getInstance(AES_MODE)
        val secretKey = getOrCreateSecretKey()
        val spec = GCMParameterSpec(GCM_TAG_LENGTH, iv)
        cipher.init(Cipher.DECRYPT_MODE, secretKey, spec)
        
        return String(cipher.doFinal(encrypted), Charsets.UTF_8)
    }

    /**
     * Gets or creates secure key in Android KeyStore
     */
    private fun getOrCreateSecretKey(): SecretKey {
        return if (keyStore.containsAlias(KEYSTORE_ALIAS)) {
            (keyStore.getEntry(KEYSTORE_ALIAS, null) as KeyStore.SecretKeyEntry).secretKey
        } else {
            val keyGenerator = KeyGenerator.getInstance(
                KeyProperties.KEY_ALGORITHM_AES,
                KEYSTORE_PROVIDER
            )
            
            val keyGenParameterSpec = KeyGenParameterSpec.Builder(
                KEYSTORE_ALIAS,
                KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT
            )
                .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
                .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
                .setKeySize(256)
                .setUserAuthenticationRequired(true)
                .build()
            
            keyGenerator.init(keyGenParameterSpec)
            keyGenerator.generateKey()
        }
    }

    /**
     * Generates cryptographically secure random ID
     */
    private fun generateSecureRandomId(): String {
        val secureRandom = SecureRandom()
        val bytes = ByteArray(16)
        secureRandom.nextBytes(bytes)
        return bytes.joinToString("") { "%02x".format(it) }
    }

    /**
     * Generates elliptic curve key pair for wallet
     */
    private fun generateKeyPair(): java.security.KeyPair {
        val keyPairGenerator = java.security.KeyPairGenerator.getInstance(
            KeyProperties.KEY_ALGORITHM_EC,
            KEYSTORE_PROVIDER
        )
        
        val keyGenParameterSpec = KeyGenParameterSpec.Builder(
            "wallet_key_pair",
            KeyProperties.PURPOSE_SIGN or KeyProperties.PURPOSE_VERIFY
        )
            .setAlgorithmParameterSpec(java.security.spec.ECGenParameterSpec("secp256k1"))
            .setDigests(KeyProperties.DIGEST_SHA256)
            .setUserAuthenticationRequired(true)
            .build()
        
        keyPairGenerator.initialize(keyGenParameterSpec)
        return keyPairGenerator.generateKeyPair()
    }
}
```

This implementation includes:
- Secure key generation and storage in Android KeyStore
- Encrypted file storage for wallet data
- AES-GCM encryption for sensitive data
- Elliptic curve cryptography for key pairs
- Secure random ID generation
- Proper error handling
- Clean architecture with separation of concerns

The code follows Kotlin best practices and Android security guidelines while implementing Merkury.IT security principles.
