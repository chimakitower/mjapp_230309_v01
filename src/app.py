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
    model = joblib.load('./src/mjapp.pkl')
    # x = get_onehot(x)
    # x = flatten(x)
    pred_label = model.predict(x.reshape(1, -1))
    return pred_label

# 推論したラベルから花の名前を返す関数
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
    tehai1 = StringField('6巡目の手牌:1枚目',
                    [validators.InputRequired(message='記入形式が正しくありません')])
    tehai2 = StringField('6巡目の手牌:2枚目',
                    [validators.InputRequired(message='記入形式が正しくありません')])
    tehai3 = StringField('6巡目の手牌:3枚目',
                    [validators.InputRequired(message='記入形式が正しくありません')])
    tehai4 = StringField('6巡目の手牌:4枚目',
                    [validators.InputRequired(message='記入形式が正しくありません')])
    tehai5 = StringField('6巡目の手牌:5枚目',
                    [validators.InputRequired(message='記入形式が正しくありません')])
    tehai6 = StringField('6巡目の手牌:6枚目',
                    [validators.InputRequired(message='記入形式が正しくありません')])
    tehai7 = StringField('6巡目の手牌:7枚目',
                    [validators.InputRequired(message='記入形式が正しくありません')])
    tehai8 = StringField('6巡目の手牌:8枚目',
                    [validators.InputRequired(message='記入形式が正しくありません')])
    tehai9 = StringField('6巡目の手牌:9枚目',
                    [validators.InputRequired(message='記入形式が正しくありません')])
    tehai10 = StringField('6巡目の手牌:10枚目',
                    [validators.InputRequired(message='記入形式が正しくありません')])
    tehai11 = StringField('6巡目の手牌:11枚目',
                    [validators.InputRequired(message='記入形式が正しくありません')])
    tehai12 = StringField('6巡目の手牌:12枚目',
                    [validators.InputRequired(message='記入形式が正しくありません')])
    tehai13 = StringField('6巡目の手牌:13枚目',
                    [validators.InputRequired(message='記入形式が正しくありません')])

    def validate_tehai1(self, tehai1):
        if tehai1.data == "":
            raise ValidationError("牌を入力してください")

        elif tehai1.data not in sanma_pai_to_num:
            raise ValidationError("例のように記入してください。（あるいは、マンズの2~8を記入していませんか？）")

    def validate_tehai2(self, tehai2):
        if tehai2.data == "":
            raise ValidationError("牌を入力してください")

        elif tehai2.data not in sanma_pai_to_num:
            raise ValidationError("例のように記入してください。（あるいは、マンズの2~8を記入していませんか？）")

    def validate_tehai3(self, tehai3):
        if tehai3.data == "":
            raise ValidationError("牌を入力してください")

        elif tehai3.data not in sanma_pai_to_num:
            raise ValidationError("例のように記入してください。（あるいは、マンズの2~8を記入していませんか？）")

    def validate_tehai4(self, tehai4):
        if tehai4.data == "":
            raise ValidationError("牌を入力してください")

        elif tehai4.data not in sanma_pai_to_num:
            raise ValidationError("例のように記入してください。（あるいは、マンズの2~8を記入していませんか？）")

    def validate_tehai5(self, tehai5):
        if tehai5.data == "":
            raise ValidationError("牌を入力してください")

        elif tehai5.data not in sanma_pai_to_num:
            raise ValidationError("例のように記入してください。（あるいは、マンズの2~8を記入していませんか？）")

    def validate_tehai6(self, tehai6):
        if tehai6.data == "":
            raise ValidationError("牌を入力してください")

        elif tehai6.data not in sanma_pai_to_num:
            raise ValidationError("例のように記入してください。（あるいは、マンズの2~8を記入していませんか？）")

    def validate_tehai7(self, tehai7):
        if tehai7.data == "":
            raise ValidationError("牌を入力してください")

        elif tehai7.data not in sanma_pai_to_num:
            raise ValidationError("例のように記入してください。（あるいは、マンズの2~8を記入していませんか？）")

    def validate_tehai8(self, tehai8):
        if tehai8.data == "":
            raise ValidationError("牌を入力してください")

        elif tehai8.data not in sanma_pai_to_num:
            raise ValidationError("例のように記入してください。（あるいは、マンズの2~8を記入していませんか？）")

    def validate_tehai9(self, tehai9):
        if tehai9.data == "":
            raise ValidationError("牌を入力してください")

        elif tehai9.data not in sanma_pai_to_num:
            raise ValidationError("例のように記入してください。（あるいは、マンズの2~8を記入していませんか？）")

    def validate_tehai10(self, tehai10):
        if tehai10.data == "":
            raise ValidationError("牌を入力してください")

        elif tehai10.data not in sanma_pai_to_num:
            raise ValidationError("例のように記入してください。（あるいは、マンズの2~8を記入していませんか？）")

    def validate_tehai11(self, tehai11):
        if tehai11.data == "":
            raise ValidationError("牌を入力してください")

        elif tehai11.data not in sanma_pai_to_num:
            raise ValidationError("例のように記入してください。（あるいは、マンズの2~8を記入していませんか？）")

    def validate_tehai12(self, tehai12):
        if tehai12.data == "":
            raise ValidationError("牌を入力してください")

        elif tehai12.data not in sanma_pai_to_num:
            raise ValidationError("例のように記入してください。（あるいは、マンズの2~8を記入していませんか？）")

    def validate_tehai13(self, tehai13):
        if tehai13.data == "":
            raise ValidationError("牌を入力してください")

        elif tehai13.data not in sanma_pai_to_num:
            raise ValidationError("例のように記入してください。（あるいは、マンズの2~8を記入していませんか？）")


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
            pai1 = sanma_pai_to_num[str(request.form['tehai1'])]
            pai2 = sanma_pai_to_num[str(request.form['tehai2'])]
            pai3 = sanma_pai_to_num[str(request.form['tehai3'])]
            pai4 = sanma_pai_to_num[str(request.form['tehai4'])]
            pai5 = sanma_pai_to_num[str(request.form['tehai5'])]
            pai6 = sanma_pai_to_num[str(request.form['tehai6'])]
            pai7 = sanma_pai_to_num[str(request.form['tehai7'])]
            pai8 = sanma_pai_to_num[str(request.form['tehai8'])]
            pai9 = sanma_pai_to_num[str(request.form['tehai9'])]
            pai10 = sanma_pai_to_num[str(request.form['tehai10'])]
            pai11 = sanma_pai_to_num[str(request.form['tehai11'])]
            pai12 = sanma_pai_to_num[str(request.form['tehai12'])]
            pai13 = sanma_pai_to_num[str(request.form['tehai13'])]

            # 入力された値を np.array に変換して推論
            x = np.array([pai1, pai2, pai3, pai4, pai5, pai6, pai7, pai8, pai9, pai10, pai11, pai12, pai13])
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