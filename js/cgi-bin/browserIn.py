#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import collections as cl
import cgi, cgitb


def main():
    cgitb.enable()

    form = cgi.FieldStorage()
    text = form.getfirst("text")
    n = form.getfirst("number")

    a = 3
    #sequence_list = []
    #print('Content-type: text/html\nAccess-Control-Allow-Origin: *\n')
    


    fw = open('data.json','w')
    #ココ重要！！
    # json.dump関数でファイルに書き込む
    json.dump(n,fw,indent=4)




if __name__=='__main__':
    main()
