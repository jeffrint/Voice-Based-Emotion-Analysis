from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Clearing background noice...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Waiting for your message...")
    recordedaudio = recognizer.listen(source)
    print("Done recording...")


try:
    print("printing the message...")
    text= recognizer.recognize_google(recordedaudio,language ='en-US')
    print('your message:{}'. format(text))
except Exception as ex:
    print(ex)


#sentiment analysis
# lst =[]

Sentence = [str(text)]
analyser = SentimentIntensityAnalyzer()
for i in Sentence:
    v = analyser.polarity_scores(i)
    
    # lst.append(v["neg"])
    # lst.append(v["neu"])
    # lst.append(v["pos"])

    if (( v["neg"] > v["neu"]) and ( v["neg"] > v["pos"])) :
        print("Negative!!!...")
    elif (( v["neg"] > v["neu"]) and ( v["neg"] < v["pos"])) :
        print("Positive!!!...")
    elif (( v["neg"] < v["neu"]) and ( v["neg"] > v["pos"])) :
        print("Neutral!!!...")
    elif (( v["neg"] < v["neu"]) and ( v["neg"] < v["pos"])) :
        if (v["neu"]) < (v["pos"]):
            print("Positive!!!...")
        else:
            print("Neutral!!!...")
        

    elif (( v["neu"] > v["neg"]) and ( v["neu"] > v["pos"])) :
        print("Neutral!!!...")
    elif (( v["neu"] > v["neg"]) and ( v["neu"] < v["pos"])) :
        print("Positive!!!...")
    elif (( v["neu"] < v["neg"]) and ( v["neu"] > v["pos"])) :
        print("Negative!!!...")
    elif (( v["neu"] < v["neg"]) and ( v["neu"] < v["pos"])) :
        if (v["neg"]) < (v["pos"]):
            print("Positive!!!...")
        else:
            print("Negative!!!...")
    

    elif (( v["pos"] > v["neg"]) and ( v["pos"] > v["neu"])) :
        print("Positive!!!...")
    elif (( v["pos"] > v["neg"]) and ( v["pos"] < v["neu"])) :
        print("Neutral!!!...")
    elif (( v["pos"] < v["neg"]) and ( v["pos"] > v["neu"])) :
        print("Negative!!!...")
    elif (( v["pos"] < v["neg"]) and ( v["pos"] < v["neu"])) :
        if (v["neg"]) < (v["neu"]):
            print("Neutral!!!...")
        else:
            print("Negative!!!...")


