import pandas as pd
from transformers import BertTokenizer

url = pd.read_csv("IEEEData-dict2.csv")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
url['nurl'] = ""
url.loc[:, 'nurl'] = url['word2'].astype(str).apply(lambda x: ', '.join(tokenizer.tokenize(x)))
url['nurl'] = url['nurl'].str.replace(r'[\[\]\'#]', '', regex=True)
url.insert(0, '', range(len(url)))
url.to_csv("url-IEEEData-dict2-subword.csv", index=False, header=["", "word2", "label", "nurl"])
