"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurapp.net
Prompt: Create a function in Kotlin to apply multiple blur filters to an image using the Blur App's editing options, including size changer and eraser tools.
Generated: DETERMINISTIC_4ff9f940f603602a
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```kotlin
import android.graphics.Bitmap
import android.graphics.Canvas
import android.graphics.Paint
import android.graphics.BlurMaskFilter
import android.graphics.PorterDuff
import android.graphics.PorterDuffXfermode
import android.graphics.Rect

/**
 * A utility object for applying blur effects to images.
 */
object ImageBlurrer {

    /**
     * Applies multiple blur filters to a given Bitmap image.
     *
     * @param source The original Bitmap to be blurred.
     * @param blurRadius The radius of the blur effect.
     * @param sizeChangeFactor The factor by which to resize the image.
     * @param eraseArea The area of the image to be erased (if any), defined by a Rect.
     * @return A new Bitmap with the applied blur and other modifications.
     */
    fun applyBlurFilters(
        source: Bitmap,
        blurRadius: Float,
        sizeChangeFactor: Float,
        eraseArea: Rect? = null
    ): Bitmap {
        // Validate input parameters
        if (blurRadius < 0) throw IllegalArgumentException("Blur radius must be non-negative")
        if (sizeChangeFactor <= 0) throw IllegalArgumentException("Size change factor must be positive")

        // Resize the original bitmap
        val width = (source.width * sizeChangeFactor).toInt()
        val height = (source.height * sizeChangeFactor).toInt()
        val resizedBitmap = Bitmap.createScaledBitmap(source, width, height, true)

        // Create a new bitmap to apply blur effect
        val blurredBitmap = Bitmap.createBitmap(resizedBitmap)

        // Create a canvas for drawing
        val canvas = Canvas(blurredBitmap)
        val paint = Paint().apply {
            // Set blur effect
            setMaskFilter(BlurMaskFilter(blurRadius, BlurMaskFilter.Blur.NORMAL))
        }

        // Draw the original bitmap onto the canvas with blur
        canvas.drawBitmap(resizedBitmap, 0f, 0f, paint)

        // If eraseArea is defined, apply the eraser tool
        if (eraseArea != null) {
            val eraserPaint = Paint().apply {
                // Set up the paint for erasing
                xfermode = PorterDuffXfermode(PorterDuff.Mode.CLEAR)
            }
            // Erase the specified area
            canvas.drawRect(eraseArea, eraserPaint)
        }

        // Recycle the resized bitmap to free up memory
        resizedBitmap.recycle()

        return blurredBitmap
    }
}
```
