from keras.models import load_model
from sklearn.preprocessing import StandardScaler
import pandas as pd 
import csv
def main():
    train = pd.read_csv('train-v3.csv')
    test = pd.read_csv('test-v3.csv')
    #載入model
    mode1 = load_model('model')
    #選取欄位
    title=['bedrooms',
           'bathrooms', 'sqft_living', 'sqft_lot','waterfront', 'view',
           'condition', 'grade', 'sqft_above', 'sqft_basement',
          'lat', 'long', 'sqft_living15',
           'sqft_lot15']
    #資料正規化
    data=train[title]
    data_test=test[title]
    scaler=StandardScaler().fit(data)
    x_test = scaler.transform(data_test)
    #訓練test
    predict_x=mode1.predict(x_test) 
    print('test_loss:',predict_x)
    ID=np.array(StockCsv_test["id"])
    data={"id":ID,
        "price":predict_x.flatten()}
    with open('test.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(ID)):
            writer.writerow({"id":ID[i],"price":predict_x.flatten()[i]})
main()