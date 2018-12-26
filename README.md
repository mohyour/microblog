# Flask Microblog

.flaskenv example:
```
FLASK_APP=microblog.py
FLASK_DEBUG=0
SECRET_KEY=<secret-key>
DATABASE_URL=<database-name>
MAIL_SERVER=smtp.googlemail.com
MAIL_PORT=587
MAIL_USE_TLS=1
MAIL_USERNAME=<your-gmail-username>
MAIL_PASSWORD=<your-gmail-password>
```
Database Migration

`flask db init` - creates database migration folder
`flask db migrate` - Generates automatic migration script
`flask db upgrade` - Apply database migration

Test error email locally - debug set to false:
Run: `python -m smtpd -n -c DebuggingServer localhost:8025`
and below in another terminal
```
export MAIL_SERVER=localhost
export MAIL_PORT=8025
```
