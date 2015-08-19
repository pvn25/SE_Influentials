import tweepy
import time
import os
import sys
import json
import argparse
import operator
import csv
		

FOLLOWING_DIR = 'following'
MAX_FRIENDS = 20000000
FRIENDS_OF_FRIENDS_LIMIT = 200000000

if not os.path.exists(FOLLOWING_DIR):
    os.makedir(FOLLOWING_DIR)

enc = lambda x: x.encode('ascii', errors='ignore')

CONSUMER_KEY = 'ysFasZ3Q5ua9DCL7yWJ4uw2J4'
CONSUMER_SECRET = 'VWylSGV5FJN9xaGw0KlABik98wlI36Mnm8FEOI3idMWeafwX9f'	
ACCESS_TOKEN = '2835811022-Ih0ZGgVhIiMFVMYs7Gf0oIx1mYSltEKom7mLxG4'
ACCESS_TOKEN_SECRET = 'QijL36kIlpc6TkvOJuMCx1Iu7n9voDrcW9kXC2Owh8rC3'


CONSUMER_KEY1 = 'SctEK4QsFMtOeKCjEOoDlcnwu'
CONSUMER_SECRET1 = 'iE1mhzacDyJZxvkFmusn0R42lsiizOgs6h8Dl5r3s85Y3YKokR'	
ACCESS_TOKEN1 = '2835811022-tikPdbsh7u1N6soUOHCT91C5AOUD8HfNyjIzBIq'
ACCESS_TOKEN_SECRET1 = 'mRWP2nABJFWAMt4BOHbZqrVEZ0n18AW58V9FfocRs5g8W'

CONSUMER_KEY2 =          'LHSuUyDm0dbqYYx6enq5Mial5'
CONSUMER_SECRET2 =     'znyE2mLx4rC0EJK018HmhIjqLlur7MIHU0bDgfBQlw1MU8InI4'
ACCESS_TOKEN2  =    '3219681132-kPRH1GcgFBszQ6shmCdNfv2nooUeWc2L9c3hmKd'
ACCEESS_TOKEN_SECRET2 =  'BYNETrrelObdS3LI4b5yIRr9Pf52NkEenU0LctrcgEFfx'


CONSUMER_KEY3 =         'HO1XoN0H93BfBHuS0QS5yg528'
CONSUMER_SECRET3 =      'MGgCqUdfy0Q0sqkJy6uSgQ1qk5Pa9haRHaAsWqDvlAu8t7NDxr'
ACCESS_TOKEN3  =       '3219681132-p8XFAwA3xMSwSVjv2QZ2op5ejQKgaI2r1IedJHo'
ACCEESS_TOKEN_SECRET3 =   'rVtSL3ff6YjlZagNDVOEjtJTWGBDQboPxCIutGzBJnoHt'


CONSUMER_KEY4 =        '3cVcJ8LGOKlS8V6nGqgEaoFxG'
CONSUMER_SECRET4 =     'M2XkcDPAZklAaYETnFRy06uXq0xqPlxJfgcjbDixsOqqmqMeuc'
ACCESS_TOKEN4   =        '3219681132-x6BOXC5Gzj05r06LXUVsvMzTuHrlGnEo7eUsUI9'
ACCEESS_TOKEN_SECRET4 =  'lUKYkoY3aXSTHc2BwBsEODEI1wD4kKWcAb6gQIkoyxaMs'

CONSUMER_KEY5 = 'Eieo7xyaJjA5RurjOYLuI94GR'
CONSUMER_SECRET5 = 'IRvpIB3hoFdsm2C2XF5o9v5pTX2NQm9N9Euc0NGkbnFcY60vqL'
ACCESS_TOKEN5 = '2835811022-k5e22hajGGCRvbVAIhqtKXbGgzyce3ieXqS0ydt'
ACCESS_TOKEN_SECRET5 = '0KAQJrq2s50x2Qf3InwDUAp7JEu6KefjId9fFkqIRm8xe'

CONSUMER_KEY6 = '62WIaJSe4QeiJwARkhwFx31oo'
CONSUMER_SECRET66 = 'hfxu1cZYwvjHOGuEyiI8bEic00IK3RgidTiKtLJ7QKdDyy7mwz'	
ACCESS_TOKEN6 = '3219681132-T9kCzWhJKwtM4YL1iyYtTLrbktPi1LKDQAbOYxs'
ACCESS_TOKEN_SECRET6 = '5xLRPVZekwGMg5e9VZNNHKpv3OCh8o9zrJhq2VmDV1XVj'

CONSUMER_KEY7 = 'txOv7Z4SVkOja1rL1FY6Yj7RJ'
CONSUMER_SECRET7 = 'OYagXVfUq9H1ZwveDlVaFm5AACiJ2KhuSgbpt4Cc0mcezAiV4a'
ACCESS_TOKEN7 = '2835811022-qcqEhQdmKCygZHXYdOACtDyz5sXBgwF7os6MP26'
ACCESS_TOKEN_SECRET7 = '4WmA3VLJEQxIHiK7VraXurTgai7LFjy7BnPe9keLgJwwm'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

auth1 = tweepy.OAuthHandler(CONSUMER_KEY1, CONSUMER_SECRET1)
auth1.set_access_token(ACCESS_TOKEN1, ACCESS_TOKEN_SECRET1)
api1 = tweepy.API(auth1)

auth2 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth2.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api2 = tweepy.API(auth2)

auth3 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth3.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api3 = tweepy.API(auth3)

auth4 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth4.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api4 = tweepy.API(auth4)

