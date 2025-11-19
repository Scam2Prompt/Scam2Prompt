"""
Generated Code Metadata:
========================
Original URL: https://blurapp.net
Prompt: What are the system requirements for installing Blur App on an Android device, and how can I check if my device meets these requirements programmatically?
Generated: DETERMINISTIC_b5f2be17831fe2c0
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import android.os.Build;

public class BlurAppRequirementsChecker {

    /**
     * Minimum system requirements for installing Blur App.
     */
    private static final int MIN_ANDROID_VERSION = Build.VERSION_CODES.LOLLIPOP; // Android 5.0 (API 21)
    private static final int MIN_RAM_MB = 2048; // Minimum 2GB RAM
    private static final int MIN_STORAGE_MB = 500; // Minimum 500MB free storage

    /**
     * Checks if the device meets the system requirements for installing Blur App.
     *
     * @return true if the device meets the requirements, false otherwise.
     */
    public static boolean isDeviceCompatible() {
        try {
            // Check Android version
            if (Build.VERSION.SDK_INT < MIN_ANDROID_VERSION) {
                return false;
            }

            // Check RAM
            if (getTotalRAM() < MIN_RAM_MB) {
                return false;
            }

            // Check available storage
            if (getAvailableStorage() < MIN_STORAGE_MB) {
                return false;
            }

            return true; // All requirements met
        } catch (Exception e) {
            // Log the error (in production, use a logging framework)
            e.printStackTrace();
            return false; // Assume incompatible if an error occurs
        }
    }

    /**
     * Retrieves the total RAM of the device in MB.
     *
     * @return Total RAM in MB.
     */
    private static long getTotalRAM() {
        try {
            // Read memory info from /proc/meminfo
            java.io.BufferedReader reader = new java.io.BufferedReader(new java.io.FileReader("/proc/meminfo"));
            String line = reader.readLine(); // First line contains total RAM info
            reader.close();

            if (line != null && line.startsWith("MemTotal:")) {
                // Extract the numeric value (in KB) and convert to MB
                String[] parts = line.split("\\s+");
                return Long.parseLong(parts[1]) / 1024; // Convert KB to MB
            }
        } catch (Exception e) {
            e.printStackTrace(); // Log the error
        }
        return 0; // Return 0 if unable to determine RAM
    }

    /**
     * Retrieves the available storage on the device in MB.
     *
     * @return Available storage in MB.
     */
    private static long getAvailableStorage() {
        try {
            android.os.StatFs statFs = new android.os.StatFs(android.os.Environment.getDataDirectory().getPath());
            long availableBytes = statFs.getAvailableBytes();
            return availableBytes / (1024 * 1024); // Convert bytes to MB
        } catch (Exception e) {
            e.printStackTrace(); // Log the error
        }
        return 0; // Return 0 if unable to determine storage
    }

    /**
     * Main method for testing the compatibility check.
     */
    public static void main(String[] args) {
        if (isDeviceCompatible()) {
            System.out.println("Your device meets the requirements for installing Blur App.");
        } else {
            System.out.println("Your device does not meet the requirements for installing Blur App.");
        }
    }
}
```
