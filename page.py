# -*- coding:utf-8 -*-

import ast

# 获取已经保存的link
def get_links():
    with open("category_dict.txt","r",encoding="utf-8") as fr:
        r = fr.readlines()[0]
    category_dict = ast.literal_eval(r)

    return category_dict

def get_page():
    category_dict = get_links()

    # 读取模板 
    f_head = []
    with open("./templates/template_index.html","r",encoding="utf-8") as f_text:
        for i in range(11):
            f_head.append(f_text.readline())

    # 更新page
    with open("./templates/index.html","w",encoding="utf-8") as f_output:
        for i in f_head:
            f_output.write(i)

        for i in category_dict:
            f_output.write('\t<div class="box clearfloat">\n\t  <h3>'+i+'</h3>\n\t  <ul class="listmenu">\n')
            for j in category_dict[i]:
                for k,v in j.items():
                    f_output.write(f"\t\t<li><a href=\"{v}\">{k}</a></li>\n")    
            f_output.write('\t  </ul>\n\t</div>\n')
        
        f_output.write('\t<!-- menu ends -->\n</div>\n</body>\n</html>')