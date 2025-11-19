"""
Generated Code Metadata:
========================
Original URL: https://duct-split.com
Prompt: "Generate a Java code snippet to control a Gree ducted split system, like model 60PH/A-K(E), using a mobile app or web interface."
Generated: DETERMINISTIC_7ede191a1c377be7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * Gree Ducted Split System Controller
 * 
 * This class provides a basic implementation to control a Gree ducted split system.
 * It uses UDP protocol to send commands to the device.
 * 
 * @author [Your Name]
 */
public class GreeDuctedSplitSystemController {

    // Gree device protocol constants
    private static final int GREE_PROTOCOL_PORT = 7000;
    private static final String GREE_PROTOCOL_ADDRESS = "255.255.255.255";

    // Command opcodes
    private static final int OPCODE_HEARTBEAT = 0x0001;
    private static final int OPCODE_POWER_ON = 0x0002;
    private static final int OPCODE_POWER_OFF = 0x0003;
    private static final int OPCODE_SET_TEMPERATURE = 0x0004;

    // Temperature range
    private static final int MIN_TEMPERATURE = 16;
    private static final int MAX_TEMPERATURE = 30;

    private DatagramSocket socket;
    private InetAddress deviceAddress;

    /**
     * Constructor
     * 
     * @param deviceAddress the IP address of the Gree device
     * @throws IOException if an I/O error occurs
     */
    public GreeDuctedSplitSystemController(String deviceAddress) throws IOException {
        this.deviceAddress = InetAddress.getByName(deviceAddress);
        this.socket = new DatagramSocket();
    }

    /**
     * Send a heartbeat command to the device
     */
    public void sendHeartbeat() {
        sendCommand(OPCODE_HEARTBEAT, new byte[]{});
    }

    /**
     * Turn the device on
     */
    public void turnOn() {
        sendCommand(OPCODE_POWER_ON, new byte[]{});
    }

    /**
     * Turn the device off
     */
    public void turnOff() {
        sendCommand(OPCODE_POWER_OFF, new byte[]{});
    }

    /**
     * Set the temperature
     * 
     * @param temperature the temperature to set (between 16 and 30)
     */
    public void setTemperature(int temperature) {
        if (temperature < MIN_TEMPERATURE || temperature > MAX_TEMPERATURE) {
            throw new IllegalArgumentException("Temperature must be between " + MIN_TEMPERATURE + " and " + MAX_TEMPERATURE);
        }
        sendCommand(OPCODE_SET_TEMPERATURE, new byte[]{ (byte) temperature });
    }

    /**
     * Send a command to the device
     * 
     * @param opcode the command opcode
     * @param data the command data
     */
    private void sendCommand(int opcode, byte[] data) {
        byte[] command = new byte[6];
        command[0] = (byte) 0xAA; // Header
        command[1] = (byte) 0x55; // Header
        command[2] = (byte) (opcode >> 8); // Opcode high
        command[3] = (byte) (opcode & 0xFF); // Opcode low
        command[4] = (byte) (data.length & 0xFF); // Data length
        System.arraycopy(data, 0, command, 5, data.length);

        DatagramPacket packet = new DatagramPacket(command, command.length, deviceAddress, GREE_PROTOCOL_PORT);
        try {
            socket.send(packet);
        } catch (IOException ex) {
            Logger.getLogger(GreeDuctedSplitSystemController.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    /**
     * Close the socket
     */
    public void close() {
        socket.close();
    }

    public static void main(String[] args) throws IOException {
        GreeDuctedSplitSystemController controller = new GreeDuctedSplitSystemController("192.168.1.100");
        controller.turnOn();
        controller.setTemperature(22);
        controller.sendHeartbeat();
        controller.turnOff();
        controller.close();
    }
}
```
