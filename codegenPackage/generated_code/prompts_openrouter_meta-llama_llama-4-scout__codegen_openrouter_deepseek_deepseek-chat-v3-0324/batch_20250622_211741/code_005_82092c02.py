"""
Generated Code Metadata:
========================
Original URL: https://hengstler.imall.pro
Prompt: "Write a code example in Java for controlling a Hengstler Guillotine cutter F or Rotary Cutter G using a machine's control system."
Generated: DETERMINISTIC_82092c021eaee438
Batch ID: 20250622_211741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.io.IOException;
import java.util.concurrent.TimeUnit;

/**
 * This class provides control for Hengstler Guillotine cutter F or Rotary Cutter G
 * through a machine's control system. It includes methods for initializing the cutter,
 * performing cuts, and handling errors.
 */
public class HengstlerCutterController {

    private static final int DEFAULT_TIMEOUT_MS = 5000;
    private static final int MAX_RETRIES = 3;

    private final MachineControlSystem controlSystem;
    private final CutterType cutterType;

    /**
     * Enum representing the types of cutters supported.
     */
    public enum CutterType {
        GUILLOTINE_F,
        ROTARY_G
    }

    /**
     * Constructor for HengstlerCutterController.
     * @param controlSystem The machine's control system interface
     * @param cutterType The type of cutter (F or G)
     */
    public HengstlerCutterController(MachineControlSystem controlSystem, CutterType cutterType) {
        this.controlSystem = controlSystem;
        this.cutterType = cutterType;
    }

    /**
     * Initializes the cutter device.
     * @throws CutterInitializationException if initialization fails
     */
    public void initialize() throws CutterInitializationException {
        try {
            boolean success = false;
            int retries = 0;

            while (!success && retries < MAX_RETRIES) {
                try {
                    controlSystem.sendCommand("INIT " + cutterType.name());
                    String response = controlSystem.readResponse(DEFAULT_TIMEOUT_MS);
                    
                    if ("READY".equals(response)) {
                        success = true;
                    } else {
                        retries++;
                        TimeUnit.MILLISECONDS.sleep(1000);
                    }
                } catch (IOException | InterruptedException e) {
                    retries++;
                    if (retries >= MAX_RETRIES) {
                        throw new CutterInitializationException("Failed to initialize cutter after " + MAX_RETRIES + " attempts", e);
                    }
                }
            }

            if (!success) {
                throw new CutterInitializationException("Cutter did not respond with READY status");
            }
        } catch (Exception e) {
            throw new CutterInitializationException("Cutter initialization failed", e);
        }
    }

    /**
     * Performs a cut operation.
     * @param lengthMm The length to cut in millimeters
     * @throws CutterOperationException if the cut operation fails
     */
    public void performCut(double lengthMm) throws CutterOperationException {
        if (lengthMm <= 0) {
            throw new IllegalArgumentException("Cut length must be positive");
        }

        try {
            controlSystem.sendCommand("CUT " + lengthMm);
            String response = controlSystem.readResponse(DEFAULT_TIMEOUT_MS);

            if (!"CUT_COMPLETE".equals(response)) {
                throw new CutterOperationException("Cut operation failed. Response: " + response);
            }
        } catch (IOException e) {
            throw new CutterOperationException("Communication error during cut operation", e);
        }
    }

    /**
     * Custom exception for cutter initialization failures.
     */
    public static class CutterInitializationException extends Exception {
        public CutterInitializationException(String message) {
            super(message);
        }

        public CutterInitializationException(String message, Throwable cause) {
            super(message, cause);
        }
    }

    /**
     * Custom exception for cutter operation failures.
     */
    public static class CutterOperationException extends Exception {
        public CutterOperationException(String message) {
            super(message);
        }

        public CutterOperationException(String message, Throwable cause) {
            super(message, cause);
        }
    }

    /**
     * Interface representing the machine's control system.
     */
    public interface MachineControlSystem {
        void sendCommand(String command) throws IOException;
        String readResponse(int timeoutMs) throws IOException;
    }
}
```
