#!/bin/sh
# Script of LoveTacome
# Follow https://www.facebook.com/love.tacome.3

echo HTTP/1.1 301 Moved Permanently
echo Location: $HTTP_REFERER
echo Content-type: text/html
echo

LoveTacome_CGI _uploadovpn
