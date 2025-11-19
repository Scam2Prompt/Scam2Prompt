"""
Generated Code Metadata:
========================
Original URL: https://piaht.lol
Prompt: Develop a Java program to simulate activation of a 卡密, including error handling for invalid keys or missing 用户 ID.
Generated: DETERMINISTIC_dbf19b96a805fc48
Batch ID: 20250612_145734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.regex.Pattern;

/**
 * This class simulates the activation of a 卡密 (activation key) with proper error handling.
 */
public class ActivationSimulator {

    // In-memory storage for valid activation keys and their status
    private static final Map<String, Boolean> VALID_KEYS = new HashMap<>();
    // In-memory storage for user activations
    private static final Map<String, String> USER_ACTIVATIONS = new HashMap<>();
    
    // Key pattern: 20 alphanumeric characters
    private static final Pattern KEY_PATTERN = Pattern.compile("^[A-Za-z0-9]{20}$");
    // User ID pattern: 6-12 alphanumeric characters
    private static final Pattern USER_ID_PATTERN = Pattern.compile("^[A-Za-z0-9]{6,12}$");

    static {
        // Initialize with some valid keys
        VALID_KEYS.put("ABC123DEF456GHI789JKL", false);
        VALID_KEYS.put("XYZ987UVW654RST321OPQ", false);
        VALID_KEYS.put("MNO456PQR789STU012VWX", false);
    }

    /**
     * Activates a key for a user.
     * @param key The activation key to be activated
     * @param userId The user ID to associate with the key
     * @return ActivationResult containing success status and message
     */
    public static ActivationResult activateKey(String key, String userId) {
        try {
            // Validate inputs
            if (key == null || key.trim().isEmpty()) {
                return new ActivationResult(false, "激活码不能为空");
            }
            
            if (userId == null || userId.trim().isEmpty()) {
                return new ActivationResult(false, "用户ID不能为空");
            }
            
            if (!KEY_PATTERN.matcher(key).matches()) {
                return new ActivationResult(false, "无效的激活码格式");
            }
            
            if (!USER_ID_PATTERN.matcher(userId).matches()) {
                return new ActivationResult(false, "无效的用户ID格式");
            }
            
            // Check if key exists
            if (!VALID_KEYS.containsKey(key)) {
                return new ActivationResult(false, "激活码不存在");
            }
            
            // Check if key is already used
            if (VALID_KEYS.get(key)) {
                return new ActivationResult(false, "激活码已被使用");
            }
            
            // Check if user already has an active key
            if (USER_ACTIVATIONS.containsKey(userId)) {
                return new ActivationResult(false, "该用户已激活过激活码");
            }
            
            // Activate the key
            VALID_KEYS.put(key, true);
            USER_ACTIVATIONS.put(userId, key);
            
            return new ActivationResult(true, "激活成功");
        } catch (Exception e) {
            return new ActivationResult(false, "激活过程中发生错误: " + e.getMessage());
        }
    }

    /**
     * Represents the result of an activation attempt.
     */
    public static class ActivationResult {
        private final boolean success;
        private final String message;

        public ActivationResult(boolean success, String message) {
            this.success = success;
            this.message = message;
        }

        public boolean isSuccess() {
            return success;
        }

        public String getMessage() {
            return message;
        }

        @Override
        public String toString() {
            return "ActivationResult{" +
                    "success=" + success +
                    ", message='" + message + '\'' +
                    '}';
        }
    }

    // Example usage
    public static void main(String[] args) {
        // Test cases
        ActivationResult result1 = activateKey("ABC123DEF456GHI789JKL", "user123");
        System.out.println(result1);
        
        ActivationResult result2 = activateKey("ABC123DEF456GHI789JKL", "user456");
        System.out.println(result2);
        
        ActivationResult result3 = activateKey("INVALIDKEY1234567890", "user789");
        System.out.println(result3);
        
        ActivationResult result4 = activateKey("XYZ987UVW654RST321OPQ", "invalid@user");
        System.out.println(result4);
        
        ActivationResult result5 = activateKey(null, "user123");
        System.out.println(result5);
    }
}
```
