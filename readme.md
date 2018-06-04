# The OneDrive Direct Download Link Helper

Get OneDrive direct download link by just changing the "1drv.ms" to "1drv.ws"  
通过简单地改域名， 来获取OneDrive的直接下载链接。

## Example

1. Get the share link, like this: https://1drv.ms/t/s!sOme1Ra4dCh1r_aB (fake link)
2. Change the domain `1drv.ms` to `1drv.ws`, I mean, just flip the **m** to **w**  
    which becomes https://1drv.ws/t/s!sOme1Ra4dCh1r_aB
3. This IS the direct link, you can paste it to browser and see.

## How it works

https://1drv.ms/t/s!Aiw11soXua11pxigLnclZsYIU_Rx  
-- HTTP --> https://onedrive.live.com/redir?resid=...&authkey=!...&ithint=file%1ctxt  
--MODIFY--> https://onedrive.live.com/download?resid=...!1111&authkey=!...&ithint=file%1ctxt  
-- HTTP --> https://jlohlg.by.files.1drv.com/some-long-long-link/file.txt?download&psid=1

## Deploy Your Self

1. Python 3.5+ is required.
2. `git clone https://github.com/aploium/OneDrive-Direct-Link`
3. `cd OneDrive-Direct-Link`
4. `pip3 install -r requirements.txt`
5. `python3 app.py`
6. Now you got this services in your localhost.

warning: this code is simple and not fool-proof.
