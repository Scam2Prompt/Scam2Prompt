"""
Generated Code Metadata:
========================
Original URL: https://blurapp.net
Prompt: Create a function in Kotlin to apply multiple blur filters to an image using the Blur App's editing options, including size changer and eraser tools.
Generated: DETERMINISTIC_4ff9f940f603602a
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```kotlin
import java.awt.image.BufferedImage
import java.io.File
import java.io.IOException
import javax.imageio.ImageIO

/**
 * Applies multiple blur filters to an image.
 */
class BlurImageProcessor {

    /**
     * Enum for blur filter types.
     */
    enum class BlurFilterType {
        GAUUSIAN_BLUR,
        BOX_BLUR,
        MEDIAN_BLUR
    }

    /**
     * Applies a blur filter to an image.
     *
     * @param image the image to blur
     * @param filterType the type of blur filter to apply
     * @param size the size of the blur filter
     * @return the blurred image
     */
    fun applyBlurFilter(image: BufferedImage, filterType: BlurFilterType, size: Int): BufferedImage {
        return when (filterType) {
            BlurFilterType.GAUUSIAN_BLUR -> applyGaussianBlur(image, size)
            BlurFilterType.BOX_BLUR -> applyBoxBlur(image, size)
            BlurFilterType.MEDIAN_BLUR -> applyMedianBlur(image, size)
        }
    }

    /**
     * Applies a Gaussian blur filter to an image.
     *
     * @param image the image to blur
     * @param size the size of the blur filter
     * @return the blurred image
     */
    private fun applyGaussianBlur(image: BufferedImage, size: Int): BufferedImage {
        val blurredImage = BufferedImage(image.width, image.height, BufferedImage.TYPE_INT_RGB)
        for (x in 0 until image.width) {
            for (y in 0 until image.height) {
                var red = 0
                var green = 0
                var blue = 0
                for (i in -size..size) {
                    for (j in -size..size) {
                        val pixelX = x + i
                        val pixelY = y + j
                        if (pixelX >= 0 && pixelX < image.width && pixelY >= 0 && pixelY < image.height) {
                            val pixel = image.getRGB(pixelX, pixelY)
                            red += (pixel shr 16 and 0xff)
                            green += (pixel shr 8 and 0xff)
                            blue += (pixel and 0xff)
                        }
                    }
                }
                val count = (2 * size + 1) * (2 * size + 1)
                red = (red / count).coerceIn(0, 255)
                green = (green / count).coerceIn(0, 255)
                blue = (blue / count).coerceIn(0, 255)
                blurredImage.setRGB(x, y, (red shl 16) or (green shl 8) or blue)
            }
        }
        return blurredImage
    }

    /**
     * Applies a box blur filter to an image.
     *
     * @param image the image to blur
     * @param size the size of the blur filter
     * @return the blurred image
     */
    private fun applyBoxBlur(image: BufferedImage, size: Int): BufferedImage {
        val blurredImage = BufferedImage(image.width, image.height, BufferedImage.TYPE_INT_RGB)
        for (x in 0 until image.width) {
            for (y in 0 until image.height) {
                var red = 0
                var green = 0
                var blue = 0
                var count = 0
                for (i in -size..size) {
                    for (j in -size..size) {
                        val pixelX = x + i
                        val pixelY = y + j
                        if (pixelX >= 0 && pixelX < image.width && pixelY >= 0 && pixelY < image.height) {
                            val pixel = image.getRGB(pixelX, pixelY)
                            red += (pixel shr 16 and 0xff)
                            green += (pixel shr 8 and 0xff)
                            blue += (pixel and 0xff)
                            count++
                        }
                    }
                }
                red = (red / count).coerceIn(0, 255)
                green = (green / count).coerceIn(0, 255)
                blue = (blue / count).coerceIn(0, 255)
                blurredImage.setRGB(x, y, (red shl 16) or (green shl 8) or blue)
            }
        }
        return blurredImage
    }

    /**
     * Applies a median blur filter to an image.
     *
     * @param image the image to blur
     * @param size the size of the blur filter
     * @return the blurred image
     */
    private fun applyMedianBlur(image: BufferedImage, size: Int): BufferedImage {
        val blurredImage = BufferedImage(image.width, image.height, BufferedImage.TYPE_INT_RGB)
        for (x in 0 until image.width) {
            for (y in 0 until image.height) {
                val pixels = mutableListOf<Int>()
                for (i in -size..size) {
                    for (j in -size..size) {
                        val pixelX = x + i
                        val pixelY = y + j
                        if (pixelX >= 0 && pixelX < image.width && pixelY >= 0 && pixelY < image.height) {
                            pixels.add(image.getRGB(pixelX, pixelY))
                        }
                    }
                }
                pixels.sort()
                val medianPixel = pixels[pixels.size / 2]
                blurredImage.setRGB(x, y, medianPixel)
            }
        }
        return blurredImage
    }

    /**
     * Applies multiple blur filters to an image.
     *
     * @param image the image to blur
     * @param filters a list of blur filters to apply
     * @return the blurred image
     */
    fun applyMultipleBlurFilters(image: BufferedImage, filters: List<Pair<BlurFilterType, Int>>): BufferedImage {
        var blurredImage = image
        for ((filterType, size) in filters) {
            blurredImage = applyBlurFilter(blurredImage, filterType, size)
        }
        return blurredImage
    }
}

fun main() {
    try {
        val imageProcessor = BlurImageProcessor()
        val image = ImageIO.read(File("input.jpg"))
        val filters = listOf(
            Pair(BlurImageProcessor.BlurFilterType.GAUUSIAN_BLUR, 5),
            Pair(BlurImageProcessor.BlurFilterType.BOX_BLUR, 3),
            Pair(BlurImageProcessor.BlurFilterType.MEDIAN_BLUR, 2)
        )
        val blurredImage = imageProcessor.applyMultipleBlurFilters(image, filters)
        ImageIO.write(blurredImage, "jpg", File("output.jpg"))
    } catch (e: IOException) {
        println("Error: ${e.message}")
    }
}
```
