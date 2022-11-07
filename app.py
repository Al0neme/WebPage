# -*- coding:utf-8 -*-

from flask import Flask, request, redirect, session,render_template
import add_link, del_link, update_link, page

app = Flask(__name__,template_folder="./templates",static_folder="./static")

ran_str = 'fwuigeuahdiuieygoijeiuwh'    # 通信过程加密
app.secret_key=ran_str  #对用户信息加密
app.jinja_env.auto_reload = True    # 实时更新

# 导航主页
@app.route('/')
def index():
    page.get_page()
    return  render_template('/index.html')

# 登录后台
@app.route('/login',methods=['GET',"POST"])
def login():
    if request.method=='GET':
        return render_template('/login.html')
    user=request.form.get('username')
    pwd=request.form.get('password')
    if user=='admin' and pwd=='123':
        session['user_info']=user
        return redirect('/manager')
    else:
        return redirect('/login')

# 管理链接后台
@app.route('/manager')
def manager():
    # 鉴权
    user_info=session.get('user_info')
    if not user_info:
        return redirect('/login')

    return  render_template('/manager.html')

# 添加链接
@app.route('/addlink',methods=["GET","POST"])
def addlink():
    user_info=session.get('user_info')
    if not user_info:
        return redirect('/login')
    
    # 获取添加的链接信息
    category=request.form.get('category')
    title=request.form.get('title')
    urladdr=request.form.get('urladdr')
    
    if not title or not urladdr:
        return redirect('/manager')

    # 更新导航页面
    add_link.page_update(category,title,urladdr)
    return redirect('/manager')

# 修改链接
@app.route('/updatelink', methods=["GET", "POST"])
def updatelink():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')

    # 获取添加的链接信息
    category = request.form.get('category')
    title = request.form.get('title')
    urladdr = request.form.get('urladdr')

    if not title or not urladdr:
        return redirect('/manager')

    # 更新导航页面
    update_link.page_update(category, title, urladdr)
    return redirect('/manager')

# 删除链接
@app.route('/dellink', methods=["GET", "POST"])
def dellink():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')

    # 获取删除的链接信息
    category = request.form.get('category')
    title = request.form.get('title')

    if not title:
        return redirect('/manager')

    # 更新导航页面
    del_link.page_update(category, title)
    return redirect('/manager')


# 退出
@app.route('/logout')
def logout_():
    del session['user_info']
    return redirect('login')


if __name__ == "__main__":
    # app.run(debug=True) # debug模式，调试开启
    app.run()