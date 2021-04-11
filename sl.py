# -*- coding:utf-8 -*-
import os
import re
import time


class SaveAndLoad(object):
    def __init__(self):
        with open(r'./sl.txt', encoding='utf-8') as f:
            a = f.read()
            b = re.findall(r'游戏的存档地址:(.*)', a)
            c = re.findall(r'你希望保存在哪的地址:(.*)', a)
            self.s = ''.join(b)
            self.l = ''.join(c)

    def save(self):
        写入 = str(input('请输入要保存的存档栏位(数字):'))
        a = os.listdir(self.s)
        ls = []
        for i in range(len(a)):
            if b := re.findall(r'survival_\d$|shipwrecked_\d$|porkland_\d$|cave_\d_\d_\d$|volcano_\d$', a[i]):
                ls.append(b[0])
        ls1 = ' '.join(ls)
        if 写入 in ls1:
            for i in range(len(ls)):
                if ls[i][-1] == 写入:
                    if 主世界 := re.findall(r'survival_\d$|shipwrecked_\d$|porkland_\d$', ls[i]):
                        描述 = input('请输入要存档描述:')
                        with open(self.s + r"\%s" % 主世界[0], encoding='utf-8') as f:
                            time1 = time.strftime('%Y-%m-%d')
                            标识 = "描述:" + 描述 + "  创建时间:" + time1 + ":结尾"
                            var = 标识 + f.read()
                            with open(self.l + '\%s' % ls[i], 'w') as x:
                                x.write(var)
                                print('存档成功')
                    if 地下 := re.findall(r'cave_\d_\d_\d$|volcano_\d$', ls[i]):
                        with open(self.s + r"\%s" % ls[i], encoding='utf-8') as z:
                            var1 = z.read()
                            with open(self.l + '\%s' % ls[i], 'w') as u:
                                u.write(var1)
        else:
            print("无该存档栏位")

    def load(self):
        ls = []
        a = os.listdir(self.l)
        for i in range(len(a)):
            if s := re.match(r'survival_\d$|shipwrecked_\d$|porkland_\d$', a[i]):
                with open(self.l + r'\%s' % a[i]) as f:
                    z = re.findall('描述:(.*):结尾', f.read())
                    描述 = ''.join(z)
                    print('存档描述: %s' % 描述)
        读取 = str(input('请输入要读取的存档栏位(数字):'))
        for i in range(len(a)):
            if b := re.findall(r'survival_\d$|shipwrecked_\d$|porkland_\d$|cave_\d_\d_\d$|volcano_\d$', a[i]):
                ls.append(b[0])
        ls1 = ' '.join(ls)
        if 读取 in ls1:
            for i in range(len(ls)):
                if ls[i][-1] == 读取:
                    with open(self.l + r"\%s" % ls[i]) as x:
                        var = re.sub(r'描述:.*:结尾', '', x.read())
                        with open(self.s + '\%s' % ls[i], 'w') as z:
                            z.write(var)
            print('读档成功')
        else:
            print("无该存档栏位")

    def name(self):
        while True:
            num = int(input('\n请选择存档/读档\n[1.存档]  [2.读档]\n'))
            if num == 1:
                self.save()
            elif num == 2:
                self.load()
            else:
                print("请你爬远一点")


if __name__ == '__main__':
    sl = SaveAndLoad()
    sl.name()
