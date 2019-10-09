#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/7/10 下午5:37
# @Author  : tudouya (chenfengwei@jd.com)
# @Version : 1.0.0

import configparser
import smtplib
import socket
import random
from email.header import Header
from email.mime.text import MIMEText
from os.path import dirname, join
from urllib.parse import urlparse

#from apps.system.models import SMTPConfig

ROOT_DIR = dirname(dirname(__file__))


def get_file_path(*path):

    return join(ROOT_DIR, *path)


def get_redis_config():
    redis_config = get_file_path('config/redis.ini')
    config_parser = configparser.ConfigParser()
    config_parser.read(redis_config)
    redis_host = config_parser.get('redis', 'host')
    redis_port = int(config_parser.get('redis', 'port'))
    redis_password = config_parser.get('redis', 'password')
    redis_db = int(config_parser.get('redis', 'db'))

    redis_config = dict()
    redis_config['host'] = redis_host
    redis_config['port'] = redis_port
    redis_config['password'] = redis_password
    redis_config['db'] = redis_db

    return redis_config

'''
def validIPAddress(IP):
    blocks = IP.split('.')
    if len(blocks) == 4:
        for i in xrange(len(blocks)):
            if not blocks[i].isdigit() or not 0 <= int(blocks[i]) < 256 or \
               (blocks[i][0] == '0' and len(blocks[i]) > 1):
                return "Neither"
        return "IPv4"

    blocks = IP.split(':')
    if len(blocks) == 8:
        for i in xrange(len(blocks)):
            if not (1 <= len(blocks[i]) <= 4) or \
               not all(c in string.hexdigits for c in blocks[i]):
                return "Neither"
        return "IPv6"
    return False

'''


def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
    except Exception as e:
        ip = None

    return ip


def url_parse(url):
    url_parse = urlparse(url)
    host_port = url_parse.netloc
    host_port = host_port.split(':')

    return host_port

'''
def send_mail(email_title, email_content, receiver):
    smtp_config_result = SMTPConfig.objects.all()
    smtp_config = random.choice(smtp_config_result)

    smtp_host = smtp_config.server
    smtp_port = smtp_config.port
    smtp_user = smtp_config.user
    smtp_passwd = smtp_config.passwd
    sender_name = smtp_config.sender_name
    sender_email = smtp_config.sender_email

    if not sender_name:
        sender_name = sender_email

    sender = '568865013@qq.com'

    message = MIMEText(email_content, 'html', 'utf-8')
    message['From'] = Header(sender_name, 'utf-8')
    message['To'] = Header(receiver, 'utf-8')

    subject = email_title
    message['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP(smtp_host)
    smtp.login(smtp_user, smtp_passwd)
    smtp.sendmail(sender_email, receiver, message.as_string())
'''