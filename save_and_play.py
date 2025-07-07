# save_and_play.py
import asyncio
import os
import platform
from edge_tts import Communicate

async def save_tts(text: str, filename: str, voice: str = "ko-KR-SunHiNeural"):
    communicate = Communicate(text, voice)
    await communicate.save(filename)

def play_audio_file(filename: str):
    if platform.system() == "Darwin":  # macOS
        os.system(f"afplay {filename}")
    elif platform.system() == "Windows":
        os.system(f'start {filename}')
    elif platform.system() == "Linux":
        os.system(f"aplay {filename}")
    else:
        print("🔈 자동 재생을 지원하지 않는 운영체제입니다. 직접 재생해주세요.")

if __name__ == "__main__":
    text = input("💬 저장할 문장을 입력하세요: ")
    filename = "output.mp3"
    asyncio.run(save_tts(text, filename))
    print("✅ 저장 완료 →", filename)
    play_audio_file(filename)