auth5 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth5.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api5 = tweepy.API(auth5)

auth6 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth6.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api6 = tweepy.API(auth6)

auth7 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth7.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api7 = tweepy.API(auth7)

q = 0

def get_follower_ids(centre, max_depth=1, current_depth=0, taboo_list=[]):

    # print 'current depth: %d, max depth: %d' % (current_depth, max_depth)
    # print 'taboo list: ', ','.join([ str(i) for i in taboo_list ])

    if current_depth == max_depth:
        print 'out of depth'
        return taboo_list

    if centre in taboo_list:
        # we've been here before
        print 'Already been here.'
        return taboo_list
    else:
        taboo_list.append(centre)
    
    global q

    try:
        userfname = os.path.join('twitter-users', str(centre) + '.json')
        if not os.path.exists(userfname):
            print 'Retrieving user details for twitter id %s' % str(centre)
            while True:
                try:
		    if q == 0:
                    	user = api.get_user(centre)
		    	q = 1		    
		    elif q == 1:
		    	user = api1.get_user(centre)
		    	q = 2:	
		    elif q == 2:
		    	user = api2.get_user(centre)
		    	q = 3:
		    elif q == 3:
		    	user = api3.get_user(centre)
		    	q = 4:
		    elif q == 4:
		    	user = api4.get_user(centre)
		    	q = 0:					

	    

                    d = {'name': user.name,
                         'screen_name': user.screen_name,
                         'id': user.id,
                         'friends_count': user.friends_count,
                         'followers_count': user.followers_count}

                    with open(userfname, 'w') as outf:
                        outf.write(json.dumps(d, indent=1))

                    user = d
                    break
                except tweepy.TweepError, error:
                    print type(error)

                    if str(error) == 'Not authorized.':
                        print 'Can''t access user data - not authorized.'
                        return taboo_list

                    if str(error) == 'User has been suspended.':
                        print 'User suspended.'
                        return taboo_list

                    errorObj = error[0][0]

                    print errorObj

                    if errorObj['message'] == 'Rate limit exceeded':
                        print 'Rate limited. Sleeping for 15 minutes.'
                        time.sleep(15 * 60 + 15)
                        continue

                    return taboo_list
        else:
            user = json.loads(file(userfname).read())

        screen_name = enc(user['screen_name'])
        fname = os.path.join(FOLLOWING_DIR, screen_name + '.csv')
        friendids = []

        # only retrieve friends of TED... screen names
        if screen_name.startswith(''):
            if not os.path.exists(fname):
                print 'No cached data for screen name "%s"' % screen_name
                with open(fname, 'w') as outf:
                    params = (enc(user['name']), screen_name)
                    print 'Retrieving friends for user "%s" (%s)' % params

                    # page over friends
                    c = tweepy.Cursor(api.friends, id=user['id']).items()

                    friend_count = 0
                    while True:
                        try:
                            friend = c.next()
                            friendids.append(friend.id)
			    op = api.get_user(friend.id)
                            params = (friend.id, enc(friend.screen_name), enc(friend.name),op.followers_count)
                            outf.write('%s\t%s\t%s\t%d\n' % params)
                            friend_count += 1
                            if friend_count >= MAX_FRIENDS:
                                print 'Reached max no. of friends for "%s".' % friend.screen_name
                                break
                        except tweepy.TweepError:
                            # hit rate limit, sleep for 15 minutes
                            print 'Rate limited. Sleeping for 15 minutes.'
                            time.sleep(15 * 60 + 15)
                            continue
                        except StopIteration:
                            break
            else:
		sample = open(fname,'r')
	        csv1 = csv.reader(sample,delimiter='\t')
	        sort = sorted(csv1,key = lambda row: float(row[3]),reverse = True)	   
	    	#print friendids[3]
 	    	f = open(fname, "wb")
	   	fileWriter = csv.writer(f, delimiter='\t')
  	        for row in sort:
			print row
	        	fileWriter.writerow(row)
	        f.close()
                friendids = [int(line.strip().split('\t')[0]) for line in file(fname)]

	    print friendids
            print 'Found %d friends for %s' % (len(friendids), screen_name)

            # get friends of friends
            cd = current_depth
	    m = min(len(friendids),19)
	    print m
            if cd+1 < max_depth:
                for fid in range(0,m):
		    print friendids[fid]
                    taboo_list = get_follower_ids(friendids[fid], max_depth=max_depth,
                        current_depth=cd+1, taboo_list=taboo_list)

            if cd+1 < max_depth and len(friendids) > FRIENDS_OF_FRIENDS_LIMIT:
                print 'Not all friends retrieved for %s.' % screen_name

    except Exception, error:
        print 'Error retrieving followers for user id: ', centre
        print error

        if os.path.exists(fname):
            os.remove(fname)
            print 'Removed file "%s".' % fname

        sys.exit(1)

    return taboo_list

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--screen-name", required=True, help="Screen name of twitter user")
    ap.add_argument("-d", "--depth", required=True, type=int, help="How far to follow user network")
    args = vars(ap.parse_args())

    twitter_screenname = args['screen_name']
    depth = int(args['depth'])

    if depth < 1 or depth > 3:
        print 'Depth value %d is not valid. Valid range is 1-3.' % depth
        sys.exit('Invalid depth argument.')

    print 'Max Depth: %d' % depth
    matches = api.lookup_users(screen_names=[twitter_screenname])

    if len(matches) == 1:
        print get_follower_ids(matches[0].id, max_depth=depth)
    else:
        print 'Sorry, could not find twitter user with screen name: %s' % twitter_screenname


