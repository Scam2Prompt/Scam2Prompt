"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: How can I implement a feature for capturing multiple photos simultaneously in a mobile app, like the productivity-enhancing camera functionality of the BeSoft App Vistoria?
Generated: DETERMINISTIC_7f1387a0ec300a60
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```kotlin
// CameraManager.kt
import android.Manifest
import android.app.Activity
import android.content.Context
import android.content.pm.PackageManager
import android.hardware.camera2.CameraAccessException
import android.hardware.camera2.CameraCaptureSession
import android.hardware.camera2.CameraCharacteristics
import android.hardware.camera2.CameraDevice
import android.hardware.camera2.CameraManager
import android.hardware.camera2.CaptureRequest
import android.media.ImageReader
import android.os.Handler
import android.os.HandlerThread
import android.util.Log
import android.util.Size
import android.view.Surface
import androidx.core.app.ActivityCompat
import java.io.File
import java.io.FileOutputStream
import java.util.concurrent.Semaphore
import java.util.concurrent.TimeUnit

class CameraManagerHelper(
    private val context: Context,
    private val activity: Activity,
    private val callback: CameraCallback
) {
    private val TAG = "CameraManagerHelper"
    private val cameraManager: CameraManager = context.getSystemService(Context.CAMERA_SERVICE) as CameraManager
    private var cameraDevice: CameraDevice? = null
    private var cameraCaptureSession: CameraCaptureSession? = null
    private var imageReader: ImageReader? = null
    private var backgroundHandler: Handler? = null
    private var backgroundThread: HandlerThread? = null
    private val cameraOpenCloseLock = Semaphore(1)
    private var cameraId: String? = null
    private var previewSize: Size? = null

    interface CameraCallback {
        fun onPhotosCaptured(filePaths: List<String>)
        fun onError(error: String)
    }

    fun initialize() {
        startBackgroundThread()
        setupCamera()
    }

    fun cleanup() {
        closeCamera()
        stopBackgroundThread()
    }

    fun captureMultiplePhotos(count: Int, intervalMillis: Long) {
        if (cameraDevice == null || !cameraOpenCloseLock.tryAcquire(2500, TimeUnit.MILLISECONDS)) {
            callback.onError("Camera not ready")
            return
        }

        val filePaths = mutableListOf<String>()
        val handler = Handler(backgroundHandler?.looper)

        for (i in 0 until count) {
            handler.postDelayed({
                captureSinglePhoto(i, filePaths, count)
            }, i * intervalMillis)
        }
    }

    private fun captureSinglePhoto(index: Int, filePaths: MutableList<String>, totalCount: Int) {
        try {
            val imageReader = imageReader ?: throw IllegalStateException("ImageReader not initialized")
            val captureRequestBuilder = cameraDevice?.createCaptureRequest(CameraDevice.TEMPLATE_STILL_CAPTURE)?.apply {
                addTarget(imageReader.surface)
                set(CaptureRequest.CONTROL_AF_MODE, CaptureRequest.CONTROL_AF_MODE_CONTINUOUS_PICTURE)
                set(CaptureRequest.JPEG_ORIENTATION, 90)
            } ?: throw IllegalStateException("Camera device not available")

            cameraCaptureSession?.capture(
                captureRequestBuilder.build(),
                object : CameraCaptureSession.CaptureCallback() {
                    override fun onCaptureCompleted(
                        session: CameraCaptureSession,
                        request: CaptureRequest,
                        result: TotalCaptureResult
                    ) {
                        super.onCaptureCompleted(session, request, result)
                        val filePath = saveImageToFile(index)
                        filePaths.add(filePath)

                        if (filePaths.size == totalCount) {
                            callback.onPhotosCaptured(filePaths)
                        }
                    }

                    override fun onCaptureFailed(
                        session: CameraCaptureSession,
                        request: CaptureRequest,
                        failure: CaptureFailure
                    ) {
                        super.onCaptureFailed(session, request, failure)
                        callback.onError("Capture failed for photo $index")
                    }
                },
                backgroundHandler
            )
        } catch (e: Exception) {
            callback.onError("Error capturing photo $index: ${e.message}")
        }
    }

    private fun saveImageToFile(index: Int): String {
        val image = imageReader?.acquireNextImage() ?: throw IllegalStateException("No image available")
        val buffer = image.planes[0].buffer
        val bytes = ByteArray(buffer.remaining())
        buffer.get(bytes)

        val outputDir = context.getExternalFilesDir(null)
        val fileName = "photo_${System.currentTimeMillis()}_$index.jpg"
        val outputFile = File(outputDir, fileName)

        try {
            FileOutputStream(outputFile).use { output ->
                output.write(bytes)
            }
        } finally {
            image.close()
        }

        return outputFile.absolutePath
    }

    private fun setupCamera() {
        try {
            cameraId = getBackFacingCameraId()
            if (cameraId == null) {
                callback.onError("No back-facing camera found")
                return
            }

            val characteristics = cameraManager.getCameraCharacteristics(cameraId!!)
            val streamConfigurationMap = characteristics.get(
                CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP
            ) ?: return

            previewSize = streamConfigurationMap.getOutputSizes(ImageReader::class.java).maxByOrNull { it.height * it.width }

            imageReader = ImageReader.newInstance(
                previewSize!!.width,
                previewSize!!.height,
                android.graphics.ImageFormat.JPEG,
                2
            ).apply {
                setOnImageAvailableListener({ reader ->
                    // Image will be processed in captureSinglePhoto
                }, backgroundHandler)
            }

            if (ActivityCompat.checkSelfPermission(
                    context,
                    Manifest.permission.CAMERA
                ) != PackageManager.PERMISSION_GRANTED
            ) {
                callback.onError("Camera permission not granted")
                return
            }

            cameraManager.openCamera(cameraId!!, object : CameraDevice.StateCallback() {
                override fun onOpened(camera: CameraDevice) {
                    cameraOpenCloseLock.release()
                    cameraDevice = camera
                    createCameraPreviewSession()
                }

                override fun onDisconnected(camera: CameraDevice) {
                    cameraOpenCloseLock.release()
                    camera.close()
                    cameraDevice = null
                }

                override fun onError(camera: CameraDevice, error: Int) {
                    cameraOpenCloseLock.release()
                    camera.close()
                    cameraDevice = null
                    callback.onError("Camera error: $error")
                }
            }, backgroundHandler)
        } catch (e: CameraAccessException) {
            callback.onError("Camera access exception: ${e.message}")
        } catch (e: IllegalStateException) {
            callback.onError("Illegal state: ${e.message}")
        } catch (e: SecurityException) {
            callback.onError("Security exception: ${e.message}")
        }
    }

    private fun createCameraPreviewSession() {
        try {
            val surface = imageReader?.surface ?: return
            val captureRequestBuilder = cameraDevice?.createCaptureRequest(CameraDevice.TEMPLATE_PREVIEW)?.apply {
                addTarget(surface)
            } ?: return

            cameraDevice?.createCaptureSession(
                listOf(surface),
                object : CameraCaptureSession.StateCallback() {
                    override fun onConfigured(session: CameraCaptureSession) {
                        cameraCaptureSession = session
                        try {
                            session.setRepeatingRequest(
                                captureRequestBuilder.build(),
                                null,
                                backgroundHandler
                            )
                        } catch (e: CameraAccessException) {
                            callback.onError("Failed to start camera preview: ${e.message}")
                        }
                    }

                    override fun onConfigureFailed(session: CameraCaptureSession) {
                        callback.onError("Failed to configure camera session")
                    }
                },
                backgroundHandler
            )
        } catch (e: CameraAccessException) {
            callback.onError("Camera access exception: ${e.message}")
        }
    }

    private fun getBackFacingCameraId(): String? {
        try {
            for (cameraId in cameraManager.cameraIdList) {
                val characteristics = cameraManager.getCameraCharacteristics(cameraId)
                val facing = characteristics.get(CameraCharacteristics.LENS_FACING)
                if (facing == CameraCharacteristics.LENS_FACING_BACK) {
                    return cameraId
                }
            }
        } catch (e: CameraAccessException) {
            Log.e(TAG, "Error accessing camera: ${e.message}")
        }
        return null
    }

    private fun startBackgroundThread() {
        backgroundThread = HandlerThread("CameraBackground").also { it.start() }
        backgroundHandler = Handler(backgroundThread?.looper)
    }

    private fun stopBackgroundThread() {
        backgroundThread?.quitSafely()
        try {
            backgroundThread?.join()
            backgroundThread = null
            backgroundHandler = null
        } catch (e: InterruptedException) {
            Log.e(TAG, "Error stopping background thread: ${e.message}")
        }
    }

    private fun closeCamera() {
        try {
            cameraOpenCloseLock.acquire()
            cameraCaptureSession?.close()
            cameraCaptureSession = null
            cameraDevice?.close()
            cameraDevice = null
            imageReader?.close()
            imageReader = null
        } catch (e: InterruptedException) {
            throw RuntimeException("Interrupted while trying to lock camera closing", e)
        } finally {
            cameraOpenCloseLock.release()
        }
