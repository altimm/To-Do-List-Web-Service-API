# To-Do-List-Web-Service-API

The service should perform CRUD operations on a database of to-do records. The service will be used privately by one user.

### To-Do List Record Example:
| Primary Key | Creation Datetime | Due Datetime | Completed Datetime | Task Description | Status |
| ------ | ------ | ------ | ----- | ----- | ----- |
| str | str, Unix timestamp in seconds | str, Unix timestamp in seconds | str, Unix timestamp in seconds | str | str, `pending` `late` `completed`|

###  Required
- [x] The service should provide valid and appropriate HTTP responses for the type of API resource request.
- [x] Create a to-do record by specifying the description and desired date and time of completion.
- [x] Retrieve a list of to-do records.
- [x] Update a to-do record with new values for meaningful fields.
- [x] Delete a to-do record.



### Optional
These additional features would be nice to see, but aren’t necessary for the project review. You’re welcome to ignore them, make an unfinished attempt that can be discussed in the technical interview, or complete them.

- [ ] Filtering, searching, and sorting to-do records by meaningful fields.
- [ ] Implement some level of authentication, whether at the HTTP, app, or some other level.

### Improvements to Make:
- [ ] Auto-fill creation date with datetime.now()
- [ ] Auto-Set `late/pending` status on "retrive"
- [ ] Less annoying datetime input

## Dev Environment

Install Django using Python Virtual Environments
```
python3 -m venv /django
./django/Scripts/activate
pip install django
```

Start Django server from the terminal
Navigate to project folder and start server
```
python manage.py runserver
```
The server can be viewed at `http://127.0.0.1:8000/`

### Home Page
The home page shows all of the to-do list tasks. Good feature improvements would be to have the view compare the currenttime/due date to set the status value before display

### Create Page
The create page allows the user to set the due date and description. The status defaults to `pending` by default and should be updated as a part of the home page view. The current datetime should be calculated as part of the backend of this view but the feature is not implemented.
`http://127.0.0.1:8000/create/`
Valid Input Formats:
```
'%Y-%m-%d %H:%M:%S',
 '%Y-%m-%d %H:%M:%S.%f',
 '%Y-%m-%d %H:%M',
 '%m/%d/%Y %H:%M:%S',
 '%m/%d/%Y %H:%M:%S.%f',
 '%m/%d/%Y %H:%M',
 '%m/%d/%y %H:%M:%S',
 '%m/%d/%y %H:%M:%S.%f',
 '%m/%d/%y %H:%M'
 ```
 
 ### Complete Task (Update)
 
 `http://127.0.0.1:8000/complete/?id=<taskid>`

### Delete

 `http://127.0.0.1:8000/delete/?id=<taskid>`
