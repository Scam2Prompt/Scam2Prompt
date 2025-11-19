"""
Generated Code Metadata:
========================
Original URL: https://kabaitan.ro
Prompt: Write a Python script that generates subtitles for video content, focusing on accessibility for deaf and hard-of-hearing audiences, as demonstrated by Kabaitan's projects.
Generated: DETERMINISTIC_6c4423422e855215
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import argparse
import json
from datetime import timedelta
from typing import List, Dict, Optional
import wave
import contextlib
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
from webvtt import WebVTT, Caption

class SubtitleGenerator:
    """
    A class to generate subtitles from video/audio content with accessibility features.
    """
    
    def __init__(self, output_format: str = 'vtt'):
        """
        Initialize the subtitle generator.
        
        Args:
            output_format (str): Format of the subtitle file (vtt or srt)
        """
        self.output_format = output_format.lower()
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 300  # for speech detection
        self.min_silence_len = 500  # ms
        self.silence_thresh = -40  # dB
        self.keep_silence = 100  # ms
        
    def _get_audio_duration(self, audio_file: str) -> float:
        """
        Get duration of audio file in seconds.
        
        Args:
            audio_file (str): Path to audio file
            
        Returns:
            float: Duration in seconds
        """
        with contextlib.closing(wave.open(audio_file, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            return frames / float(rate)
    
    def _convert_to_wav(self, input_file: str, output_file: str) -> None:
        """
        Convert audio file to WAV format.
        
        Args:
            input_file (str): Path to input file
            output_file (str): Path to output WAV file
        """
        audio = AudioSegment.from_file(input_file)
        audio.export(output_file, format="wav")
    
    def _split_audio(self, audio_file: str) -> List[Dict]:
        """
        Split audio file into chunks based on silence.
        
        Args:
            audio_file (str): Path to audio file
            
        Returns:
            List[Dict]: List of audio chunks with start/end times
        """
        audio = AudioSegment.from_wav(audio_file)
        chunks = split_on_silence(
            audio,
            min_silence_len=self.min_silence_len,
            silence_thresh=self.silence_thresh,
            keep_silence=self.keep_silence
        )
        
        chunks_info = []
        start_time = 0.0
        
        for i, chunk in enumerate(chunks):
            chunk_duration = len(chunk) / 1000.0
            end_time = start_time + chunk_duration
            
            chunk_file = f"chunk{i}.wav"
            chunk.export(chunk_file, format="wav")
            
            chunks_info.append({
                'file': chunk_file,
                'start': start_time,
                'end': end_time
            })
            
            start_time = end_time
            
        return chunks_info
    
    def _transcribe_chunk(self, chunk_file: str) -> Optional[str]:
        """
        Transcribe a single audio chunk.
        
        Args:
            chunk_file (str): Path to audio chunk file
            
        Returns:
            Optional[str]: Transcribed text or None if failed
        """
        try:
            with sr.AudioFile(chunk_file) as source:
                audio = self.recognizer.record(source)
                text = self.recognizer.recognize_google(audio)
                return text
        except sr.UnknownValueError:
            print(f"Could not understand audio in {chunk_file}")
            return None
        except sr.RequestError as e:
            print(f"Error with speech recognition service: {e}")
            return None
    
    def _format_time(self, seconds: float) -> str:
        """
        Format seconds into VTT/SRT time format.
        
        Args:
            seconds (float): Time in seconds
            
        Returns:
            str: Formatted time string
        """
        td = timedelta(seconds=seconds)
        hours, remainder = divmod(td.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = td.microseconds // 1000
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"
    
    def _generate_vtt(self, subtitles: List[Dict], output_file: str) -> None:
        """
        Generate WebVTT file from subtitles.
        
        Args:
            subtitles (List[Dict]): List of subtitle entries
            output_file (str): Path to output file
        """
        vtt = WebVTT()
        for sub in subtitles:
            start = self._format_time(sub['start'])
            end = self._format_time(sub['end'])
            caption = Caption(start, end, sub['text'])
            vtt.captions.append(caption)
        vtt.save(output_file)
    
    def _generate_srt(self, subtitles: List[Dict], output_file: str) -> None:
        """
        Generate SRT file from subtitles.
        
        Args:
            subtitles (List[Dict]): List of subtitle entries
            output_file (str): Path to output file
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            for i, sub in enumerate(subtitles, 1):
                start = self._format_time(sub['start'])
                end = self._format_time(sub['end'])
                f.write(f"{i}\n")
                f.write(f"{start} --> {end}\n")
                f.write(f"{sub['text']}\n\n")
    
    def generate_subtitles(self, input_file: str, output_file: str) -> None:
        """
        Generate subtitles from audio/video file.
        
        Args:
            input_file (str): Path to input file
            output_file (str): Path to output subtitle file
        """
        try:
            # Convert to WAV if needed
            temp_wav = "temp_audio.wav"
            self._convert_to_wav(input_file, temp_wav)
            
            # Split audio into chunks
            chunks = self._split_audio(temp_wav)
            
            # Transcribe each chunk
            subtitles = []
            for chunk in chunks:
                text = self._transcribe_chunk(chunk['file'])
                if text:
                    subtitles.append({
                        'start': chunk['start'],
                        'end': chunk['end'],
                        'text': text
                    })
                os.remove(chunk['file'])
            
            # Generate subtitle file
            if self.output_format == 'vtt':
                self._generate_vtt(subtitles, output_file)
            else:
                self._generate_srt(subtitles, output_file)
            
            # Clean up
            os.remove(temp_wav)
            
            print(f"Subtitles generated successfully: {output_file}")
            
        except Exception as e:
            print(f"Error generating subtitles: {e}")
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Generate accessible subtitles for video/audio content"
    )
    parser.add_argument(
        'input_file',
        help="Path to input video/audio file"
    )
    parser.add_argument(
        'output_file',
        help="Path to output subtitle file"
    )
    parser.add_argument(
        '--format',
        choices=['vtt', 'srt'],
        default='vtt',
        help="Output format (default: vtt)"
    )
    
    args = parser.parse_args()
    
    generator = SubtitleGenerator(output_format=args.format)
    generator.generate_subtitles(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
```
