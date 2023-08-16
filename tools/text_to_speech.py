from aip import AipSpeech
import pygame
import io
from config import *

def play_generated_audio(text):
    """
    文字转语音，并且自动播放语音
    """
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.synthesis(text, 'zh', 1, {
        'vol': 5,
    })

    if not isinstance(result, dict):
        # Create an in-memory stream for the generated MP3
        mp3_stream = io.BytesIO(result)

        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Load the MP3 stream
        pygame.mixer.music.load(mp3_stream)
        
        # Play the MP3
        pygame.mixer.music.play()
        
        # Wait until the music finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Adjust the ticks as needed
