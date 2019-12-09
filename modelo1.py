#python example to train doc2vec model 

import gensim.models as g
import logging

# doc2vec parameters
vector_size = 300
window_size = 15
min_count = 1
sampling_threshold = 1e-5
negative_size = 5
train_epoch = 100
dm = 0 #0 = dbow; 1 = dmpv
worker_count = 1 #number of parallel processes

#pretrained word embeddings
pretrained_emb = "C:/Users/THE_PUNISHER/Documents/gp3.1/textos/pretrained_word_embeddings.txt" #None if use without pretrained embeddings

#input corpus
train_corpus = "C:/Users/THE_PUNISHER/Documents/gp3.1/textos/train_docs.txt"

#output model
saved_path = "C:/Users/THE_PUNISHER/Documents/gp3.1/textos/model1.bin"

#enable logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#train doc2vec model
docs = g.doc2vec.TaggedLineDocument(train_corpus)
model = g.Doc2Vec(docs, size=vector_size, window=window_size, min_count=min_count, sample=sampling_threshold, workers=worker_count, hs=0, dm=dm, negative=negative_size, dbow_words=1, dm_concat=1, pretrained_emb=pretrained_emb, iter=train_epoch)

#save model
model.save(saved_path)