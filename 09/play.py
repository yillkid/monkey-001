import random
# 載入其他檔案中的函式
import speech_recognition as sr
from speech import recognize_speech_from_mic
from line import linebot_write
from chance import list_chance
from fate import list_fate

# 載入設定檔
from config import CHUNK_SIZE, SAMPLE_RATE

balance = 1000
points = 0
while True:
    deposit = 0
    withdrawal = 0
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
        print("You say: {}".format(result["transcription"]))

    # 辨識失敗
    if result["error"]:
        print("ERROR: {}".format(result["error"]))
        continue

    # 擲骰子語音
    if result["transcription"] == "隨機":
        points = random.randint(1, 6)
        print("點數為: " + str((points)))

    # if 機會
    if result["transcription"] == "機會":
        print(list_chance[random.randint(0, 1)])
        
    # if 命運
    if result["transcription"] == "命運":
        print(list_fate[random.randint(0, 1)])

    # if 賺錢
    if "增加" in result["transcription"]:
        list_value = result["transcription"].split("增加")
        deposit = list_value[1]

    # if 扣錢
    if "減少" in result["transcription"]:
        list_value = result["transcription"].split("減少")
        withdrawal = list_value[1]

    balance = balance + int(deposit)
    balance = balance - int(withdrawal)

    print("我的本金剩下: " + str(balance))

    if balance <=0:
        print("你破產了！")

