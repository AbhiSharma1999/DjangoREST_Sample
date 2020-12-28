# DjangoREST_Sample


The hosted endpoints can be found at BASE_URL = 'http://abhishek3ic.pythonanywhere.com/authors'

The databse can be extracted in json format by running python manage.py dumpdata > store.json in the Virtual MAchine where the server is hosted , the endpoint to download the json file has not been made as it is not a good practice to expose the entire databse.

## /posts =>

GET = Returns a json file with all the posts in ascending order of their id . This request enables entitly level filtering,sorting and search.

POST = Creates the object with the next available id

  headers = {
              'Content-Type' : 'application/json'
            }
						
  body = {
            'title' : 'title1',
            'author' : 'CIQ',
            'views' : 100,
            'reviews' : 20
         }
   
 
## /posts/{Integer} =>

GET = Returns a json with id {Integer} 

PUT = Updates the object with id {Integer}

  headers = {
              'Content-Type' : 'application/json'
            }
	    
  body = {
            'title' : 'title1',
            'author' : 'CIQ',
         }  
         Note : Both title and author are necessary
	 
PATCH = Updates the object with id {Integer}

  headers = {
              'Content-Type' : 'application/json'
            }
	    
  body = {
            'title' : 'title1',
         }

DELETE = Deletes the object with id {Integer}
	 

         
         
## /authors =>

GET = Returns a json file with all the authors in ascending order of their id . This request enables entitly level filtering,sorting and search.

POST = Creates the object with the next available id

  headers = {
              'Content-Type' : 'application/json'
            }
						
  body = {
            'first_name' : 'title1',
            'lst_name' : 'CIQ',
            'posts' : 100,
         }
   
 
## /authors/{Integer} =>

GET = Returns a json with id {Integer} 

PUT = Updates the object with id {Integer}

  headers = {
              'Content-Type' : 'application/json'
            }
						
  body = {
            'first_name' : 'title1',
            'lst_name' : 'CIQ',
            'posts' : 100,
         }  
         Note : Both title and author are necessary
				 
PATCH = Updates the object with id {Integer}

  headers = {
              'Content-Type' : 'application/json'
            }
						
  body = {
            'first_name' : 'title1',
            'lst_name' : 'CIQ'
         }
				 
DELETE = Deletes the object with id {Integer}
         
         
