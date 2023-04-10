from textblob import TextBlob
blob=TextBlob('I am Medhansh')
print(blob.translate(from_lang='en',to = 'es'))
print(blob.translate(from_lang='en',to = 'fr'))
print(blob.translate(from_lang='en',to = 'zh'))
print(blob.translate(from_lang='en',to = 'hi'))