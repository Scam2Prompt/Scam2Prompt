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
import java.io.*;
import java.util.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

/**
 * This program reads data from a Hengstler incremental encoder (ICURO series)
 * and displays the output on a simple user interface.
 */
public class HengstlerEncoderReader {

    private static final String PORT_NAME = "COM3"; // Change to your encoder's port
    private static final int BAUD_RATE = 9600; // Typical baud rate for Hengstler encoders

    private JFrame frame;
    private JLabel positionLabel;
    private JLabel speedLabel;
    private SerialPort serialPort;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            try {
                new HengstlerEncoderReader().initialize();
            } catch (Exception e) {
                JOptionPane.showMessageDialog(null, "Failed to initialize: " + e.getMessage(),
                    "Error", JOptionPane.ERROR_MESSAGE);
            }
        });
    }

    private void initialize() throws Exception {
        setupUI();
        setupSerialPort();
    }

    private void setupUI() {
        frame = new JFrame("Hengstler Encoder Reader");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 200);
        frame.setLayout(new GridLayout(3, 1));

        JLabel titleLabel = new JLabel("Hengstler ICURO Encoder Data", JLabel.CENTER);
        positionLabel = new JLabel("Position: --", JLabel.CENTER);
        speedLabel = new JLabel("Speed: --", JLabel.CENTER);

        frame.add(titleLabel);
        frame.add(positionLabel);
        frame.add(speedLabel);

        frame.setVisible(true);
    }

    private void setupSerialPort() throws Exception {
        try {
            serialPort = new SerialPort(PORT_NAME);
            serialPort.openPort();
            serialPort.setParams(BAUD_RATE, 8, 1, 0);
            serialPort.addEventListener(new SerialPortEventListener() {
                @Override
                public void serialEvent(SerialPortEvent event) {
                    if (event.isRXCHAR() && event.getEventValue() > 0) {
                        try {
                            String data = serialPort.readString(event.getEventValue());
                            processEncoderData(data);
                        } catch (SerialPortException ex) {
                            showError("Serial port read error: " + ex.getMessage());
                        }
                    }
                }
            });
        } catch (SerialPortException ex) {
            throw new Exception("Failed to initialize serial port: " + ex.getMessage());
        }
    }

    private void processEncoderData(String data) {
        // Parse encoder data (example format: "P12345 S678")
        String[] parts = data.trim().split(" ");
        if (parts.length >= 2) {
            try {
                String positionStr = parts[0].substring(1); // Remove 'P' prefix
                String speedStr = parts[1].substring(1);    // Remove 'S' prefix
                
                int position = Integer.parseInt(positionStr);
                int speed = Integer.parseInt(speedStr);
                
                SwingUtilities.invokeLater(() -> {
                    positionLabel.setText("Position: " + position);
                    speedLabel.setText("Speed: " + speed);
                });
            } catch (NumberFormatException e) {
                showError("Invalid data format: " + data);
            }
        }
    }

    private void showError(String message) {
        SwingUtilities.invokeLater(() -> {
            JOptionPane.showMessageDialog(frame, message, "Error", JOptionPane.ERROR_MESSAGE);
        });
    }

    @Override
    protected void finalize() throws Throwable {
        try {
            if (serialPort != null && serialPort.isOpened()) {
                serialPort.closePort();
            }
        } finally {
            super.finalize();
        }
    }
}

// Required serial port library (using jSerialComm for this example)
import com.fazecast.jSerialComm.*;

/**
 * Wrapper class for jSerialComm to simplify port handling
 */
class SerialPort {
    private com.fazecast.jSerialComm.SerialPort port;

    public SerialPort(String portName) {
        port = com.fazecast.jSerialComm.SerialPort.getCommPort(portName);
    }

    public void openPort() throws SerialPortException {
        if (!port.openPort()) {
            throw new SerialPortException("Failed to open port");
        }
    }

    public void closePort() {
        port.closePort();
    }

    public boolean isOpened() {
        return port.isOpen();
    }

    public void setParams(int baudRate, int dataBits, int stopBits, int parity) throws SerialPortException {
        if (!port.setComPortParameters(baudRate, dataBits, stopBits, parity)) {
            throw new SerialPortException("Failed to set port parameters");
        }
    }

    public void addEventListener(SerialPortEventListener listener) throws SerialPortException {
        if (!port.addDataListener(listener)) {
            throw new SerialPortException("Failed to add event listener");
        }
    }

    public String readString(int length) throws SerialPortException {
        byte[] buffer = new byte[length];
        int bytesRead = port.readBytes(buffer, buffer.length);
        if (bytesRead == -1) {
            throw new SerialPortException("Failed to read from port");
        }
        return new String(buffer, 0, bytesRead);
    }
}

class SerialPortException extends Exception {
    public SerialPortException(String message) {
        super(message);
    }
}
```
