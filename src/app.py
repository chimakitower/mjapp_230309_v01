# 必要なモジュールのインポート
import joblib
from flask import Flask, request, render_template
from wtforms import Form, StringField, SubmitField, validators, ValidationError
import numpy as np
from function import *


#　学習済みモデルをもとに推論する関数
#　xは1行13列のndarrayでIDとしたい  
def output_predict(x): 
    # 学習済みモデル（iris.pkl）を読み込み
    # model = joblib.load('./src/mjapp.pkl')
    model = joblib.load('mjapp.pkl')
    pred_label = model.predict(x.reshape(1, -1))
    return pred_label

# 推論したラベルから予測結果を返す関数
def getName(label):
    if label == 0:
        return '失点しなさそう'
    elif label == 1:
        return '失点しそう'
    else:
        return 'Error'


# Flaskのインスタンスを作成
app = Flask(__name__)

# 入力フォームの設定
class TehaiForm(Form):
    tehai = StringField('6巡目の手牌を記入例に従って記入してください',
                    [validators.InputRequired()])
    
    def validate_tehai(self, tehai):
        if tehai.data == "":
            raise ValidationError("牌を入力してください")

        # elif tehai.data not in sanma_pai_to_num:
        #     raise ValidationError("例のように記入してください。（あるいは、マンズの2~8を記入していませんか？）")

    # html 側で表示する submit ボタンの設定
    submit = SubmitField('送信')


# URL にアクセスがあった場合の挙動の設定
@app.route('/', methods = ['GET', 'POST'])
def predicts():
    # TForms で構築したフォームをインスタンス化
    tehaiForm = TehaiForm(request.form)
    # POST メソッドの定義
    if request.method == 'POST':

        # 条件に当てはまらない場合
        if tehaiForm.validate() == False:
            return render_template('index.html', forms=tehaiForm)
        # 条件に当てはまる場合の、推論を実行
        else:
            pai = str(request.form['tehai'])
            pai_list = split_pai(pai)
            x = np.array(pai_list)
            
            # 入力された値を np.array に変換して推論
            x = get_onehot(x)
            x = flatten(x)
            pred = output_predict(x)
            output_ = getName(pred)
            return render_template('result.html', output=output_)

    # GET 　メソッドの定義
    elif request.method == 'GET':
        return render_template('index.html', forms=tehaiForm)

# アプリケーションの実行
if __name__ == '__main__':
    app.run() 