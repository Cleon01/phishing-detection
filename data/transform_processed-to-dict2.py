import pandas as pd

urldata1 = pd.read_csv("processed_IEEEData.csv")
processed_data = []

for index, row in urldata1.iterrows():
    url = row['url']
    label = row['label']

    url = url.replace("https://", "").replace("http://", "").replace("ftp://", "")

    word2 = url.split("/")
    word3 = word2[0].split(".") 
    word4 = url[url.find("/") + 1:] 
    word5 = word4.split("?")[0] 
    word6 = word5.split("/") 

    words = [j.lower() for j in (word3 + word6) if j]
    processed_url = " ".join(words)
    processed_data.append([processed_url, label])

df_dict2 = pd.DataFrame(processed_data, columns=["word2", "label"])
df_dict2.to_csv("IEEEData-dict2.csv", index=False)
