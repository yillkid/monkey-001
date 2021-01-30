import random
# 載入其他檔案中的函式
import speech_recognition as sr
from speech import recognize_speech_from_mic
from line import linebot_write

# 載入設定檔
from config import CHUNK_SIZE, SAMPLE_RATE

balance = 1000
points = 0
while True:
    print("本金 " + str(balance))

    # 呼叫 Google speech recognizer
    recognizer = sr.Recognizer()

    # 設定麥克風
    # chunk_size: 越高，麥克風靈敏度越低 
    # sample_rate: 取樣，越高，音質越好，但是辨識速度越慢
    microphone = sr.Microphone(chunk_size = CHUNK_SIZE, sample_rate = SAMPLE_RATE)

    # 啟用麥克風 -->  聽 --> 思考 --> 把語音轉成文字丟出來
    result = recognize_speech_from_mic(recognizer, microphone)

    # 辨識成功
    if result["success"]:
        linebot_write("你說的是： " + str(format(result["transcription"])))
        print("You say: {}".format(result["transcription"]))

    # 辨識失敗
    if result["error"]:
        print("ERROR: {}".format(result["error"]))
        continue

    # 擲骰子語音
    if result["transcription"] == "隨機":
        points = random.randint(1, 6)
        print("點數為: " + str((points)))

    # 到這裡繼續往上迴圈！
    continue


    # if 機會

    # if 命運

    # if 賺錢
    print("需要賺錢嗎?")
    deposit = input()

    # if 扣錢
    print("需要扣錢嗎?")
    withdrawal = input()

    balance = balance + int(deposit)
    balance = balance - int(withdrawal)

    print("我的本金剩下: " + str(balance))

