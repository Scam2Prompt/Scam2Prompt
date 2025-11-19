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
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.Socket;

/**
 * This class represents a simple GUI application that reads data from a Hengstler incremental encoder
 * and displays the output on the user interface.
 */
public class EncoderReaderApp extends JFrame {
    private JTextArea outputArea;
    private JButton startButton;
    private JButton stopButton;
    private volatile boolean running;
    private Socket socket;
    private BufferedReader reader;

    // Encoder connection parameters
    private static final String ENCODER_IP = "192.168.1.100"; // Replace with actual IP
    private static final int ENCODER_PORT = 12345; // Replace with actual port

    public EncoderReaderApp() {
        // Set up the frame
        setTitle("Hengstler Encoder Reader");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Initialize components
        outputArea = new JTextArea();
        outputArea.setEditable(false);
        startButton = new JButton("Start Reading");
        stopButton = new JButton("Stop Reading");

        // Add components to the frame
        add(new JScrollPane(outputArea), BorderLayout.CENTER);
        JPanel buttonPanel = new JPanel();
        buttonPanel.add(startButton);
        buttonPanel.add(stopButton);
        add(buttonPanel, BorderLayout.SOUTH);

        // Add action listeners
        startButton.addActionListener(new StartButtonListener());
        stopButton.addActionListener(new StopButtonListener());
    }

    /**
     * Starts reading data from the encoder in a separate thread.
     */
    private void startReading() {
        running = true;
        new Thread(() -> {
            try {
                // Establish connection to the encoder
                socket = new Socket(ENCODER_IP, ENCODER_PORT);
                reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));

                String line;
                while (running && (line = reader.readLine()) != null) {
                    // Update the output area on the Event Dispatch Thread
                    SwingUtilities.invokeLater(() -> outputArea.append(line + "\n"));
                }
            } catch (IOException e) {
                handleError("Error reading from encoder: " + e.getMessage());
            } finally {
                cleanup();
            }
        }).start();
    }

    /**
     * Stops reading data from the encoder.
     */
    private void stopReading() {
        running = false;
        cleanup();
    }

    /**
     * Cleans up resources and closes the socket.
     */
    private void cleanup() {
        try {
            if (reader != null) {
                reader.close();
            }
            if (socket != null && !socket.isClosed()) {
                socket.close();
            }
        } catch (IOException e) {
            handleError("Error closing resources: " + e.getMessage());
        }
    }

    /**
     * Handles errors by displaying them in the output area.
     *
     * @param message The error message to display.
     */
    private void handleError(String message) {
        SwingUtilities.invokeLater(() -> outputArea.append("ERROR: " + message + "\n"));
    }

    // Action listener for the start button
    private class StartButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            startReading();
        }
    }

    // Action listener for the stop button
    private class StopButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            stopReading();
        }
    }

    /**
     * Main method to run the application.
     *
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            EncoderReaderApp app = new EncoderReaderApp();
            app.setVisible(true);
        });
    }
}
```
