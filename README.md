# Description
X9 is an automated xss discovery tool. 

- All you need is a list of urls and a wordlist.
- x9 will use nuclei and the custom template to look for xss sinks inside the DOM.

# Usage:

Install Nuclei: https://github.com/projectdiscovery/nuclei

`python3 main.py -l [URL LIST] -w [PARAMETERS WORDLIST] -gs [append - combine - replace]`

help attributes:

  - -debug disable silent mode for Nuclei
  - -l list of urls
  - -w Specify the wordlist
  - -wb [Get Wayback Data] (NOT WORKING YET)
  - -m Specify number of chunks. Default: 150
  - -gs Combining parameter format: combine - append - replace - all
  - -t Specify number of Threads. Default: 10
  - -tc Specify number of chunks for each temp file. Default: 10000

