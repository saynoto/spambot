# -*- coding: cp1252 -*-
import praw

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='android:com.example.reddit(by/u/soylent)',
                     username='',
                     password='')

#print(reddit.read_only)  # Output: False
spammsg = "spammsg"
subreddit = reddit.subreddit('Insert subreddit here')
usrs = 0
for submission in subreddit.new(limit=999999999):
	print(submission.author)  # Output: name of the redditor
	try:	
		reddit.redditor(str(submission.author)).message('Important Information', spammsg)
		usrs +=1
	except praw.exceptions.APIException:
		continue
	#print("Message sent to %s, total messages sent to far: %f" % submission.author % usrs)
	



	
	
	

from praw.models import MoreComments
submission.comments.replace_more(limit=0)
for top_level_comment in submission.comments:
   if isinstance(top_level_comment, MoreComments):
       continue
   submission.comments.replace_more(limit=None)
   
   
   try:
	   reddit.redditor(str(top_level_comment.author)).message('Important Information', spammsg)
	   usrs +=1
   except praw.exceptions.APIException:
	      continue
	
comment_queue = submission.comments[:]  # Seed with top-level
#while comment_queue:
   # comment = comment_queue.pop(0)
#comment_queue.extend(comment.replies)
print ("Successfully sent private messages to %d users" % usrs)



    
	
	
	
