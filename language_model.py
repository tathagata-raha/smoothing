import sys
import nltk
import itertools  
import re

def bigrams(text):
    bigram=[]
    for i in range(len(text)-1):
        temp=[]
        temp.append(text[i])
        temp.append(text[i+1])
        bigram.append(temp)
    return bigram

def trigrams(text):
    trigram=[]
    for i in range(len(text)-2):
        temp=[]
        temp.append(text[i])
        temp.append(text[i+1])
        temp.append(text[i+2])
        trigram.append(temp)
    return trigram

def fourgrams(text):
    fourgram=[]
    for i in range(len(text)-3):
        temp=[]
        temp.append(text[i])
        temp.append(text[i+1])
        temp.append(text[i+2])
        temp.append(text[i+3])
        fourgram.append(temp)
    return fourgram
def freq(my_list): 
    freq = {} 
    for item in my_list: 
        if (str(item) in freq): 
            freq[str(item)] += 1
        else: 
            freq[str(item)] = 1  
    return freq
n=int(sys.argv[1])
types=str(sys.argv[2])
corpusf=str(sys.argv[3])
print('input sentence:' , end=' ')
raw_sen=input()
raw_sen = re.sub('[^A-Za-z]+', ' ', raw_sen)
raw_sen = raw_sen.lower()
sen=nltk.tokenize.word_tokenize(raw_sen)
sbigrams=bigrams(sen)
strigrams=trigrams(sen)
sfourgrams=fourgrams(sen)
# print(*map(' '.join, sbigrams), sep=', ')
raw=open(corpusf, "r").read()
raw = re.sub('[^A-Za-z]+', ' ', raw)
raw = raw.lower()
# print(raw)
corpus=nltk.tokenize.word_tokenize(raw)
cbigrams=bigrams(corpus)
ctrigrams=trigrams(corpus)
cfourgrams=fourgrams(corpus)
#compute frequency distribution for all the bigrams in the text
fdist_u= freq(corpus)
fdist_b = freq(cbigrams)
fdist_t = freq(ctrigrams)
fdist_f=freq(cfourgrams)
b_keys = list(set([tuple(l) for l in cbigrams]))
u_keys=list(set(corpus))
t_keys=list(set([tuple(l) for l in ctrigrams]))
f_keys=list(set([tuple(l) for l in cfourgrams]))
# print(b_keys[0])
# print(fdist_u)
firstTerm=[]
lambda_var=[]
d=0.75
prob=1
if(types=='k'):
    if(n==3):
        for i in strigrams:
            d=0.5
            lambda1=0
            lambda2=0
            lambda3=0
            pkn1=0
            pkn2=0
            pkn3=0
            ft1=0
            ft2=0
            ft3=0
            b_count=0
            for j in b_keys:
                if(i[2]==j[1]):
                    b_count+=1
            ft1=(b_count-d)/len(b_keys) if b_count-d>0 and len(b_keys)>0 else 0
            lambda1=d*len(b_keys)/len(corpus) if len(corpus)>0 else 0
            pkn1=ft1+lambda1/len(u_keys) if len(u_keys)>0 else 0
            d=0.75
            t1_count=0
            for j in t_keys:
                if(i[2]==j[2] and i[1]==j[1]):
                    t1_count+=1
            t2_count=0
            for j in t_keys:
                if(i[1]==j[1]):
                    t2_count+=1
            t3_count=0
            for j in ctrigrams:
                if(i[1]==j[1]):
                    t3_count+=1
            ft2=(t1_count-d)/t2_count if t2_count>0 and t1_count-d>0 else 0
            lambda2=d*t2_count/t3_count if t3_count>0 else 0
            pkn2=ft2+lambda2*pkn1
            d=2.5
            f1_count=0
            f2_count=0
            for j in t_keys:
                if(i[2]==j[2] and i[1]==j[1] and i[0]==j[0]):
                    f1_count+=1
            for j in t_keys:
                if(i[0]==j[0] and i[1]==j[1]):
                    f2_count+=1
            ft3=(f1_count-d)/f2_count if f2_count>0 and f1_count-d>0 else 0
            f3_count=0
            for j in f_keys:
                if(i[0]==j[1] and i[1]==j[2]):
                    f3_count+=1
            f4_count=0
            for j in cfourgrams:
                if(i[0]==j[1] and i[1]==j[2]):
                    f4_count+=1
            # print("val,",f3_count)
            lambda3=d*f3_count/f4_count if f4_count>0 else 0
            pkn3=ft3+lambda3*pkn2
            prob*=pkn3
            # print(ft3,lambda3,pkn2)
    if(n==2):
        for i in sbigrams:
            d=0.5
            lambda1=0
            lambda2=0
            pkn1=0
            pkn2=0
            ft1=0
            ft2=0
            b_count=0
            for j in b_keys:
                if(i[1]==j[1]):
                    b_count+=1
            ft1=(b_count-d)/len(b_keys) if b_count-d>0 and len(b_keys)>0 else 0
            lambda1=d*len(b_keys)/len(corpus) if len(corpus)>0 else 0
            pkn1=ft1+lambda1/len(u_keys) if len(u_keys)>0 else 0
            d=0.75
            t1_count=0
            for j in b_keys:
                if(i[1]==j[1] and i[0]==j[0]):
                    t1_count+=1
            t2_count=0
            for j in b_keys:
                if(i[0]==j[0]):
                    t2_count+=1
            ft2=(t1_count-d)/t2_count if t2_count>0 and t1_count-d>0 else 0
            t3_count=0
            for j in t_keys:
                if(i[0]==j[1]):
                    t3_count+=1
            t4_count=0
            for j in ctrigrams:
                if(i[0]==j[1]):
                    t4_count+=1
            lambda2=d*t3_count/t4_count if t4_count>0 else 0
            pkn2=ft2+lambda2*pkn1
            # print(ft1,ft2,lambda1,lambda2,pkn1,pkn2)
            prob*=pkn2
    if(n==1):
        for i in sen:
            d=0.5
            lambda1=0
            ft1=0
            pkn1=0
            count=0
            for j in corpus:
                if(i==j):
                    count+=1
            ft1=(count-d)/len(corpus) if count-d>0 and len(corpus)>0 else 0
            count2=len(b_keys)
            lambda1=d*count2/len(corpus) if count2>0 else 0
            pkn1=ft1+lambda1/len(corpus)
            # print(ft1,lambda1,pkn1)
            prob*=pkn1
