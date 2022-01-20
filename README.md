# 房價預測
## 資料來源
    Kaggle:https://www.kaggle.com/c/machine-learningntut-2021-autumn-regression
    欄位:id	price	sale_yr	sale_month	sale_day	bedrooms	bathrooms	sqft_living	sqft_lot	floors	waterfront	view	condition	grade	sqft_above	sqft_basement	yr_built	yr_renovated	zipcode	lat	long	sqft_living15	sqft_lot15
![image](https://user-images.githubusercontent.com/93694868/143486998-58a47bd7-1ad0-4084-b610-b2293fdf5984.png)

    
    Train:12967筆
    Valid:2161筆
    Test:6485筆
## 使用的版本
    查看 function.txt

## 資料分析 
    使用線性回歸與股價比對相關性使找出較相關的資料
![下載 (3)](https://user-images.githubusercontent.com/93694868/143734601-d87ae097-be7c-4cb5-9a48-188f81713902.png)

![bathrooms線性回歸](https://user-images.githubusercontent.com/93694868/143471952-a02c66d3-0242-44c1-b25e-a4f7634e269a.png)
![bedrooms線性回歸](https://user-images.githubusercontent.com/93694868/143472000-9a714e5a-02f6-47e5-aa2d-b756d24a536a.png)
![condition線性回歸](https://user-images.githubusercontent.com/93694868/143472013-47cb8148-57a6-4311-a757-1df9d81ae84a.png)
![floors線性回歸](https://user-images.githubusercontent.com/93694868/143472019-15924e63-c725-4112-bb20-3254d6b6afbb.png)
![grade線性回歸](https://user-images.githubusercontent.com/93694868/143472026-4ad3897f-d5c5-40d7-9889-5916154f079f.png)
![lat線性回歸](https://user-images.githubusercontent.com/93694868/143472033-8d16327b-697b-4f00-bef6-f4232f077c69.png)
![long線性回歸](https://user-images.githubusercontent.com/93694868/143472046-01f98cf1-167e-497f-93c6-8bbce6b0ad7b.png)
![sale_day線性回歸](https://user-images.githubusercontent.com/93694868/143472057-2e6fe0ae-ea80-423b-9a28-45fd8e3e819f.png)
![sale_month線性回歸](https://user-images.githubusercontent.com/93694868/143472066-99b55e65-72e2-497a-89a3-8468af5922c9.png)
![sale_yr線性回歸](https://user-images.githubusercontent.com/93694868/143472074-f45760cc-44ab-4f22-840a-78fb694afa9f.png)
![sqft_above線性回歸](https://user-images.githubusercontent.com/93694868/143472083-f3fa16be-6710-47cd-949d-4214021c829c.png)
![sqft_basement線性回歸](https://user-images.githubusercontent.com/93694868/143472089-fcdf4ae7-5902-453d-b057-a038adbae2af.png)
![sqft_living15線性回歸](https://user-images.githubusercontent.com/93694868/143472096-39c828c7-88a0-4d4a-a9a3-c421653c7369.png)
![sqft_living線性回歸](https://user-images.githubusercontent.com/93694868/143472102-d38b2ab4-123d-4e0e-8982-a206487cd5b6.png)
![sqft_lot15線性回歸](https://user-images.githubusercontent.com/93694868/143472117-00e059c6-af3f-4471-b700-03a16802442f.png)
![sqft_lot線性回歸](https://user-images.githubusercontent.com/93694868/143472127-990956d3-3006-4188-9d33-5a16c83c7369.png)
![view線性回歸](https://user-images.githubusercontent.com/93694868/143472141-39873092-ad36-4244-9299-af45962c85fc.png)
![waterfront線性回歸](https://user-images.githubusercontent.com/93694868/143472158-2f91a5cf-db1e-4028-b996-82b61a9b87ea.png)
![yr_built線性回歸](https://user-images.githubusercontent.com/93694868/143472175-5eb8a15b-b943-493d-a83a-bcf855f5c27e.png)
![zipcode線性回歸](https://user-images.githubusercontent.com/93694868/143472193-45c64399-3e14-4762-b66d-4a24f43ac00d.png)
    
    最後選擇:bedrooms  bathrooms  sqft_living  sqft_lot  waterfront  view  condition   grade  sqft_above  sqft_basement  lat  long  sqft_living15  sqft_lot15
    
## 資料處理
    使用Z-Score對資料進行資料分析
## 模型
    使用類神經網路進行模擬
    model.add(Dense(units=80,activation="relu", input_shape=(Size,)))
    model.add(Dense(units =100, activation="relu"))
    model.add(Dense(units =400, activation="relu"))
    model.add(Dense(units =100, activation="relu"))
    model.add(Dense(units =80, activation="linear"))
    model.add(Dense(units =1))
## 程式如何執行
### 模型使用
    執行model.py可以訓練模型，也可以用 Train.sh執行
    執行Test.py可以執行使用練好的模型，如果要更改test的參數，可以直接更改pd.read_csv('test-v3.csv')的檔案
    也可以用 Test.sh執行
