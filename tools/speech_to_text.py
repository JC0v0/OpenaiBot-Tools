import sounddevice as sd
import numpy as np
import wave
from aip import AipSpeech
from config import *


def record_audio(output_filename, duration, sample_rate=16000):
    """
    语音转文字
    """
    print("Recording...")

    audio = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()

    print("Recording finished.")

    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio.tobytes())

    
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    # 读取文件
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    # 识别本地文件
    re=client.asr(get_file_content('recorded_audio.wav'), 'wav', 16000, {'dev_pid': 1537,})
    re1=re['result'][0]
    print(re1)
    
    return re1

