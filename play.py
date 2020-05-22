# 載入其他檔案中的函式
import speech_recognition as sr
from speech import recognize_speech_from_mic
from line import linebot_write
from tty import serial_read, serial_write

# 載入設定檔
from config import CHUNK_SIZE, SAMPLE_RATE

# 無限迴圈
while True:
    # 呼叫 Google speech recognizer
    recognizer = sr.Recognizer()

    # 設定麥克風
    # chunk_size: 越高，麥克風靈敏度越低 
    # sample_rate: 取樣，越高，音質越好，但是辨識速度越慢
    microphone = sr.Microphone(chunk_size = CHUNK_SIZE, sample_rate = SAMPLE_RATE)

    # 告訴 micro:bit 我要開始了
    serial_write("0")

    # 啟用麥克風 -->  聽 --> 思考 --> 把語音轉成文字丟出來
    result = recognize_speech_from_mic(recognizer, microphone)
    
    # 辨識成功
    if result["success"]:
        print("You say: {}".format(result["transcription"]))
        # linebot_write("你說的是： ".format(result["transcription"]))
        serial_write("1")

    # 辨識失敗
    if result["error"]:
        print("ERROR: {}".format(result["error"]))
        serial_write("2")
