# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mosjlpT_xZKdNTXKAqT2T6a_Hi0rQdW9
"""

!pip install nltk
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Descargar el lexicón de VADER
nltk.download('vader_lexicon')

# Crear un analizador de sentimientos
sia = SentimentIntensityAnalyzer()
review = "Este producto es increíble, lo recomiendo mucho."

# Obtener el puntaje de sentimientos
sentiment_score = sia.polarity_scores(review)

# Mostrar los resultados
print(sentiment_score)

# Determinar si la reseña es positiva, negativa o neutral
if sentiment_score['compound'] >= 0.05:
    print("Sentimiento: Positivo")
elif sentiment_score['compound'] <= -0.05:
    print("Sentimiento: Negativo")
else:
    print("Sentimiento: Neutral")