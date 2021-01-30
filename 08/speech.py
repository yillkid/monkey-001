import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # Read from serial for listening
    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        try:
            recognizer.adjust_for_ambient_noise(source)
            print("1/3: 我正在聽呢 ... ...")
            recognizer.dynamic_energy_threshold = False
            audio = recognizer.listen(source, timeout = 2.0, phrase_time_limit = 2.0)
            print("我聽完了！")

        except Exception as e:
            response["success"] = False
            response["error"] = e
            return response

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    # update the response object accordingly

    try:
        print("2/3: 我正在思考您說的是什麼 ... ...")
        response["transcription"] = recognizer.recognize_google(audio, language='zh-TW')
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"

    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "我的 Google 語音辨識好像失效了！"

    print("3/3: 我猜完了！")
    
    return response
