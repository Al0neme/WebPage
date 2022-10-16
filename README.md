# WebPage

基于python+flask实现的轻量简单网页导航

## 前言

自己搜藏了很多链接，也装过插件或者找一些在线网站保存，但是用别人的始终害怕哪一天跑路了导致自己找不回这些东西，就简单写了个这个，前端语言不是很熟，python也只是脚本水平，勉强够自己用

## Install

安装flask

```
pip install flask
```

下载源码，启动

```
git clone https://github.com/Al0neme/WebPage.git
cd WebPage
python app.py
```

导航地址：`http://xx.xx.xx:5000/`，登录路由为`/login`，用户名密码：`admin/123`，采用硬编码，可在app.py文件中修改

## 效果

导航主页

![webpage-index](https://raw.githubusercontent.com/Al0neme/StaticFiles/main/webpage-demo-1.png)

登录

![webpage-login](https://raw.githubusercontent.com/Al0neme/StaticFiles/main/webpage-demo-2.png)

添加链接

![webpage-add-link](https://raw.githubusercontent.com/Al0neme/StaticFiles/main/webpage-demo-3.png)

## 后续

目前功能单一，有时间慢慢优化吧

### 已实现功能

- 登录

- 添加链接

### 待实现功能

- 删除和修改链接信息
- 自定义更新分类（目前分类写死在category_dict.txt中，添加只能手动修改文件）
- UI优化
- ...
