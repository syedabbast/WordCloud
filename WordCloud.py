import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
import re
# Load the data from CSV file
df = pd.read_csv('customer_reviews.csv')
# Concatenate all reviews into a single string
text = " ".join(review for review in df['Review'])
# Clean the text data
stopwords = set(stopwords.words('english'))
text = re.sub('[^A-Za-z]+', ' ', text)
words = text.split()
clean_text = [word for word in words if word.lower() not in stopwords]
clean_text = ' '.join(clean_text)
# Generate the word cloud
wc = WordCloud(width=800, height=400, background_color='white').generate(clean_text)
# Display the word cloud using matplotlib
plt.figure(figsize=(12,6))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
