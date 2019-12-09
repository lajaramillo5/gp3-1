#python example to infer document vectors from trained doc2vec model
import gensim.models as g
import codecs

#parameters
model = "C:/Users/THE_PUNISHER/Documents/gp3.1/textos/model1.bin"
test_docs = "C:/Users/THE_PUNISHER/Documents/gp3.1/textos/test_docs.txt"
output_file = "C:/Users/THE_PUNISHER/Documents/gp3.1/textos/test_vectors1.txt"

#inference hyper-parameters
start_alpha = 0.01
infer_epoch = 1000

#load model
m = g.Doc2Vec.load(model)
test_docs = [ x.strip().split() for x in codecs.open(test_docs, "r", "utf-8").readlines() ]

#infer test vectors
output = open(output_file, "w")
for d in test_docs:
    output.write( " ".join([str(x) for x in m.infer_vector(d, alpha=start_alpha, steps=infer_epoch)]) + "\n" )
output.flush()
output.close()