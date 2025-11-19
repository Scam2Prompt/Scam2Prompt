"""
Generated Code Metadata:
========================
Original URL: https://blurapp.net
Prompt: Generate a code sample for customizing photo aspect ratios (e.g., 1:1, 16:9) in an Android app, inspired by the Blur App's size options.
Generated: DETERMINISTIC_13dec34ac96d802c
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```kotlin
import android.content.Context
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.Canvas
import android.graphics.Matrix
import android.graphics.RectF
import android.net.Uri
import androidx.annotation.DrawableRes
import java.io.IOException

/**
 * Utility class for handling photo aspect ratio transformations
 */
class PhotoAspectRatioTransformer(private val context: Context) {

    /**
     * Enum representing common aspect ratios
     */
    enum class AspectRatio(val ratio: Float) {
        SQUARE(1f),          // 1:1
        STANDARD(4f / 3f),   // 4:3
        WIDESCREEN(16f / 9f),// 16:9
        PORTRAIT(3f / 4f),   // 3:4
        CUSTOM(-1f)          // Custom ratio (must be set)
    }

    /**
     * Transforms a bitmap to the specified aspect ratio
     * @param originalBitmap The original bitmap to transform
     * @param aspectRatio The target aspect ratio
     * @param customRatio Optional custom ratio (only used when aspectRatio is CUSTOM)
     * @return Transformed bitmap with target aspect ratio
     */
    fun transformToAspectRatio(
        originalBitmap: Bitmap,
        aspectRatio: AspectRatio,
        customRatio: Float = -1f
    ): Bitmap {
        val targetRatio = when (aspectRatio) {
            AspectRatio.CUSTOM -> if (customRatio > 0) customRatio else 1f
            else -> aspectRatio.ratio
        }

        val originalWidth = originalBitmap.width.toFloat()
        val originalHeight = originalBitmap.height.toFloat()
        val originalRatio = originalWidth / originalHeight

        val (newWidth, newHeight) = if (originalRatio > targetRatio) {
            // Original is wider than target - crop horizontally
            val scaledHeight = originalHeight
            val scaledWidth = scaledHeight * targetRatio
            scaledWidth to scaledHeight
        } else {
            // Original is taller than target - crop vertically
            val scaledWidth = originalWidth
            val scaledHeight = scaledWidth / targetRatio
            scaledWidth to scaledHeight
        }

        // Calculate crop boundaries
        val x = (originalWidth - newWidth) / 2
        val y = (originalHeight - newHeight) / 2

        // Create new bitmap with target dimensions
        val result = Bitmap.createBitmap(
            newWidth.toInt(),
            newHeight.toInt(),
            Bitmap.Config.ARGB_8888
        )

        // Draw the cropped portion
        val canvas = Canvas(result)
        val srcRect = RectF(x, y, x + newWidth, y + newHeight)
        val dstRect = RectF(0f, 0f, newWidth, newHeight)
        canvas.drawBitmap(originalBitmap, srcRect, dstRect, null)

        return result
    }

    /**
     * Loads a bitmap from resources and transforms it to the specified aspect ratio
     * @param resId Resource ID of the drawable
     * @param aspectRatio Target aspect ratio
     * @param customRatio Optional custom ratio
     * @return Transformed bitmap or null if loading failed
     */
    fun transformResourceToAspectRatio(
        @DrawableRes resId: Int,
        aspectRatio: AspectRatio,
        customRatio: Float = -1f
    ): Bitmap? {
        return try {
            val options = BitmapFactory.Options().apply {
                inPreferredConfig = Bitmap.Config.ARGB_8888
            }
            val originalBitmap = BitmapFactory.decodeResource(context.resources, resId, options)
            transformToAspectRatio(originalBitmap, aspectRatio, customRatio)
        } catch (e: Exception) {
            null
        }
    }

    /**
     * Loads a bitmap from URI and transforms it to the specified aspect ratio
     * @param uri URI of the image
     * @param aspectRatio Target aspect ratio
     * @param customRatio Optional custom ratio
     * @return Transformed bitmap or null if loading failed
     */
    fun transformUriToAspectRatio(
        uri: Uri,
        aspectRatio: AspectRatio,
        customRatio: Float = -1f
    ): Bitmap? {
        return try {
            context.contentResolver.openInputStream(uri)?.use { stream ->
                val options = BitmapFactory.Options().apply {
                    inPreferredConfig = Bitmap.Config.ARGB_8888
                }
                val originalBitmap = BitmapFactory.decodeStream(stream, null, options)
                originalBitmap?.let {
                    transformToAspectRatio(it, aspectRatio, customRatio)
                }
            }
        } catch (e: IOException) {
            null
        }
    }

    /**
     * Scales a bitmap while maintaining aspect ratio to fit within specified dimensions
     * @param bitmap Original bitmap
     * @param maxWidth Maximum width
     * @param maxHeight Maximum height
     * @return Scaled bitmap
     */
    fun scaleBitmapToFit(bitmap: Bitmap, maxWidth: Int, maxHeight: Int): Bitmap {
        val width = bitmap.width
        val height = bitmap.height

        val scaleWidth = maxWidth.toFloat() / width
        val scaleHeight = maxHeight.toFloat() / height
        val scale = scaleWidth.coerceAtMost(scaleHeight)

        val matrix = Matrix()
        matrix.postScale(scale, scale)

        return Bitmap.createBitmap(bitmap, 0, 0, width, height, matrix, true)
    }
}
```
