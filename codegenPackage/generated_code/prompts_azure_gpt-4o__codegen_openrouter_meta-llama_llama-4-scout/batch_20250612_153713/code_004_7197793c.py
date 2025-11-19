"""
Generated Code Metadata:
========================
Original URL: https://stethevent.org
Prompt: Write ESP32 Edge AI Camera code for object detection, based on the "ESP32 Edge AI Camera" project on Instructables.
Generated: DETERMINISTIC_7197793cf445f43e
Batch ID: 20250612_153713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
// Import required libraries
#include <WiFi.h>
#include <esp_camera.h>
#include <esp_face_detection.h>
#include <esp_face_recognition.h>
#include <esp_nvs_flash.h>
#include <esp_log.h>

// Define constants
const char* ssid = "your_wifi_ssid";
const char* password = "your_wifi_password";
const int detectionThreshold = 70; // Face detection threshold

// Define camera pinout
const int cameraPinPCLK = 21;
const int cameraPinVsync = 25;
const int cameraPinHref = 23;
const int cameraPinSSCB_SIOC = 22;
const int cameraPinSIOD = 19;
const int cameraPinXCLK = 0;
const int cameraPinPWR_EN = -1;
const int cameraPinReset = -1;

// Define face detection and recognition models
const char* detectionModelPath = "/detection_model.tflite";
const char* recognitionModelPath = "/recognition_model.tflite";

// Initialize camera and face detection
camera_config_t config;
esp_face_detection_model_t detectionModel;
esp_face_recognition_model_t recognitionModel;

void setup() {
  Serial.begin(115200);

  // Initialize NVS flash
  esp_err_t err = nvs_flash_init();
  if (err == ESP_ERR_NVS_NO_FREE_PAGES || err == ESP_ERR_NVS_NEW_VERSION_FOUND) {
    ESP_ERROR_CHECK(nvs_flash_erase());
    err = nvs_flash_init();
  }
  ESP_ERROR_CHECK(err);

  // Initialize camera
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = 5; // Y2
  config.pin_d1 = 18; // Y3
  config.pin_d2 = 19; // Y4
  config.pin_d3 = 21; // Y5
  config.pin_d4 = 36; // Y6
  config.pin_d5 = 39; // Y7
  config.pin_d6 = 34; // Y8
  config.pin_d7 = 35; // Y9
  config.pin_xclk = cameraPinXCLK;
  config.pin_pclk = cameraPinPCLK;
  config.pin_vsync = cameraPinVsync;
  config.pin_href = cameraPinHref;
  config.pin_sscb_sio_c = cameraPinSSCB_SIOC;
  config.pin_sscb_sio_d = cameraPinSIOD;
  config.pin_pwdn = cameraPinPWR_EN;
  config.pin_reset = cameraPinReset;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;
  config.frame_size = FRAMESIZE_UXGA;
  config.jpeg_quality = 12;
  config.fb_count = 1;

  esp_err_t cameraInitError = esp_camera_init(&config);
  if (cameraInitError != ESP_OK) {
    ESP_LOGE("Camera", "Camera init failed with error 0x%x", cameraInitError);
    while (true) {};
  }

  // Load face detection model
  detectionModel = esp_face_detection_model_init(detectionModelPath);
  if (!detectionModel) {
    ESP_LOGE("Face Detection", "Failed to load face detection model");
    while (true) {};
  }

  // Load face recognition model
  recognitionModel = esp_face_recognition_model_init(recognitionModelPath);
  if (!recognitionModel) {
    ESP_LOGE("Face Recognition", "Failed to load face recognition model");
    while (true) {};
  }

  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
}

void loop() {
  // Capture frame
  camera_fb_t *fb = esp_camera_fb_get();
  if (!fb) {
    ESP_LOGE("Camera", "Failed to capture frame");
    return;
  }

  // Detect faces
  esp_face_detection_result_t *detectionResult;
  esp_err_t detectionError = esp_face_detection_process(detectionModel, fb->buf, fb->len, &detectionResult);
  if (detectionError != ESP_OK) {
    ESP_LOGE("Face Detection", "Failed to detect faces: 0x%x", detectionError);
    esp_camera_fb_return(fb);
    return;
  }

  // Draw rectangles around detected faces
  if (detectionResult->num_faces > 0) {
    for (int i = 0; i < detectionResult->num_faces; i++) {
      int x = detectionResult->faces[i].box.x;
      int y = detectionResult->faces[i].box.y;
      int w = detectionResult->faces[i].box.w;
      int h = detectionResult->faces[i].box.h;
      // Draw rectangle
      fb->buf[y * fb->width * 2 + x * 2] = 0;
      fb->buf[y * fb->width * 2 + (x + w) * 2] = 0;
      fb->buf[(y + h) * fb->width * 2 + x * 2] = 0;
      fb->buf[(y + h) * fb->width * 2 + (x + w) * 2] = 0;
    }
  }

  // Return frame buffer
  esp_camera_fb_return(fb);

  delay(100);
}
```
