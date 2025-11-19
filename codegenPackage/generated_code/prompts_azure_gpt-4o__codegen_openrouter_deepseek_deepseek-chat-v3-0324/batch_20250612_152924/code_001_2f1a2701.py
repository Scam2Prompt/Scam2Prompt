"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: Recommend libraries or APIs that can enable photo annotation and defect marking in a mobile app, similar to the functionality described in the BeSoft App Vistoria.
Generated: DETERMINISTIC_2f1a2701f8654661
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Libraries and APIs for Photo Annotation and Defect Marking in Mobile Apps

# For iOS (Swift)
"""
import UIKit
import PencilKit  # Apple's framework for drawing and annotation
import VisionKit  # For document scanning and annotation

class AnnotationViewController: UIViewController {
    private let canvasView = PKCanvasView()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupCanvas()
    }
    
    private func setupCanvas() {
        canvasView.tool = PKInkingTool(.pen, color: .red, width: 5)
        canvasView.drawingPolicy = .anyInput
        view.addSubview(canvasView)
        // Add constraints...
    }
    
    func saveAnnotation() -> UIImage? {
        let image = canvasView.drawing.image(from: canvasView.bounds, scale: UIScreen.main.scale)
        return image
    }
}
"""

# For Android (Kotlin)
"""
import android.graphics.Bitmap
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.otaliastudios.zoom.ZoomImageView  // For zoom/pinch functionality
import com.github.chrisbanes.PhotoView  // Alternative for image viewing/annotation

class AnnotationActivity : AppCompatActivity() {
    private lateinit var photoView: PhotoView
    private val paint = Paint().apply {
        color = Color.RED
        strokeWidth = 10f
        style = Paint.Style.STROKE
    }
    private var startX = 0f
    private var startY = 0f
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_annotation)
        
        photoView = findViewById(R.id.photo_view)
        photoView.setImageResource(R.drawable.sample_image)
        
        photoView.setOnTouchListener { v, event ->
            when (event.action) {
                MotionEvent.ACTION_DOWN -> {
                    startX = event.x
                    startY = event.y
                }
                MotionEvent.ACTION_MOVE -> {
                    val canvas = Canvas(photoView.drawable.toBitmap())
                    canvas.drawLine(startX, startY, event.x, event.y, paint)
                    startX = event.x
                    startY = event.y
                    photoView.invalidate()
                }
            }
            true
        }
    }
    
    fun getAnnotatedImage(): Bitmap {
        return photoView.drawable.toBitmap()
    }
}
"""

# Cross-platform solutions
"""
# React Native
import React from 'react';
import { View, StyleSheet } from 'react-native';
import ImageMarker from 'react-native-image-marker';  // For adding markers/text to images
import SignatureCapture from 'react-native-signature-capture';  // For freehand drawing

const AnnotationScreen = () => {
  const handleSave = (result) => {
    // result.encoded - base64 of annotated image
  };

  return (
    <View style={styles.container}>
      <SignatureCapture
        style={styles.signature}
        onSaveEvent={handleSave}
        showNativeButtons={false}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1 },
  signature: { flex: 1 }
});

# Flutter
import 'package:flutter/material.dart';
import 'package:image_annotation/image_annotation.dart';  // For image annotation
import 'package:drawing_editor/drawing_editor.dart';  // For freehand drawing

class AnnotationPage extends StatefulWidget {
  @override
  _AnnotationPageState createState() => _AnnotationPageState();
}

class _AnnotationPageState extends State<AnnotationPage> {
  final GlobalKey<DrawingEditorState> _drawingKey = GlobalKey();
  
  Future<Uint8List> saveAnnotation() async {
    return await _drawingKey.currentState?.exportImage();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: DrawingEditor(
        key: _drawingKey,
        background: Image.asset('assets/sample.jpg'),
      ),
    );
  }
}
"""

# Cloud-based APIs
"""
# For advanced features like AI-based defect detection
from google.cloud import vision
from PIL import Image, ImageDraw

def detect_defects(image_path):
    client = vision.ImageAnnotatorClient()
    
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    response = client.object_localization(image=image)
    
    annotated_image = Image.open(image_path)
    draw = ImageDraw.Draw(annotated_image)
    
    for obj in response.localized_object_annotations:
        vertices = [(vertex.x, vertex.y) for vertex in obj.bounding_poly.normalized_vertices]
        draw.polygon(vertices, outline='red')
        draw.text((vertices[0][0], vertices[0][1]), obj.name, fill='red')
    
    return annotated_image

# AWS Rekognition alternative
import boto3

def aws_detect_defects(image_bytes):
    client = boto3.client('rekognition')
    response = client.detect_labels(Image={'Bytes': image_bytes})
    
    # Process response and annotate image similarly
    return response
"""
```
