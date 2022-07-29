#!/usr/bin/env python3
"""
Author: Eshan Singh (R0X4R)
Version: 1.0.0
"""

#@> IMPORTING ALL THE DEPENDENCIES
import re
import argparse
from urllib.parse import urlparse
from sys import stdin, stdout, exit

#@> PROCESSING COMMAND LINE ARGUMENTS
parser = argparse.ArgumentParser(epilog="\tExample:\nwaybackurls sub.domain.tld | parshu")
parser._optionals.title = "OPTIONS"

#@> OPTIONS
parser.add_argument('-x', dest='xss', action='store_true', help="Filter all URLS where you check for xss.")
parser.add_argument('-r', dest='redirect', action='store_true', help="Filter all URLS where you check for open-redirect.")
parser.add_argument('-l', dest='lfi', action='store_true', help="Filter all URLS where you check for lfi.")
parser.add_argument('-s', dest='sql', action='store_true', help="Filter all URLS where you check for sqli.")
parser.add_argument('-t', dest='ssti', action='store_true', help="Filter all URLS where you check for ssti.")
parser.add_argument('-f', dest='ssrf', action='store_true', help="Filter all URLS where you check for ssrf.")
parser.add_argument('-c', dest='rce', action='store_true', help="Filter all URLS where you check for rce.")
parser.add_argument('-q', dest='query', action='store_true', help="Filter all URLS which contains query parameters.")

cmd = parser.parse_args()

#@> REGEX PATTERNS
PATTERN = "(\.asp|\.aspx|\.bat|\.cfm|\.cgi|\.css|\.dll|\.exe|\.htm|\.html|\.inc|\.jhtml|\.js|\.jsa|\.jsp|\.log|\.mdb|\.nsf|\.pcap|\.php|\.php2|\.php3|\.php4|\.php5|\.php6|\.php7|\.phps|\.pht|\.phtml|\.pl|\.reg|\.sh|\.shtml|\.sql|\.swf|\.txt|\.xml|\.ini|\,xml|\.bat|\.LOG|\.tn|\.bak|\.sql)"
XSS_REGEX = "(api=|api_key=|begindate=|callback=|=|categoryid=|csrf_token=|email=|emailto=|enddate=|id=|imagine=|immagine=|item=|jsonp=|key=|keyword=|keywords=|l=|lang=|list_type=|month=|name=|p=|page=|page_id=|password=|pid=|pp=|q=|query=|s=|search=|terms=|token=|type=|unsubscribe_token=|url=|username=|view=|year=)"
RED_REGEX = "(Lmage_url=|Open=|callback=|cgi-bin/redirect.cgi|cgi-bin/redirect.cgi?|checkout=|checkout_url=|continue=|data=|dest=|destination=|dir=|domain=|feed=|file=|file_name=|file_url=|folder=|folder_url=|forward=|from_url=|go=|goto=|host=|html=|image_url=|img_url=|load_file=|load_url=|login?to=|login_url=|logout=|navigation=|next=|next_page=|out=|page=|page_url=|path=|port=|redir=|redirect=|redirect_to=|redirect_uri=|redirect_url=|reference=|return=|returnTo=|return_path=|return_to=|return_url=|rt=|rurl=|show=|site=|target=|to=|uri=|url=|val=|validate=|view=|window=)"
SQL_REGEX = "(id=|select=|report=|role=|update=|query=|user=|name=|sort=|where=|search=|params=|process=|row=|view=|table=|from=|sel=|results=|sleep=|fetch=|order=|keyword=|column=|field=|delete=|string=|number=|filter=)"
STI_REGEX = "(template=|preview=|id=|view=|activity=|name=|content=|redirect=)"
SRF_REGEX = "(access=|admin=|dbg=|debug=|edit=|grant=|test=|alter=|clone=|create=|delete=|disable=|enable=|exec=|execute=|load=|make=|modify=|rename=|reset=|shell=|toggle=|adm=|root=|cfg=|dest=|redirect=|uri=|path=|continue=|url=|window=|next=|data=|reference=|site=|html=|val=|validate=|domain=|callback=|return=|page=|feed=|host=|port=|to=|out=|view=|dir=|show=|navigation=|open=|file=|document=|folder=|pg=|php_path=|style=|doc=|img=|filename=)"
LFI_REGEX = "(file=|document=|folder=|root=|path=|pg=|style=|pdf=|template=|php_path=|doc=|page=|name=|cat=|dir=|action=|board=|date=|detail=|download=|prefix=|include=|inc=|locate=|show=|site=|type=|view=|content=|layout=|mod=|conf=|url=)"
RCE_REGEX = "(daemon=|upload=|dir=|download=|log=|ip=|cli=|cmd=|exec=|command=|execute=|ping=|query=|jump=|code=|reg=|do=|func=|arg=|option=|load=|process=|step=|read=|function|req=|feature=|exe=|module=|payload=|run=|print=)"

