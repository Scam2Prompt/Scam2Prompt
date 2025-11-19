"""
Generated Code Metadata:
========================
Original URL: https://votex.sbs
Prompt: Design an AI-powered animation production tool, similar to Cheehoo's platform, and describe its architecture and potential applications.
Generated: DETERMINISTIC_e3c7fb651415aae0
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# AI Animation Production Tool
# Architecture and Implementation

import os
import json
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import cv2
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from diffusers import StableDiffusionPipeline
from typing import List, Dict, Optional, Tuple

# Configuration
class Config:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.frame_size = (512, 512)
        self.max_frames = 300
        self.animation_fps = 24
        self.model_paths = {
            "text_generation": "gpt2-medium",
            "image_generation": "stabilityai/stable-diffusion-2-1",
            "motion_prediction": "pretrained_motion_model.pth"
        }
        self.cache_dir = "./cache"
        self.output_dir = "./output"
        
        # Create directories if they don't exist
        os.makedirs(self.cache_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)

# Core Animation Generator
class AnimationGenerator:
    def __init__(self, config: Config):
        self.config = config
        self.text_model = self._load_text_model()
        self.image_model = self._load_image_model()
        self.motion_model = self._load_motion_model()
        
    def _load_text_model(self) -> Tuple[GPT2LMHeadModel, GPT2Tokenizer]:
        """Load text generation model and tokenizer"""
        tokenizer = GPT2Tokenizer.from_pretrained(
            self.config.model_paths["text_generation"]
        )
        model = GPT2LMHeadModel.from_pretrained(
            self.config.model_paths["text_generation"]
        ).to(self.config.device)
        return model, tokenizer
    
    def _load_image_model(self) -> StableDiffusionPipeline:
        """Load image generation model"""
        return StableDiffusionPipeline.from_pretrained(
            self.config.model_paths["image_generation"],
            torch_dtype=torch.float16 if self.config.device == "cuda" else torch.float32
        ).to(self.config.device)
    
    def _load_motion_model(self) -> nn.Module:
        """Load motion prediction model"""
        model = MotionPredictionModel().to(self.config.device)
        model.load_state_dict(torch.load(
            self.config.model_paths["motion_prediction"],
            map_location=self.config.device
        ))
        model.eval()
        return model
    
    def generate_storyboard(self, prompt: str, max_length: int = 500) -> str:
        """Generate animation storyboard from text prompt"""
        try:
            inputs = self.text_model[1](prompt, return_tensors="pt").to(self.config.device)
            outputs = self.text_model[0].generate(
                **inputs,
                max_length=max_length,
                num_return_sequences=1,
                pad_token_id=self.text_model[1].eos_token_id
            )
            return self.text_model[1].decode(outputs[0], skip_special_tokens=True)
        except Exception as e:
            raise RuntimeError(f"Failed to generate storyboard: {str(e)}")
    
    def generate_key_frames(self, storyboard: str, num_frames: int = 5) -> List[Image.Image]:
        """Generate key frames from storyboard"""
        try:
            frames = []
            for i in range(num_frames):
                frame_prompt = f"{storyboard} - Frame {i+1}/{num_frames}"
                image = self.image_model(frame_prompt).images[0]
                frames.append(image)
            return frames
        except Exception as e:
            raise RuntimeError(f"Failed to generate key frames: {str(e)}")
    
    def interpolate_frames(self, key_frames: List[Image.Image], total_frames: int) -> List[np.ndarray]:
        """Interpolate between key frames to create smooth animation"""
        try:
            if len(key_frames) < 2:
                raise ValueError("At least 2 key frames required for interpolation")
            
            # Convert PIL Images to numpy arrays
            key_arrays = [np.array(frame) for frame in key_frames]
            
            # Calculate number of interpolated frames between each key frame
            frames_per_segment = total_frames // (len(key_frames) - 1)
            
            interpolated_frames = []
            for i in range(len(key_frames) - 1):
                start_frame = key_arrays[i]
                end_frame = key_arrays[i + 1]
                
                # Use motion model to predict intermediate frames
                with torch.no_grad():
                    start_tensor = torch.from_numpy(start_frame).float().to(self.config.device)
                    end_tensor = torch.from_numpy(end_frame).float().to(self.config.device)
                    
                    for j in range(frames_per_segment):
                        alpha = j / frames_per_segment
                        interpolated = self.motion_model(start_tensor, end_tensor, alpha)
                        interpolated_frames.append(interpolated.cpu().numpy())
            
            return interpolated_frames
        except Exception as e:
            raise RuntimeError(f"Failed to interpolate frames: {str(e)}")
    
    def save_animation(self, frames: List[np.ndarray], output_path: str) -> None:
        """Save animation as video file"""
        try:
            height, width, _ = frames[0].shape
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            video = cv2.VideoWriter(
                output_path,
                fourcc,
                self.config.animation_fps,
                (width, height)
            )
            
            for frame in frames:
                video.write(cv2.cvtColor(frame.astype('uint8'), cv2.COLOR_RGB2BGR))
            
            video.release()
        except Exception as e:
            raise RuntimeError(f"Failed to save animation: {str(e)}")

# Motion Prediction Model Architecture
class MotionPredictionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(256, 512, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        
        self.motion_estimator = nn.Sequential(
            nn.Linear(512 * 16 * 16 * 2, 1024),
            nn.ReLU(),
            nn.Linear(1024, 512 * 16 * 16),
            nn.ReLU()
        )
        
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(512, 256, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(256, 128, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.Conv2d(128, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 3, kernel_size=3, padding=1),
            nn.Sigmoid()
        )
    
    def forward(self, frame1: torch.Tensor, frame2: torch.Tensor, alpha: float) -> torch.Tensor:
        """Predict intermediate frame between two frames"""
        # Normalize frames
        frame1 = frame1.permute(2, 0, 1).unsqueeze(0) / 255.0
        frame2 = frame2.permute(2, 0, 1).unsqueeze(0) / 255.0
        
        # Encode both frames
        enc1 = self.encoder(frame1)
        enc2 = self.encoder(frame2)
        
        # Flatten encodings
        enc1_flat = enc1.view(enc1.size(0), -1)
        enc2_flat = enc2.view(enc2.size(0), -1)
        
        # Concatenate encodings
        combined = torch.cat([enc1_flat, enc2_flat], dim=1)
        
        # Estimate motion
        motion = self.motion_estimator(combined)
        motion = motion.view(-1, 512, 16, 16)
        
        # Interpolate
        interpolated = (1 - alpha) * enc1 + alpha * motion
        
        # Decode
        output = self.decoder(interpolated)
        output = output.squeeze(0).permute(1,
