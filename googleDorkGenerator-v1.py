# Author: Nuriddin No'monov

kategoriyalar = """
  All Categories
[1] Admin Page Search 
[2] Vulnerability Search
[3] Files Search
[4] Index Pages Search
[5] Technology & Version Search
"""

print(kategoriyalar)
kiritish = input("[$] Choose one of the categories> ")


admPageSearch = [
    "inurl:admin", 
    "inurl:login", 
    "inurl:dashboard", 
    "intitle:'admin panel'", 
    "intitle:'login'"
]

filesSearch = [
    "filetype:log", 
    "filetype:txt", 
    "filetype:sql", 
    "filetype:env", 
    "filetype:config", 
    "filetype:bak"
]

vulnSearch = [
    "intext:error", 
    "intext:warning", 
    "intext:password", 
    "intext:confidential", 
    "inurl:debug", 
    "inurl:backup"
]

indexSearch = [
    "intitle:'index of'", 
    "intitle:'directory listing'", 
    "intitle:'browse'"
]

techSearch = [
    "intext:'powered by'", 
    "intext:'running on'", 
    "intext:'version'", 
    "inurl:version"
]

sayt = input("\n[$] Type the site name> ")

dorklar = []

if kiritish == "1":
    dorklar = admPageSearch
elif kiritish == "2":
    dorklar = vulnSearch
elif kiritish == "3":
    dorklar = filesSearch
elif kiritish == "4":
    dorklar = indexSearch
elif kiritish == "5":
    dorklar = techSearch
elif kiritish.lower() in ["all", "6", ""]:  
    dorklar = admPageSearch + vulnSearch + filesSearch + indexSearch + techSearch
else:
    print("[$] Wrong choice! Default search: Admin panels.")
    dorklar = admPageSearch

print("\n[$] Google Dorking Surveys:")

for dork in dorklar:
    print(f"site:{sayt} {dork}")
