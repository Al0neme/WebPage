# -*- coding:utf-8 -*-

import ast


# 更新链接方法，
def update_link(category_text, link_title, link_text):
    with open("category_dict.txt", "r", encoding="utf-8") as fr:
        r = fr.readlines()[0]
    category_dict = ast.literal_eval(r)  # 字符串转字典

    for i in category_dict[category_text]:
        if link_title in i:
            category_dict[category_text][category_dict[category_text].index(i)]={link_title:link_text}

    with open("category_dict.txt", "w", encoding="utf-8") as fw:
        fw.write(str(category_dict))

    return category_dict  # 新的导航目录字典


def page_update(category_text, link_title, link_text):
    # 读取模板
    f_head = []
    with open("./templates/template_index.html", "r", encoding="utf-8") as f_text:
        for i in range(12):
            f_head.append(f_text.readline())

    category_dict = update_link(category_text, link_title, link_text)

    # 更新page
    with open("./templates/index.html", "w", encoding="utf-8") as f_output:
        for i in f_head:
            f_output.write(i)  # 写入模板部分

        for i in category_dict:
            f_output.write('\t<div class="box clearfloat">\n\t  <h3>' + i + '</h3>\n\t  <ul class="listmenu">\n')
            for j in category_dict[i]:
                # 迭代获取link和title
                for k, v in j.items():
                    f_output.write(f"\t\t<li><a href=\"{v}\">{k}</a></li>\n")
            f_output.write('\t  </ul>\n\t</div>\n')

        f_output.write('\t<!-- menu ends -->\n</div>\n</body>\n</html>')