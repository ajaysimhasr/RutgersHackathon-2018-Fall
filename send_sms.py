#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 16:38:23 2018

@author: ajaysimha
"""

from twilio.rest import Client
from receive_sms import sms_reply

account_sid = 'AC98f9c9f7398d39e60ce1fb59dd3f8b2b'
auth_token = 'bb0a8423dacc34ca395d8f3be08bc61c'

client = Client(account_sid, auth_token)

client.messages.create(
        to = '+12013493160',
        from_ = '+19292039742',
        body = 'This is my first twilio text message'
        )