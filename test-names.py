#!/usr/local/bin/python3.7

import os
import pandas
import random
import sys


male_name     = pandas.read_csv('boys_names.csv')
female_name   = pandas.read_csv('girls_names.csv')
surname       = pandas.read_csv('surname-only.csv')
street_suburb = pandas.read_csv('20240119000odstreet.csv')
email         = pandas.read_csv('email.csv')

surname_max = len(surname) -1
male_max    = len(male_name) -1
female_max  = len(female_name) -1
street_max  = len(street_suburb) -1
email_max   = len(email) -1

phone_area_code = {}
phone_area_code['QLD'] = "7"
phone_area_code['ACT'] = "2"
phone_area_code['VIC'] = "3"
phone_area_code['WA']  = "8"
phone_area_code['NSW'] = "7"
phone_area_code['SA']  = "8"
phone_area_code['TAS'] = "3"
phone_area_code['NT']  = "3"

post_code = {}
post_code['QLD'] = "4"
post_code['ACT'] = "26"
post_code['VIC'] = "3"
post_code['WA']  = "6"
post_code['NSW'] = "2"
post_code['SA']  = "5"
post_code['TAS'] = "7"
post_code['NT']  = "2"

## Setup the loop
max_value = 25
count     = 1

## Generate the value
print("{:3} {:15} {:15} {:20} {:6} {:25} {:10} {:6} {:4} {:11} {:25}"
  .format('ID', 'First Name','Last Name', 'Suburb', 'No', 'Street', 'Type', 'State', 'Code', 'Phone', 'Email'))

while count <= max_value:

   gender = random.choice(["M","F"])
   if gender == "M":
     first_name = (male_name.iloc[random.randint(0,male_max),0])
   else:
     first_name = (female_name.iloc[random.randint(0,female_max),0])

   last_name    = (surname.iloc[random.randint(0, surname_max),0]).title()
   suburb_rand  = random.randint(0, street_max)
   suburb       = street_suburb.iloc[suburb_rand,0].title()
   street_rand  = random.randint(0, street_max)
   street       = street_suburb.iloc[street_rand,0].title()
   street_type  = random.choice(['Street','Lane','Road','Avenue','Court','Circut','Parade','Close','Cresent', 'Drive'])

   ## Make more realistice street numbers
   street_choice = random.choice(['single','double','tripple','large','unit_single','unit_double'])
   if street_choice == 'single':
     number = random.randint(1,9)
   elif street_choice == 'double':
     number = random.randint(10,99)
   elif street_choice == 'tripple':
     number = random.randint(100,999)
   elif street_choice == 'large':
     number = random.randint(1000,5000)
   elif street_choice == 'unit_single':
     #letter_choice = random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
     letter_choice = random.choice(['a','b','c','d','e','f','g'])
     number = "{}{}".format(random.randint(1,9), letter_choice)
   elif street_choice == 'unit_double':
     #letter_choice = random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
     letter_choice = random.choice(['a','b','c','d','e','f','g'])
     number = "{}{}".format(random.randint(10,99), letter_choice)

   state  = random.choice(['WA','VIC','SA','NSW','ACT','QLD','NT','TAS'])
   state_post_code  = post_code[state]

   if len(state_post_code) == 1:
     final_post_code = "{}{:03d}".format(state_post_code, random.randint(0,999))
   elif len(state_post_code) == 2:
     final_post_code = "{}{:02d}".format(state_post_code, random.randint(0,18))

   ## Set phone
   has_phone        = random.choice(["Yes","No"])
   if has_phone == "Yes":
     phone_prefix     = phone_area_code[state]
     land_line        = "61{}{}".format(phone_prefix, random.randint(10000000,99999999))
   else:
     land_line        = ''


   ## Create the email address
   email_choice   = random.choice(['short','long','first','last','none'])
   email_provider = email.iloc[random.randint(1,email_max),0]

   if email_choice == 'short':
     email_address = "{:1}.{}@{}".format(first_name, last_name, email_provider)
   elif email_choice == 'long':
     email_address = "{}.{}@{}".format(first_name,last_name, email_provider)
   elif email_choice == 'first':
     email_address = "{}{}@{}".format(first_name,random.randint(1,100), email_provider)
   elif email_choice == 'last':
     email_address = "{}{}@{}".format(last_name,random.randint(1,100), email_provider)
   elif email_choice == 'none':
     email_address = ''
   else:
     email_address = ''
   
   print("{:003d} {:<15} {:<15} {:<20} {:<6} {:<25} {:<10} {:<6} {:<4} {:<11} {:<25}"
     .format(count, first_name, last_name, suburb, number, street, street_type, state, final_post_code, land_line, email_address ))

   count += 1
  #print("%s %s %s " % (count, first_name, last_name))

