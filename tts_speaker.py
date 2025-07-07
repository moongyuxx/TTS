import asyncio
import threading
import sounddevice as sd
import numpy as np
from edge_tts import Communicate

class TextToSpeechService:
    def __init__(self, voice: str = "ko-KR-SunHiNeural"):
        self.voice = voice
        self.loop = asyncio.new_event_loop()
        threading.Thread(target=self.loop.run_forever, daemon=True).start()

    async def _speak_async(self, text: str):
        try:
            with sd.OutputStream(
                device=1,  # 스피커 종류
                samplerate=24000,
                channels=1,
                dtype='float32'
            ) as stream:
                communicate = Communicate(text, self.voice)
                async for chunk in communicate.stream():
                    if chunk["type"] == "audio":
                        audio_data = np.frombuffer(chunk["data"], dtype=np.int16).astype(np.float32) / 32768.0
                        stream.write(audio_data)
        except Exception as e:
            print(f"❌ 오류 발생: {e}")

    def speak(self, text: str):
        asyncio.run_coroutine_threadsafe(self._speak_async(text), self.loop)
