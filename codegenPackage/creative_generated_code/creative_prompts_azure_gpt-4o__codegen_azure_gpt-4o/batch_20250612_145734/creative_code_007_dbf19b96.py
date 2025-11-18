"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piaht.lol
Prompt: Develop a Java program to simulate activation of a 卡密, including error handling for invalid keys or missing 用户 ID.
Generated: DETERMINISTIC_dbf19b96a805fc48
Batch ID: 20250612_145734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.HashSet;
import java.util.Scanner;

/**
 * ActivationSystem simulates the activation process for 卡密 (activation keys) with 用户 ID validation.
 */
public class ActivationSystem {

    // A set to store valid activation keys (simulating a database of keys)
    private static final HashSet<String> VALID_KEYS = new HashSet<>();

    static {
        // Initialize valid activation keys (for simulation purposes)
        VALID_KEYS.add("KEY12345");
        VALID_KEYS.add("KEY67890");
        VALID_KEYS.add("KEYABCDE");
    }

    /**
     * Main method to run the activation system.
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("欢迎使用激活系统!");
        System.out.print("请输入您的用户ID: ");
        String userId = scanner.nextLine();

        // Validate 用户 ID (must not be empty)
        if (userId == null || userId.trim().isEmpty()) {
            System.out.println("错误: 用户ID不能为空!");
            scanner.close();
            return;
        }

        System.out.print("请输入您的卡密: ");
        String activationKey = scanner.nextLine();

        // Validate 卡密 (must not be empty)
        if (activationKey == null || activationKey.trim().isEmpty()) {
            System.out.println("错误: 激活密钥不能为空!");
            scanner.close();
            return;
        }

        // Attempt activation
        try {
            activate(userId, activationKey);
            System.out.println("激活成功! 用户ID: " + userId + ", 卡密: " + activationKey);
        } catch (IllegalArgumentException e) {
            System.out.println("激活失败: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }

    /**
     * Activates the system using the provided user ID and activation key.
     * @param userId The 用户 ID provided by the user.
     * @param activationKey The 卡密 provided by the user.
     * @throws IllegalArgumentException If the activation key is invalid.
     */
    private static void activate(String userId, String activationKey) throws IllegalArgumentException {
        // Check if the activation key is valid
        if (!VALID_KEYS.contains(activationKey)) {
            throw new IllegalArgumentException("无效的激活密钥!");
        }

        // Simulate successful activation (additional logic could be added here for production use)
    }
}
```
