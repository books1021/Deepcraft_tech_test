### データをクリーンアップし、クリーンなデータを保存する新しい csv ファイルを作成します。
### データを日付順に並べる
### na データはありません。すべてのデータが有効です
### 価格変動率、取引量を文字列データ型から浮動小数点数に変換する必要があります。
### 日付を文字列データ型から datetime オブジェクトに変換します

import pandas as pd

data = pd.read_csv('time-series-prediction\stock_price.csv')

# 英語の列名、ASCII 標準を使用します。
data.columns=['date','close','open','high','low','volumeM','change']

# 日付をdatetimeオブジェクトに変換する
data['date']=pd.to_datetime(data['date'])

# 毎日の % 変化を % で処理し、浮動小数点数に変換します
# 列の変更は毎日の相対的な価格変化を表します
if data['change'].dtype=='O':
    data['change']=data['change'].str.replace('%','',regex=True).astype(float)*0.01
    
# 浮動小数点数のボリューム列を作成
def numberconvert(x):
    ''' convert volume data to float number, volumn are marked in Million or Billion
    '''
    if 'B' in x:
        return float(x.replace('B',''))*1000000000
    elif 'M' in x:
        return float(x.replace('M',''))*1000000
    else:
        return float(x)

data['volume']=data['volumeM'].apply(numberconvert)

data.drop(columns=['volumeM'],inplace=True)

### データを日付順に並べる
data.iloc[::-1]

### データを新しい csv ファイルに保存する
data.to_csv('time-series-prediction\price_clean_full.csv', index=False)  