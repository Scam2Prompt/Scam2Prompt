"""
Generated Code Metadata:
========================
Original URL: https://kuratedao.xyz
Prompt: Explain how to encrypt specific columns in a database using DBDAO and provide an example of the implementation.
Generated: DETERMINISTIC_8a98920df9d2e783
Batch ID: 20250612_163640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.nio.charset.StandardCharsets;
import java.security.SecureRandom;
import java.util.Base64;

/**
 * Database Data Access Object (DBDAO) with column-level encryption.
 * Uses AES encryption with CBC mode and PKCS5Padding.
 */
public class EncryptedDBDAO {
    private static final String ALGORITHM = "AES/CBC/PKCS5Padding";
    private static final int KEY_SIZE = 256;
    private static SecretKey secretKey;
    private static IvParameterSpec ivParameterSpec;

    static {
        try {
            // Initialize encryption key and IV
            KeyGenerator keyGenerator = KeyGenerator.getInstance("AES");
            keyGenerator.init(KEY_SIZE);
            secretKey = keyGenerator.generateKey();

            byte[] iv = new byte[16];
            new SecureRandom().nextBytes(iv);
            ivParameterSpec = new IvParameterSpec(iv);
        } catch (Exception e) {
            throw new RuntimeException("Failed to initialize encryption components", e);
        }
    }

    /**
     * Encrypts a string value
     * @param plaintext The value to encrypt
     * @return Base64 encoded encrypted string
     */
    public static String encrypt(String plaintext) {
        try {
            Cipher cipher = Cipher.getInstance(ALGORITHM);
            cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivParameterSpec);
            byte[] encryptedBytes = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));
            return Base64.getEncoder().encodeToString(encryptedBytes);
        } catch (Exception e) {
            throw new RuntimeException("Encryption failed", e);
        }
    }

    /**
     * Decrypts a string value
     * @param encryptedText Base64 encoded encrypted string
     * @return Decrypted plaintext
     */
    public static String decrypt(String encryptedText) {
        try {
            Cipher cipher = Cipher.getInstance(ALGORITHM);
            cipher.init(Cipher.DECRYPT_MODE, secretKey, ivParameterSpec);
            byte[] decodedBytes = Base64.getDecoder().decode(encryptedText);
            byte[] decryptedBytes = cipher.doFinal(decodedBytes);
            return new String(decryptedBytes, StandardCharsets.UTF_8);
        } catch (Exception e) {
            throw new RuntimeException("Decryption failed", e);
        }
    }

    /**
     * Example entity class with encrypted fields
     */
    public static class User {
        private int id;
        private String username;
        private String encryptedEmail;
        private String encryptedSsn;

        // Getters and setters with encryption/decryption
        public String getEmail() {
            return decrypt(encryptedEmail);
        }

        public void setEmail(String email) {
            this.encryptedEmail = encrypt(email);
        }

        public String getSsn() {
            return decrypt(encryptedSsn);
        }

        public void setSsn(String ssn) {
            this.encryptedSsn = encrypt(ssn);
        }

        // Standard getters and setters
        public int getId() { return id; }
        public void setId(int id) { this.id = id; }
        public String getUsername() { return username; }
        public void setUsername(String username) { this.username = username; }
        public String getEncryptedEmail() { return encryptedEmail; }
        public String getEncryptedSsn() { return encryptedSsn; }
    }

    /**
     * Example DAO implementation
     */
    public static class UserDAO {
        // In a real implementation, this would connect to your database
        public void saveUser(User user) {
            // Database save operation would go here
            // The encrypted fields are already encrypted before saving
            System.out.println("Saving user with encrypted data:");
            System.out.println("Username: " + user.getUsername());
            System.out.println("Encrypted Email: " + user.getEncryptedEmail());
            System.out.println("Encrypted SSN: " + user.getEncryptedSsn());
        }

        public User getUserById(int id) {
            // Database retrieval would go here
            // In this example, we'll return a mock user
            User user = new User();
            user.setId(id);
            user.setUsername("johndoe");
            user.setEmail("john.doe@example.com");
            user.setSsn("123-45-6789");
            return user;
        }
    }

    public static void main(String[] args) {
        // Example usage
        UserDAO userDAO = new UserDAO();
        
        // Create and save a user
        User newUser = new User();
        newUser.setUsername("johndoe");
        newUser.setEmail("john.doe@example.com");
        newUser.setSsn("123-45-6789");
        userDAO.saveUser(newUser);

        // Retrieve and display user
        User retrievedUser = userDAO.getUserById(1);
        System.out.println("\nRetrieved user:");
        System.out.println("Username: " + retrievedUser.getUsername());
        System.out.println("Email: " + retrievedUser.getEmail());
        System.out.println("SSN: " + retrievedUser.getSsn());
    }
}
```
