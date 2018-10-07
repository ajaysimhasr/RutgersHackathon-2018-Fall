#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 15:05:33 2018

@author: ajaysimha
"""

import urllib.request, json
import pandas as pd

with urllib.request.urlopen("http://pru-mock.herokuapp.com/HackRUData.json") as url:
    data = json.loads(url.read())

    df = pd.DataFrame(data)


email = input() # this will be from the chat input api. Eg: User Name

row_id = df[df['email']==email].index[0]

firstName = df.iloc[row_id].firstName
#print(firstName)

lastName = df.iloc[row_id].lastName
#print(lastName)

street = df.iloc[row_id].street
city = df.iloc[row_id].city
state = df.iloc[row_id].state
zip_ = str(df.iloc[row_id].zip)
address = street + ', ' + city + ', ' + state + ' - ' + zip_
#print(address)

phone = df.iloc[row_id].phone
#print(phone)

email = df.iloc[row_id].email
#print(email)

accountNumber = df.iloc[row_id].accountNumber
#print(accountNumber)

accountBalance = df.iloc[row_id].accountBalance
#print(accountBalance)

policyType = df.iloc[row_id].policyType
#print(policyType)

policyStatus = df.iloc[row_id].policyStatus
#print(policyStatus)
