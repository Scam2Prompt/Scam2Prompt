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
import android.graphics.PorterDuff
import android.graphics.PorterDuffXfermode
import android.renderscript.Allocation
import android.renderscript.Element
import android.renderscript.RenderScript
import android.renderscript.ScriptIntrinsicBlur

/**
 * Applies multiple blur filters to an image with options for size adjustment
 * and eraser tool functionality.
 *
 * @param bitmap The original bitmap to be processed.
 * @param blurRadii List of blur radii to apply sequentially.
 * @param newSize Optional new size for the image dimensions (width, height).
 * @param eraserMask Optional bitmap mask indicating areas to erase (transparent).
 * @param context The application context for RenderScript initialization.
 *
 * @return A new bitmap with the applied blur effects, resized, and eraser mask applied.
 */
fun applyBlurFilters(
    bitmap: Bitmap,
    blurRadii: List<Float>,
    newSize: Pair<Int, Int>? = null,
    eraserMask: Bitmap? = null,
    context: android.content.Context
): Bitmap {
    try {
        // Resize the bitmap if newSize is provided
        val resizedBitmap = newSize?.let {
            Bitmap.createScaledBitmap(bitmap, it.first, it.second, true)
        } ?: bitmap

        var resultBitmap = resizedBitmap

        // Apply sequential blur filters using RenderScript
        val renderScript = RenderScript.create(context)
        blurRadii.forEach { radius ->
            if (radius < 0 || radius > 25) {
                throw IllegalArgumentException("Blur radius must be between 0 and 25")
            }

            val input = Allocation.createFromBitmap(renderScript, resultBitmap)
            val output = Allocation.createTyped(renderScript, input.type)
            val blurScript = ScriptIntrinsicBlur.create(renderScript, Element.U8_4(renderScript))

            blurScript.setRadius(radius)
            blurScript.setInput(input)
            blurScript.forEach(output)
            output.copyTo(resultBitmap)

            input.destroy()
            output.destroy()
            blurScript.destroy()
        }

        renderScript.destroy()

        // Apply eraser mask if provided
        eraserMask?.let { mask ->
            if (mask.width != resultBitmap.width || mask.height != resultBitmap.height) {
                throw IllegalArgumentException("Eraser mask dimensions must match the bitmap dimensions")
            }

            val outputBitmap = Bitmap.createBitmap(resultBitmap.width, resultBitmap.height, resultBitmap.config)
            val canvas = Canvas(outputBitmap)
            val paint = Paint()

            // Draw the blurred bitmap
            canvas.drawBitmap(resultBitmap, 0f, 0f, paint)

            // Set up eraser mode using PorterDuff
            paint.xfermode = PorterDuffXfermode(PorterDuff.Mode.CLEAR)
            canvas.drawBitmap(mask, 0f, 0f, paint)
            paint.xfermode = null

            resultBitmap = outputBitmap
        }

        return resultBitmap
    } catch (e: Exception) {
        // Handle unexpected errors gracefully
        throw RuntimeException("Error applying blur filters: ${e.message}", e)
    }
}
```
