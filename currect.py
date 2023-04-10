from textblob import TextBlob
d=(input("Enter a statement, we will correct the gramaticle mistakes"))
b=TextBlob(d)
print(b.correct())