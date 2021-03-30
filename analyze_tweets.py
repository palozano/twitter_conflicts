import spacy
from spacy.language import Language
from spacy.tokenizer import Tokenizer
import re

# Creating the model with English
nlp = spacy.load('en_core_web_sm')

# Reading data

# file_name = 'introduction.txt'
# introduction_file_text = open(file_name).read()

# introduction_text = ('This tutorial is about Natural Language Processing in Spacy.')
introduction_text = ('Gus Proto is a Python developer currently'
                     ' working for a London-based Fintech'
                     ' company. He is interested in learning'
                     ' Natural Language Processing.')

introduction_doc = nlp(introduction_text)

print([token.text for token in introduction_doc])

# Sentence detection
sentences = list(introduction_doc.sents)

for sentence in sentences:
    print(sentence)

# Set customs boundaries for text
@Language.component('my')
def set_custom_boundaries(doc):
    # Adds support to use `...` as the delimiter for sentence detection
    for token in doc[:-1]:
        if token.text == '...':
            doc[token.i+1].is_sent_start = True
    return doc

ellipsis_text = ('Gus, can you, ... never mind, I forgot'
                 ' what I was saying. So, do you think'
                 ' we should ...')

custom_nlp = spacy.load('en_core_web_sm')
custom_nlp.add_pipe(factory_name='my', before='parser')
custom_ellipsis_doc = custom_nlp(ellipsis_text)
custom_ellipsis_sentences = list(custom_ellipsis_doc.sents)

for sentence in custom_ellipsis_sentences:
    print(sentence)


# Tokenization
for token in introduction_doc:
    print(token, token.idx)

    # print(token, token.idx, token.text_with_ws, token.is_alpha, token.is_punct, token.is_space, token.shape_, token.is_stop)


# You can customize the tokenization by updating the tokenizer property on the nlp object
custom_nlp = spacy.load('en_core_web_sm')
prefix_re = spacy.util.compile_prefix_regex(custom_nlp.Defaults.prefixes)
suffix_re = spacy.util.compile_suffix_regex(custom_nlp.Defaults.suffixes)
infix_re = re.compile(r'''[-~]''')
def customize_tokenizer(nlp):
    # Adds support to use `-` as the delimiter for tokenization
    return Tokenizer(nlp.vocab, prefix_search=prefix_re.search,
                     suffix_search=suffix_re.search,
                     infix_finditer=infix_re.finditer,
                     token_match=None
                     )
custom_nlp.tokenizer = customize_tokenizer(custom_nlp)
custom_tokenizer_about_doc = custom_nlp(introduction_text)
print([token.text for token in custom_tokenizer_about_doc])
