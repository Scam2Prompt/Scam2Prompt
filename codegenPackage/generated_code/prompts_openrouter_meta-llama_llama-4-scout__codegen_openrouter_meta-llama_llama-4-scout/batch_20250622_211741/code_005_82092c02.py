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
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketTimeoutException;

/**
 * Hengstler Cutter Control Class
 * 
 * This class provides methods to control a Hengstler Guillotine cutter F or Rotary Cutter G.
 * 
 * @author [Your Name]
 */
public class HengstlerCutterController {

    // Define the cutter types
    public enum CutterType {
        GUILLOTINE_F,
        ROTARY_G
    }

    // Define the command codes
    private static final String CUTTER_MOVE_UP = "M1";
    private static final String CUTTER_MOVE_DOWN = "M2";
    private static final String CUTTER_STOP = "M0";
    private static final String CUTTER_HOME = "H";

    // Machine's control system connection settings
    private String controlSystemIp;
    private int controlSystemPort;

    /**
     * Constructs a HengstlerCutterController instance.
     * 
     * @param controlSystemIp IP address of the machine's control system
     * @param controlSystemPort Port number of the machine's control system
     */
    public HengstlerCutterController(String controlSystemIp, int controlSystemPort) {
        this.controlSystemIp = controlSystemIp;
        this.controlSystemPort = controlSystemPort;
    }

    /**
     * Connects to the machine's control system.
     * 
     * @return true if connected successfully, false otherwise
     */
    private boolean connectToControlSystem() {
        Socket socket = new Socket();
        try {
            socket.connect(new InetSocketAddress(controlSystemIp, controlSystemPort), 1000);
            socket.close();
            return true;
        } catch (SocketTimeoutException e) {
            System.err.println("Connection timed out");
        } catch (IOException e) {
            System.err.println("Error connecting to control system: " + e.getMessage());
        }
        return false;
    }

    /**
     * Sends a command to the cutter.
     * 
     * @param cutterType Type of cutter
     * @param command Command to send
     * @return true if command sent successfully, false otherwise
     */
    private boolean sendCommand(CutterType cutterType, String command) {
        if (!connectToControlSystem()) {
            return false;
        }

        String commandString = cutterType.name() + "," + command;
        try (Socket socket = new Socket(controlSystemIp, controlSystemPort)) {
            socket.getOutputStream().write(commandString.getBytes());
            return true;
        } catch (IOException e) {
            System.err.println("Error sending command: " + e.getMessage());
        }
        return false;
    }

    /**
     * Moves the cutter up.
     * 
     * @param cutterType Type of cutter
     * @return true if command sent successfully, false otherwise
     */
    public boolean moveCutterUp(CutterType cutterType) {
        return sendCommand(cutterType, CUTTER_MOVE_UP);
    }

    /**
     * Moves the cutter down.
     * 
     * @param cutterType Type of cutter
     * @return true if command sent successfully, false otherwise
     */
    public boolean moveCutterDown(CutterType cutterType) {
        return sendCommand(cutterType, CUTTER_MOVE_DOWN);
    }

    /**
     * Stops the cutter.
     * 
     * @param cutterType Type of cutter
     * @return true if command sent successfully, false otherwise
     */
    public boolean stopCutter(CutterType cutterType) {
        return sendCommand(cutterType, CUTTER_STOP);
    }

    /**
     * Homes the cutter.
     * 
     * @param cutterType Type of cutter
     * @return true if command sent successfully, false otherwise
     */
    public boolean homeCutter(CutterType cutterType) {
        return sendCommand(cutterType, CUTTER_HOME);
    }

    public static void main(String[] args) {
        HengstlerCutterController controller = new HengstlerCutterController("192.168.1.100", 8080);

        // Example usage:
        CutterType cutterType = CutterType.GUILLOTINE_F;
        System.out.println("Moving cutter up: " + controller.moveCutterUp(cutterType));
        System.out.println("Moving cutter down: " + controller.moveCutterDown(cutterType));
        System.out.println("Stopping cutter: " + controller.stopCutter(cutterType));
        System.out.println("Homing cutter: " + controller.homeCutter(cutterType));
    }
}
```
