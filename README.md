# saveouya-db
Database lister for final snapshot of Ouya eshop
It has working database model (for now) and rudimentary admin interface. 
to run:
 - create python venv
 - run `pip install < requirements.txt` from inside venv
 - run `python app.py` 
 - open http://localhost:5000/admin to access webadmin

TODO:

Database:
 - add more metadata to files (perhaps separate files_meta table that will hold stuff from apk dump?)
 - add MN relations for tag and genre
 - (maybe) split developer info from games
 - add contributor info (who sent the file, who tested the file...)

Other:
 - reimplement store scrapers (eg Eryofus) in python so we can push everything as one package
 - add json parser or script aroud apk tools to extract metadata automatically (ask around in discord)
 - start working on a frontend, eventually :)
