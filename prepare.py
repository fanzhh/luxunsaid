# coding: utf-8
import jieba # 结巴分词
import re


def load_doc(filename):
    file = open(filename,'r')
    text = file.read()
    file.close()
    print('doc loaded')
    return text


def clean_doc(doc):
    punctions = '，。（）“”——『』.：:()《》！-/\n,一二三四五六七八九〇○*=；？[]'
    for p in punctions:
        doc = doc.replace(p, ' ')
    filtrate = re.compile('[A-Za-z0-9]')
    doc = filtrate.sub(r'', doc)
    print('begin 分词')
    tokens = jieba.cut(doc, cut_all=False)
    print('end 分词')
    print('doc cleaned')
    return (' '.join(tokens)).split()

def save_doc(lines, filename):
    data = '\n'.join(lines)
    file = open(filename,'w')
    file.write(data)
    print('doc saved')
    file.close()


in_filename = 'luxun_utf8.txt'
doc = load_doc(in_filename)
print(doc[:200])

tokens = clean_doc(doc)
print(tokens[:200])
print('Total Tokens: %d' % len(tokens))
print('Unique Tokens: %d' % len(set(tokens)))

length = 50 + 1
sequences = list()
for i in range(length, len(tokens)):
    seq = tokens[i-length:i]
    line = ' '.join(seq)
    sequences.append(line)
print('Total Sequences: %d' % len(sequences))

out_filename = 'luxun_sequences.txt'
save_doc(sequences, out_filename)
