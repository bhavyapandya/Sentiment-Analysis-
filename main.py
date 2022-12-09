from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import pickle

class Sentiment:
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"

class Review:
    def __init__(self,text,score):
        self.text = text
        self.score =score
        self.sentiment = self.get_sentiment()
    
    def get_sentiment(self):
        if self.score == str(2):
            return Sentiment.POSITIVE
        elif self.score == str(1):
            return Sentiment.NEGATIVE


counter = 0
reviews = []
with open("./data/test.ft.txt/test.txt", encoding="utf8") as f:
    for line in f:
        reviews.append(Review(line[11:],line[9]))
        counter+=1
        if counter>= 30000:
            break

train_x = [x.text for x in reviews]
train_y = [x.sentiment for x in reviews]
X_train, x_test, Y_train, y_test = train_test_split(train_x,train_y,train_size=0.8) 
vectorizer = TfidfVectorizer()

train_x_vector = vectorizer.fit_transform(X_train)
test_x_vector = vectorizer.transform(x_test)
clf = svm.SVC()
clf.fit(train_x_vector,Y_train)

with open("./model/trained_sentiment.pkl","wb") as f:
    pickle.dump(clf,f)



print(clf.score(test_x_vector,y_test))
print(f1_score(y_test,clf.predict(test_x_vector),average=None, labels=[Sentiment.POSITIVE, Sentiment.NEGATIVE]))

for i in range(5):
    test = input("Enter: ")
    transformed = vectorizer.transform([test])
    print(clf.predict(transformed))
