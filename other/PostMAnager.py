"""

this is a script to help me write my posts in the home path index.html.
it is neeat.

"""

from colorama import Fore as F
from sys import argv
from json import dumps, loads
from pprint import pprint
from _io import TextIOWrapper
from time import sleep
dot = "."
OUTPUTFILE_ = "material/Posts.html"

HTML_ = "Output/index.html"

UPPERHTML_ = open("material/template1.html", "r").read().encode()

LEGHTML_ = open("material/template2.html", "r").read().encode()

def getJSON(FILE: str) -> dict:
    """Gets the json"""
    with open(FILE, 'r') as f:
        return loads(f.read())


def writeJSON(FILE: str, dict_: dict) -> None:
    """ over writes the json """
    with open(FILE, "w+") as f:
        f.write(dumps(dict_, indent=4))


def addPost(FILE: str = "Home.json") -> str:
    """ manages my posts data """
    Data0 = getJSON(FILE)
    Header = input(f"{F.YELLOW} post title : {F.WHITE}")
    post_resume = input(f"{F.YELLOW} post paragraph : {F.WHITE}")
    Data0["paragraphs"].append(post_resume)
    Data0["Titles"].append(Header)
    Data0["Dates"].append("soon..")
    Data0["PostCount"] += 1
    writeJSON(FILE, Data0)
    return f"""
<div class="section">
        <h2>
            {Header}<span class="date"> {Data0["Dates"][-1]} </span>
        </h2>
        <p class="paragraph">
           {post_resume}
        </p>
        <a href="#" class="button">
            read more         
        </a>
</div>
"""

def dumpOUTPUT(content: str, OUTPUTFILE: str = OUTPUTFILE_):
    """ generates the html to an html file """
    with open(f"{OUTPUTFILE}", "ab") as f:
        f.write(content.encode())
        f.write(b"<|>")
        print(f"{F.GREEN} Written!!")

def getPOSTS(OUTPUTFILE: str = OUTPUTFILE_):
    """ getting all the post that have been stored as html """
    with open(OUTPUTFILE, "r") as f:
        return [i for i in f.read().split("<|>")[:-1]]


def generateHTML():
    """ Generating the html Binary """
    HTML = UPPERHTML_
    for i in getPOSTS():
        HTML += i.encode()
    HTML += LEGHTML_
    return HTML


# prompt to make the post properties

div = addPost()
dumpOUTPUT(div)
# generates the html binary then returns it as bytes-like object.
Html = generateHTML()
c = input(f"{F.GREEN}want to apply to the page (Y/N): ")
c = c.upper().strip()
if c in ["Y", "N"]:
    if c == "Y":
        with open("../index.html", "wb") as f:
            f.write(Html)
            print(f"{F.GREEN}the root html file has been updated with the new html.")
    else:
        with open(HTML_, "wb") as f:
            f.write(Html)
            print(f"{F.GREEN}the HTML has been redirected succefully to => {HTML_}")
else:
    print(f"...invalid answer, {c}")

print(F.RESET)

