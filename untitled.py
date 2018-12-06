from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS)

def show_wordcloud(data, color, title = None):
    wordcloud = WordCloud(
        background_color= color,
        stopwords=stopwords,
        max_words=250,
        max_font_size=40, 
        scale=3,
        random_state=0 
).generate(str(data))

    fig = plt.figure(1, figsize=(20, 20))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.show()