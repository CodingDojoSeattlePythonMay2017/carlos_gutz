#!/usr/bin/env python
# -*- coding: utf-8 -*-

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
  ],
 'Instructors': [
     {'first_name': 'Michael', 'last_name': 'Choi'},
     {'first_name': 'Martin', 'last_name': 'Puryear'}
  ]
 }

# Making a function to print out values of lists.


def gimmevalues(insertlist):
    for items in insertlist:
        getnames = ""
        for key, values in items.iteritems():
            getnames += values + " "
        print(getnames)

gimmevalues(students)

# Making a function to print out values of a dictionary and its sub values and total lens of sub values.


def gimmedeepvalues(innerdictionary):
    for key, values in innerdictionary.iteritems():
        makingnewheader = ""
        makingnewheader += key
        print(makingnewheader)
        counter = 0
        for items in values:
            addingnames = ""
            getmylen = 0
            for junk, stuff in items.iteritems():
                addingnames += stuff + " "
                getmylen += len(stuff)
            counter += 1
            print("{0} - {1}- {2}".format(counter, addingnames, getmylen))


gimmedeepvalues(users)
