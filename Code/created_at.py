import tweepy
import os

arr1 = ["BillGates",
"timoreilly",
"Pogue",
"ericschmidt",
"waltmossberg",
"codinghorror",
"martinfowler",
"shanselman",
"spolsky",
"KentBeck",
"jack",
"masason",
"biz",
"notch",
"elonmusk",
"ev",
"TEDchris",
"Padmasree",
"kevinrose",
"dickc",
"noaheverett",
"Ghonim",
"om",
"kaifulee",
"jeb_",
"tim_cook",
"karaswisher",
"marissamayer",
"MichaelDell",
"majornelson",
"kenichiromogi",
"alaa",
"onambiguity",
"Chad_Hurley",
"leolaporte",
"anildash",
"pierre",
"SethBling",
"Dinnerbone",
"mikeyk",
"mattcutts",
"satyanadella",
"saurik",
"stevewoz",
"johnmaeda",
"chadfowler",
"john",
"ginatrapani",
"jbernhardsson",
"zeldman",
"pod2g",
"evad3rs",
"finkd",
"bgurley",
"pmarca",
"tnatsu",
"DuvalMagic",
"rsarver",
"reidhoffman",
"Fwiz",
"durov",
"DavidVonderhaar",
"Gronkh",
"MichaelCondrey",
"sivers",
"therealcliffyb",
"jkottke",
"digiphile",
"jkalucki",
"paulg",
"HIDEO_KOJIMA_EN",
"iH8sn0w",
"ID_AA_Carmack",
"nzkoz",
"myspacetom",
"abdur",
"carlmanneh",
"bs",
"todsacerdoti",
"timberners_lee",
"mollstam",
"_tomcc",
"Kappische",
"vpieters",
"jeresig",
"JahKob",
"p0sixninja",
"danfrisk",
"bhorowitz",
"noobde",
"minliangtan",
"cdixon",
"Benioff",
"IGLevine",
"paul_irish",
"srlm",
"robhoward",
"pschiller",
"tconrad",
"jonkagstrom",
"preillyme",
"demandrichard",
"shoemoney",
"levie",
"dongatory",
"_grum",
"mezzoblue",
"a",
"dhh",
"JD_2020",
"rkmt",
"e_kaspersky",
"joebelfiore",
"i0n1c",
"KrisJelbring",
"chriscoyier",
"sundarpichai",
"xlson",
"jemimakiss",
"RiotPendragon",
"lukew",
"carnalizer",
"drewhouston",
"ZacheryNielson",
"paulsingh",
"austinnotduncan",
"scottgu",
"chpwn",
"RamyRaoof",
"jimmy_wales",
"JonCrawford",
"zephoria",
"rocket2guns",
"LoaiNagati",
"ZeinabSamir",
"Joi",
"pmolyneux",
"l2k",
"sorenmacbeth",
"mkapor",
"sarahcuda",
"anamitra",
"addyosmani",
"akirareiko",
"wol_lay",
"skonnard",
"jsa",
"AquaXetine",
"f",
"Swiftor",
"DaveSumter",
"RanaASaid",
"AkihiroHino",
"habibh",
"ChrisMetzen",
"gr33ndata",
"simplebits",
"andrewchen",
"EdmundMcMillenn",
"stanleytang",
"meyerweb",
"BomuBoi",
"ryan",
"Harada_TEKKEN",
"marcoarment",
"tha_rami",
"sama",
"willsmith",
"reckless",
"br",
"travisk",
"larryellison",
"harrymccracken",
"EvilSeph",
"ibogost",
"jeff",
"fart",
"photomatt",
"dens",
"Arubin",
"j_smedley",
"SamFURUKAWA",
"PG_kamiya",
"scottebales",
"aaronwall",
"chrismessina",
"tinyBuild",
"Jonathan_Blow",
"kevin",
"Goldman44",
"stephenlrose",
"pgeuder",
"JeremyCMorgan",
"Pentadact",
"t",
"Werner",
"tanakaryusaku",
"beep",
"chrisremo",
"petecashmore"	
]


CONSUMER_KEY =         'HO1XoN0H93BfBHuS0QS5yg528'
CONSUMER_SECRET =      'MGgCqUdfy0Q0sqkJy6uSgQ1qk5Pa9haRHaAsWqDvlAu8t7NDxr'
ACCESS_TOKEN   =       '3219681132-p8XFAwA3xMSwSVjv2QZ2op5ejQKgaI2r1IedJHo'
ACCESS_TOKEN_SECRET =   'rVtSL3ff6YjlZagNDVOEjtJTWGBDQboPxCIutGzBJnoHt'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
fname = os.path.join('Results','createdat.csv')	
f = open(fname,"a")

for i in range(180,200):
	user = api.get_user(arr1[i])
	params = (user.created_at)
	f.write('%s\n' % params)
