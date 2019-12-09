Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import gensim.models as g


>>> import logging
>>> # doc2vec parámetros
>>> vector_size=300
>>> window_size = 15
>>> min_count = 1
>>> sampling_threshold = 1e-5
>>> negative_size = 5
>>> train_epoch = 100
>>> dm = 0
>>> worker_count = 1 # número de procesos paralelos
>>> # incrustaciones de palabras preparadas
>>> pretrained_emb = "C:/Users/THE_PUNISHER/Documents/gp3.1/textos/S0004-06142005000900014-1.txt"
>>> # corpus de entrada
>>> train_corpus = "C:/Users/THE_PUNISHER/Documents/gp3.1/textos/S0004-06142006000500002-4.txt"
>>> # modelo de salida
>>> saved_path = "C:/Users/THE_PUNISHER/Documents/gp3.1/textos/model.bin"
>>> #habilitar el registro
>>> logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
>>> #train doc2vec model
>>> docs = g.doc2vec.TaggedLineDocument(train_corpus)
>>> model = g.Doc2Vec(docs, size=vector_size, window=window_size, min_count=min_count, sample=sampling_threshold, workers=worker_count, hs=0, dm=dm, negative=negative_size, dbow_words=1, dm_concat=1, pretrained_emb=pretrained_emb, iter=train_epoch)

Warning (from warnings module):
  File "C:\Users\THE_PUNISHER\AppData\Local\Programs\Python\Python36\lib\site-packages\gensim\models\doc2vec.py", line 570
    warnings.warn("The parameter `iter` is deprecated, will be removed in 4.0.0, use `epochs` instead.")
UserWarning: The parameter `iter` is deprecated, will be removed in 4.0.0, use `epochs` instead.

Warning (from warnings module):
  File "C:\Users\THE_PUNISHER\AppData\Local\Programs\Python\Python36\lib\site-packages\gensim\models\doc2vec.py", line 574
    warnings.warn("The parameter `size` is deprecated, will be removed in 4.0.0, use `vector_size` instead.")
