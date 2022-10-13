# To-Do-List-Web-Service-API

The service should perform CRUD operations on a database of to-do records. The service will be used privately by one user.

### To-Do List Record Example:
| Primary Key | Creation Datetime | Due Datetime | Completed Datetime | Task Description | Status |
| ------ | ------ | ------ | ----- | ----- | ----- |
| str | str, Unix timestamp in seconds | str, Unix timestamp in seconds | str, Unix timestamp in seconds | str | str, `pending` `late` `completed`|

###  Required
- [ ] The service should provide valid and appropriate HTTP responses for the type of API resource request.
- [ ] Create a to-do record by specifying the description and desired date and time of completion.
- [ ] Retrieve a list of to-do records.
- [ ] Update a to-do record with new values for meaningful fields.
- [ ] Delete a to-do record.

### Optional
These additional features would be nice to see, but aren’t necessary for the project review. You’re welcome to ignore them, make an unfinished attempt that can be discussed in the technical interview, or complete them.

- [ ] Filtering, searching, and sorting to-do records by meaningful fields.
- [ ] Implement some level of authentication, whether at the HTTP, app, or some other level.

## Dev Environment
