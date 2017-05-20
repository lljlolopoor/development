#!/bin/bash

export DISPLAY=:0

/usr/bin/python /home/lijuan/work/up-title/up-title.py > /home/lijuan/work/up-title/run.log

mails='your_email'
mailx -s "TopPost result ---This mail is auto sent by system. please do not reply to  it! thanks!" $mails toemail1 toemail2 < /home/lijuan/work/up-title/run.log
