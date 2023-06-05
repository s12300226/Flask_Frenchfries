"""
/にリクエストがあった時の処理


URLにアクセスがあった時の処理
@app.route(URL)
def xxx():
    処理

"""
from flask import request, url_for, render_template, flash, session,redirect

from flask_blog import app

@app.route('/test')
def show_tests():
    # templates/entries/index.htmlを返す設定
    return render_template('entries/test.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        # username = request.form['username']
        if request.form['username']!=app.config['USERNAME']:
            flash('ユーザー名がちがうよ！')
        elif request.form['password']!= app.config['PASSWORD']:
            flash('パスワードが違うよ！')
        else:
            # ログイン成功したらログイン状態に設定
            # user_name = request.form['username']
            # print(user_name)
            session['logged_in'] = True
            flash('ログインしました')
            # ホームへ移動
            return redirect(url_for('show_entries'))
    print('-------------------------')
    return render_template('login.html')
    
@app.route('/logout')
def logout():
    """
    ログアウト処理
    """
    session.pop('logged_in',None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))

