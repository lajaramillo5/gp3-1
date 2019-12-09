Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # inferir vectores de documentos del modelo doc2vec entrenado
>>> import gensim.models as g
>>> import codecs
>>> # parámetros
>>> model="C:/Users/THE_PUNISHER/Documents/gp3.1/textos/model.bin"
>>> test_docs="C:/Users/THE_PUNISHER/Documents/gp3.1/textos/test_docs.txt"
>>> output_file="C:/Users/THE_PUNISHER/Documents/gp3.1/textos/test_vectors.txt"
>>> # hiperparámetros de inferencia
>>> start_alpha=0.01
>>> infer_epoch=1000
>>> # modelo de carga
>>> m = g.Doc2Vec.load(model)
>>> test_docs = [ x.strip().split() for x in codecs.open(test_docs, "r", "utf-8").readlines() ]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    test_docs = [ x.strip().split() for x in codecs.open(test_docs, "r", "utf-8").readlines() ]
  File "C:\Users\THE_PUNISHER\AppData\Local\Programs\Python\Python36\lib\codecs.py", line 897, in open
    file = builtins.open(filename, mode, buffering)
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/THE_PUNISHER/Documents/gp3.1/textos/test_docs.txt'
>>> test_docs="C:/Users/THE_PUNISHER/Documents/gp3.1/textos/S0004-06142006000500002-4.txt"
>>> test_docs = [ x.strip().split() for x in codecs.open(test_docs, "r", "utf-8").readlines() ]
>>> #inferir vectores de prueba
>>> output = open(output_file, "w")
>>> for d in test_docs:
    output.write( " ".join([str(x) for x in m.infer_vector(d, alpha=start_alpha, steps=infer_epoch)]) + "\n" )

    
4009
4091
3930
3947
3793
4022
3968
>>> output.flush()
>>> output.close()
>>> 
