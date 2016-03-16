# -*- coding: cp936 -*-
#coding = utf-8
import re
import urllib

url_top = "http://tieba.baidu.com/f?kw=%C0%CF%CC%EC%CF%C2&fr=index"
picnum = 0

#��ȡָ����ҳ�е�html
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#��ȡ��ҳ�е�img�ļ�
def getImg(html):
    global picnum
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre =re.compile(reg)
    imglist = re.findall(imgre,html)
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % picnum)
        picnum+=1
    return picnum

#��ȡ��ҳ��ҳ���е���ҳ��
def getImgNum(html):
    #<a href="/p/3215166874?pn=4340">βҳ</a>
    reg = r'<a href="\/p\/.+=(\d+)">.+</a>'
    pagere =re.compile(reg)
    pagelist = re.findall(pagere,html)
    return pagelist
def getPostNum(html):
##<a href="/p/4121689629" title="�󳯻�Ϧʰ�������ݣ����򶼿���" target="_blank" class="j_th_tit ">
    reg = r'<a href="\/p\/(\d+)" title='#ƥ��������ַ�������ֵ�����ʽ
    pagere =re.compile(reg)
    pnumlist = re.findall(pagere,html)
##    print len(pnumlist)
    pnumlist = list(set(pnumlist))#ȥ��
##    print len(pnumlist)
    return pnumlist

def getPostUrl(l_postnum):
    l_posturl = []
    page_head = "http://tieba.baidu.com/p/"
##    print page_head
    for ipnum in l_postnum:
        ipage = page_head+ipnum
##        print ipage
        l_posturl.append(ipage)
    return l_posturl

def getPostImgFile(l_url):
    for iurl in l_url:
        print iurl
        ihtml = getHtml(iurl)
        l_numstr = getImgNum(ihtml)
        print l_numstr
        l_numint = map(eval, l_numstr)#�ַ����б�ת�����б�
        if len(l_numint):
            max_urlnum = max(l_numint)
            for ipage in range(1,max_urlnum+1):
                url_page = "?pn=%d"%ipage
                ijurl = iurl + url_page
                print ijurl
                ihtml = getHtml(ijurl)
                print getImg(ihtml)
        else:
            print "Empty page list."
            

if __name__ == '__main__':
    html = getHtml(url_top)
    l_postnum = getPostNum(html)#��ȡҳ�������б�
    l_posturl = getPostUrl(l_postnum)
    getPostImgFile(l_posturl)
