#!/usr/bin/python

months = ['January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'November',
'December']

def valid_month:
   for i in months:
      if(i.lower() == months.lower()):
        return i

print valid_month("January")
print valid_month("january")
