from flask import Flask, render_template, request, redirect
#static_folderの設定をしていた。
app = Flask(__name__)
if __name__ == '__main__':
    # 環境変数からポート番号を取得（なければデフォルト値5000を使用）
    port = int(os.environ.get("PORT", 5000))
    # 全てのIPアドレスでリッスン
    app.run(host='0.0.0.0', port=port)
    # これでLAN内の他のデバイスからマシンのIPアドレスを使ってアクセス可能

@app.route('/')
def indexget():
    return render_template('index.html')#htmlファイルの表示

@app.route('/page1', methods=['POST'])#POSTの処理
def get_page():
    selected_option = request.form.get('options')#どちらのページに移動するか選択
    if selected_option == 'pageS1':
        return redirect('/pageS1')
    elif selected_option == 'pageK1':
        return redirect('/pageK1')
    else:
        return redirect('/')

@app.route('/pageS1', methods=['GET','POST']) #GETとPOSTをリクエストできるようにする
def S1get():
    return render_template('pageS1.html') 

def S1post():
    if request.method == 'POST': #POSTの処理
      screen_name = request.form['screen_name'] #formのname属性を取得
      return render_template('pageS1.html', screen_name=screen_name) #screen_nameを代入
    return  render_template('pageS1.html')

@app.route('/pageS2', methods = ["GET" , "POST"]) 
def S2get():
    return render_template('pageS2.html') 

def S2post():
    if request.method == 'POST': 
      screen_name = request.form['screen_name'] 
      return render_template('pageS2.html', screen_name=screen_name) 
    return render_template('pageS2.html')

@app.route('/pageS3', methods = ["GET" , "POST"]) 
def S3get():
    return render_template('pageS3.html') 

def S3post():
    if request.method == 'POST': 
      screen_name = request.form['screen_name'] 
      return render_template('pageS3.html', screen_name=screen_name) 
    return render_template('pageS3.html')

@app.route('/pageS4', methods = ["GET","POST"]) 
def S4get():
    return render_template('pageS4.html') 

def S4post():
    if request.method == 'POST':
      screen_name = request.form['screen_name'] 
      return render_template('pageS4.html', screen_name=screen_name) 
    return render_template('pageS4.html')

@app.route('/pageK1', methods = ["GET"]) 
def K1get():
    return render_template('pageK1.html') 

@app.route('/pageK1result',methods=["GET","POST"])
def K1resultget():
    return render_template('pageK1result.html')

def K1resultpost():
    if request.method == 'POST': 
      screen_name = request.form['screen_name'] 
      return render_template('pageK1result.html', screen_name=screen_name) 
    return render_template('pageK1result.html')

@app.route('/pageK2',methods=["GET","POST"])
def K2get():
    return render_template('pageK2.html')

@app.route('/pageK2result',methods=["GET","POST"])
def K2resultget():
    return render_template('pageK2result.html')

def K2resultpost():
    if request.method == 'POST': 
      screen_name = request.form['screen_name'] 
      return render_template('pageK2result.html', screen_name=screen_name) 
    return render_template('pageK2result.html')

@app.route('/pageK3',methods=["GET","POST"])
def K3get():
    return render_template('pageK3.html')

@app.route('/pageK3result',methods=["GET","POST"])
def K3resultget():
    return render_template('pageK3result.html')

def K3resultpost():
    if request.method == 'POST': 
      screen_name = request.form['screen_name'] 
      return render_template('pageK3result.html', screen_name=screen_name) 
    return render_template('pageK3result.html')

@app.route('/pageK4',methods=["GET","POST"])
def K4get():
    return render_template('pageK4.html')

@app.route('/pageK4result',methods=["GET","POST"])
def K4resultget():
    return render_template('pageK4result.html')

def K4resultpost():
    if request.method == 'POST': 
      screen_name = request.form['screen_name'] 
      return render_template('pageK4result.html', screen_name=screen_name) 
    return render_template('pageK4result.html')

if __name__ == '__main__':
    app.run()