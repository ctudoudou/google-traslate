#https://translate.google.cn/?newwindow=1&safe=strict&biw=1366&bih=652&bav=on.2,or.r_cp.&um=1&ie=UTF-8&hl=zh-CN&client=tw-ob#en/zh-CN/father
#https://translate.google.com/translate_a/t?client=t&sl=en&tl=zh-TW&hl=zh-TW&v=1.0&source=is&tk=3479.416175&q=ask&q=asked&q=asking&q=ask%20for&q=ask%20me&q=askew&q=ask%20and%20answer&q=ask%20questions
#https://translate.google.com/translate_a/t?client=t&sl=en&tl=zh-TW&hl=zh-TW&v=1.0&source=is&tk=717124.836912&q=ask
# tk 計算 717124.836912
import urllib.request as ure
import execjs

def get_Tk(a):
    js=execjs.compile("""
function VL(a) {
        var b = a.trim();
        return "&tk="+TL(b);
}
function TL(a) {
    var k = "";
    var b = 406644;
    var b1 = 3293161072;
    var jd = ".";
    var bb = "+-a^+6";
    var Zb = "+-3^+b+-f";
    for (var e = [], f = 0, g = 0; g < a.length; g++) {
        var m = a.charCodeAt(g);
        // alert(m);
        128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
        e[f++] = m >> 18 | 240,
        e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
        e[f++] = m >> 6 & 63 | 128),
        e[f++] = m & 63 | 128)
    }
    a = b;
    for (f = 0; f < e.length; f++) a += e[f],
    a = RL(a, bb);
    a = RL(a, Zb);
    a ^= b1 || 0;
    0 > a && (a = (a & 2147483647) + 2147483648);
    a %= 1E6;
    return a.toString() + jd + (a ^ b)
};
function RL(a, b) { 
	var t = "a";
    var Yb = "+";
    for (var c = 0; c < b.length - 2; c += 3) {
        var d = b.charAt(c + 2),
        d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
        d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
        a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
    }
    return a
}
    """)
    a=js.call("VL",str(a))
    return a

def get_result(mo,word):#https://translate.google.com/translate_a/t?client=t&hl=zh-TW&v=1.0&source=is&sl=en&tl=zh-CN&tk=717124.836912&q=ask
    weburl="https://translate.google.com/translate_a/t?client=t&hl=zh-TW&v=1.0&source=is"
    webheard={
        'Connection': 'Keep-Alive',
        'Accept':'text/html,application/xhtml+xml,*/*',
        'Accept-Language':'en-US,en;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
        'Host':'translate.google.cn',
        'DNT':'1'
    }
    if mo=="1" or mo=="":
        weburl=weburl+"&sl=en&tl=zh-CN"+url_end(word)
    elif mo=="2":
        weburl=weburl+"&sl=zh-CN&tl=en"+url_end(word)
    elif mo=="3":
        weburl = weburl + "&sl=zh-CN&tl=ja" + url_end(word)
    elif mo == "4":
        weburl = weburl + "&sl=zh-CN&tl=zh-TW" + url_end(word)
    else:
        return "異常錯誤"
    re = ure.Request(url=weburl, headers=webheard)
    webPage = ure.urlopen(re)
    data = webPage.read()
    data = data.decode('UTF-8')
    print(data)

def url_end(word):
    a=ure.quote(word)
    return get_Tk(word) + "&q=" + a
if __name__=="__main__":
    while True:
        mo = input("""
請輸入要翻譯的格式所對應的數字：默認是(英->漢(简体))
1. 英->漢(简体)
2. 漢(简体)->英
3. 漢(简体)->日
4. 漢(简体)->漢(繁體)
5. 退出
""")
        if mo not in ["1", "2", "", "3", "4","5"]:
            print("請確認輸入的數字")
        elif mo=="5":
            break
        else:
            word = input("請輸入要翻譯的語言:")
            get_result(mo, word)