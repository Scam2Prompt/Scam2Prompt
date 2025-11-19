"""
Generated Code Metadata:
========================
Original URL: https://mobilesolana.web.app
Prompt: Explain how to implement AES encryption for securing user seeds in a mobile application built on the Solana Mobile Stack.
Generated: DETERMINISTIC_142ed15d7e3d43fd
Batch ID: 20250612_162707
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```kotlin
import android.security.keystore.KeyGenParameterSpec
import android.security.keystore.KeyProperties
import android.util.Base64
import java.nio.charset.StandardCharsets
import java.security.KeyStore
import javax.crypto.Cipher
import javax.crypto.KeyGenerator
import javax.crypto.SecretKey
import javax.crypto.spec.GCMParameterSpec

/**
 * Helper class for AES-GCM encryption/decryption using Android Keystore
 */
class AesEncryptionHelper(private val keyAlias: String) {

    companion object {
        private const val ANDROID_KEYSTORE = "AndroidKeyStore"
        private const val AES_MODE = "AES/GCM/NoPadding"
        private const val IV_LENGTH_BYTES = 12 // 96 bits for GCM
        private const val TAG_LENGTH_BITS = 128 // 128 bits for GCM
    }

    private val keyStore: KeyStore = KeyStore.getInstance(ANDROID_KEYSTORE).apply {
        load(null)
    }

    /**
     * Generates or retrieves the AES key from Android Keystore
     */
    private fun getOrCreateSecretKey(): SecretKey {
        if (!keyStore.containsAlias(keyAlias)) {
            val keyGenerator = KeyGenerator.getInstance(
                KeyProperties.KEY_ALGORITHM_AES,
                ANDROID_KEYSTORE
            )

            keyGenerator.init(
                KeyGenParameterSpec.Builder(
                    keyAlias,
                    KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT
                )
                    .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
                    .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
                    .setKeySize(256)
                    .setUserAuthenticationRequired(false)
                    .build()
            )

            return keyGenerator.generateKey()
        }

        return (keyStore.getEntry(keyAlias, null) as KeyStore.SecretKeyEntry).secretKey
    }

    /**
     * Encrypts the given plaintext using AES-GCM
     * @param plaintext The text to encrypt
     * @return Base64 encoded string containing IV + ciphertext
     */
    fun encrypt(plaintext: String): String {
        val cipher = Cipher.getInstance(AES_MODE)
        val secretKey = getOrCreateSecretKey()

        cipher.init(Cipher.ENCRYPT_MODE, secretKey)
        val iv = cipher.iv
        val ciphertext = cipher.doFinal(plaintext.toByteArray(StandardCharsets.UTF_8))

        // Combine IV and ciphertext
        val encryptedData = ByteArray(iv.size + ciphertext.size)
        System.arraycopy(iv, 0, encryptedData, 0, iv.size)
        System.arraycopy(ciphertext, 0, encryptedData, iv.size, ciphertext.size)

        return Base64.encodeToString(encryptedData, Base64.DEFAULT)
    }

    /**
     * Decrypts the given ciphertext using AES-GCM
     * @param encryptedData Base64 encoded string containing IV + ciphertext
     * @return The decrypted plaintext
     * @throws Exception if decryption fails
     */
    fun decrypt(encryptedData: String): String {
        val combined = Base64.decode(encryptedData, Base64.DEFAULT)
        val iv = ByteArray(IV_LENGTH_BYTES)
        val ciphertext = ByteArray(combined.size - IV_LENGTH_BYTES)

        System.arraycopy(combined, 0, iv, 0, iv.size)
        System.arraycopy(combined, iv.size, ciphertext, 0, ciphertext.size)

        val cipher = Cipher.getInstance(AES_MODE)
        val secretKey = getOrCreateSecretKey()

        cipher.init(
            Cipher.DECRYPT_MODE,
            secretKey,
            GCMParameterSpec(TAG_LENGTH_BITS, iv)
        )

        val plaintext = cipher.doFinal(ciphertext)
        return String(plaintext, StandardCharsets.UTF_8)
    }

    /**
     * Deletes the encryption key from Android Keystore
     */
    fun deleteKey() {
        if (keyStore.containsAlias(keyAlias)) {
            keyStore.deleteEntry(keyAlias)
        }
    }
}
```

```kotlin
// Example usage in a ViewModel or Repository
class SeedManager(private val encryptionHelper: AesEncryptionHelper) {

    fun storeSeed(seedPhrase: String): String {
        return try {
            encryptionHelper.encrypt(seedPhrase)
        } catch (e: Exception) {
            throw SeedEncryptionException("Failed to encrypt seed phrase", e)
        }
    }

    fun retrieveSeed(encryptedSeed: String): String {
        return try {
            encryptionHelper.decrypt(encryptedSeed)
        } catch (e: Exception) {
            throw SeedDecryptionException("Failed to decrypt seed phrase", e)
        }
    }

    fun clearKey() {
        encryptionHelper.deleteKey()
    }
}

class SeedEncryptionException(message: String, cause: Throwable) : Exception(message, cause)
class SeedDecryptionException(message: String, cause: Throwable) : Exception(message, cause)
```
