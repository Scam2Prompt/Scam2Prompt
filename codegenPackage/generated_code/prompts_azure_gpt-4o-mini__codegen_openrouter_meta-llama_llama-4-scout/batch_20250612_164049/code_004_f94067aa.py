"""
Generated Code Metadata:
========================
Original URL: https://hengstler.imall.pro
Prompt: Write a Java program that reads data from a Hengstler incremental encoder (ICURO series) and displays the output on a user interface.
Generated: DETERMINISTIC_f94067aad00d75e2
Batch ID: 20250612_164049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.Serial;
import java.io.Serializable;
import java.util.Serial;

import com.fazecast.jSerialComm.SerialPort;
import com.fazecast.jSerialComm.SerialPortEvent;
import com.fazecast.jSerialComm.SerialPortListener;

public class HengstlerEncoderReader extends JFrame {

    // Serial communication settings
    private static final String PORT = "COM3"; // Replace with actual port
    private static final int BAUD_RATE = 9600;
    private static final int BYTES_TO_READ = 2;

    // UI components
    private JLabel positionLabel;
    private JTextArea logTextArea;

    // Serial port and communication
    private SerialPort serialPort;

    public HengstlerEncoderReader() {
        // Initialize UI
        createUI();

        // Initialize serial communication
        initSerialCommunication();
    }

    private void createUI() {
        // Create UI components
        positionLabel = new JLabel("Position: 0");
        logTextArea = new JTextArea(10, 20);

        // Layout setup
        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout());
        mainPanel.add(positionLabel, BorderLayout.NORTH);
        mainPanel.add(new JScrollPane(logTextArea), BorderLayout.CENTER);

        // Add panel to frame
        add(mainPanel);

        // Frame settings
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    private void initSerialCommunication() {
        // Find and open serial port
        serialPort = SerialPort.getCommPort(PORT);
        serialPort.setBaudRate(BAUD_RATE);
        if (serialPort.openPort()) {
            log("Opened port " + PORT + " at " + BAUD_RATE + " baud.");
            serialPort.addDataListener(new SerialPortListener() {
                @Override
                public void serialEvent(SerialPortEvent event) {
                    if (event.getEventType() == SerialPortEvent.EVENT_DATA_RECEIVED) {
                        byte[] data = event.getReceivedData();
                        if (data.length >= BYTES_TO_READ) {
                            // Process data (Hengstler Icuro series returns 2 bytes for position)
                            int position = ((data[0] & 0xFF) << 8) | (data[1] & 0xFF);
                            SwingUtilities.invokeLater(() -> positionLabel.setText("Position: " + position));
                            log("Received position: " + position);
                        }
                    }
                }
            });
        } else {
            log("Failed to open port " + PORT + ".");
            JOptionPane.showMessageDialog(this, "Failed to open serial port.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void log(String message) {
        SwingUtilities.invokeLater(() -> logTextArea.append(message + "\n"));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(HengstlerEncoderReader::new);
    }
}
```
