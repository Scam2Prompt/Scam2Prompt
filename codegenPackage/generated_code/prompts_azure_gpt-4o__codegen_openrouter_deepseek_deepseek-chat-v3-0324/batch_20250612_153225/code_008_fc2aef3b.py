"""
Generated Code Metadata:
========================
Original URL: https://klar-sehen.ch
Prompt: Generate a Java program that simulates visualizations and relaxation techniques for individuals with eye strain, incorporating concepts like "Visualisations-Kraftwelten" from Klar Sehen.
Generated: DETERMINISTIC_fc2aef3b77f234e1
Batch ID: 20250612_153225
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
import java.util.Random;

/**
 * A program that simulates visualizations and relaxation techniques for eye strain relief.
 * Incorporates concepts from "Visualisations-Kraftwelten" (Klar Sehen).
 */
public class EyeStrainRelaxationApp {
    private static final int WINDOW_WIDTH = 800;
    private static final int WINDOW_HEIGHT = 600;
    private static final int ANIMATION_DURATION = 30000; // 30 seconds per exercise
    private static final Color[] RELAXATION_COLORS = {
            new Color(173, 216, 230), // Light blue
            new Color(144, 238, 144), // Light green
            new Color(255, 228, 196), // Bisque
            new Color(221, 160, 221)  // Plum
    };

    private JFrame frame;
    private JPanel mainPanel;
    private JLabel instructionLabel;
    private Timer animationTimer;
    private Random random = new Random();

    public EyeStrainRelaxationApp() {
        initializeUI();
    }

    private void initializeUI() {
        frame = new JFrame("Eye Strain Relaxation Visualizer");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(WINDOW_WIDTH, WINDOW_HEIGHT);
        frame.setLayout(new BorderLayout());

        mainPanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                drawRelaxationVisualization(g);
            }
        };
        mainPanel.setBackground(Color.WHITE);

        instructionLabel = new JLabel("", SwingConstants.CENTER);
        instructionLabel.setFont(new Font("SansSerif", Font.BOLD, 18));
        instructionLabel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

        JPanel buttonPanel = new JPanel(new FlowLayout());
        JButton startButton = new JButton("Start Relaxation");
        JButton stopButton = new JButton("Stop");

        startButton.addActionListener(e -> startRelaxationExercise());
        stopButton.addActionListener(e -> stopRelaxationExercise());

        buttonPanel.add(startButton);
        buttonPanel.add(stopButton);

        frame.add(mainPanel, BorderLayout.CENTER);
        frame.add(instructionLabel, BorderLayout.NORTH);
        frame.add(buttonPanel, BorderLayout.SOUTH);

        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

    private void startRelaxationExercise() {
        if (animationTimer != null && animationTimer.isRunning()) {
            animationTimer.stop();
        }

        String[] exercises = {
                "Follow the moving circle with your eyes",
                "Focus on the center and relax your gaze",
                "Imagine the colors flowing into your eyes",
                "Blink slowly while watching the patterns"
        };

        String instruction = exercises[random.nextInt(exercises.length)];
        instructionLabel.setText(instruction);

        animationTimer = new Timer(100, new ActionListener() {
            long startTime = System.currentTimeMillis();

            @Override
            public void actionPerformed(ActionEvent e) {
                long elapsed = System.currentTimeMillis() - startTime;
                if (elapsed >= ANIMATION_DURATION) {
                    stopRelaxationExercise();
                    instructionLabel.setText("Exercise complete. Take a deep breath.");
                } else {
                    mainPanel.repaint();
                }
            }
        });
        animationTimer.start();
    }

    private void stopRelaxationExercise() {
        if (animationTimer != null) {
            animationTimer.stop();
        }
        mainPanel.repaint();
    }

    private void drawRelaxationVisualization(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        int width = mainPanel.getWidth();
        int height = mainPanel.getHeight();

        // Draw background gradient
        GradientPaint gradient = new GradientPaint(
                0, 0, RELAXATION_COLORS[0],
                width, height, RELAXATION_COLORS[1]);
        g2d.setPaint(gradient);
        g2d.fillRect(0, 0, width, height);

        // Draw moving elements
        long time = System.currentTimeMillis();
        int centerX = width / 2;
        int centerY = height / 2;

        // Draw pulsing circle
        int pulseSize = 50 + (int) (30 * Math.sin(time / 300.0));
        g2d.setColor(new Color(255, 255, 255, 150));
        g2d.fillOval(centerX - pulseSize / 2, centerY - pulseSize / 2, pulseSize, pulseSize);

        // Draw rotating lines
        int lineLength = Math.min(width, height) / 3;
        g2d.setStroke(new BasicStroke(3));
        for (int i = 0; i < 8; i++) {
            double angle = (time / 1000.0) + (i * Math.PI / 4);
            int x2 = centerX + (int) (lineLength * Math.cos(angle));
            int y2 = centerY + (int) (lineLength * Math.sin(angle));
            g2d.setColor(new Color(0, 0, 0, 100));
            g2d.drawLine(centerX, centerY, x2, y2);
        }

        // Draw floating particles
        for (int i = 0; i < 20; i++) {
            double offset = i * Math.PI * 2 / 20;
            int x = centerX + (int) (lineLength * 0.6 * Math.sin(time / 1000.0 + offset));
            int y = centerY + (int) (lineLength * 0.6 * Math.cos(time / 1000.0 + offset));
            int size = 5 + (int) (3 * Math.sin(time / 500.0 + i));
            g2d.setColor(new Color(255, 255, 255, 200));
            g2d.fillOval(x - size / 2, y - size / 2, size, size);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new EyeStrainRelaxationApp());
    }
}
```
