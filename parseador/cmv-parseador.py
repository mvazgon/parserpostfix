#!/usr/bin/python
import sys
import mysql.connector

file=open(sys.argv[1])

#print str(file.name)

Conn=mysql.connector.connect(user='psfxDB',password='BL679e5o3hwIBnS0',host='127.0.0.1',database='psfxDB')

for linea in file:
	arrayLinea=linea.split()
	if  len(arrayLinea) != 0 :
		print str(file.tell())+ '|||'+ str(len(arrayLinea))+"|||"+linea
		if str(arrayLinea[4]) == "postfix/smtp":
			print str(file.tell())+ '|||'+ str(len(arrayLinea))+"|||"+linea
		elif str(arrayLinea[4]) == "dovecot" :
			if str(arrayLinea[5]) =~ "auth-worker":
				print "Error MySQL"				
			elif str(arrayLinea[5] =~ "imap" :
				print 
			elif str(arrayLinea[5] == "imap-login:" :
			elif str(arrayLinea[5] == "lda" :
			elif str(arrayLinea[5] == "pop3-login:" :
		elif str(arrayLinea[4] == "filtro/autorespuesta:" :
		elif str(arrayLinea[4] == "filtro/pipe:" :
		elif str(arrayLinea[4] == "opendkim" :
		elif str(arrayLinea[4] == "postfix/anvil" :
		elif str(arrayLinea[4] == "postfix/bounce" :
		elif str(arrayLinea[4] == "postfix/cleanup" :
		elif str(arrayLinea[4] == "postfix/error" :
		elif str(arrayLinea[4] == "postfix/error" :
		elif str(arrayLinea[4] == "postfix/pickup" :
		elif str(arrayLinea[4] == "postfix/pipe" :
		elif str(arrayLinea[4] == "postfix/policy-spf" :
		elif str(arrayLinea[4] == "postfix/qmgr":
		elif str(arrayLinea[4] == "postfix/smtp" :
		elif str(arrayLinea[4] == "postfix/smtpd" : 
		elif str(arrayLinea[4] == "postfix/submission/smtpd":
		elif str(arrayLinea[4] == "postfix/trivial-rewrite" :
		elif str(arrayLinea[4] == "spamd" :
		elif str(arrayLinea[4] == "NOQUEUE" :


Conn.close()
file.close()
