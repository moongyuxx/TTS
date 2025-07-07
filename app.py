
# import sounddevice as sd
# print(sd.query_devices())

from tts_speaker import TextToSpeechService

if __name__ == "__main__":
    tts = TextToSpeechService()
    print("✅ 실시간 TTS 준비 완료! 'exit' 입력 시 종료됩니다.")

    while True:
        text = input("💬 말할 문장 입력: ")
        if text.strip().lower() == "exit":
            break
        tts.speak(text)


# # flask_app.py 이후 flask 연동 예시
# from flask import Flask, request
# from tts_speaker import TextToSpeechService

# app = Flask(__name__)
# tts = TextToSpeechService()

# @app.route("/speak", methods=["POST"])
# def speak():
#     text = request.json.get("text", "")
#     if text:
#         tts.speak(text)
#     return {"status": "ok"}

# if __name__ == "__main__":
#     app.run(debug=True)
