# The OneDrive Direct Download Link Helper

Get OneDrive direct download link by just changing the "1drv.ms" to "1drv.ws"  
通过简单地改域名， 来获取OneDrive的直接下载链接。

## Usage

1. Get the share link, like this: https://1drv.ms/u/s!Aiw77soXua44hZslqWUtBIPbWMMl4g
2. Change the domain `1drv.ms` to `1drv.ws`, I mean, just flip the **m** to **w**  
    which becomes https://1drv.ws/u/s!Aiw77soXua44hZslqWUtBIPbWMMl4g
3. This IS the direct link, you can paste it to browser and see.

btw, you can add `?txt` at the end of url, to display text link, instead of a 301 redirect.<br>
eg: https://1drv.ws/u/s!Aiw77soXua44hZslqWUtBIPbWMMl4g?txt

## How it works

https://1drv.ms/t/s!Aiw11soXua11pxigLnclZsYIU_Rx  
-- HTTP --> https://onedrive.live.com/redir?resid=...&authkey=!...&ithint=file%1ctxt  
--MODIFY--> https://onedrive.live.com/download?resid=...!1111&authkey=!...&ithint=file%1ctxt  
-- HTTP --> https://jlohlg.by.files.1drv.com/some-long-long-link/file.txt?download&psid=1

## Tips

* Play OneDrive video directly in local player (eg:PotPlayer), most player support "play from url"
* dispaly as image <img src='https://1drv.ws/u/s!Aiw77soXua44hZslqWUtBIPbWMMl4g' height="32" width="32"> `<img src='https://1drv.ws/u/s!Aiw77soXua44hZslqWUtBIPbWMMl4g'>`

## Deploy Your Self

1. Python 3.5+ is required.
2. `git clone https://github.com/aploium/OneDrive-Direct-Link`
3. `cd OneDrive-Direct-Link`
4. `pip3 install -r requirements.txt`
5. `python3 app.py`
6. Now you got this services in your localhost.

warning: this code is simple and not fool-proof.
