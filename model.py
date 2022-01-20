import numpy as np 
import pandas as pd 
from tensorflow.keras.models import Sequential
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.layers import Dense
import csv
def main ():
    train = pd.read_csv('train-v3.csv')
    valid = pd.read_csv('valid-v3.csv')
    test = pd.read_csv('test-v3.csv')
    #選取欄位
    title=['bedrooms',
           'bathrooms', 'sqft_living', 'sqft_lot','waterfront', 'view',
           'condition', 'grade', 'sqft_above', 'sqft_basement',
          'lat', 'long', 'sqft_living15',
           'sqft_lot15']
    #資料正規化
    Size=len(title)
    data=train[title]
    data_valid=valid[title]
    data_test=test[title]
    y_train = train["price"]
    y_valid = valid["price"] 
    scaler=StandardScaler().fit(data)
    x_train = preprocessing.scale(data)
    x_valid = scaler.transform(data_valid)
    x_test = scaler.transform(data_test)
    #模型
    model = Sequential() 
    model.add(Dense(units=80,activation="relu", input_shape=(Size,)))
    model.add(Dense(units =100, activation="relu"))
    model.add(Dense(units =400, activation="relu"))
    model.add(Dense(units =100, activation="relu"))
    model.add(Dense(units =80, activation="linear"))
    model.add(Dense(units =1))
    model.summary()
    model.compile(loss='mean_absolute_error',optimizer='adam')
    history = model.fit(x_train,y_train,validation_data=(x_valid,y_valid), epochs=200, batch_size=32
    #顯示loss 跟 val_loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    #訓練test
    predict_x=model.predict(x_test) 
    print(predict_x)
    #存成csv檔
    ID=np.array(test["id"])
    data={"id":ID,
        "price":predict_x.flatten()}
    with open('/content/gdrive/My Drive/Colab Notebooks/11-20-2Submission.csv', 'w', newline='') as csvfile:
      fieldnames = ['id', 'price']
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()
      for i in range(len(ID)):
        writer.writerow({"id":ID[i],"price":predict_x.flatten()[i]})
    #儲存訓練的model
    model.save("model")
main ()