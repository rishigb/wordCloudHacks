''' Inspired by http://sebastianraschka.com/Articles/2014_twitter_wordcloud.html#turn-your-twitter-timeline-into-a-word-cloud-using-python '''
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread

df = pd.read_csv('rishigb_tweets.csv')

# join tweets to a single string
words = ' '.join(df['text'])

#print (words)
twitter_mask = imread('./twitter_mask.png', flatten=True)


# remove URLs, RTs, and twitter handles
no_urls_no_tags = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                                and word !='via'
                            ])

wordcloud = WordCloud(
                      font_path='CabinSketch-Bold.ttf',
                      stopwords=STOPWORDS,
                      background_color='white',
                      width=1800,
                      height=1400,
                      mask = twitter_mask
                     ).generate(no_urls_no_tags)

print(wordcloud)
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('./my_twitter_wordcloud_3.png', dpi=1000)
plt.show()

