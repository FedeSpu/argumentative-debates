# Structure of the project
Steps 1 and 2 can be skipped if, for the process, is used the file [dataframe.csv](dataframe/dataframe.csv) or is followed the step 3
1. Use the scraper [selen.py](scraper/selen.py) to download debates from [Kialo](https://www.kialo.com/), that are saved as csv file
2. In the notebook [argumentative-debates.ipynb](./argumentative-debates.ipynb) the debates (in format csv with ';' as separator) are loaded and "cleaned" (according to what is written in the [Proia-Spurio-Urbinati_NLP-Exam.pdf](./Proia-Spurio-Urbinati_NLP-Exam.pdf) file)
3. The dataset can be build and cleaned as in point 1 and 2 or can be loaded adding as shortcut this [Google Drive directory](https://drive.google.com/drive/folders/1aS0M6QPvnldf-AkgB7X7rbFcXByWmwAQ?usp=sharing) in the path `drive/MyDrive/NLP/project` (or load into Colab only the `dataframe.csv` and change the load path)
4. Models
   - Neural Network models, based on Bi-LSTM
   - Machine Learning models: Linear Regressor, Decision Tree Regressor, Random Forest Regressor, Support Vector Regressor


