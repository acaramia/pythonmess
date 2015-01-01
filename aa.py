import gdata
import sys

print sys.version
import gdata.docs.service


def test1():
	# Create a client class which will make HTTP requests with Google Docs server.
	client = gdata.docs.service.DocsService()
	# Authenticate using your Google Docs email address and password.
	client.ClientLogin('user@gmail.com', 'app-specific-password')

	# Query the server for an Atom feed containing a list of your documents.
	documents_feed = client.GetDocumentListFeed()
	# Loop through the feed and extract each document entry.
	for document_entry in documents_feed.entry:
	  # Display the title of the document on the command line.
	  print document_entry.title.text

def test2():
	import sheetsync
	data = { "Kermit": {"Color" : "Green", "Performer" : "Jim Henson"},
	         "Miss Piggy" : {"Color" : "Pink", "Performer" : "Frank Oz"}
	        }

	# Get or create a spreadsheet...
	target = sheetsync.Sheet(username="user@gmail.com",
	                         password="app-specific-password",
	                         document_name="Let's try out SheetSync")
	# Insert or update rows on the spreadsheet...
	target.inject(data)
	print "Review the new spreadsheet created here: %s" % target.document_href

test2()