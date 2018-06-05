# coding=utf-8
import requests
from flask import Flask, request, redirect
from cachetools.func import ttl_cache

app = Flask(__name__)


@ttl_cache(1024, ttl=600)
def get_direct_url(ch, share_token):
    url_step1 = 'https://1drv.ms/{ch}/s!{share_token}'.format(
        ch=ch,  # the ch could be w u t or more
        share_token=share_token
    )
    resp_step1 = requests.get(url_step1, timeout=10, allow_redirects=False)
    url_step2 = resp_step1.headers['Location']
    url_step3 = url_step2.replace('/redir?', '/download?')
    resp_step3 = requests.get(url_step3, timeout=10, allow_redirects=False)
    url_final = resp_step3.headers['Location']

    return url_final


@app.route('/<ch>/s!<share_token>')
def share_ts(ch, share_token):
    url_direct = get_direct_url(ch, share_token)

    if 'txt' in request.args:
        # display plain text
        return url_direct
    else:
        # 301 redirect
        return redirect(url_direct, code=301)


@app.route('/')
def index():
    return """<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>The OneDrive Direct Download Link Helper</title>
<meta name="keywords" content="OneDrive,direct,download,link,OneDrive direct download"/>
<meta name="description" content="Get OneDrive direct download link by just changing the 1drv.ms to 1drv.ws"/>
</head>
<body>
<h1>The OneDrive Direct Download Link Helper</h1>
<p>Get OneDrive direct download link by just changing the "1drv.ms" to "1drv.ws"</p>
<p>Example: <br>
1. Get the share link, like this: <code>https://1drv.ms/t/s!sOme1Ra4dCh1r_aB</code> (fake link)<br>
2. Change the domain <b>1drv.ms</b> to <b>1drv.ws</b>, I mean, just flip the <b>m</b> to <b>w</b><br>
which becomes <code>https://1drv.<b>w</b>s/t/s!sOme1Ra4dCh1r_aB</code><br>
3. This <b>IS</b> the direct link, you can paste it to browser and see.<br>
</p>
<p>btw, you can add <code>?txt</code> at the end of url, to display text link, instead of a 301 redirect.<br>
eg: <code>https://1drv.<b>w</b>s/t/s!sOme1Ra4dCh1r_aB?<b>txt</b></code>
</p>
<hr>
<h2>How it works</h2>
<pre>
https://1drv.ms/t/s!Aiw11soXua11pxigLnclZsYIU_Rx
-- HTTP --> https://onedrive.live.com/redir?resid=...&authkey=!...&ithint=file%1ctxt
--MODIFY--> https://onedrive.live.com/<em>download</em>?resid=...!1111&authkey=!...&ithint=file%1ctxt
-- HTTP --> https://jlohlg.by.files.1drv.com/some-long-long-link/file.txt?download&psid=1
</pre>
<hr>
<p>More Info: <a href='https://github.com/aploium/OneDrive-Direct-Link'>GitHub OneDrive-Direct-Link</a></p>
</body>
</html>
"""


if __name__ == '__main__':
    app.run()
