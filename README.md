# ￼Exercise Definition
## Constraints
When writing your solution, please abide by the following conditions:
* Your code should be original and not taken from any other source, online or otherwise. If you do use external code, please indicate that clearly in your solution.
* Code should be written to be compatible with a Python 2.x version no later than 2.6. Please indicate the version of Python you’ve used for development and testing.
* You may use any of the Python standard library, but no other third-party libraries.
## Background
Imagine that a company ExampleCo provides shared web hosting services to multiple customers for the purposes of serving static files (for example, image or movie files). The hosting is provided under a single website where each customer has their own top-level directory.
￼￼￼The names of the customer directories may be any valid directory name. The directory structure beneath each customer’s directory is under the customer’s own control.
ExampleCo charges its customers on a monthly basis based on the total bytes transmitted in response to requests for their files. The entire website is served from a single webserver instance. It generates a set of access log files in the standard Apache Combined Log Format and these log files contain a line for each HTTP request which is made to the server. A summary of this log file format is contained in a later section.
## ￼Requirements
The aim of the exercise is to produce a Python script to process a set of access log files and produce a report containing three types of statistics. The values required are:
1. The percentage of requests that were referred from off-site.
2. The total number of GB of responses served per top-level customer directory.
3. The top 10 URLs sorted by number of requests, including the number of requests for each.
The script should take a directory as a command-line argument and it should assume all files in this directory are access log files. The Apache Combined Log Format used for these files is covered in more detail in the following section.
The script should process all such log files, calculate the above statistics across all log entries so found and finally print the statistics to standard output. You may assume that the script is to be run by systems administrators rather than general users, but that they will not be familiar with Python so output such as stack backtraces should be avoided.
## Clarifications
When calculating the statistics, the following clarifications should also be taken into account:
* For the purposes of this script, the definition of an off-site request is one where the hostname portion of the referrer URL is not example.com or a subdomain thereof. For example a request with a referrer URL of http://www.website.com/site/index.html would count as off-site, whereas a request from http://host4.example.com/catalogue.html would not.
* The total number of GB should be produced per top-level directory. Each total should include the bytes for every request for a file within that directory – this includes error responses such as 404. For the purposes of this exercise, 1GB is calculated as 1,000,000,000 bytes.
* The top 10 URLs by number of requests should only take account of requests that resulted in 2xx responses – any error requests (e.g. 404) should not be counted.
* All requests may be treated identically irrespective of method (e.g. GET, POST, PUT, etc.).
￼An example of the style of output to be produced for some sample data is shown below:
    ￼￼￼￼￼￼￼￼Off-site requests: 3920 of 12000 (32.67%)

    Top 10 URLs:
               32 - /greenace/data/muskellunge.lst
               29 - /sunhouse/proficiently.php
               25 - /sandanfase/movies/courser.mov
               25 - /ontozoom/data/stereophonic.dat
               25 - /greenace/movies/sneezed.avi
               25 - /greenace/data/restfullest.lst
               24 - /sunhouse/warm.php
               24 - /sandanfase/resources/schoolbook.dat 24 - /ontozoom/images/towers.png
               24 - /ontozoom/images/guests.jpg
    Customer usage summary:
             0.03 GB - fixlab
             7.85 GB - sunhouse
             0.10 GB - icecode
             1.49 GB - namcom
             0.30 GB - groovecorporation
             5.11 GB - zathtam
             6.47 GB - ontozoom
             0.10 GB - careity
             1.40 GB - recore
             0.78 GB - medron
             7.85 GB - greenace
             0.02 GB - canetone
             0.28 GB - fincom
             3.16 GB - freshfax
             4.94 GB - latstrip
             0.00 GB - roundplus
             0.01 GB - citycity
             0.77 GB - joyline
             6.07 GB - sandanfase
             3.06 GB – mediaplus
## ￼Access Log Format
The format of the access logs is a space-separated list of fields, some of which are enclosed in double-quotes. The list of fields is:
* IP address – the IP address of the client machine performing the request.
* RFC-1413 ID – the identity of the remote user, can be assumed to always be “-” in these logs.
* User ID – the logged in user, can be assumed to always be “-” in these logs.
* Time – the time of the request in the form [DD/MM/YYYY:hh:mm:ss +ZZZZ] where ZZZZ is the time zone specification in a four-digit offset from UTC.
* Request – the request method, URL and HTTP version enclosed in quotes (e.g. “GET /path HTTP/1.1”).
* Status – the HTTP status code of the response as an integer (e.g. 200). Bytes – the total number of bytes in the response sent.
* Referrer – the content of the Referer header enclosed in quotes. This indicates the URL of the page which linked to the resource being requested.
* User-Agent – the content of the User-Agent header enclosed in quotes. This is a string identifying the client application making the request.
If a double-quote character occurs in a double-quoted field, it is escaped by prefixing it with a backslash. Similarly, backslash characters themselves are represented by a double- backslash.
A sample log line in this format is shown below (note that it is wrapped for space reasons here, but it represents a single line in the real log file):
￼￼￼￼￼￼    171.3.142.225 - - [12/07/2011:00:15:32 +0000] "GET /ontozoom/data/cepheid.dat HTTP/1.1" 200 8871065 "http://www.fixlab.com/cherry.html" "Mozilla/4.5 RPT-HTTPClient/0.3- 2"