try:
    if stdin.isatty():
        exit(0)
        
    if cmd.xss:
        for URL in stdin.readlines():
            """
            STDOUT all the URLS which contains xss parameters.
            """
            link = str(URL.strip())
            if re.search(XSS_REGEX, link):
                stdout.write(re.sub(r"'|(|)", "", link) + '\n')

    elif cmd.redirect:
        for URL in stdin.readlines():
            """
            STDOUT all the URLS which contains open-redirect parameters.
            """
            link = str(URL.strip())
            if re.search(RED_REGEX, link):
                stdout.write(re.sub(r"'|(|)", "", link) + '\n')
    
    elif cmd.lfi:
        for URL in stdin.readlines():
            """
            STDOUT all the URLS which contains lfi parameters.
            """
            link = str(URL.strip())
            if re.search(LFI_REGEX, link):
                stdout.write(re.sub(r"'|(|)", "", link) + '\n')
    
    elif cmd.sql:
        for URL in stdin.readlines():
            """
            STDOUT all the URLS which contains sql parameters.
            """
            link = str(URL.strip())
            if re.search(SQL_REGEX, link):
                stdout.write(re.sub(r"'|(|)", "", link) + '\n')
    
    elif cmd.ssti:
        for URL in stdin.readlines():
            """
            STDOUT all the URLS which contains ssti parameters.
            """
            link = str(URL.strip())
            if re.search(STI_REGEX, link):
                stdout.write(re.sub(r"'|(|)", "", link) + '\n')
    
    elif cmd.ssrf:
        for URL in stdin.readlines():
            """
            STDOUT all the URLS which contains ssrf parameters.
            """
            link = str(URL.strip())
            if re.search(SRF_REGEX, link):
                stdout.write(re.sub(r"'|(|)", "", link) + '\n')
    
    elif cmd.rce:
        for URL in stdin.readlines():
            """
            STDOUT all the URLS which contains rce parameters.
            """
            link = str(URL.strip())
            if re.search(RCE_REGEX, link):
                stdout.write(re.sub(r"'|(|)", "", link) + '\n')

    elif cmd.query:
        for URL in stdin.readlines():
            """
            STDOUT all the URLS which contains query parameters.
            """
            link = str(URL.strip())
            if re.search("(=|&)", link):
                stdout.write(re.sub(r"'|(|)", "", link) + '\n')
    
    else:
        for URL in stdin.readlines():
            """
            STDOUT all the URLS except which contains query parameters and files.
            """
            links = re.split('/', urlparse(URL.strip()).path)[-1]

            if re.search(PATTERN, links):
                output = re.sub(r"([^/\\]+)(\.php|\.p|\%|\.asp|\.aspx|\.bat|\.cfm|\.cgi|\.css|\.dll|\.exe|\.htm|\.html|\.inc|\.jhtml|\.js|\.jsa|\.jsp|\.log|\.mdb|\.nsf|\.pcap|\.php2|\.php3|\.php4|\.php5|\.php6|\.php7|\.phps|\.pht|\.phtml|\.pl|\.reg|\.sh|\.shtml|\.sql|\.swf|\.txt|\.xml|\.ini|\,xml|\.bat|\.LOG|\.tn|\.bak|\.sql).*", "", str(URL.strip()))
                stdout.write(re.sub(r"'|(|)", "", output) + '\n')

            elif re.search(r"(&|=|\?|\%)", URL.strip()):
                pass

            else:
                link= urlparse(URL.strip()).scheme + "://" + urlparse(URL.strip()).netloc + urlparse(URL.strip()).path
                output = re.sub(r"([^/\\]+)(\.php|\.p|\%).*", "", link)
                stdout.write(str(re.sub(r"'|(|)", "", output)) + '\n')
except KeyboardInterrupt:
    exit(0)
except:
    pass
