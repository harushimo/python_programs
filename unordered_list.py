#!/usr/bin/python


def unordered(items):
    """
    Create an unordered html list when a list is passed
    """
    ul = "<ul>\n"
    li = ""
    for item in items:
        li += "<li>" + str(item) + "</li>\n"
    li += "</ul>"
    final_list = ul + li
    print final_list
    return final_list


def unorderedUser():
    """
    Creating an unordered html list when a user inputs the list.
    """
    stored = []
    maxItems = 6
    while len(stored) < maxItems:
        user_input = (raw_input("Enter a item: "))
        if user_input != '':
            stored.append(user_input)
    print stored
    unordered(stored)


def createHTMLpage():
    """
    Create HTML template with unordered list
    """
    HTML_page = '''
    <!DOCTYPE html>
    <html>
     <head>
        <meta charset="utf-8">
        <title>Unordered List</title>
      </head>
      <body>
        '''+str(unordered())+'''
      </body>
    </html>
    '''

    print HTML_page

# Test cases
#names = ['Tom', 'Judy', 'Kari']
# states = ['Illinois', 'Michigan', 'California', 'Oregon']

#unordered(names)
createHTMLpage()
unorderedUser()
