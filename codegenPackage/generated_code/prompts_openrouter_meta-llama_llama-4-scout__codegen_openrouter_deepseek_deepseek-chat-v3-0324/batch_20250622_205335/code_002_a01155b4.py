"""
Generated Code Metadata:
========================
Original URL: https://blurapp.net
Prompt: Generate Java code to implement a simple image editor with blur filters and effects, similar to Blur App.
Generated: DETERMINISTIC_a01155b407e88243
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class ImageEditor {
    
    /**
     * Main method to demonstrate image editing functionality
     */
    public static void main(String[] args) {
        try {
            // Load an image
            BufferedImage originalImage = loadImage("input.jpg");
            
            // Apply blur effects
            BufferedImage boxBlurImage = applyBoxBlur(originalImage, 3);
            BufferedImage gaussianBlurImage = applyGaussianBlur(originalImage, 3);
            BufferedImage motionBlurImage = applyMotionBlur(originalImage, 5);
            
            // Save processed images
            saveImage(boxBlurImage, "box_blur_output.jpg");
            saveImage(gaussianBlurImage, "gaussian_blur_output.jpg");
            saveImage(motionBlurImage, "motion_blur_output.jpg");
            
        } catch (IOException e) {
            System.err.println("Error processing image: " + e.getMessage());
        }
    }
    
    /**
     * Loads an image from file
     * @param filePath Path to the image file
     * @return BufferedImage object
     * @throws IOException if file cannot be read
     */
    public static BufferedImage loadImage(String filePath) throws IOException {
        File file = new File(filePath);
        if (!file.exists()) {
            throw new IOException("File not found: " + filePath);
        }
        return ImageIO.read(file);
    }
    
    /**
     * Saves an image to file
     * @param image Image to save
     * @param filePath Destination path
     * @throws IOException if file cannot be written
     */
    public static void saveImage(BufferedImage image, String filePath) throws IOException {
        File output = new File(filePath);
        ImageIO.write(image, "jpg", output);
    }
    
    /**
     * Applies box blur effect to an image
     * @param image Original image
     * @param radius Blur radius
     * @return Blurred image
     */
    public static BufferedImage applyBoxBlur(BufferedImage image, int radius) {
        int width = image.getWidth();
        int height = image.getHeight();
        BufferedImage blurredImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                int[] rgb = getAverageRGB(image, x, y, radius);
                int newRGB = new Color(rgb[0], rgb[1], rgb[2]).getRGB();
                blurredImage.setRGB(x, y, newRGB);
            }
        }
        
        return blurredImage;
    }
    
    /**
     * Applies Gaussian blur effect to an image
     * @param image Original image
     * @param radius Blur radius
     * @return Blurred image
     */
    public static BufferedImage applyGaussianBlur(BufferedImage image, int radius) {
        int width = image.getWidth();
        int height = image.getHeight();
        BufferedImage blurredImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        
        // Create Gaussian kernel
        float[] kernel = createGaussianKernel(radius);
        
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                int[] rgb = applyKernel(image, x, y, radius, kernel);
                int newRGB = new Color(rgb[0], rgb[1], rgb[2]).getRGB();
                blurredImage.setRGB(x, y, newRGB);
            }
        }
        
        return blurredImage;
    }
    
    /**
     * Applies motion blur effect to an image
     * @param image Original image
     * @param length Blur length
     * @return Blurred image
     */
    public static BufferedImage applyMotionBlur(BufferedImage image, int length) {
        int width = image.getWidth();
        int height = image.getHeight();
        BufferedImage blurredImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                int[] rgb = getMotionBlurRGB(image, x, y, length);
                int newRGB = new Color(rgb[0], rgb[1], rgb[2]).getRGB();
                blurredImage.setRGB(x, y, newRGB);
            }
        }
        
        return blurredImage;
    }
    
    /**
     * Calculates average RGB values in a square area
     * @param image Source image
     * @param x Center x-coordinate
     * @param y Center y-coordinate
     * @param radius Area radius
     * @return Array of average RGB values
     */
    private static int[] getAverageRGB(BufferedImage image, int x, int y, int radius) {
        int width = image.getWidth();
        int height = image.getHeight();
        int count = 0;
        int r = 0, g = 0, b = 0;
        
        for (int dy = -radius; dy <= radius; dy++) {
            for (int dx = -radius; dx <= radius; dx++) {
                int nx = x + dx;
                int ny = y + dy;
                
                if (nx >= 0 && nx < width && ny >= 0 && ny < height) {
                    Color color = new Color(image.getRGB(nx, ny));
                    r += color.getRed();
                    g += color.getGreen();
                    b += color.getBlue();
                    count++;
                }
            }
        }
        
        return new int[] {r/count, g/count, b/count};
    }
    
    /**
     * Creates Gaussian kernel for blur
     * @param radius Kernel radius
     * @return Gaussian kernel array
     */
    private static float[] createGaussianKernel(int radius) {
        int size = radius * 2 + 1;
        float[] kernel = new float[size * size];
        float sigma = radius / 3.0f;
        float sum = 0.0f;
        
        for (int y = -radius; y <= radius; y++) {
            for (int x = -radius; x <= radius; x++) {
                float value = (float)Math.exp(-(x*x + y*y)/(2*sigma*sigma));
                kernel[(y + radius) * size + (x + radius)] = value;
                sum += value;
            }
        }
        
        // Normalize the kernel
        for (int i = 0; i < kernel.length; i++) {
            kernel[i] /= sum;
        }
        
        return kernel;
    }
    
    /**
     * Applies convolution kernel to a pixel
     * @param image Source image
     * @param x Center x-coordinate
     * @param y Center y-coordinate
     * @param radius Kernel radius
     * @param kernel Convolution kernel
     * @return Array of resulting RGB values
     */
    private static int[] applyKernel(BufferedImage image, int x, int y, int radius, float[] kernel) {
        int width = image.getWidth();
        int height = image.getHeight();
        float r = 0, g = 0, b = 0;
        int size = radius * 2 + 1;
        int index = 0;
        
        for (int dy = -radius; dy <= radius; dy++) {
            for (int dx = -radius; dx <= radius; dx++) {
                int nx = x + dx;
                int ny = y + dy;
                
                if (nx >= 0 && nx < width && ny >= 0 && ny < height) {
                    Color color = new Color(image.getRGB(nx, ny));
                    float weight = kernel[index];
                    r += color.getRed() * weight;
                    g += color.getGreen() * weight;
                    b += color.getBlue() * weight;
                }
                index++;
            }
        }
        
        return new int[] {(int)r, (int)g, (int)b};
    }
    
    /**
     * Calculates motion blur RGB values
     * @param image Source image
     * @param x Center x-coordinate
     * @param y Center y-coordinate
     * @param length Blur length
     * @return Array of average RGB values
     */
    private static int[] getMotionBlurRGB(BufferedImage image, int x, int y, int length) {
        int width = image.getWidth();
        int height = image.getHeight();
        int count = 0;
        int r = 0, g = 0, b = 0;
        
        for (int i = -length; i <= length; i++) {
            int nx = x + i;
            int ny = y + i;
            
            if (nx >= 0 && nx < width && ny >= 0 && ny < height
