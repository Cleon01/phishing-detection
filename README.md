# **Phishing URL Detection**

## **Project Overview**

This project applies machine learning and deep learning models for phishing URL detection, utilizing NLP-based tokenization techniques and various neural network architectures. It evaluates six models, including fine-tuned BERT, CNN, and LSTM networks, to classify malicious URLs and compare their performance on processed datasets.

The published paper is available here: https://ieeexplore.ieee.org/document/9979860.

### **Project Structure**

The project is organized into four main folders:

- 📂 **data/** – Contains raw and transformed datasets.
- 📂 **programs/** – Jupyter notebooks for different models.
- 📂 **result/** – Summarized results stored in an Excel file.
- 📂 **saved\_models/** – Trained model weights (some of the h5 files are too large to upload).

---

## **1. Models Implemented**

The project includes six models for phishing URL detection:

| Model                             | Tokenization Method    |
| --------------------------------- | ---------------------- |
| ✅ Fine-Tuned BERT                 | Subword Tokenization   |
| ✅ Fine-Tuned BERT + Random Forest | Subword Tokenization   |
| ✅ CNN                             | Character Tokenization |
| ✅ CNN                             | Subword Tokenization   |
| ✅ LSTM                            | Character Tokenization |
| ✅ LSTM                            | Subword Tokenization   |

---

## **2. Data Preprocessing & Transformation**

The datasets undergo several transformation steps before training:

1. **Transform `processed_IEEEData.csv` → `IEEEData-dict2.csv`**
   - Run `transform_processed-to-dict2.py`.

2. **Transform `IEEEData-dict2.csv` → `url-IEEEData-dict2-subword.csv`**
   - Run `transform_dict2-to-subword.py`.

3. **Create Train & Validation Splits**

   - Running `FineTuneBERT-IEEEData-CM2.ipynb` generates:
     - `IEEE-dict2-train.csv`
     - `IEEE-dict2-val.csv`
   - These are used for `FineTuneBERT_IEEEData_RF_withDelimiter_2.ipynb`.

---

## **3. Model Training Notebooks**

Each model is implemented in a Jupyter Notebook. Below are the data sources and output for each:

### **BERT-Based Models**

| Notebook                                               | Datasets Loaded                              | Datasets/ Models Created                            |
| ------------------------------------------------------ | -------------------------------------------- | ---------------------------------------------------- |
| **FineTuneBERT-IEEEData-CM2.ipynb**                    | `IEEEData-dict2.csv`                         | Creates `IEEE-dict2-train.csv`, `IEEE-dict2-val.csv` |
| **FineTuneBERT\_IEEEData\_RF\_withDelimiter\_2.ipynb** | `IEEE-dict2-train.csv`, `IEEE-dict2-val.csv` | None                                                 |

### **LSTM-Based Models**

| Notebook                | Datasets Loaded                  | Datasets/ Models Created                               |
| ----------------------- | -------------------------------- | ------------------------------------------------------ |
| **Char-LSTM.ipynb**     | `processed_IEEEData.csv`         | `Char-biLSTM_iter10.h5`                                |
| **subword\_lstm.ipynb** | `url-IEEEData-dict2-subword.csv` | `Subword-biLSTM_iter10.h5`, `Subword-biLSTM_iter15.h5` |

### **CNN-Based Models**

| Notebook                       | Datasets Loaded                  | Datasets/ Models Created                         |
| ------------------------------ | -------------------------------- | ------------------------------------------------ |
| **Char-CNN-Filters-3-4.ipynb** | `processed_IEEEData.csv`         | `Char-CNN_iter10.h5`                             |
| **subword\_cnn.ipynb**         | `url-IEEEData-dict2-subword.csv` | `Subword-CNN_iter10.h5`, `Subword-CNN_iter20.h5` |

---

## **4. Results**

The summarized model performance is provided below:

| Model                       | Training Loss | Validation Loss | Training Accuracy | Validation Accuracy |
| --------------------------- | ------------- | --------------- | ----------------- | ------------------- |
| **Char LSTM**               | 0.107         | 0.1069          | 95.97%            | 96.30%              |
| **Subword LSTM**            | 0.0249        | 0.0778          | 99.09%            | 97.96%              |
| **Char CNN**                | 0.0175        | 0.111           | 99.36%            | 96.71%              |
| **Subword CNN**             | 0.0311        | 0.0841          | 98.94%            | 97.60%              |
| **Subword Fine-Tuned BERT** | 0.0596        | 0.0562          | 97.84%            | 98.54%              |

A more detailed breakdown of results is available in the **Excel file inside the ********`result/`******** folder**.

