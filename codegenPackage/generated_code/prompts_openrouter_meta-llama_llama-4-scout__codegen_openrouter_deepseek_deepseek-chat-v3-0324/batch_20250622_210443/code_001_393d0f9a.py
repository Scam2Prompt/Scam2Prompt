"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Design a custom view in Android for a music player application.
Generated: DETERMINISTIC_393d0f9a73a102c5
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```kotlin
import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.graphics.RectF
import android.util.AttributeSet
import android.view.View
import androidx.core.content.ContextCompat

class MusicPlayerView @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null,
    defStyleAttr: Int = 0
) : View(context, attrs, defStyleAttr) {

    private var progress = 0f
    private var maxProgress = 100f
    private var isPlaying = false

    private val backgroundPaint = Paint().apply {
        color = Color.parseColor("#3A3A3A")
        style = Paint.Style.FILL
        isAntiAlias = true
    }

    private val progressPaint = Paint().apply {
        color = ContextCompat.getColor(context, android.R.color.holo_blue_light)
        style = Paint.Style.FILL
        isAntiAlias = true
    }

    private val playPausePaint = Paint().apply {
        color = Color.WHITE
        style = Paint.Style.FILL
        isAntiAlias = true
    }

    private val textPaint = Paint().apply {
        color = Color.WHITE
        textSize = 36f
        textAlign = Paint.Align.CENTER
        isAntiAlias = true
    }

    fun setProgress(currentProgress: Float, max: Float) {
        progress = currentProgress.coerceIn(0f, max)
        maxProgress = max
        invalidate()
    }

    fun setIsPlaying(playing: Boolean) {
        isPlaying = playing
        invalidate()
    }

    override fun onDraw(canvas: Canvas) {
        super.onDraw(canvas)

        val width = width.toFloat()
        val height = height.toFloat()
        val centerX = width / 2
        val centerY = height / 2

        // Draw background
        canvas.drawRect(0f, 0f, width, height, backgroundPaint)

        // Draw progress bar
        val progressBarHeight = height * 0.1f
        val progressBarTop = height * 0.8f
        val progressWidth = (progress / maxProgress) * width
        canvas.drawRect(0f, progressBarTop, progressWidth, progressBarTop + progressBarHeight, progressPaint)

        // Draw play/pause button
        val buttonSize = height * 0.3f
        val buttonLeft = centerX - buttonSize / 2
        val buttonTop = centerY - buttonSize / 2
        val buttonRight = centerX + buttonSize / 2
        val buttonBottom = centerY + buttonSize / 2

        if (isPlaying) {
            // Draw pause button (two rectangles)
            val barWidth = buttonSize / 3
            canvas.drawRect(
                buttonLeft,
                buttonTop,
                buttonLeft + barWidth,
                buttonBottom,
                playPausePaint
            )
            canvas.drawRect(
                buttonRight - barWidth,
                buttonTop,
                buttonRight,
                buttonBottom,
                playPausePaint
            )
        } else {
            // Draw play button (triangle)
            val path = android.graphics.Path().apply {
                moveTo(buttonLeft, buttonTop)
                lineTo(buttonRight, centerY)
                lineTo(buttonLeft, buttonBottom)
                close()
            }
            canvas.drawPath(path, playPausePaint)
        }

        // Draw song info text
        val textY = height * 0.3f
        canvas.drawText("Now Playing", centerX, textY, textPaint)
    }

    override fun onMeasure(widthMeasureSpec: Int, heightMeasureSpec: Int) {
        val minWidth = suggestedMinimumWidth + paddingLeft + paddingRight
        val minHeight = suggestedMinimumHeight + paddingTop + paddingBottom

        val width = resolveSizeAndState(minWidth, widthMeasureSpec, 1)
        val height = resolveSizeAndState(minHeight, heightMeasureSpec, 1)

        setMeasuredDimension(width, height)
    }
}
```