UserWarning: The parameter `size` is deprecated, will be removed in 4.0.0, use `vector_size` instead.
2019-11-15 18:56:17,878 : INFO : collecting all words and their counts
2019-11-15 18:56:17,882 : INFO : PROGRESS: at example #0, processed 0 words (0/s), 0 word types, 0 tags
2019-11-15 18:56:17,886 : INFO : collected 207 word types and 7 unique tags from a corpus of 7 examples and 334 words
2019-11-15 18:56:17,889 : INFO : Loading a fresh vocabulary
2019-11-15 18:56:17,905 : INFO : effective_min_count=1 retains 207 unique words (100% of original 207, drops 0)
2019-11-15 18:56:17,917 : INFO : effective_min_count=1 leaves 334 word corpus (100% of original 334, drops 0)
2019-11-15 18:56:17,929 : INFO : deleting the raw counts dictionary of 207 items
2019-11-15 18:56:17,943 : INFO : sample=1e-05 downsamples 207 most-common words
2019-11-15 18:56:17,951 : INFO : downsampling leaves estimated 14 word corpus (4.4% of prior 334)
2019-11-15 18:56:17,960 : INFO : estimated required memory for 207 words and 300 dimensions: 608700 bytes
2019-11-15 18:56:17,975 : INFO : resetting layer weights
2019-11-15 18:56:18,087 : INFO : training model with 1 workers on 208 vocabulary and 300 features, using sg=1 hs=0 sample=1e-05 negative=5 window=15
2019-11-15 18:56:18,126 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,151 : INFO : EPOCH - 1 : training on 334 raw words (21 effective words) took 0.1s, 407 effective words/s
2019-11-15 18:56:18,162 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,171 : INFO : EPOCH - 2 : training on 334 raw words (27 effective words) took 0.0s, 2567 effective words/s
2019-11-15 18:56:18,191 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,202 : INFO : EPOCH - 3 : training on 334 raw words (24 effective words) took 0.0s, 1785 effective words/s
2019-11-15 18:56:18,227 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,234 : INFO : EPOCH - 4 : training on 334 raw words (29 effective words) took 0.0s, 2873 effective words/s
2019-11-15 18:56:18,245 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,256 : INFO : EPOCH - 5 : training on 334 raw words (23 effective words) took 0.0s, 1608 effective words/s
2019-11-15 18:56:18,270 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,277 : INFO : EPOCH - 6 : training on 334 raw words (18 effective words) took 0.0s, 2195 effective words/s
2019-11-15 18:56:18,309 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,319 : INFO : EPOCH - 7 : training on 334 raw words (24 effective words) took 0.0s, 1948 effective words/s
2019-11-15 18:56:18,329 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,346 : INFO : EPOCH - 8 : training on 334 raw words (20 effective words) took 0.0s, 1064 effective words/s
2019-11-15 18:56:18,357 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,368 : INFO : EPOCH - 9 : training on 334 raw words (23 effective words) took 0.0s, 1774 effective words/s
2019-11-15 18:56:18,383 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,390 : INFO : EPOCH - 10 : training on 334 raw words (25 effective words) took 0.0s, 2596 effective words/s
2019-11-15 18:56:18,408 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,422 : INFO : EPOCH - 11 : training on 334 raw words (24 effective words) took 0.0s, 1335 effective words/s
2019-11-15 18:56:18,438 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,443 : INFO : EPOCH - 12 : training on 334 raw words (21 effective words) took 0.0s, 2397 effective words/s
2019-11-15 18:56:18,467 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,474 : INFO : EPOCH - 13 : training on 334 raw words (18 effective words) took 0.0s, 2215 effective words/s
2019-11-15 18:56:18,493 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,503 : INFO : EPOCH - 14 : training on 334 raw words (25 effective words) took 0.0s, 1715 effective words/s
2019-11-15 18:56:18,512 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,529 : INFO : EPOCH - 15 : training on 334 raw words (29 effective words) took 0.0s, 1585 effective words/s
2019-11-15 18:56:18,540 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,551 : INFO : EPOCH - 16 : training on 334 raw words (20 effective words) took 0.0s, 1637 effective words/s
2019-11-15 18:56:18,571 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,578 : INFO : EPOCH - 17 : training on 334 raw words (18 effective words) took 0.0s, 2194 effective words/s
2019-11-15 18:56:18,590 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,607 : INFO : EPOCH - 18 : training on 334 raw words (21 effective words) took 0.0s, 1102 effective words/s
2019-11-15 18:56:18,620 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,628 : INFO : EPOCH - 19 : training on 334 raw words (22 effective words) took 0.0s, 2253 effective words/s
2019-11-15 18:56:18,648 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,655 : INFO : EPOCH - 20 : training on 334 raw words (23 effective words) took 0.0s, 2263 effective words/s
2019-11-15 18:56:18,670 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,684 : INFO : EPOCH - 21 : training on 334 raw words (18 effective words) took 0.0s, 921 effective words/s
2019-11-15 18:56:18,693 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,704 : INFO : EPOCH - 22 : training on 334 raw words (30 effective words) took 0.0s, 2455 effective words/s
2019-11-15 18:56:18,716 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,723 : INFO : EPOCH - 23 : training on 334 raw words (23 effective words) took 0.0s, 2388 effective words/s
2019-11-15 18:56:18,735 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,759 : INFO : EPOCH - 24 : training on 334 raw words (16 effective words) took 0.0s, 589 effective words/s
2019-11-15 18:56:18,774 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,787 : INFO : EPOCH - 25 : training on 334 raw words (23 effective words) took 0.0s, 1489 effective words/s
2019-11-15 18:56:18,804 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,810 : INFO : EPOCH - 26 : training on 334 raw words (19 effective words) took 0.0s, 2357 effective words/s
2019-11-15 18:56:18,825 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,833 : INFO : EPOCH - 27 : training on 334 raw words (24 effective words) took 0.0s, 2450 effective words/s
2019-11-15 18:56:18,843 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,859 : INFO : EPOCH - 28 : training on 334 raw words (18 effective words) took 0.0s, 1020 effective words/s
2019-11-15 18:56:18,873 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,885 : INFO : EPOCH - 29 : training on 334 raw words (18 effective words) took 0.0s, 1347 effective words/s
2019-11-15 18:56:18,917 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,928 : INFO : EPOCH - 30 : training on 334 raw words (29 effective words) took 0.0s, 2044 effective words/s
2019-11-15 18:56:18,939 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,957 : INFO : EPOCH - 31 : training on 334 raw words (20 effective words) took 0.0s, 1011 effective words/s
2019-11-15 18:56:18,971 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:18,979 : INFO : EPOCH - 32 : training on 334 raw words (21 effective words) took 0.0s, 2098 effective words/s
2019-11-15 18:56:18,995 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,008 : INFO : EPOCH - 33 : training on 334 raw words (19 effective words) took 0.0s, 1262 effective words/s
2019-11-15 18:56:19,021 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,028 : INFO : EPOCH - 34 : training on 334 raw words (25 effective words) took 0.0s, 3093 effective words/s
2019-11-15 18:56:19,052 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,058 : INFO : EPOCH - 35 : training on 334 raw words (26 effective words) took 0.0s, 3173 effective words/s
2019-11-15 18:56:19,076 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,086 : INFO : EPOCH - 36 : training on 334 raw words (24 effective words) took 0.0s, 1531 effective words/s
2019-11-15 18:56:19,095 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,109 : INFO : EPOCH - 37 : training on 334 raw words (22 effective words) took 0.0s, 1433 effective words/s
2019-11-15 18:56:19,120 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,127 : INFO : EPOCH - 38 : training on 334 raw words (22 effective words) took 0.0s, 2595 effective words/s
2019-11-15 18:56:19,143 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,156 : INFO : EPOCH - 39 : training on 334 raw words (19 effective words) took 0.0s, 1266 effective words/s
2019-11-15 18:56:19,170 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,177 : INFO : EPOCH - 40 : training on 334 raw words (23 effective words) took 0.0s, 2801 effective words/s
2019-11-15 18:56:19,201 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,208 : INFO : EPOCH - 41 : training on 334 raw words (23 effective words) took 0.0s, 2719 effective words/s
2019-11-15 18:56:19,230 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,238 : INFO : EPOCH - 42 : training on 334 raw words (20 effective words) took 0.0s, 1788 effective words/s
2019-11-15 18:56:19,249 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,269 : INFO : EPOCH - 43 : training on 334 raw words (23 effective words) took 0.0s, 1004 effective words/s
2019-11-15 18:56:19,293 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,304 : INFO : EPOCH - 44 : training on 334 raw words (24 effective words) took 0.0s, 1319 effective words/s
2019-11-15 18:56:19,315 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,322 : INFO : EPOCH - 45 : training on 334 raw words (25 effective words) took 0.0s, 2499 effective words/s
2019-11-15 18:56:19,346 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,354 : INFO : EPOCH - 46 : training on 334 raw words (17 effective words) took 0.0s, 1858 effective words/s
2019-11-15 18:56:19,383 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,398 : INFO : EPOCH - 47 : training on 334 raw words (24 effective words) took 0.0s, 1251 effective words/s
2019-11-15 18:56:19,413 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,421 : INFO : EPOCH - 48 : training on 334 raw words (27 effective words) took 0.0s, 2788 effective words/s
2019-11-15 18:56:19,433 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,452 : INFO : EPOCH - 49 : training on 334 raw words (30 effective words) took 0.0s, 1315 effective words/s
2019-11-15 18:56:19,477 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,489 : INFO : EPOCH - 50 : training on 334 raw words (17 effective words) took 0.0s, 1037 effective words/s
2019-11-15 18:56:19,499 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,507 : INFO : EPOCH - 51 : training on 334 raw words (24 effective words) took 0.0s, 2337 effective words/s
2019-11-15 18:56:19,529 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,537 : INFO : EPOCH - 52 : training on 334 raw words (26 effective words) took 0.0s, 2645 effective words/s
2019-11-15 18:56:19,561 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,569 : INFO : EPOCH - 53 : training on 334 raw words (29 effective words) took 0.0s, 3120 effective words/s
2019-11-15 18:56:19,583 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,591 : INFO : EPOCH - 54 : training on 334 raw words (18 effective words) took 0.0s, 1557 effective words/s
2019-11-15 18:56:19,604 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,626 : INFO : EPOCH - 55 : training on 334 raw words (21 effective words) took 0.0s, 901 effective words/s
2019-11-15 18:56:19,644 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,661 : INFO : EPOCH - 56 : training on 334 raw words (20 effective words) took 0.0s, 996 effective words/s
2019-11-15 18:56:19,678 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,686 : INFO : EPOCH - 57 : training on 334 raw words (22 effective words) took 0.0s, 2199 effective words/s
2019-11-15 18:56:19,699 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,713 : INFO : EPOCH - 58 : training on 334 raw words (25 effective words) took 0.0s, 1326 effective words/s
2019-11-15 18:56:19,724 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,731 : INFO : EPOCH - 59 : training on 334 raw words (17 effective words) took 0.0s, 1969 effective words/s
2019-11-15 18:56:19,749 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,757 : INFO : EPOCH - 60 : training on 334 raw words (23 effective words) took 0.0s, 2136 effective words/s
2019-11-15 18:56:19,775 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,786 : INFO : EPOCH - 61 : training on 334 raw words (17 effective words) took 0.0s, 1134 effective words/s
2019-11-15 18:56:19,795 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,812 : INFO : EPOCH - 62 : training on 334 raw words (26 effective words) took 0.0s, 1450 effective words/s
2019-11-15 18:56:19,823 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,830 : INFO : EPOCH - 63 : training on 334 raw words (26 effective words) took 0.0s, 2897 effective words/s
2019-11-15 18:56:19,850 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,861 : INFO : EPOCH - 64 : training on 334 raw words (22 effective words) took 0.0s, 1445 effective words/s
2019-11-15 18:56:19,874 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,890 : INFO : EPOCH - 65 : training on 334 raw words (17 effective words) took 0.0s, 933 effective words/s
2019-11-15 18:56:19,903 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,925 : INFO : EPOCH - 66 : training on 334 raw words (33 effective words) took 0.0s, 1441 effective words/s
2019-11-15 18:56:19,937 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,949 : INFO : EPOCH - 67 : training on 334 raw words (23 effective words) took 0.0s, 1693 effective words/s
2019-11-15 18:56:19,964 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:19,972 : INFO : EPOCH - 68 : training on 334 raw words (19 effective words) took 0.0s, 1803 effective words/s
2019-11-15 18:56:19,992 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,001 : INFO : EPOCH - 69 : training on 334 raw words (16 effective words) took 0.0s, 1346 effective words/s
2019-11-15 18:56:20,012 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,029 : INFO : EPOCH - 70 : training on 334 raw words (18 effective words) took 0.0s, 994 effective words/s
2019-11-15 18:56:20,040 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,047 : INFO : EPOCH - 71 : training on 334 raw words (19 effective words) took 0.0s, 2169 effective words/s
2019-11-15 18:56:20,063 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,075 : INFO : EPOCH - 72 : training on 334 raw words (18 effective words) took 0.0s, 1291 effective words/s
2019-11-15 18:56:20,088 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,108 : INFO : EPOCH - 73 : training on 334 raw words (26 effective words) took 0.0s, 1173 effective words/s
2019-11-15 18:56:20,127 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,146 : INFO : EPOCH - 74 : training on 334 raw words (21 effective words) took 0.0s, 831 effective words/s
2019-11-15 18:56:20,157 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,167 : INFO : EPOCH - 75 : training on 334 raw words (24 effective words) took 0.0s, 2088 effective words/s
2019-11-15 18:56:20,188 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,194 : INFO : EPOCH - 76 : training on 334 raw words (25 effective words) took 0.0s, 2763 effective words/s
2019-11-15 18:56:20,206 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,222 : INFO : EPOCH - 77 : training on 334 raw words (15 effective words) took 0.0s, 830 effective words/s
2019-11-15 18:56:20,233 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,246 : INFO : EPOCH - 78 : training on 334 raw words (23 effective words) took 0.0s, 1494 effective words/s
2019-11-15 18:56:20,259 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,267 : INFO : EPOCH - 79 : training on 334 raw words (23 effective words) took 0.0s, 2379 effective words/s
2019-11-15 18:56:20,286 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,294 : INFO : EPOCH - 80 : training on 334 raw words (20 effective words) took 0.0s, 1811 effective words/s
2019-11-15 18:56:20,306 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,327 : INFO : EPOCH - 81 : training on 334 raw words (24 effective words) took 0.0s, 1044 effective words/s
2019-11-15 18:56:20,338 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,345 : INFO : EPOCH - 82 : training on 334 raw words (25 effective words) took 0.0s, 2829 effective words/s
2019-11-15 18:56:20,373 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,392 : INFO : EPOCH - 83 : training on 334 raw words (19 effective words) took 0.0s, 830 effective words/s
2019-11-15 18:56:20,403 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,410 : INFO : EPOCH - 84 : training on 334 raw words (15 effective words) took 0.0s, 1794 effective words/s
2019-11-15 18:56:20,428 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,441 : INFO : EPOCH - 85 : training on 334 raw words (22 effective words) took 0.0s, 1422 effective words/s
2019-11-15 18:56:20,454 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,461 : INFO : EPOCH - 86 : training on 334 raw words (28 effective words) took 0.0s, 3526 effective words/s
2019-11-15 18:56:20,484 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,490 : INFO : EPOCH - 87 : training on 334 raw words (25 effective words) took 0.0s, 3172 effective words/s
2019-11-15 18:56:20,507 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,518 : INFO : EPOCH - 88 : training on 334 raw words (21 effective words) took 0.0s, 1399 effective words/s
2019-11-15 18:56:20,527 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,545 : INFO : EPOCH - 89 : training on 334 raw words (25 effective words) took 0.0s, 1257 effective words/s
2019-11-15 18:56:20,560 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,568 : INFO : EPOCH - 90 : training on 334 raw words (26 effective words) took 0.0s, 2744 effective words/s
2019-11-15 18:56:20,578 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,593 : INFO : EPOCH - 91 : training on 334 raw words (19 effective words) took 0.0s, 1092 effective words/s
2019-11-15 18:56:20,604 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,611 : INFO : EPOCH - 92 : training on 334 raw words (25 effective words) took 0.0s, 3113 effective words/s
2019-11-15 18:56:20,628 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,639 : INFO : EPOCH - 93 : training on 334 raw words (17 effective words) took 0.0s, 1344 effective words/s
2019-11-15 18:56:20,650 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,663 : INFO : EPOCH - 94 : training on 334 raw words (16 effective words) took 0.0s, 985 effective words/s
2019-11-15 18:56:20,676 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,686 : INFO : EPOCH - 95 : training on 334 raw words (15 effective words) took 0.0s, 1299 effective words/s
2019-11-15 18:56:20,711 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,719 : INFO : EPOCH - 96 : training on 334 raw words (19 effective words) took 0.0s, 1892 effective words/s
2019-11-15 18:56:20,729 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,743 : INFO : EPOCH - 97 : training on 334 raw words (23 effective words) took 0.0s, 1531 effective words/s
2019-11-15 18:56:20,753 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,760 : INFO : EPOCH - 98 : training on 334 raw words (27 effective words) took 0.0s, 3127 effective words/s
2019-11-15 18:56:20,778 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,791 : INFO : EPOCH - 99 : training on 334 raw words (24 effective words) took 0.0s, 1500 effective words/s
2019-11-15 18:56:20,804 : INFO : worker thread finished; awaiting finish of 0 more threads
2019-11-15 18:56:20,810 : INFO : EPOCH - 100 : training on 334 raw words (24 effective words) took 0.0s, 2916 effective words/s
2019-11-15 18:56:20,833 : INFO : training on a 33400 raw words (2219 effective words) took 2.7s, 811 effective words/s
>>> #save model
>>> model.save(saved_path)
2019-11-15 18:56:44,656 : INFO : saving Doc2Vec object under C:/Users/THE_PUNISHER/Documents/gp3.1/textos/model.bin, separately None
2019-11-15 18:56:44,722 : INFO : saved C:/Users/THE_PUNISHER/Documents/gp3.1/textos/model.bin
>>> 
