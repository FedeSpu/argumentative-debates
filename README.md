# Come aprire il file su colab e fare i commit:
## Aprire il file su colab
Andare sul sito di [Colab](https://colab.research.google.com/?utm_source=scs-index) e selezionare la casella GitHub. 
Inserire le proprie credenziali e spuntare "Includi repository privati".  
Selezionare poi il repository e il ramo (che corrisponde alla branch su cui lavorare)

## Salvare il file su GitHub con commit:
Su Colab selezionare File -> Save a copy in GitHub e selezionare la branch corretta (se non si sta lavorando su main). Cambiare il "commit message" e premere OK

# Struttura base
1. Scaricare dataset (kialo, reddit, twitter)
   - scaricare impatto
2. Pre-processing dataset
3. Model
   - Regressione, dato intervento, predirre impatto 
   - Classificazione, dato intervento, maggior votazione

## Estensioni
3. - Attention a livello di commento, sopra e sotto, intero ramo...
   - tree-lstm
   - svm
   - graph nn

# Link utili
- https://towardsdatascience.com/predicting-reddit-comment-karma-a8f570b544fc
- https://docs.dgl.ai/en/0.6.x/tutorials/models/2_small_graph/3_tree-lstm.html
- https://arxiv.org/pdf/1901.00066.pdf
- https://www.researchgate.net/publication/309039730_Prediction_of_Rating_from_Comments_based_on_Information_Retrieval_and_Sentiment_Analysis
