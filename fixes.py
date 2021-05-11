import pywikibot
import mwparserfromhell
import re
#import mysql.connector


#mydb = mysql.connector.connect(
 # host="localhost",
  #user="newuser",
  #password="password",
  #database="commons_task4_run"
#)

#search_sql = "SELECT title FROM runs WHERE title = '%s'"
search = r"\[(?:https?:\/\/api\.aucklandmuseum\.com\/id\/)([^\/]+)\/([^\/]+)\/(\d+) Object record\]\<br\>"


site = pywikibot.Site('commons','commons')

for page in pywikibot.Category(site, "Category:Images from Auckland Museum"):

#page = pywikibot.Page(site, 'File:"Mariposa" passenger liner next to yacht (AM 79747-1).jpg')
    #mycursor.execute(search_sql, page.title())
    #myresult = mycursor.fetchall()
    #if len(myresult) > 0:
    #    print("Already done")
    #    continue

    wikicode = mwparserfromhell.parse(page.text)
    for template in wikicode.filter_templates():
        if template.name == "Images from Auckland Museum":
            print("Already done")
            continue
    #x = re.search(search, page.text)
    #section = x.group(1)
    #object = x.group(2)
    #id = x.group(3)
    #print(section)
    #print(object)
    #print(id)
    page.text = search_in(page)
    #page.text = re.sub(search, "{{Images from Auckland Museum|section=" + section + "|object=" + object + "|id=" + id + "}}", page.text)
    page.save( summary=u"Adding [[Template:Images from Auckland Museum]] ([[Commons:Bots/Requests/TheSandBot 4|BRFA]])", minor=True, botflag=True, force=True

def search_in(page):
    x = re.search(search, page.text)
    section = x.group(1)
    object = x.group(2)
    id = x.group(3)
    return re.sub(search, "{{Images from Auckland Museum|section=" + section + "|object=" + object + "|id=" + id + "}}", page.text)
