from gensim.models import Word2Vec
frases=[["escribir","tutoriales","es","gratificante"],["pero","comer","papas","bravas","es","mucho","mejor"]]
modelo = Word2Vec(frases,min_count=1)
modelo.save("C:/Users/THE_PUNISHER/Documents/gp3.1/nombre_del_modelo")
nuevo_modelo=Word2Vec.load("C:/Users/THE_PUNISHER/Documents/gp3.1/nombre_del_modelo")