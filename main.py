import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image #PILもImageも大文字小文字に気を付ける
import time
#=============================================
#streamlit を実行するには
#①cd C:\Users\hanafuku\OneDrive\Desktop\マイクロソフトCWBJ\python
#②streamlit run main.py←run以降はファイル名

#=============================================

#一端実行すると、公開されたページを更新すれば変更が表示確認できる
#=============================================

#streamlit終了は
#①コントロール＋C
#または
#②exit()
#=============================================

#タイトルの入力
st.title("streamlit 超入門")

#テキストの追加
st.write("DataFrame")


#データフレームの作成・・・dict型｛｝
df= pd.DataFrame({
                    "１列目":[1,2,3,4],
                    "2列目":[10,40,30,40]
})

#データフレームの表示＿１　…テキストの追加と同じ書き方
st.write(df)

#データフレームの表示＿２　…テキストの追加と同じ書き方
st.dataframe(df,width = 100, height=100) #dataframeだと、widthやheightの指定ができる
#データフレームの表示＿２　…テキストの追加と同じ書き方
st.dataframe(df.style.highlight_max(axis = 0) ,width = 300, height=200) #列ごとのMax数値にハイライトを追加

#データフレームの表示＿３　…テキストの追加と同じ書き方
st.table(df) #静的な表が表示される

#グラフを作成する
#グラフ用データの作成・・・２０行３列の整数（ランダム）
graf_df = pd.DataFrame(
                        np.random.rand(20,3),
                        columns =["a","b","c"]
)

#折れ線グラフ・・・line_chart()
st.line_chart(graf_df)

#塗りつぶし折れ線グラフ・・・line_chart()
st.area_chart(graf_df)

#棒グラフ・・・line_chart()
st.bar_chart(graf_df)


#マッピングを作成する
#マッピング用データの作成・・・100行2列の整数（ランダム）
#[35.69,139.70]・・・東京新宿付近の緯度・経度。それにランダムで発生させた数値（５０分の１）を足し引きしたランダム数をデータとする
#coolumnsの名前は必ず"lat","lon"にしなければならない    
map_df = pd.DataFrame(
                        np.random.rand(100,2)/[50,50]+[35.69,139.70],
                        columns =["lat","lon"]
)

#マッピング
st.map(map_df)

st.write("Display Image")

#=============================================
#インタラクティブな表示（チェックボックス等と、処理分岐（if文等）を組み合わせる）
#=============================================

#チェックボックス
if st.checkbox("画像を表示する場合は、チェックボックスにチェックを入れてください"):
    #画像の読込・・・PILの読込が必要

    img = Image.open("カフェ.jpg")
    st.image(img, caption = "カフェ広告", use_container_width= True)


#セレクトボックス
option = st.selectbox("貴方の好きな数字を教えてください",
             list(range(1,11))
             )

#sr.write()しなくても、表示させることができる（なんでだよ）
"貴方の好きな数字は、", option, "です"

#テキストボックス
text= st.text_input(
                        "貴方の趣味を教えてください"
)
"貴方の趣味:",text

#スライダー
condition = st.slider('貴方のコンディションは？',0,100,50)
"コンディション:",condition

#=============================================
#ブログレスバーの表示
#=============================================

st.write("プレグレスバーの表示")
'start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"iterationゲージ:{i+1}") #タイトルと、数値の表示
    bar.progress(i+1) #ゲージバーの表示
    time.sleep(0.1) #表示速度を0.1に遅くしている

#↓以下の処理の開始を、time.sleepさせることで遅延させている

#=============================================
#レイアウトを整える
#=============================================

#サイドバー
condition_01 = st.sidebar.slider('サイドバーの貴方のコンディションは？',0,100,50)
st.sidebar.write("コンディション:",condition_01)

#２ｶﾗﾑ
left_column,right_column = st.columns(2)

#ボタンの設置
button =left_column.button("右カラムに文字を表示")

if button: #buttonが押されたら
    right_column.write("ここは右カラムです")

#エクスパンダー
expander_01 = st.expander("会社の歴史")
expander_01.write("１.変革と概要")
expander_01.write("２.今後の展望")
expander_02 = st.expander("業務内容")
expander_02.write("1.卸業")
expander_02.write("2.小売業務＿店舗")




"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

