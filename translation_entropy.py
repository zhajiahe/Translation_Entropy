__author__ = 'hazhang'

import numpy as np
import ipdb
import os, sys
from math import log
from collections import OrderedDict
vocab_a, vocab_b,align, text_a, text_b = sys.argv[1:]
Lang = text_a[-2:]
def translation_entropy(vocab_a, vocab_b, align, text_a, text_b):
    vocab_A = {}
    vocab_B = {}
    Alignment = None
    text_A = []
    text_B = []
    Dict = {}
    """READ in Data"""
    with open(vocab_a,'r') as f:
        lines = f.readlines()
        for i,line in enumerate(lines):
            vocab_A[line.split()[0]] = i
            Dict[line.split()[0]] = {}
    index_vocab_A = dict(zip(vocab_A.values(), vocab_A.keys()))
    with open(vocab_b,'r') as f:
        lines = f.readlines()
        for i,line in enumerate(lines):
            vocab_B[line.split()[0]] = i
    index_vocab_B = dict(zip(vocab_B.values(), vocab_B.keys()))
    with open(align,'r') as f:
        lines = f.readlines()
        Alignment = [line.strip().split() for line in lines]
    with open(text, 'r') as f:
        lines = f.readlines()
        for line in lines:
            s = line.strip().split(' ||| ')
            text_A.append(s[0].split())
            text_B.append(s[1].split())
    """PROCESS"""
    for i, line in enumerate(Alignment):
        for st in line:
            s, t = st.split('-')
            s_token = text_A[i][int(s)]
            t_token = text_B[i][int(t)]
            if s_token not in vocab_A:
                continue
            if t_token not in vocab_B:
                continue
            # s_index = vocab_A[s_token]
            # t_index = vocab_B[t_token]
            try:
                Dict[s_token][t_token] += 1
            except:
                Dict[s_token][t_token] = 1
    """STATISTICS"""
    entropys = OrderedDict()
    for word, freqs in Dict.items():
        entropys[word] = Cal_entropy(freqs)
    with open('trans_entropy.' + Lang, 'w') as f:
        for word, ent in entropys.items():
            f.writelines(word + ' ' + str(ent) + '\n')

def Cal_entropy(freqs):
    if not freqs or len(freqs) == 1: # if have not alignment
        return 0  # defalut 0
    cnt = sum(freqs.values())
    ent = 0
    for k,v in freqs.items():
        p = v / cnt
        ent += - p * log(p)
    return ent


translation_entropy(vocab_a, vocab_b, align, text_a, text_b)


    
