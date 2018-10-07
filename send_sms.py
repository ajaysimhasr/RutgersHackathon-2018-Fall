#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 16:38:23 2018

@author: ajaysimha
"""

from twilio.rest import Client

account_sid = 'Axxxxxxxxxxxxxxxxx'
auth_token = 'bbzzzzzzzzzzzzzzzzz'

client = Client(account_sid, auth_token)

client.messages.create(
        to = '+12222222222',
        from_ = '+1234567894',
        body = 'This is my first twilio text message'
        )
