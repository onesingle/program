#coding:utf-8
# made in 2014-03-21
#一个用来刷百度经验网页的小脚本
import urllib,re,cookielib
import urllib2
import os,random,time


def openurl(url):
    try:
        url = urllib.urlopen(url)
        text = url.read()
        p = re.compile(r'(\d+\.\d+\.\d+\.\d+)</td>\n<td>(\d+)</')
        port = re.compile(r'<td>\d+</td>')
        print 'hello world'
        ip_all = p.findall(str(text))
    except:
        print 'cant open url'
    print ip_all
    return ip_all

def proxyurl(url):
    #urllist = openurl(url)
    proxyurl = []
    for ip in url:
        #urllib.urlopen(proxy_ip)
        url =  "http://"+ ip[0] + ":"+ip[1]
        proxyurl.append(url)
    return proxyurl

#这里用python 自带的库来打开,这里先不用.
def proxy_open(des_url,proxy_url):
    header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
    }
    for ip in proxy_url:
        cj=cookielib.CookieJar()
        cookie_support=urllib2.HTTPCookieProcessor(cj)

        #opener=urllib2.build_opener(cookie_support,urllib2.HTTPBasicAuthHandler)
        proxy_handler = urllib2.ProxyHandler({'http':ip})
        opener = urllib2.build_opener(cookie_support,proxy_handler)
        opener.addheaders = [(r'User-Agent',r'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/28')]
        for  ip in des_url:
            try:
                opener.open('http://www.baidu.com')
                opener.open(ip[0])
                opener.open(ip[1])
                print "成功打开" + ip[1]
            except:
                pass
#这里用的是在命令行中打开chromium浏览器,并且启用代理.这里是要更加模仿用户
def google(des_url,proxy_url):
    print 'google'
    for ip in proxy_url[7:8]:  #这里只是举例,所以所以只选了俩个ip,

        a =os.system('mkdir /tmp/wang-'+str(ip[7:]) +' &') #创建用户data文件夹
        print a
        dir = '/tmp/wang-'+str(ip[7:])
        print dir
        for myurl in des_url:
            try:
                #这里--proxy-server是代理参数,--no-startup-window 是不启动chromium窗口,
                #--user-data-dir用户数据文件夹,启动后像是新安装浏览器
                chrome =  os.system('chromium-browser  --proxy-server='+ ip +' '+' \
                    --no-default-browse-check --no-startup-window --user-data-dir='+dir +"  " +myurl[0]+" "+myurl[1]+' &' )

                time.sleep(15)
                #杀死chromium进程

                os.system('pkill -f chromium-browser)
                #删掉用户数据缓存
                os.system('rm -r /tmp/wang-*')

                print 'file is not kill'

            except:
                print 'url not open'

#第三方数据库实现
def Request():
    header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
    }
    for ip in proxy_url:
        s = requests.Session()

        '''
        cj=cookielib.CookieJar()
        cookie_support=urllib2.HTTPCookieProcessor(cj)

        #opener=urllib2.build_opener(cookie_support,urllib2.HTTPBasicAuthHandler)
        proxy_handler = urllib2.ProxyHandler({'http':ip})
        opener = urllib2.build_opener(cookie_support,proxy_handler)
        opener.addheaders = [(r'User-Agent',r'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1')]
        '''

        for  ip in des_url:
            try:
                s.get("www.baidu.com")
                s.get(ip[0])
                s.get(ip[1])
                print "成功打开" + ip[1]
            except:
                pass


if __name__ == '__main__':

    url = 'http://cn-proxy.com/'

    des_url = [("http://www.baidu.com/s?tn=12092018_12_hao_pg\&ie=utf-8\&bs=jingyan\&f=8\&rsv_bp=1\&wd=%E5%A6%82%E4%BD%95%E5%B0%86pdf%E6%A0%BC%E5%BC%8F%E6%96%87%E4%BB%B6%E8%BD%AC%E6%88%90mobi%E6%A0%BC%E5%BC%8F\&rsv_sug3=2\&rsv_sug4=171\&rsv_sug1=1\&rsv_n=2\&rsv_sug2=0\&inputT=5","http://jingyan.baidu.com/article/2f9b480db215e341cb6cc21e.html"),
               ("http://www.baidu.com/s?word=ubuntu%E5%AE%89%E8%A3%85eclipse%2Bpydev\&tn=12092018_12_hao_pg\&ie=utf-8","http://jingyan.baidu.com/article/3a2f7c2e766f4a26aed61145.html"),
               ("http://www.baidu.com/s?word=windows+xp%E6%B8%85%E9%99%A4%E5%AF%86%E7%A0%81\&tn=12092018_12_hao_pg\&ie=utf-8","http://jingyan.baidu.com/article/922554468dff6b851748f454.html")
               ]

    urllist = openurl(url)
    proxy_url = proxyurl(urllist)
    #proxy_open(des_url,proxy_url)
    google(des_url,proxy_url)




