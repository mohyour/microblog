# Flask Microblog

.flaskenv example:
```
FLASK_APP=microblog.py
FLASK_DEBUG=True
SECRET_KEY=<secret-key>
DATABASE_URL=<database-name>
```
Database Migration

`flask db init` - creates database migration folder
`flask db migrate` - Generates automatic migration script
`flask db upgrade` - Apply database migration
