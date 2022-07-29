<h1 align="center">
  <br>
  <a href="https://github.com/R0X4R/Parshu"><img src=".github/static/logo.png" width="50%" alt="Parshu logo"></a>
</h1>

<h4 align="center"><b>Filter URLs to save your time using regex</b></h4><br>

<p align="center">
  <a href="https://github.com/R0X4R/Parshu/releases">
    <img src="https://img.shields.io/github/release/R0X4R/Parshu.svg?label=version">
  </a>
  <a href="#"><img src="https://madewithlove.org.in/badge.svg"></a>
<a href="https://twitter.com/R0X4R/"><img src="https://img.shields.io/badge/twitter-%40R0X4R-blue.svg"></a>
<a href="https://github.com/R0X4R/Garud/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/R0X4R/Parshu/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="https://github.com/R0X4R?tab=followers"><img src="https://img.shields.io/badge/github-%40R0X4R-orange"></a>
  <a href="https://github.com/R0X4R/Parshu/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues-closed-raw/R0X4R/Parshu?color=dark-green&label=issues%20fixed">
  </a>
  <a href="https://travis-ci.com/R0X4R/Parshu">
      <img src="https://img.shields.io/travis/com/R0X4R/Parshu.svg?color=dark-green&label=tests">
  </a>
</p>

<p align="center"><img src=".github/static/usage.png" alt="Parshu usage"></p>

---

**Parshu** uses regex to filter out the custom results. Remembering every regex or writing regexes for a task which you do daily is not easy, so **parshu** will help you to automate the task.

_Inspired from [tomnomnom's gf](https://github.com/tomnomnom/gf) tool_

### Features
- You can also add your custom regex to get results
- Filter out all the query parameters which you use to check vulnerabilities

### Installation


```console
$ pip3 install parshu
```

```console
$ wget -O parshu https://raw.githubusercontent.com/R0X4R/Parshu/main/parshu.py -q && chmod +x parshu && mv parshu /usr/bin/
```

### Usage

<p align="center"><img src=".github/static/usage-2.png" alt="Parshu usage"></p>

+ **For `linux`, `unix` and `debian` based systems**

    ```console
    $ waybackurls sub.domain.tld | parshu

    http://sub.domain.tld/wvstests/
    http://sub.domain.tld/wvstests/pmwiki_2_1_19
    http://sub.domain.tld/wvstests/pmwiki_2_1_19/scripts
    http://sub.domain.tld/wvstests/pmwiki_2_1_19/scripts/
    ```

+ **For `windows` based systems**

    ```console
    cmd> type urls.txt | python3 parshu.py
    ```

+ **If `no arguments` passed**

    ```console
    $ waybackurls sub.domain.tld | parshu

    http://sub.domain.tld/wvstests/
    http://sub.domain.tld/wvstests/pmwiki_2_1_19
    http://sub.domain.tld/wvstests/pmwiki_2_1_19/scripts
    http://sub.domain.tld/wvstests/pmwiki_2_1_19/scripts/
    ```

+ **To filter out the results for xss**

    > **Note**: To get parameters for other vulnerabilites use other arguments. To get all the arguments use `parshu -h`

    ```console
    $ waybackurls testphp.vulnweb.com | parshu -x

    http://testphp.vulnweb.com/artists.php?artist=1
    http://testphp.vulnweb.com/showimage.php?file=./pictures/1.jpg
    http://testphp.vulnweb.com/showimage.php?file=./pictures/1.jpg&size=160
    ```

### Donate
If this tool helped you or you like my work

</br><a href="https://www.buymeacoffee.com/R0X4R"><img src="https://img.buymeacoffee.com/button-api/?text=Help me to buy oscp&emoji=😇&slug=R0X4R&button_colour=5F7FFF&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00"/></a> <a style=" width: 135px; background-color: #1065b7; text-align: center; font-weight: 800; padding: 11px 0px; color: white; font-size: 12px; display: inline-block; text-decoration: none; " href='https://pmny.in/bIKNZngt4ys1'> Donate Now </a> <a href="https://ko-fi.com/i/IK3K34SJSA"><img src="https://ko-fi.com/img/githubbutton_sm.svg"></a><br/><br/>