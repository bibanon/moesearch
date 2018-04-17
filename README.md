MoeSearch
=========

A Python library for [desuarchive.org](http://desuarchive.org/) (dump retrived from archive.moe, that was previously known as FoolzArchive) REST API.  
To be fair, actually it should work with every installation of FoolFuuka, but you have to try that.

Helpful binaries included.

Fixed from the [moesearch](https://pypi.org/project/moesearch/) library, which became broken due to a hardcoded domain. We plan to make the URL a constructor argument (so you can use it with 4plebs, rbt.asia, though not warosu, which is fuuka). We also plan to make this compatible with [the 4plebs definition of the FoolFuuka API.](https://4plebs.tech/foolfuuka/)

BEWARE
------

This software is experimental, use it at your own risk.
For those who want to try this...  
[PyPI archive](https://pypi.python.org/pypi/moesearch/)

Quickstart
--------

(You can check the executables in /bin folder).
FoolFuuka docs are available [at foolz.us](https://web.archive.org/web/20140728111047/http://www.foolz.us/docs/foolfuuka/documentation.html).  
```py
>>> import moesearch
>>> print(moesearch.search(board="a", text="woxxy")[2].comment)
>>112732805
Fuck Woxxy.
>>> print(moesearch.index("a", 1)["112834776"].op.media.media_link)
http://data.archive.moe/board/a/image/1366/74/1366741186747.jpg
>>> print(moesearch.post("a", 112766871).board.short_name)
a
>>> print(moesearch.thread("a", 112800651).posts[0].comment)
>>112800651
I fucking went grocery shopping all the time when I was a kid. I didn't have qt lesbian friends to go with though.
```

LICENSE
-------

```
        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
                    Version 2, December 2004 

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 

 Everyone is permitted to copy and distribute verbatim or modified 
 copies of this license document, and changing it is allowed as long 
 as the name is changed. 

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

  0. You just DO WHAT THE FUCK YOU WANT TO.
```
