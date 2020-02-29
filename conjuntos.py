d1 = "Afraid you've lost it all Unsure what the future holds And now, I can hear your call tonight"

bow_d1 = d1.split(" ")

d2 = "Too late to turn back now And you'll be safe and sound I know that we'll make it through the night"

bow_d2 = d2.split(" ")

d3 = "I'll dry every river in your eyes light up the darkness in your mind Remember when life is so unfair Hold on"

bow_d3 = d3.split(" ")

d4 = "And when you feel lostNow don't be scared Hold on, hold on we're almost there"

bow_d4 = d4.split(" ")

unique_words = set(bow_d1).union(set(bow_d2).union(set(bow_d3).union(set(bow_d4))))

print(unique_words)

tc_d1 = dict.fromkeys(unique_words, 0)
for w in bow_d1:
    tc_d1[w] += 1

tc_d2 = dict.fromkeys(unique_words, 0)
for w in bow_d2:
    tc_d2[w] += 1

tc_d3 = dict.fromkeys(unique_words, 0)
for w in bow_d3:
    tc_d3[w] += 1

tc_d4 = dict.fromkeys(unique_words, 0)
for w in bow_d4:
    tc_d4[w] += 1

tf_d1 = {}
total = float(len(bow_d1))
for w, c in tc_d1.items():
    tf_d1[w] = c / total

tf_d2 = {}
total = float(len(bow_d2))
for w, c in tc_d2.items():
    tf_d2[w] = c / total

tf_d3 = {}
total = float(len(bow_d3))
for w, c in tc_d3.items():
    tf_d3[w] = c / total

tf_d4 = {}
total = float(len(bow_d4))
for w, c in tc_d4.items():
    tf_d4[w] = c / total

print(tf_d1)
print(tf_d2)
print(tf_d3)
print(tf_d4)

import math

documents = [tc_d1, tc_d2, tc_d3, tc_d4]

N = len(documents)

idf = dict.fromkeys(unique_words, 0)

for d in documents:
    for w, c in d.items():
        if c > 0:
            idf[w] += 1
for w, c in idf.items():
    idf[w] = math.log(N / float(c))


tf_idf_d1 = {}
for w, c in tf_d1.items():
    tf_idf_d1[w] = c * idf[w]

tf_idf_d2 = {}
for w, c in tf_d2.items():
    tf_idf_d2[w] = c * idf[w]

tf_idf_d3 = {}
for w, c in tf_d3.items():
    tf_idf_d3[w] = c * idf[w]

tf_idf_d4 = {}
for w, c in tf_d4.items():
    tf_idf_d4[w] = c * idf[w]


#distancia entre d1 e e2

ds = []

for w in unique_words:
    dif = tf_idf_d1[w] - tf_idf_d2[w]
    ds.append(dif * dif)

soma = 0

for i in ds:
    soma += i

dist_d1_d2 = math.sqrt(soma)

ds = []

for w in unique_words:
    dif = tf_idf_d1[w] - tf_idf_d3[w]
    ds.append(dif * dif)

soma1 = 0

for i in ds:
    soma1 += i

dist_d1_d3 = math.sqrt(soma1)

ds = []

for w in unique_words:
    dif = tf_idf_d1[w] - tf_idf_d4[w]
    ds.append(dif * dif)

soma2 = 0

for i in ds:
    soma2 += i

dist_d1_d4 = math.sqrt(soma2)

ds = []

for w in unique_words:
    dif = tf_idf_d2[w] - tf_idf_d3[w]
    ds.append(dif * dif)

soma3 = 0

for i in ds:
    soma3 += i

dist_d2_d3 = math.sqrt(soma3)

ds = []

for w in unique_words:
    dif = tf_idf_d2[w] - tf_idf_d4[w]
    ds.append(dif * dif)

soma4 = 0

for i in ds:
    soma4 += i

dist_d2_d4 = math.sqrt(soma4)

ds = []

for w in unique_words:
    dif = tf_idf_d3[w] - tf_idf_d4[w]
    ds.append(dif * dif)

soma5 = 0

for i in ds:
    soma5 += i

dist_d3_d4 = math.sqrt(soma5)



dist_d1_d2 = math.sqrt(soma)
dist_d1_d3 = math.sqrt(soma1)
dist_d1_d4 = math.sqrt(soma2)
dist_d2_d3 = math.sqrt(soma3)
dist_d2_d4 = math.sqrt(soma4)
dist_d3_d4 = math.sqrt(soma5)



print(dist_d1_d2)
print(dist_d1_d3)
print(dist_d1_d4)
print(dist_d2_d3)
print(dist_d2_d4)
print(dist_d3_d4)
