if(types=='w'):
    if(n==3):
        for i in strigrams:
            t_val=0
            z_val=0
            n_val=0
            p1=0
            p2=0
            p3=0
            lambda1=0
            for j in t_keys:
                if(i[0]==j[0] and i[1]==j[1]):
                    t_val+=1
            for j in ctrigrams:
                if(i[0]==j[0] and i[1]==j[1]):
                    n_val+=1            
            # print(t_val,n_val)
            z_val=len(u_keys)-t_val
            if i in t_keys:
                p1=(t_val/(z_val*(n_val+t_val)))
            else:
                count=0
                for j in ctrigrams:
                    if(i[0]==j[0] and i[1]==j[1] and i[2]==j[2]):
                        count+=1
                p1=count/(n_val+t_val) if (n_val+t_val)>0 else 0
            lambda1=1-(t_val/(n_val+t_val)) if (n_val+t_val)>0 else 0
            t_val=0
            z_val=0
            n_val=0
            for j in b_keys:
                if(i[1]==j[0]):
                    t_val+=1
            for j in cbigrams:
                if(i[1]==j[0]):
                    n_val+=1
            z_val=len(u_keys)-t_val
            if i in b_keys:
                p2=(t_val/(z_val*(n_val+t_val)))
            else:
                count=0
                for j in cbigrams:
                    if(i[1]==j[0] and i[2]==j[1]):
                        count+=1
                p2=count/(n_val+t_val) if (n_val+t_val)>0 else 0
            lambda2=1-(t_val/(n_val+t_val)) if (n_val+t_val)>0 else 0
            count=0
            for j in corpus:
                if(j==i[2]):
                    count+=1
            p3=count/(len(corpus)*len(u_keys))
            # print(lambda1)
            # print(p1)
            # print((lambda2*p2+(1-lambda2)*p3))
            prob*=lambda1*p1+(1-lambda1)*(lambda2*p2+(1-lambda2)*p3)
    if(n==2):
        for i in sbigrams:
            t_val=0
            z_val=0
            n_val=0
            p1=0
            p2=0
            lambda1=0
            for j in b_keys:
                if(i[0]==j[0]):
                    t_val+=1
            for j in cbigrams:
                if(i[0]==j[0]):
                    n_val+=1
            z_val=len(u_keys)-t_val
            if i in b_keys:
                p1=(t_val/(z_val*(n_val+t_val)))
            else:
                count=0
                for j in cbigrams:
                    if(i[0]==j[0] and i[1]==j[1]):
                        count+=1
                p1=count/(n_val+t_val) if (n_val+t_val)>0 else 0
            lambda1=1-(t_val/(n_val+t_val)) if (n_val+t_val)>0 else 0 
            count=0
            for j in corpus:
                if(j==i[1]):
                    count+=1
            p2=count/(len(corpus)*len(u_keys))
            prob*=(lambda1*p1+(1-lambda1)*p2)
    if(n==1):
        for i in sen:
            count=0
            for j in corpus:
                if(j==i):
                    count+=1
            prob*=count/(len(corpus)*len(u_keys))
print("Prob: ",prob)