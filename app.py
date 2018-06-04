# coding=utf-8
import requests
from flask import Flask, Response

app = Flask(__name__)


@app.route('/t/s!<ts_token>')
def share_ts(ts_token):
    session = requests.Session()
    url_step1 = 'https://1drv.ms/t/s!' + ts_token
    resp_step1 = session.get(url_step1, timeout=10, allow_redirects=False)
    url_step2 = resp_step1.headers['Location']
    url_step3 = url_step2.replace('/redir?', '/download?')
    resp_step3 = session.get(url_step3, timeout=10, allow_redirects=False)
    url_final = resp_step3.headers['Location']

    return Response(url_final,
                    status=302,
                    headers={'Location': url_final},
                    mimetype='text/plain',
                    )


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
1. Get the share link, like this: https://1drv.ms/t/s!sOme1Ra4dCh1r_aB<br>
2. Change the <b>1drv.ms</b> to <b>1drv.ws</b>, I mean, just flip the <b>m</b> to <b>w</b><br>
which becomes https://1drv.<b>w</b>s/t/s!sOme1Ra4dCh1r_aB<br>
3. This IS the direct link, you can paste it to browser and see.<br>
</p>
<hr>
<h2>How it works</h2>
<pre>
https://1drv.ms/t/s!Aiw11soXua11pxigLnclZsYIU_Rx
-- HTTP --> https://onedrive.live.com/redir?resid=...&authkey=!...&ithint=file%1ctxt
--MODIFY--> https://onedrive.live.com/download?resid=...!1111&authkey=!...&ithint=file%1ctxt
-- HTTP --> https://jlohlg.by.files.1drv.com/some-long-long-link/file.txt?download&psid=1
</pre>
</body>
</html>
"""


if __name__ == '__main__':
    app.run()
