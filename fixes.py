import pywikibot
import mwparserfromhell
import re

search = r"\[(?:https?:\/\/api\.aucklandmuseum\.com\/id\/)([^\/]+)\/([^\/]+)\/(\d+) Object record\]\<br\>"

site = pywikibot.Site('commons','commons')

for page in pywikibot.Category(site, "Category:Images from Auckland Museum"):
    wikicode = mwparserfromhell.parse(page.text)
    for template in wikicode.filter_templates():
        if template.name == "Images from Auckland Museum":
            print("Already done")
            continue
    page.text = search_in(page)
    page.save(summary=u"Adding [[Template:Images from Auckland Museum]] ([[Commons:Bots/Requests/TheSandBot 4|BRFA]])", minor=True, botflag=True, force=True)

def search_in(page):
    x = re.search(search, page.text)
    section = x.group(1)
    object = x.group(2)
    id = x.group(3)
    return re.sub(search, "{{Images from Auckland Museum|section=" + section + "|object=" + object + "|id=" + id + "}}", page.text)
