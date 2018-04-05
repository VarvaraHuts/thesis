
# coding: utf-8

# In[5]:

from iwnlp.iwnlp_wrapper import IWNLPWrapper


# In[6]:

lemmatizer = IWNLPWrapper(lemmatizer_path='C:/Users/1/Desktop/thesis/IWNLP.Lemmatizer_20170501.json')


# In[5]:

def capitalize(word):
    if len(word) > 1:
        word = word[0].upper() + word[1:]
    return word


# In[4]:

def get_lemma(word):
    lemma = lemmatizer.lemmatize_plain(word)
    if lemma is None:
        return capitalize(word)
    else:
        return capitalize(lemma[0])


# In[5]:

z = open("C:/Users/1/Desktop/thesis/corpus_final/6.txt", "r", encoding="utf-8")
lines_z = z.readlines()


# In[6]:

lines_z[:5]


# In[7]:

w = open("C:/Users/1/Desktop/thesis/corpus_final/7.txt", "w", encoding="utf-8")


# In[8]:

for line in lines_z:
    items = line.split("/")
    comp = items[0]
    lem = get_lemma(comp)
    line_new = line.replace(comp, lem)
    w.write(line_new)
w.close()


# In[1]:

z = open("C:/Users/1/Desktop/thesis/corpus_final/7.txt", "r", encoding="utf-8")
lines_z = z.readlines()


# In[2]:

lines_z[:3]


# In[3]:

file_words = open('C:/Users/1/Desktop/thesis/wortliste.txt', 'r', encoding='utf-8')
lines_words = file_words.readlines()


# In[6]:

dictionary = []
for line in lines_words:
    line_new = line.split(' ')
    dictionary.append(capitalize(line_new[0]))


# In[7]:

import operator


# In[8]:

def in_dic(word):
    if word in dictionary:
        return True


# In[9]:

def is_part(word):
    if len(word) > 1 and in_dic(word) is True:
        return True
    if (word.endswith('n') or word.endswith('e') or word.endswith('s') or word.endswith('-')) and in_dic(word[:-1]):
        return True
    if (word.endswith('en') or word.endswith('er') or word.endswith('es')) and in_dic(word[:-2]):
        return True


# In[10]:

def choose_split(arr):
    lens = []
    for item in arr:
        var_len = len(item[0] + item[1])
        lens.append(var_len)
    index, value = max(enumerate(lens), key=operator.itemgetter(1))
    return arr[index]


# In[11]:

def get_suff(word):
    max_ind = len(word)
    splits = []
    
    for ind, char in enumerate(word):
        left_compound = word[0:max_ind-ind]
        right_compound = word[max_ind-ind:max_ind]
        
        if is_part(left_compound) and len(left_compound) != len(word):
            right_compound_upper = capitalize(right_compound)
            
            if is_part(right_compound_upper):
                if not in_dic(left_compound) and in_dic(left_compound[:-1]):
                    splits.append([left_compound[:-1], right_compound_upper, left_compound[-1]])
                if not in_dic(left_compound) and in_dic(left_compound[:-2]):
                    splits.append([left_compound[:-2], right_compound_upper, left_compound[-2:]])
                if in_dic(left_compound):
                    splits.append([left_compound, right_compound_upper, "no"])
               
    print (splits)
    if len(splits) > 1:
        return choose_split(splits)[2]
    if len(splits) == 1:
        return splits[0][2]
    if splits == []:
        return None


# In[13]:

w = open("C:/Users/1/Desktop/thesis/corpus_final/8.txt", "w", encoding="utf-8")


# In[14]:

for line in lines_z:
    items = line.split("/")
    suff = get_suff(items[0])
    ind = items[-1]
    x = suff + "/" + ind
    line_n = line.replace(ind, x)
    w.write(line_n)
w.close()

