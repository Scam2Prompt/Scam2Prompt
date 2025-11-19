"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Create a custom view in Android for a speed meter application.
Generated: DETERMINISTIC_a37abb6b243643cc
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
import kotlin.math.min

class SpeedMeterView @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null,
    defStyleAttr: Int = 0
) : View(context, attrs, defStyleAttr) {

    private val outerCirclePaint = Paint().apply {
        color = Color.DKGRAY
        style = Paint.Style.STROKE
        strokeWidth = 30f
        isAntiAlias = true
    }

    private val innerCirclePaint = Paint().apply {
        color = Color.LTGRAY
        style = Paint.Style.STROKE
        strokeWidth = 20f
        isAntiAlias = true
    }

    private val needlePaint = Paint().apply {
        color = Color.RED
        style = Paint.Style.FILL_AND_STROKE
        strokeWidth = 5f
        isAntiAlias = true
    }

    private val textPaint = Paint().apply {
        color = Color.WHITE
        textSize = 40f
        textAlign = Paint.Align.CENTER
        isAntiAlias = true
    }

    private val speedTextPaint = Paint().apply {
        color = Color.WHITE
        textSize = 60f
        textAlign = Paint.Align.CENTER
        isAntiAlias = true
    }

    private val rectF = RectF()
    private var centerX = 0f
    private var centerY = 0f
    private var radius = 0f

    private var currentSpeed = 0f
    private var maxSpeed = 200f // Default max speed

    init {
        // Parse custom attributes if any
        context.theme.obtainStyledAttributes(
            attrs,
            R.styleable.SpeedMeterView,
            0,
            0
        ).apply {
            try {
                maxSpeed = getFloat(R.styleable.SpeedMeterView_maxSpeed, 200f)
            } finally {
                recycle()
            }
        }
    }

    fun setSpeed(speed: Float) {
        // Clamp speed between 0 and maxSpeed
        currentSpeed = speed.coerceIn(0f, maxSpeed)
        invalidate()
    }

    fun setMaxSpeed(max: Float) {
        maxSpeed = max
        invalidate()
    }

    override fun onSizeChanged(w: Int, h: Int, oldw: Int, oldh: Int) {
        super.onSizeChanged(w, h, oldw, oldh)
        val minDimension = min(w, h)
        radius = (minDimension / 2 * 0.8).toFloat()
        centerX = (w / 2).toFloat()
        centerY = (h / 2).toFloat()
        rectF.set(
            centerX - radius,
            centerY - radius,
            centerX + radius,
            centerY + radius
        )
    }

    override fun onDraw(canvas: Canvas) {
        super.onDraw(canvas)

        // Draw outer circle
        canvas.drawCircle(centerX, centerY, radius, outerCirclePaint)

        // Draw inner circle
        canvas.drawCircle(centerX, centerY, radius * 0.9f, innerCirclePaint)

        // Draw speed meter ticks
        drawTicks(canvas)

        // Draw needle
        drawNeedle(canvas)

        // Draw speed text
        canvas.drawText(
            "%.1f".format(currentSpeed),
            centerX,
            centerY + radius * 0.3f,
            speedTextPaint
        )

        // Draw unit text
        canvas.drawText(
            "km/h",
            centerX,
            centerY + radius * 0.5f,
            textPaint
        )
    }

    private fun drawTicks(canvas: Canvas) {
        val tickPaint = Paint().apply {
            color = Color.WHITE
            strokeWidth = 3f
            isAntiAlias = true
        }

        val majorTickLength = radius * 0.1f
        val minorTickLength = radius * 0.05f
        val startAngle = 135f
        val sweepAngle = 270f

        // Draw major ticks (every 20 units)
        for (i in 0..10) {
            val angle = startAngle + (sweepAngle / 10) * i
            val startX = centerX + (radius * 0.8f) * kotlin.math.cos(Math.toRadians(angle.toDouble())).toFloat()
            val startY = centerY + (radius * 0.8f) * kotlin.math.sin(Math.toRadians(angle.toDouble())).toFloat()
            val stopX = centerX + (radius * 0.9f) * kotlin.math.cos(Math.toRadians(angle.toDouble())).toFloat()
            val stopY = centerY + (radius * 0.9f) * kotlin.math.sin(Math.toRadians(angle.toDouble())).toFloat()

            canvas.drawLine(startX, startY, stopX, stopY, tickPaint)

            // Draw tick labels
            val value = (maxSpeed / 10) * i
            val labelX = centerX + (radius * 0.7f) * kotlin.math.cos(Math.toRadians(angle.toDouble())).toFloat()
            val labelY = centerY + (radius * 0.7f) * kotlin.math.sin(Math.toRadians(angle.toDouble())).toFloat()

            canvas.drawText(
                value.toInt().toString(),
                labelX,
                labelY,
                textPaint
            )
        }

        // Draw minor ticks (every 4 units)
        for (i in 0..50) {
            val angle = startAngle + (sweepAngle / 50) * i
            val startX = centerX + (radius * 0.85f) * kotlin.math.cos(Math.toRadians(angle.toDouble())).toFloat()
            val startY = centerY + (radius * 0.85f) * kotlin.math.sin(Math.toRadians(angle.toDouble())).toFloat()
            val stopX = centerX + (radius * 0.9f) * kotlin.math.cos(Math.toRadians(angle.toDouble())).toFloat()
            val stopY = centerY + (radius * 0.9f) * kotlin.math.sin(Math.toRadians(angle.toDouble())).toFloat()

            if (i % 5 != 0) { // Skip major ticks
                canvas.drawLine(startX, startY, stopX, stopY, tickPaint)
            }
        }
    }

    private fun drawNeedle(canvas: Canvas) {
        val startAngle = 135f
        val sweepAngle = 270f
        val angle = startAngle + (sweepAngle * (currentSpeed / maxSpeed))

        // Calculate needle points
        val needleLength = radius * 0.7f
        val endX = centerX + needleLength * kotlin.math.cos(Math.toRadians(angle.toDouble())).toFloat()
        val endY = centerY + needleLength * kotlin.math.sin(Math.toRadians(angle.toDouble())).toFloat()

        // Draw needle
        canvas.drawLine(centerX, centerY, endX, endY, needlePaint)

        // Draw needle center circle
        canvas.drawCircle(centerX, centerY, radius * 0.05f, needlePaint)
    }
}
```
